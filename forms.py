from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, ValidationError,EmailField,BooleanField,IntegerField, DateField, HiddenField
from wtforms.validators import InputRequired,Email,EqualTo,Length,email_validator

class LoginForm(FlaskForm):
    username = StringField(label='Enter your username',validators = [InputRequired()])
    email = EmailField(label='Your Email Address',validators=[InputRequired(),Email()])
    password = PasswordField(label='Password',validators = [InputRequired(), Length(min=5, max = 50)])
    remember = BooleanField(label='Remember me')
    submit = SubmitField(label='Login')

class SignupForm(FlaskForm):
    first_name = StringField(label='First Name',validators=[InputRequired()])
    last_name = StringField(label=' Last Name',validators=[InputRequired()])
    username = StringField(label='Username',validators=[InputRequired()])
    email = EmailField(label='Email',validators=[InputRequired(),Email(message = 'Invalid Email')])
    password = PasswordField(label='Password',validators = [InputRequired(),Length(min=5, max=50)])
    submit = SubmitField(label='Sign Up')

class PitchesForm(FlaskForm):
    pitch = StringField(label='pitch',validators=[InputRequired(), Length(min=10, max=100)])
    category = StringField(label='category',validators=[InputRequired()])
    user_id = HiddenField(label='user_id')
    submit = SubmitField(label='Submit')

class CommentsForm(FlaskForm):
    comment = StringField(label='comment')




    

