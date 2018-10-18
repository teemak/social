from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

#FORM to pass data
class QuestionForm(FlaskForm):
    question = StringField('What is your question?', validators=[DataRequired()])
    submit = SubmitField('Submit Question')

class AnswerForm(FlaskForm):
    question_id = HiddenField('id')
    answer = TextAreaField('answer', validators=[DataRequired()])
    submit = SubmitField('submit')
