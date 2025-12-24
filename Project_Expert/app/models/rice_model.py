from app.extensions import db
from flask_login import UserMixin

# តារាង ១: ជំងឺ
class Disease(db.Model):
    __tablename__ = 'diseases'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(50), nullable=True)
    rules = db.relationship('Rule', backref='disease', lazy=True)

# តារាង ២: រោគសញ្ញា
class Symptom(db.Model):
    __tablename__ = 'symptoms'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    rules = db.relationship('Rule', backref='symptom', lazy=True)

# តារាង ៣: Rules (ភ្ជាប់ជំងឺ <-> រោគសញ្ញា)
class Rule(db.Model):
    __tablename__ = 'rules'
    id = db.Column(db.Integer, primary_key=True)
    symptom_id = db.Column(db.Integer, db.ForeignKey('symptoms.id'), nullable=False)
    disease_id = db.Column(db.Integer, db.ForeignKey('diseases.id'), nullable=False)

# តារាង ៤: អ្នកប្រើប្រាស់ (User) - ត្រូវមានតែមួយនេះគត់!
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')