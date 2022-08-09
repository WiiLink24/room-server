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
