import enum

from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.query import Query
from sqlalchemy import func, String, ForeignKey, LargeBinary, BigInteger, JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_searchable import make_searchable
from sqlalchemy_utils import TSVectorType
from datetime import datetime
from typing import Optional
from wtforms.fields import SelectField

import sqlalchemy
import json

db = SQLAlchemy()


class Locale(enum.Enum):
    """Locale are the codes for various languages.
    TODO: We do not follow any standard which is not terrible but still, we should fix in the next patch release.
    """

    jp = "Japanese"
    Ge = "German"
    En = "English"
    Fr = "French"
    Sp = "Spanish"
    Du = "Dutch"
    It = "Italian"
    ptbr = "Portuguese"
    ru = "Russian"

    @classmethod
    def choices(cls):
        return [(choice, choice.value) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(item) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class RoomMenu(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    room_id: Mapped[int]
    data: Mapped[bytes] = mapped_column(
        JSONB
    )  # This is a dict with keys in it for that type.


class Posters(db.Model):
    poster_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    msg: Mapped[str] = mapped_column(String(15))
    movie_id: Mapped[int]
    # While a maximum of 47 characters seems arbitrary, it is what it is.
    # It appears they mandate the last byte in their char array is null (and sprintf),
    # so perhaps the internal type is char[48]?
    title: Mapped[str] = mapped_column(String(47))
    locale: Mapped[Locale]


class News(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    msg: Mapped[str] = mapped_column(String(146))
    locale: Mapped[Locale]


class PayPosters(db.Model):
    poster_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    msg: Mapped[str] = mapped_column(String(15))
    title: Mapped[str] = mapped_column(String(47))
    type: Mapped[int]
    aspect: Mapped[bool]
    locale: Mapped[Locale]


class ConciergeMiiActions(enum.Enum):
    NormalMaleA = 1
    NormalFemaleS = 2
    NormalMaleS = 3
    NormalFemaleS2 = 4
    NormalMaleS2 = 5
    CheerfulMaleA = 6
    CheerfulFemaleS = 7
    CheerfulMaleS = 8
    SaluteMaleA = 9
    SaluteFemaleS = 10
    SaluteMaleS = 11
    ForeignerA = 12
    ForeignerS = 13
    CelebrityA = 14
    CelebrityS = 15
    CelebrationA = 16
    CelebrationS = 17
    AmazingA = 18
    AmazingS = 19
    GreetingS = 20
    ApologyS = 21
    Zundoko = 24
    Takeshi = 25

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class ConciergeMiis(db.Model):
    mii_id: Mapped[int] = mapped_column(
        ForeignKey("mii_data.mii_id"), primary_key=True, unique=True
    )
    clothes: Mapped[int]
    action: Mapped[ConciergeMiiActions]
    prof: Mapped[str] = mapped_column(String(129))
    movie_id: Mapped[int]
    voice: Mapped[bool] = mapped_column(default=False)
    locale: Mapped[Locale]


# MiiData provides the genuine Mii alongside other common information.
class MiiData(db.Model):
    mii_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    data: Mapped[LargeBinary] = mapped_column(LargeBinary(74))
    name: Mapped[str] = mapped_column(String(10))
    color1: Mapped[str] = mapped_column(String(6))
    color2: Mapped[str] = mapped_column(String(6))


class MiiMsgInfo(db.Model):
    # We make both the Mii's ID and message type unique, as to allow row
    # identification for SQLAlchemy.
    mii_id: Mapped[int] = mapped_column(ForeignKey("mii_data.mii_id"), primary_key=True)
    type: Mapped[int] = mapped_column(primary_key=True)
    seq: Mapped[int] = mapped_column(primary_key=True)
    msg: Mapped[str] = mapped_column(String(51))
    face: Mapped[int]


make_searchable(db.metadata)


class FullTextSearchable(Query):
    pass


class MovieGenres(enum.Enum):
    """For localization’s sake, we use the colours rather than the meanings."""

    White = 0
    Gray = 1
    Green = 2
    Orange = 3
    Pink = 4
    Blue = 5

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class Movies(db.Model):
    query_class = FullTextSearchable

    movie_id: Mapped[int] = mapped_column(
        autoincrement=True, primary_key=True, unique=True
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.category_id"),
        primary_key=True,
    )
    title: Mapped[str] = mapped_column(String(47))
    length: Mapped[str] = mapped_column(String(8))
    aspect: Mapped[bool]
    genre: Mapped[MovieGenres]
    sp_page_id: Mapped[int]
    ds_mov_id: Mapped[Optional[int]]
    staff: Mapped[bool]
    date_added: Mapped[datetime] = mapped_column(server_default=func.now())
    unlisted: Mapped[bool] = mapped_column(default=False)

    search_vector = mapped_column(TSVectorType("title"))


class PayMovies(db.Model):
    query_class = FullTextSearchable

    movie_id: Mapped[int] = mapped_column(
        autoincrement=True, primary_key=True, unique=True
    )
    title: Mapped[str] = mapped_column(String(47))
    length: Mapped[str]
    note: Mapped[str] = mapped_column(String(76))
    price: Mapped[int]
    released: Mapped[str] = mapped_column(String(10))
    category_id: Mapped[int] = mapped_column(
        ForeignKey("pay_categories.category_id"),
        primary_key=True,
    )
    reference_id: Mapped[str] = mapped_column(String(32))
    # Must be 7 digits long
    price_code: Mapped[int] = mapped_column(autoincrement=True)
    date_added: Mapped[datetime] = mapped_column(server_default=func.now())
    search_vector = db.Column(TSVectorType("title", "note"))


class PayCategories(db.Model):
    category_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String(61))
    # Starts at 10, goes up by 1 each time
    genre_id: Mapped[Optional[int]]
    sp_page_id: Mapped[Optional[int]]
    locale: Mapped[Locale]


class PayCategoryHeaders(db.Model):
    title: Mapped[str] = mapped_column(String(30), primary_key=True, unique=True)


class Categories(db.Model):
    category_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String(61))
    sp_page_id: Mapped[Optional[int]]
    unlisted: Mapped[bool] = mapped_column(default=False)
    locale: Mapped[Locale]


class RoomBGMTypes(enum.Enum):
    SOFT_GUITAR = 1
    NORMAL = 2
    FOLK = 3
    JAZZY = 4
    TRUMPET = 5
    CHIMES = 6
    WESTERN = 7
    HARP = 8

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class RoomContentBGMTypes(enum.Enum):
    Sadness = 1
    Upbeat = 2
    Relaxing = 3
    Classical = 4
    Playful = 5
    Chill = 6
    Adventurous = 7
    Jolly = 8
    Happiness = 9
    Casino = 10
    Parade = 11
    Excitement = 12
    idk = 13

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class Rooms(db.Model):
    room_id: Mapped[int] = mapped_column(
        autoincrement=True, primary_key=True, unique=True
    )
    bgm: Mapped[RoomBGMTypes]
    parade_mii: Mapped[int] = mapped_column(ForeignKey("mii_data.mii_id"))
    mascot: Mapped[bool]
    # Each message has a limit of 51. However, there can be 10 sequences. How we handle sequences is by splitting the
    # text by newline.
    intro_msg: Mapped[str]
    contact_data: Mapped[str] = mapped_column(String(2599))
    news: Mapped[str] = mapped_column(String(41))
    level: Mapped[int] = mapped_column(default=1)
    locale: Mapped[Locale]


class RoomMiis(db.Model):
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.room_id"))
    mii_id: Mapped[int] = mapped_column(
        ForeignKey("mii_data.mii_id"), unique=True, primary_key=True
    )
    # Same thing as intro_msg in Rooms.
    mii_msg: Mapped[str]
    seq: Mapped[int]


class EvaluateData(db.Model):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    movie_id: Mapped[int] = mapped_column(index=True)
    gender: Mapped[int]
    blood: Mapped[int]
    age: Mapped[int]
    vote: Mapped[int]


class PollData(db.Model):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    poll_id: Mapped[int] = mapped_column(index=True)
    wii_num: Mapped[int] = mapped_column(BigInteger)
    choice: Mapped[int]
    age: Mapped[int]
    gender: Mapped[int]


class ContentTypes(enum.Enum):
    Video = 0
    Image = 1

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class LinkTypes(enum.Enum):
    Regular = 0
    TheatreMovie = 1
    TheatreCategory = 2
    Shop = 3
    Room = 4
    Category = 5

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class IntroInfo(db.Model):
    cnt_id: Mapped[int] = mapped_column(
        BigInteger, autoincrement=True, primary_key=True, unique=True
    )
    cnt_type: Mapped[ContentTypes]
    cat_name: Mapped[Optional[str]] = mapped_column(String(61))
    link_type: Mapped[LinkTypes]
    link_id: Mapped[Optional[int]]
    position: Mapped[int]
    locale: Mapped[Locale]


class Giveaways(db.Model):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    giveaway_id: Mapped[int]
    wii_id: Mapped[str]
    email: Mapped[str]


class MovieCredits(db.Model):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.movie_id"))
    role: Mapped[str] = mapped_column(String(30), nullable=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    order: Mapped[int]


class ConciergeMovies(db.Model):
    """Movies that are linked to a concierge."""

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.movie_id"), nullable=False)
    mii_id: Mapped[int] = mapped_column(ForeignKey("mii_data.mii_id"), nullable=False)


class Logs(db.Model):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    action: Mapped[str]
    user: Mapped[str]
    timestamp: Mapped[datetime]
