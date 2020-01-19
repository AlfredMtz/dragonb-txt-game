from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from dragonb_game.models import User


class RegistrationForm(FlaskForm):
    # VALIDATORS:
    # DataRequired() -- Field can not be empty
    # Length() -- Min and Max characters allow in the field
    # Email() -- Makes sure user inputs a valid email address
    # EqualTo() -- Makes sure the the confirm password is the same as inputed password
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password',
                                     validators=[DataRequired(), EqualTo('password')])
    # This is a button which will submit all the inputted form's data
    submit = SubmitField('Sign Up')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


    def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email=StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # BooleanField -- Allows users to stay login sometime after they loged in by using a secure cookie
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

    # Validates whether the new username is different then current username
    def validate_username(self, username):
        if username.data != current_user.username:
            # .first() -- returns first result with the database that meets the conditions IF there is one.
            user = User.query.filter_by(username=username.data).first()
            # If there is an username within the database already in use, the below message will be thrown. Else, nothing will happend.
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
    
    # Validates whether the new email is different then current email
    def validate_email(self, email):
        # Conditional validation
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

# Hinherits functionality from FlaskForm
class RequestResetForm(FlaskForm):
    # Fields the form will have
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    #Checks if email doesn't exists
    def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            # if user doesn't exist
            if user is None:
                raise ValidationError(
                    'There is no account with that email, you must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
