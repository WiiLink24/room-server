import io

import config

from asset import Asset
from typing import Union
from wtforms import FileField
from room import s3
from werkzeug.exceptions import NotFound

from url1.wall_metadata import wall_metadata
from url1.category_n import list_category_n


class RoomLogoAsset(Asset):
    """Used for a company logo within a room."""

    def __init__(self, room_id: int):
        self.dimensions = (320, 180)
        self.asset_dir = self.base_asset_dir / "special" / f"{room_id}"
        self.asset_name = "f1234.img"
        self.s3_tag = f"special/{room_id}/img"

    def upload_to_s3(self, im: bytes):
        # First the image
        s3.upload_fileobj(
            io.BytesIO(im),
            config.r2_bucket_name,
            self.s3_path(),
            ExtraArgs={"ContentType": "image/jpeg"},
        )


class ParadeBannerAsset(Asset):
    """Used as the logo within a parade, identifying a room."""

    def __init__(self, room_id: int):
        self.dimensions = (184, 80)
        self.asset_dir = self.base_asset_dir / "special" / f"{room_id}"
        self.asset_name = "parade_banner.jpg"
        self.room_id = room_id
        self.always_save = True

    def _upload_xmls_to_s3(self):
        from url1.special.allbin import special_allbin

        allbin_xml = special_allbin()
        s3.upload_fileobj(
            io.BytesIO(allbin_xml),
            config.r2_bucket_name,
            "special/allbin.xml",
            ExtraArgs={"ContentType": "text/xml"},
        )

        from url1.special.all import special_all

        all_xml = special_all()
        s3.upload_fileobj(
            io.BytesIO(all_xml),
            config.r2_bucket_name,
            "special/all.xml",
            ExtraArgs={"ContentType": "text/xml"},
        )

        from url1.special.contact import special_contact_n

        contact_xml = special_contact_n(self.room_id)

        if not isinstance(contact_xml, NotFound):
            s3.upload_fileobj(
                io.BytesIO(contact_xml),
                config.r2_bucket_name,
                f"special/{self.room_id}/contact.xml",
                ExtraArgs={"ContentType": "text/xml"},
            )

        from url1.special.page import special_page_n

        page_xml = special_page_n(self.room_id)
        if not isinstance(contact_xml, NotFound):
            s3.upload_fileobj(
                io.BytesIO(page_xml),
                config.r2_bucket_name,
                f"special/{self.room_id}/page.xml",
                ExtraArgs={"ContentType": "text/xml"},
            )

    def upload_to_s3(self, im: bytes):
        # For this specifically we need to upload to both S3 and save to disk.
        s3.upload_fileobj(
            io.BytesIO(im),
            config.r2_bucket_name,
            f"special/{self.room_id}/img/g1234.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )

        self._upload_xmls_to_s3()

    def remove_from_s3(self):
        s3.delete_object(
            Bucket=config.r2_bucket_name, Key=f"special/{self.room_id}/img/g1234.img"
        )

        # Update the XMLs
        self._upload_xmls_to_s3()


class NormalCategoryAsset(Asset):
    """Used for categories within the normal Shows tab."""

    def __init__(self, category_id: int):
        self.dimensions = (160, 120)
        self.asset_dir = self.base_asset_dir / "normal-category"
        self.asset_name = f"{category_id}.img"

        self.raw_asset_name = category_id
        self.s3_tag = "list/category/img"

    def upload_to_s3(self, im: bytes):
        # First the image
        s3.upload_fileobj(
            io.BytesIO(im),
            config.r2_bucket_name,
            self.s3_path(),
            ExtraArgs={"ContentType": "image/jpeg"},
        )

        # Next mirror the updates to the categories xml
        s3.upload_fileobj(
            io.BytesIO(list_category_n("01")),
            config.r2_bucket_name,
            "list/category/01.xml",
            ExtraArgs={"ContentType": "text/xml"},
        )


class PayCategoryAsset(Asset):
    """Used for categories within the Theater."""

    def __init__(self, category_id: int):
        self.dimensions = (160, 120)
        self.asset_dir = self.base_asset_dir / "pay-category"
        self.asset_name = f"{category_id}.img"


class TVScreenAsset(Asset):
    """Used in both the Normal and Theatre room TV's"""

    def __init__(self, seq: int, is_theatre: bool, is_movie: bool):
        if is_theatre:
            asset_dir = "pay-intro"
        else:
            asset_dir = "normal-intro"

        if is_movie:
            asset_name = f"{seq}-1.mov"
        else:
            asset_name = f"{seq}-1.img"

        self.dimensions = (832, 456)
        self.asset_dir = self.base_asset_dir / asset_dir
        self.asset_name = asset_name

    def upload_movie(self, in_bytes: Union[bytes, FileField]):
        """Uploads a movie to its proper path"""
        if isinstance(in_bytes, FileField):
            content = in_bytes.data.read()
        else:
            content = in_bytes

        self.ensure_exists()

        with open(self.asset_path(), "wb") as file:
            file.write(content)


class PosterAsset(Asset):
    """Used for posters in the Theatre or Normal room"""

    def __init__(self, seq: int, is_theatre: bool):
        if is_theatre:
            asset_dir = "pay-wall"
        else:
            asset_dir = "normal-wall"

        asset_name = f"{seq}.img"

        self.dimensions = (256, 360)
        self.asset_dir = self.base_asset_dir / asset_dir
        self.asset_name = asset_name
        self.raw_asset_name = seq

        if is_theatre:
            self.s3_tag = "pay/wall"
        else:
            self.s3_tag = "wall"

    def upload_to_s3(self, im: bytes):
        s3.upload_fileobj(
            io.BytesIO(im),
            config.r2_bucket_name,
            self.s3_path(),
            ExtraArgs={"ContentType": "image/jpeg"},
        )

        # Now for the metadata
        met = self.asset_name.replace("img", "met")
        s3.upload_fileobj(
            io.BytesIO(wall_metadata(self.raw_asset_name)),
            config.r2_bucket_name,
            self.s3_tag + "/" + met,
            ExtraArgs={"ContentType": "text/xml"},
        )


class PayMovieAsset(Asset):
    def __init__(self, seq: int):
        asset_name = f"{seq}.emo"

        self.asset_dir = self.base_asset_dir / "pay-wall"
        self.asset_name = asset_name

    def upload_movie(self, in_bytes: Union[bytes, FileField]):
        """Uploads a movie to its proper path"""
        if isinstance(in_bytes, FileField):
            content = in_bytes.data.read()
        else:
            content = in_bytes

        self.ensure_exists()

        with open(self.asset_path(), "wb") as file:
            file.write(content)
