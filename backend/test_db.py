from Lacuna_DB import db, Video, Student, Course, Enrolled

db.create_all()
u = Student(uni="yc3877", password_hash='lala', name='alice', lastname='alice', email='yc3877@columbia.edu', school='SEAS')
v = Video(link="examplelink.com", title="example video", description="This is a example video", author_uni="yc3877", course_id=13778)
e = Enrolled(user_uni="yc3877", course_number=13778, semester='Spring', year=2021)
c = Course(call_number=13778, course_name="ECON", professor="gulati")

db.session.add(u)
db.session.add(v)
db.session.add(e)
db.session.add(c)
db.session.commit()

print(Student.query.all())