import six
from six import PY2, PY3, text_type, string_types
from six.moves import urllib


if six.PY3:
    memoryview = memoryview
    buffer_types = (bytes, bytearray, memoryview)
else:
    # memoryview and buffer are not strictly equivalent, but should be fine for
    # django core usage (mainly BinaryField). However, Jython doesn't support
    # buffer (see http://bugs.jython.org/issue1521), so we have to be careful.
    if sys.platform.startswith('java'):
        memoryview = memoryview
    else:
        memoryview = buffer
    buffer_types = (bytearray, memoryview)


# Mostly taken from Django.
def force_text(s, encoding='utf-8', errors='strict'):
    # Handle the common case first for performance reasons.
    if isinstance(s, text_type):
        return s
    try:
        if not isinstance(s, string_types):
            if PY3:
                if isinstance(s, bytes):
                    s = text_type(s, encoding, errors)
                else:
                    s = text_type(s)
            elif hasattr(s, '__unicode__'):
                s = text_type(s)
            else:
                s = text_type(bytes(s), encoding, errors)
        else:
            # Note: We use .decode() here, instead of
            # six.text_type(s, encoding, # errors), so that if `s` is a
            # SafeBytes, it ends up being a # SafeText at the end.
            s = s.decode(encoding, errors)
    except UnicodeDecodeError as e:
        if not isinstance(s, Exception):
            raise UnicodeDecodeError(s, *e.args)
        else:
            # If we get to here, the caller has passed in an Exception
            # subclass populated with non-ASCII bytestring data without a
            # working unicode method. Try to handle this without raising a
            # further exception by individually forcing the exception args
            # to unicode.
            s = ' '.join([force_text(arg, encoding, errors) for arg in s])
    return s


def force_bytes(s, encoding='utf-8', errors='strict'):
    # Handle the common case first for performance reasons.
    if isinstance(s, bytes):
        if encoding == 'utf-8':
            return s
        else:
            return s.decode('utf-8', errors).encode(encoding, errors)
    if isinstance(s, memoryview):
        return bytes(s)
    if not isinstance(s, six.string_types):
        try:
            if six.PY3:
                return six.text_type(s).encode(encoding)
            else:
                return bytes(s)
        except UnicodeEncodeError:
            if isinstance(s, Exception):
                # An Exception subclass containing non-ASCII data that doesn't
                # know how to print itself properly. We shouldn't raise a
                # further exception.
                return b' '.join(
                    force_bytes(arg, encoding, errors) for arg in s)
            return six.text_type(s).encode(encoding, errors)
    else:
        return s.encode(encoding, errors)
