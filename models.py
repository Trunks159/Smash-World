from config import db
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from config import login
from hashlib import md5

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	password_hash = db.Column(db.String(128))
	#posts = db.relationship('Post', backref='author', lazy='dynamic')
	about_me = db.Column(db.String(140))
	#last_seen = db.Column(db.DateTime, default=datetime.utcnow)


	#def avatar(self, size):
	#	digest = md5(self.email.lower().encode('utf-8')).hexdigest()
	#	return 'https://www.gravatar.com/avatar/:{}?d=identicon&s={}'.format(digest, size)

	def __repr__(self):
		return 'User {}'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)