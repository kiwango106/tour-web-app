from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=200)])
    body = TextAreaField('Content', validators=[Length(min=10)])
    published = BooleanField('Publish immediately')
    submit = SubmitField('Save Post')
