from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class ItineraryForm(FlaskForm):
    title = StringField('Itinerary Title', validators=[DataRequired(), Length(min=5, max=200)])
    destination = StringField('Destination', validators=[DataRequired()])
    duration_days = IntegerField('Number of Days', validators=[
        DataRequired(), NumberRange(min=1, max=3)
    ])
    submit = SubmitField('Create Itinerary')


class DayForm(FlaskForm):
    title = StringField('Day Title', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Description')
    accommodation = StringField('Accommodation', validators=[Length(max=200)])
    submit = SubmitField('Save Day')
