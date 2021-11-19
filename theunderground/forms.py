from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    FileField,
    SelectField,
    TextAreaField,
    BooleanField,
)
from wtforms.validators import DataRequired, Length, ValidationError

from models import RoomBGMTypes, RoomContentBGMTypes

"""
Reference:
        movie_id = form.movie_id.data
        place = form.place.data
        imageid = form.imageid.data
        title = form.title.data
"""


class RoomMovieForm(FlaskForm):
    movie_id = StringField("Movie ID")
    place = StringField("Place in Room")
    imageid = StringField("Image ID")
    title = StringField("Movie Title")
    submit = SubmitField("Done!")


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField("Enter the underground")


class NewsForm(FlaskForm):
    news = TextAreaField("News Contents", validators=[DataRequired()])
    create = SubmitField("Create!")


class MiiUploadForm(FlaskForm):
    mii = FileField("Mii Selection", validators=[FileRequired()])
    name = StringField("Mii Name", validators=[DataRequired()])
    color1 = StringField("Shirt Color (Hex)", validators=[DataRequired()])
    color2 = StringField("Pants Color (Hex)", validators=[DataRequired()])
    upload = SubmitField("Add Mii")


class NewUserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password1 = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Confirm Password", validators=[DataRequired()])
    upload = SubmitField("Complete")

    def validate_password1(self, _):
        if self.password1.data != self.password2.data:
            return ValidationError("New passwords must be the same")


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField("Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[DataRequired()])
    new_password_confirmation = PasswordField(
        "Confirm New Password", validators=[DataRequired()]
    )
    complete = SubmitField("Complete")

    def validate_current_password(self, _):
        if self.current_password.data == self.new_password.data:
            return ValidationError("New password cannot be the same as current!")

    def validate_new_password(self, _):
        if self.new_password.data != self.new_password_confirmation.data:
            return ValidationError("New passwords must be the same")


class MovieUploadForm(FlaskForm):
    movie = FileField("Movie", validators=[FileRequired()])
    title = StringField("Movie title", validators=[DataRequired(), Length(max=48)])
    thumbnail = FileField("Movie thumbnail", validators=[FileRequired()])
    # Choices for the select field are only evaluated once, so we must set it when necessary.
    category = SelectField("Movie category", validators=[DataRequired()])
    upload = SubmitField("Add Movie")


class PayMovieUploadForm(FlaskForm):
    movie = FileField("Trailer", validators=[FileRequired()])
    poster = FileField("Poster", validators=[FileRequired()])
    thumbnail = FileField("Thumbnail", validators=[FileRequired()])
    # For now there is a 15 char limit for the title. If we edit the brlyt we can unlock this.
    title = StringField("Title", validators=[DataRequired()])
    release = StringField(
        "Release Date(YYYY-MM-DD)", validators=[DataRequired(), Length(max=10)]
    )
    note = StringField("Description", validators=[DataRequired()])
    price = StringField("Price", validators=[DataRequired()])
    category = SelectField("Movie Category", validators=[DataRequired()])
    upload = SubmitField("Add Movie")


class CategoryAddForm(FlaskForm):
    category_name = StringField("Category Name", validators=[DataRequired()])
    thumbnail = FileField("Movie thumbnail", validators=[FileRequired()])
    submit = SubmitField("Add")


class CategoryEditForm(FlaskForm):
    category_name = StringField("Category Name", validators=[DataRequired()])
    thumbnail = FileField("Movie thumbnail")
    submit = SubmitField("Edit")


class ParadeForm(FlaskForm):
    room_id = StringField("Room ID", validators=[DataRequired()])
    mii_msg = StringField("Mii Message", validators=[DataRequired()])
    image = FileField("Parade Banner")
    submit = SubmitField("Create")


class RoomForm(FlaskForm):
    mii_id = StringField("Intro Message")
    bgm = SelectField(
        "Background Music",
        choices=RoomBGMTypes.choices(),
        coerce=RoomBGMTypes.coerce,
    )
    room_logo = FileField("Room Logo", validators=[FileRequired()])
    has_mascot = BooleanField("Mascot Enabled")
    has_contact = BooleanField("Show Contact Information")
    intro_msg = StringField("Intro Message", validators=[DataRequired()])
    news = StringField("Company", validators=[DataRequired()])
    contact = StringField("Contact Information", validators=[DataRequired()])
    submit = SubmitField("Create")


class PreRoomData(FlaskForm):
    type = SelectField(
        "Type",
        choices=[("Delivery"), ("Poll"), ("Movie"), ("Coupon"), ("Link"), ("Picture")],
    )
    next = SubmitField("Next")


class RoomDeliveryData(FlaskForm):
    movie = FileField("Movie", validators=[FileRequired()])
    title = StringField("Title", validators=[DataRequired()])
    tv = FileField("TV Screen Image", validators=[FileRequired()])
    image = FileField("Image After Movie", validators=[FileRequired()])
    upload = SubmitField("Upload")


class RoomVoteData(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    tv = FileField("TV Screen Image", validators=[FileRequired()])
    image1 = FileField("Answer Photo 1", validators=[FileRequired()])
    image2 = FileField("Answer Photo 2", validators=[FileRequired()])
    image3 = FileField("Answer Photo 3", validators=[FileRequired()])
    question = StringField("Question", validators=[DataRequired()])
    mii_msg = StringField("Mii Message", validators=[DataRequired()])
    upload = SubmitField("Upload")


class RoomMovieData(FlaskForm):
    movie_id = StringField(
        "Movie ID(Make sure you know the ID of the movie you want)",
        validators=[DataRequired()],
    )
    title = StringField("Title", validators=[DataRequired()])
    image = FileField("TV Screen Image", validators=[FileRequired()])
    upload = SubmitField("Upload")


class RoomLinkData(FlaskForm):
    bgm = SelectField(
        "Background Music",
        choices=RoomContentBGMTypes.choices(),
        coerce=RoomContentBGMTypes.coerce,
    )
    title = StringField("Title", validators=[DataRequired()])
    link = StringField("Link", validators=[DataRequired()])
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
    title = StringField("Title", validators=[DataRequired()])
    tv = FileField("TV Screen Image", validators=[FileRequired()])
    image1 = FileField("Image 1", validators=[FileRequired()])
    image2 = FileField("Image 2", validators=[FileRequired()])
    image3 = FileField("Image 3", validators=[FileRequired()])
    upload = SubmitField("Upload")


class DeleteForm(FlaskForm):
    given_id = StringField("ID", validators=[DataRequired()])
    submit = SubmitField("Delete")


class ConciergeForm(FlaskForm):
    prof = StringField("Profession", validators=[DataRequired()])
    message1 = StringField("Message 1", validators=[DataRequired()])
    message2 = StringField("Message 2", validators=[DataRequired()])
    message3 = StringField("Message 3", validators=[DataRequired()])
    message4 = StringField("Message 4", validators=[DataRequired()])
    message5 = StringField("Message 5", validators=[DataRequired()])
    message6 = StringField("Message 6", validators=[DataRequired()])
    message7 = StringField("Message 7", validators=[DataRequired()])
    movieid = StringField("Movie ID", validators=[DataRequired()])
    submit = SubmitField("Create!")


class PosterForm(FlaskForm):
    file = FileField("Poster Image", validators=[FileRequired()])
    title = StringField("Title", validators=[DataRequired()])
    msg = StringField("Message", validators=[DataRequired()])
    upload = SubmitField("Create Poster!")
