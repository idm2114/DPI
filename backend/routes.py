from Lacuna_DB import app, Student, Video, Course, Enrolled
from flask import render_template, redirect, url_for, request
from flask import current_user, login_user, logout_user, login_required

@app.route('/')
@app.route('/index')
@login_required
def index():
	render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
	error = None
	if current_user.is_authenticated:
		redirect(url_for('index'))
	else:
		student = Student.query.filter_by(uni=request.form['uni']).first()
		if student is None or not student.check_password(request.form['password']):
			error = "Invalid uni/password"
			return redirect(url_for('login'), error=error)
		else:
			login_user(student)
	return redirect(url_for('index'))

@app.route('/course/<int:id>', methods=['GET'])
def course():
	return render_template('course.html', course=Course.query.filter_by(call_number=id))

@app.route('/user/<string:uni>', methods=['GET', 'PATCH', 'DELETE'])
def user():
	if request.method == 'GET':
		return render_template('user.html', user=current_user)
	elif request.method == 'PATCH':
		current_user.name = request.form['name']
		current_user.lastname = request.form['lastname']
		current_user.email = request.form['email']
		current_user.school = request.form['school']
		db.session.commit()
		return redirect(url_for('user'))
	elif request.method == 'DELETE':
		enrolled = Enrolled.filter_by(uni=request.form.['uni'])
		for e in enrolled:
			db.session.delete(e)
		student = Student.filter_by(uni=request.form.['uni'])
		db.session.delete(student)
		db.session.commit()
		return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		student = Student(uni=request.form['uni'], name='alice', lastname=request.form['lastname'], email=request.form['email'], school=request.form['school'])
		student.set_password(request.form['password'])
		db.session.add(student)
		db.session.commit()
		return redirect(url_for('login'))
	elif request.method == 'GET':
		render_template('signup.html')


