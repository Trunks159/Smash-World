from flask import url_for, render_template
from config import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/tourney')
def tourney():
	return render_template('tourney.html')
if "__name__" == "__main__":
	app.run(debug = True)