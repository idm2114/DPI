from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import TypeDecorator, VARCHAR
from sqlalchemy_utils import ChoiceType
from flask_migrate import Migrate
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Enrolled(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_uni = db.Column(db.String(12), db.ForeignKey('student.uni'), index=True)
	course_number = db.Column(db.Integer, db.ForeignKey('course.call_number'), index=True)

	semester = db.Column(db.String(8))
	year = db.Column(db.Integer)

	students = db.relationship("Student", back_populates="courses")
	courses = db.relationship("Course", back_populates="students")

class Course(db.Model):
	call_number = db.Column(db.Integer, primary_key = True)
	course_name = db.Column(db.String(32), unique = True)
	professor = db.Column(db.String(32))

	students = db.relationship("Enrolled", back_populates="courses")
	videos = db.relationship('Video', backref='course')

	def __repr__(self):
		return '<Course {}>'.format(self.course_name)

class Student(db.Model):
	uni = db.Column(db.String(12), primary_key=True)
	password_hash = db.Column(db.String(128))
	name = db.Column(db.String(64))
	lastname = db.Column(db.String(64))
	email = db.Column(db.String(120), index=True, unique=True)
	school = db.Column(ChoiceType([(u"CC", u"Columbia College"), (u"SEAS", u"SEAS"), (u"Barnard", u"Barnard")]))

	courses = db.relationship("Enrolled", back_populates='students')
	videos = db.relationship('Video', backref='author', lazy='dynamic')
	comments = db.relationship('Comment', backref='author', lazy='dynamic')

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<Student {}>'.format(self.uni)


class Video(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	link = db.Column(db.String(128))
	title = db.Column(db.String(64))
	description = db.Column(db.Text)
	timestamp = db.Column(db.DateTime, default=datetime.now)
	author_uni = db.Column(db.String(12), db.ForeignKey('student.uni'))
	course_id = db.Column(db.Integer, db.ForeignKey('course.call_number'))

	def __repr__(self):
		return '<Video {}>'.format(self.title)

# Still trying to figure out how an array works here
class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	comments = db.Column(db.Text)
	author = db.Column(db.String(12), db.ForeignKey('student.uni'))

	def __repr(self):
		return 'Comment'.format(self.comments)

class Thread(db.Model):
	id = db.Column(db.Integer.primary_key=True)
	thread = 

# 	array of comments with user id


# from Lacuna_DB import db, Video, Student, Course, Enrolled
# db.create_all()
# u = Student(uni="yc3877", password_hash='lala', name='alice', lastname='alice', email='yc3877@columbia.edu', school='SEAS')
# v = Video(link="examplelink.com", title="example video", description="This is a example video", author_uni="yc3877", course_id="13778")
# e = Enrolled(semester='Spring', year=2021)
# c = Course(call_number=13778, course_name="ECON", professor="gulati")
