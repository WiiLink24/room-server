import io
import os
import pathlib
from typing import Union

import flask
from PIL import ImageFile, Image
from flask import send_from_directory, redirect
from wtforms import FileField
from room import s3
import config


class Asset(object):
    """Asset allows easy manipulation of an asset type on disk."""

    # The base asset directory used throughout this server.
    base_asset_dir = pathlib.Path("./assets")

    # The directory for this type of asset within the base folder.
    asset_dir: pathlib.Path

    # The filename of this asset within its directory.
    asset_name: str

    s3_tag: str

    always_save = False

    def asset_path(self) -> pathlib.Path:
        """The full path to this asset."""
        return self.asset_dir / self.asset_name

    def s3_path(self) -> str:
        return self.s3_tag + "/" + self.asset_name

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

        if s3:
            img = io.BytesIO()
            im.save(img, "jpeg", subsampling="4:2:0", progressive=False)
            self.upload_to_s3(img.getvalue())

            if self.always_save:
                with open(self.asset_path(), "wb") as f:
                    f.write(img.getvalue())
        else:
            # These defaults are required for the Wii to read an JPEG.
            im.save(self.asset_path(), "jpeg", subsampling="4:2:0", progressive=False)

    def delete(self):
        if s3:
            self.remove_from_s3()
        else:
            os.remove(self.asset_path())

    def send_file(self) -> flask.Response:
        """Wraps around Flask's send_from_directory method."""
        return send_from_directory(self.asset_dir, self.asset_name)

    def upload_to_s3(self, im: bytes):
        # I don't know why we have to convert the BytesIO object to bytes then back, but if we don't it will upload
        # nothing.
        s3.upload_fileobj(
            io.BytesIO(im),
            config.r2_bucket_name,
            self.s3_path(),
            ExtraArgs={"ContentType": "image/jpeg"},
        )

    def remove_from_s3(self):
        s3.delete_object(Bucket=config.r2_bucket_name, Key=self.s3_path())
