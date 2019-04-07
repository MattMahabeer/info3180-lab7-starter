from wtforms import TextAreaField, StringField, SelectField
from wtforms.validators import Email, InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import FlaskForm
class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[InputRequired(message='A description is required.')])
    photo = FileField('Upload Photo', validators=[FileRequired('Upload Photo'), FileAllowed(['jpg', 'jpeg', 'png'], 'You can only upload images')])
    

