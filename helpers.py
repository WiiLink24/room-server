import base64
import functools
from datetime import datetime
from lxml import etree


def xml_node_name(node_name):
    """ Custom decorator to serialize a returned dictionary as XML with a given name. """

    def decorator(func):
        @functools.wraps(func)
        def serialization_wrapper(*args, **kwargs):
            returned_value = func(*args, **kwargs)

            # Ensure we are truly dealing with a dictionary.
            if isinstance(returned_value, dict):
                # First, serialize to an ETree.
                elements = dict_to_etree(node_name, returned_value)

                # Next, insert a 'ver' key at the very top.
                # Versions must equate to 3 once divided by 100.
                # As such, 399 was chosen for no other reason than the fact this is true.
                ver = etree.SubElement(elements, "ver")
                ver.text = "399"
                elements.insert(0, ver)

                # We now must convert from ETree to actual XML we can respond with.
                return etree.tostring(elements, pretty_print=True)
            else:
                # We only apply XML operations to dicts.
                return returned_value

        return serialization_wrapper

    return decorator


def dict_to_etree(tag_name: str, d: dict) -> etree.Element:
    """ Derived from https://stackoverflow.com/a/10076823. """

    def _to_etree(d, root):
        if d is None:
            pass
        elif isinstance(d, bool):
            # We can only accept 0 or 1 as Nintendo's "boolean" types.
            root.text = "1" if d else "0"
        elif isinstance(d, int):
            root.text = f"{d}"
        elif isinstance(d, str):
            root.text = d
        elif isinstance(d, bytes):
            # We're going to assume this needs to be Base64 encoded.
            root.text = base64.b64encode(d)
        elif isinstance(d, tuple) or isinstance(d, list):
            # As we're backed by K/V notation,a tuple or a list is useless.
            # It should only contain our special
            # RepeatedKeys and RepeatedNodes types.
            should_delete = False
            for v in d:
                if isinstance(v, RepeatedElement):
                    # We'd like to duplicate this specific node in its parent.
                    # Now we need to obtain such.
                    parent_elem = root.getparent()
                    # Create a new sub-element in the parent with the current
                    # element's name.
                    new_elem = etree.SubElement(parent_elem, root.tag)

                    _to_etree(v.contents, new_elem)
                    should_delete = True
                elif isinstance(v, RepeatedKey):
                    # We'd like to duplicate keys within this node.
                    # Retain the parent and operate on the dict.
                    _to_etree(v.contents, root)
                else:
                    raise ValueError(f"invalid type {type(v).__name__} specified")
            if should_delete:
                # Delete ourselves once added as other repeated elements have replaced us.
                root.getparent().remove(root)

        elif isinstance(d, dict):
            for k, v in d.items():
                assert isinstance(k, str)
                _to_etree(v, etree.SubElement(root, k))
        else:
            assert d == "invalid type", (type(d), d)

    assert isinstance(d, dict)
    node = etree.Element(tag_name)
    _to_etree(d, node)
    return node


def current_date_and_time():
    """ Returns the current date time in a format usable by Nintendo. """

    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")


def current_date():
    """ Returns the current date in a format usable by Nintendo. """

    return datetime.utcnow().strftime("%Y-%m-%d")


class RepeatedKey:
    """This class is intended to clarify disambiguation when converting from a dict.
    Its specific behavior is to repeat its keys within a parent node.

    For example:
    <Parent>
        <key>value</key>
        <second>value</second>
        <key>value</key>
        <second>value</second>
    </Parent>
    """

    contents = {}

    def __init__(self, passed_dict):
        if not isinstance(passed_dict, dict):
            raise ValueError("Please only pass dicts to RepeatedKey.")
        self.contents = passed_dict


class RepeatedElement:
    """This class is intended to clarify disambiguation when converting from a dict.
    Its specific behavior is to allow repeating an element against its parent.

    For example:
    <Parent>
        <key>value</key>
        <second>value</second>
    </Parent>
    <Parent>
        <key>value</key>
        <second>value</second>
    </Parent>
    """

    contents = {}

    def __init__(self, passed_dict):
        if not isinstance(passed_dict, dict):
            raise ValueError("Please only pass dicts to RepeatedElement.")
        self.contents = passed_dict
