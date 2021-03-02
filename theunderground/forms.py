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

from models import RoomBGMTypes

"""
Reference:
        movie_id = form.movie_id.data
        place = form.place.data
        imageid = form.imageid.data
        title = form.title.data
"""


class RoomLinkForm(FlaskForm):
    place = StringField("Place in Room")
    imageid = StringField("Image ID")
    linkid = StringField("Link ID")
    title = StringField("Link Title")
    url = StringField("Link")
    submit = SubmitField("Done!")

class RoomSMPForm(FlaskForm):
    title = StringField("Delivery Title")
    url = StringField("Callback URL")
    submit = SubmitField("Done!")

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


class ParadeForm(FlaskForm):
    news = StringField("News", validators=[DataRequired()])
    company = StringField("Company", validators=[DataRequired()])
    image = FileField("Parade Banner", validators=[FileRequired()])
    submit = SubmitField("Create")


class RoomForm(FlaskForm):
    bgm = SelectField(
        "Background Music",
        choices=RoomBGMTypes.choices(),
        coerce=RoomBGMTypes.coerce,
    )
    room_logo = FileField("Room Logo", validators=[FileRequired()])
    has_mascot = BooleanField("Mascot Enabled")
    has_contact = BooleanField("Show Contact Information")
    intro_msg = StringField("Intro Message", validators=[DataRequired()])
    mii_msg = StringField("Mii Message", validators=[DataRequired()])
    submit = SubmitField("Create")


class KillMii(FlaskForm):
    # Form for deleting a concierge mii
    given_mii_id = StringField("Mii ID", validators=[DataRequired()])
    submit = SubmitField("Delete!")


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
