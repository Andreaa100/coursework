from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from wtforms import HiddenField, IntegerField
from wtforms.validators import NumberRange


class AddToCartForm(FlaskForm):
    product_id = HiddenField('Product ID', validators=[DataRequired()])
    quantity = IntegerField('Quantity', default=1, validators=[DataRequired(), 
        NumberRange(min=1)])
    submit = SubmitField('Add to Cart')

class AddToFavoriteForm(FlaskForm):
    product_id = HiddenField('Product ID', validators=[DataRequired()])
    submit = SubmitField('Add to Favorites')

class RegistrationForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
        ],
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6),
        ],
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password'),
        ],
    )
    name = StringField(
        'Name',
        validators=[
            DataRequired(),
            Length(min=1, max=50),
        ],
    )
    surname = StringField(
        'Surname',
        validators=[
            DataRequired(),
            Length(min=1, max=50),
        ],
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
