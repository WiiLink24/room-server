from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import (
    StringField,
    SubmitField,
    FileField,
    SelectField,
    TextAreaField,
    BooleanField,
    IntegerField,
    FieldList,
)
from wtforms.validators import DataRequired, Length

from models import (
    RoomBGMTypes,
    RoomContentBGMTypes,
    ContentTypes,
    LinkTypes,
    ConciergeMiiActions,
    MovieGenres,
)

"""
Reference:
        movie_id = form.movie_id.data
        place = form.place.data
        imageid = form.imageid.data
        title = form.title.data
"""


class NewsForm(FlaskForm):
    news = TextAreaField("News Contents", validators=[DataRequired(), Length(max=146)])
    create = SubmitField("Create!")


class MiiUploadForm(FlaskForm):
    mii = FileField("Mii Selection")
    name = StringField("Mii Name", validators=[DataRequired(), Length(max=10)])
    color1 = StringField(
        "Shirt Color (Hex)", validators=[DataRequired(), Length(max=6)]
    )
    color2 = StringField(
        "Pants Color (Hex)", validators=[DataRequired(), Length(max=6)]
    )
    upload = SubmitField("Add Mii")


class MovieUploadForm(FlaskForm):
    movie = FileField("Movie")
    ds_movie = FileField("DSi Movie")
    title = StringField("Movie title", validators=[DataRequired(), Length(max=47)])
    thumbnail = FileField("Movie thumbnail")
    genre = SelectField(
        "Genre",
        choices=MovieGenres.choices(),
        coerce=MovieGenres.coerce,
    )
    # Choices for the select field are only evaluated once, so we must set it when necessary.
    category = SelectField("Movie category", validators=[DataRequired()])
    room = SelectField("Room", validators=[DataRequired()])
    upload = SubmitField("Add Movie")


class PayMovieUploadForm(FlaskForm):
    movie = FileField("Trailer", validators=[FileRequired()])
    poster = FileField("Poster", validators=[FileRequired()])
    thumbnail = FileField("Thumbnail", validators=[FileRequired()])
    # For now there is a 15 char limit for the title. If we edit the brlyt we can unlock this.
    title = StringField("Title", validators=[DataRequired(), Length(max=47)])
    release = StringField(
        "Release Date(YYYY-MM-DD)", validators=[DataRequired(), Length(max=10)]
    )
    price_code = IntegerField("Price Code", validators=[DataRequired()])
    ref_id = StringField("Reference ID", validators=[DataRequired(), Length(min=16)])
    note = StringField("Description", validators=[DataRequired(), Length(max=76)])
    price = StringField("Price", validators=[DataRequired()])
    category = SelectField("Movie Category", validators=[DataRequired()])
    upload = SubmitField("Add Movie")


class CategoryForm(FlaskForm):
    category_name = StringField(
        "Category Name", validators=[DataRequired(), Length(max=61)]
    )
    room = SelectField("Room", validators=[DataRequired()])
    thumbnail = FileField("Category Thumbnail")
    submit = SubmitField("Add")


class RoomForm(FlaskForm):
    mii = FieldList(StringField())
    bgm = SelectField(
        "Background Music",
        choices=RoomBGMTypes.choices(),
        coerce=RoomBGMTypes.coerce,
    )
    room_logo = FileField("Room Logo")
    parade_banner = FileField("Parade Banner")
    category_logo = FileField("Category Logo")
    mascot = FileField("Mascot")
    has_mascot = BooleanField("Mascot Enabled")
    intro_msg = TextAreaField("Intro Message", validators=[DataRequired()])
    news = StringField("Company", validators=[DataRequired(), Length(max=41)])
    # PostgreSQL treats an empty string ('') separately from NULL (None in Python).
    # https://stackoverflow.com/a/21853689
    contact = StringField("Contact Information", filters=[lambda x: x or None])
    submit = SubmitField("Create")


class PreRoomData(FlaskForm):
    type = SelectField(
        "Type",
        choices=["Delivery", "Poll", "Movie", "Coupon", "Website Link", "Picture"],
    )
    next = SubmitField("Next")


class RoomDeliveryData(FlaskForm):
    movie = FileField("Movie", validators=[FileRequired()])
    title = TextAreaField("Title", validators=[DataRequired(), Length(max=47)])
    tv = FileField("TV Screen Image", validators=[FileRequired()])
    image = FileField("Image After Movie", validators=[FileRequired()])
    upload = SubmitField("Upload")


class RoomVoteData(FlaskForm):
    title = TextAreaField("Title", validators=[DataRequired(), Length(max=47)])
    tv = FileField("TV Screen Image", validators=[FileRequired()])
    image1 = FileField("Answer Photo 1", validators=[FileRequired()])
    image2 = FileField("Answer Photo 2", validators=[FileRequired()])
    image3 = FileField("Answer Photo 3", validators=[FileRequired()])
    question = StringField("Question", validators=[DataRequired(), Length(max=41)])
    mii_msg = TextAreaField("Mii Message", validators=[DataRequired(), Length(max=51)])
    upload = SubmitField("Upload")


