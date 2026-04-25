from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'foydalanuvchilar'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))


class Mentor(db.Model):
    __tablename__ = 'mentors'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    master_id = db.Column(db.Integer)


class Groupss(db.Model):
    __tablename__ = 'groupss'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10))
    mentor_id = db.Column(db.Integer)



class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    grade = db.Column(db.Integer)


class StudentGroups(db.Model):
    __tablename__ = 'studentgroups'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    group_id = db.Column(db.Integer)


class Student_heights(db.Model):
    __tablename__ = 'student_heights'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    height = db.Column(db.Integer)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
