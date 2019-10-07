import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask



basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
	config = {'SECRET_KEY': os.environ.get('SECRET_KEY') or 'password', 
		'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL') or \
    	'sqlite:///' + os.path.join(basedir, 'app.db'), 'SQLALCHEMY_TRACK_MODIFICATIONS':False}

	def configure(self, app):
		for key in self.config:
			app.config[key]= self.config[key]

app = Flask(__name__)
Config().configure(app)