import io
import pathlib
from typing import Union

import flask
from PIL import ImageFile, Image
from flask import send_from_directory
from wtforms import FileField


class Asset(object):
    """Asset allows easy manipulation of an asset type on disk."""

    # The base asset directory used throughout this server.
    base_asset_dir = pathlib.Path("./assets")

    # The directory for this type of asset within the base folder.
    asset_dir: pathlib.Path

    # The filename of this asset within its directory.
    asset_name: str

    def asset_path(self) -> pathlib.Path:
        """The full path to this asset."""
        return self.asset_dir / self.asset_name

    def ensure_exists(self):
        """Creates the parent directories for this asset."""
        self.asset_dir.mkdir(parents=True, exist_ok=True)

    # Override the width and height if this asset is an image.
    # Tuple is (width, height)
    dimensions: tuple[int, int] = (0, 0)

    def encode(self, in_bytes: Union[bytes, FileField]):
        """Encodes an image to a format suitable for the Wii."""
        if isinstance(in_bytes, FileField):
            content = in_bytes.data.read()
        else:
            content = in_bytes

        self.ensure_exists()

        ImageFile.LOAD_TRUNCATED_IMAGES = True
        im = Image.open(io.BytesIO(content))

        # If we have an alpha channel, it must be removed.
        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")

        im = im.resize(self.dimensions)

        # These defaults are required for the Wii to read an JPEG.
        im.save(self.asset_path(), "jpeg", subsampling="4:2:0", progressive=False)

    def send_file(self) -> flask.Response:
        """Wraps around Flask's send_from_directory method."""
        return send_from_directory(self.asset_dir, self.asset_name)
