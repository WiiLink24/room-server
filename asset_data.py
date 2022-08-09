from asset import Asset


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
