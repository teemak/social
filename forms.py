from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("School Email", validators=[DataRequired()])
    submit = SubmitField("Login")

#FORM to pass data
class QuestionForm(FlaskForm):
    question = StringField('What is your question?', validators=[DataRequired()])
    score = HiddenField('points')
    submit = SubmitField('Submit Question')

class AnswerForm(FlaskForm):
    question_id = HiddenField('id')
    answer = TextAreaField('answer', validators=[DataRequired()])
    submit = SubmitField('submit')
