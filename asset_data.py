from asset import Asset
from typing import Union
from wtforms import FileField


class RoomLogoAsset(Asset):
    """Used for a company logo within a room."""

    def __init__(self, room_id: int):
        self.dimensions = (320, 180)
        self.asset_dir = self.base_asset_dir / "special" / f"{room_id}"
        self.asset_name = "f1234.img"


class ParadeBannerAsset(Asset):
    """Used as the logo within a parade, identifying a room."""

    def __init__(self, room_id: int):
        self.dimensions = (184, 80)
        self.asset_dir = self.base_asset_dir / "special" / f"{room_id}"
        self.asset_name = "parade_banner.jpg"


class NormalCategoryAsset(Asset):
    """Used for categories within the normal Shows tab."""

    def __init__(self, category_id: int):
        self.dimensions = (160, 120)
        self.asset_dir = self.base_asset_dir / "normal-category"
        self.asset_name = f"{category_id}.img"


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
