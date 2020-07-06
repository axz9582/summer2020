from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    keep_signed_in = BooleanField("Keep me signed in")
    submit = SubmitField("Sign in")


class CreateAccountForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm = PasswordField("Confirm your password", validators=[DataRequired(),
                                                                 EqualTo("password", message="Passwords must match")])
    submit = SubmitField("Create Account")
