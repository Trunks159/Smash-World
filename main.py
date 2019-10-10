from flask import url_for, render_template, redirect
from config import app, db
from forms import LoginForm
from models import User


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/login', methods = ['GET', 'Post'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('index'))
	return render_template('login.html', form = form)

@app.route('/tourney')
def tourney():
	return render_template('tourney.html')
if "__name__" == "__main__":
	app.run(debug = True)