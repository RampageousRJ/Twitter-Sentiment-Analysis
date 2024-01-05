from wtforms.validators import DataRequired
from wtforms import TextAreaField,SubmitField
from flask_wtf import FlaskForm,RecaptchaField

class TweetForm(FlaskForm):
    tweet = TextAreaField(label="Enter tweet",validators=[DataRequired()])
    recaptcha = RecaptchaField(validators=[DataRequired()])
    submit = SubmitField(label="Submit")