class RoomMovieData(FlaskForm):
    movie_id = StringField(
        "Movie ID(Make sure you know the ID of the movie you want)",
        validators=[DataRequired()],
    )
    title = TextAreaField("Title", validators=[DataRequired(), Length(max=47)])
    image = FileField("TV Screen Image", validators=[FileRequired()])
    upload = SubmitField("Upload")


class RoomLinkData(FlaskForm):
    bgm = SelectField(
        "Background Music",
        choices=RoomContentBGMTypes.choices(),
        coerce=RoomContentBGMTypes.coerce,
    )
    is_internet_channel = BooleanField(
        "Launch Internet Channel", validators=[DataRequired()]
    )
    title = TextAreaField("Title", validators=[DataRequired(), Length(max=47)])
    link = StringField("Link", validators=[DataRequired(), Length(max=100)])
    tv = FileField("TV Screen Image", validators=[FileRequired()])
    image1 = FileField("Image After Movie", validators=[FileRequired()])
    image2 = FileField("Link Image", validators=[FileRequired()])
    movie = FileField("Movie", validators=[FileRequired()])
    upload = SubmitField("Upload")


class RoomPicData(FlaskForm):
    bgm = SelectField(
        "Background Music",
        choices=RoomContentBGMTypes.choices(),
        coerce=RoomContentBGMTypes.coerce,
    )
    title = TextAreaField("Title", validators=[DataRequired(), Length(max=47)])
    tv = FileField("TV Screen Image", validators=[FileRequired()])
    image1 = FileField("Image 1", validators=[FileRequired()])
    image2 = FileField("Image 2", validators=[FileRequired()])
    image3 = FileField("Image 3", validators=[FileRequired()])
    upload = SubmitField("Upload")


class DeleteForm(FlaskForm):
    given_id = StringField("ID", validators=[DataRequired()])
    submit = SubmitField("Delete")


class ConciergeForm(FlaskForm):
    prof = TextAreaField("Profession", validators=[DataRequired(), Length(max=129)])

    action = SelectField(
        "Mii Action",
        choices=ConciergeMiiActions.choices(),
        coerce=ConciergeMiiActions.coerce,
    )

    # Message fields
    message1 = TextAreaField("Message 1", validators=[DataRequired()])
    message2 = TextAreaField("Message 2", validators=[])
    message3 = TextAreaField("Message 3", validators=[])
    message4 = TextAreaField("Message 4", validators=[])
    message5 = TextAreaField("Message 5", validators=[])
    message6 = TextAreaField("Message 6", validators=[])
    message7 = TextAreaField("Message 7", validators=[])

    face_choices = [
        (1, "Neutral"),
        (2, "Smiley"),
        (3, "Angry"),
        (4, "Sad"),
        (5, "Astonished"),
        (6, "Blissed"),
        (7, "Shocked"),
    ]

    # Face expression fields for each message
    action1 = SelectField(
        "Face Expression", choices=face_choices, coerce=int, default=1
    )
    action2 = SelectField(
        "Face Expression", choices=face_choices, coerce=int, default=1
    )
    action3 = SelectField(
        "Face Expression", choices=face_choices, coerce=int, default=1
    )
    action4 = SelectField(
        "Face Expression", choices=face_choices, coerce=int, default=1
    )
    action5 = SelectField(
        "Face Expression", choices=face_choices, coerce=int, default=1
    )
    action6 = SelectField(
        "Face Expression", choices=face_choices, coerce=int, default=1
    )
    action7 = SelectField(
        "Face Expression", choices=face_choices, coerce=int, default=1
    )

    movieid = StringField("Movie ID", validators=[DataRequired()])
    submit = SubmitField("Save")


class PosterForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=47)])
    msg = StringField("Message", validators=[DataRequired(), Length(max=15)])
    movie_id = IntegerField("Movie ID", validators=[DataRequired()])
    poster = FileField("Poster")
    upload = SubmitField("Create Poster!")


class PayPosterForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=47)])
    msg = StringField("Message", validators=[DataRequired(), Length(max=15)])
    poster = FileField("Poster")
    movie = FileField("Movie")
    upload = SubmitField("Create Poster!")


class IntroInfoForm(FlaskForm):
    cnt_type = SelectField(
        "Content Type", choices=ContentTypes.choices(), coerce=ContentTypes.coerce
    )
    link_type = SelectField(
        "Link Type", choices=LinkTypes.choices(), coerce=LinkTypes.coerce
    )
    link_id = IntegerField("Link ID")
    cat_name = StringField("Category Name", validators=[Length(max=61)])
    asset = FileField("Asset", validators=[FileRequired()])
    upload = SubmitField("Create Intro Info!")


class PayCategoryHeaderForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Create!")


class CreditsForm(FlaskForm):
    role_and_name_list = FieldList(StringField())
    submit = SubmitField("Create!")


class RoomCouponData(FlaskForm):
    title = TextAreaField("Title", validators=[DataRequired(), Length(max=47)])
    tv = FileField("TV Screen Image", validators=[FileRequired()])
    image_after = FileField("Image After Movie", validators=[FileRequired()])
    movie = FileField("Movie", validators=[FileRequired()])
    coupon = FileField("Coupon", validators=[FileRequired()])
    upload = SubmitField("Upload")


class ConciergeMovieForm(FlaskForm):
    movie_id = StringField("Movie ID", validators=[DataRequired()])
    submit = SubmitField("Submit")
