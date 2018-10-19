from flask import Flask, render_template, url_for, request, redirect
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from forms import QuestionForm, AnswerForm
from config import url

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hackathon'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#DB OBJECT
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(120), nullable=False)
    #Column answer called answer_list
    answers = db.relationship('Answer', backref="answer_list", lazy=True)

    def __repr__(self):
        return f"{self.question}"

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(250), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

    def __repr__(self):
        return f"{self.answer}"

@app.route('/')
def index():
    questions = Question.query.all()
    return render_template('index.html', questions=questions)

@app.route('/question/<int:id>')
def get_question(id):
    form = AnswerForm(question_id=id)

    query = Question.query.get_or_404(id)
    return render_template('question.html', query=query, form=form)

@app.route('/answer_question', methods=["GET", "POST"])
def answer_question():
    form = AnswerForm()
    
    if form.validate_on_submit():
        id = form.question_id.data
        print('This is the question_id: ', id)
        answer = Answer(answer=form.answer.data, question_id=id)
        db.session.add(answer)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('answer.html')

@app.route('/add_question', methods=["GET","POST"])
def add_question():
    #Pass form to template
    form = QuestionForm()
    
    if form.validate_on_submit():
        #save data to db
        data = Question(question=form.question.data)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_question.html', form=form)

@app.route('/api/all_questions')
def all_questions():
    query = Question.query.all()
    return render_template('all_questions.html', query=query)

@app.route('/api/all_answers')
def all_answers():
    query = Answer.query.all()
    return render_template('all_answers.html', query=query)

@app.route('/account/')
def get_account():
    return render_template('account.html')


if __name__ == "__main__":
    app.run()
