from structure import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(50), nullable=False)
	files = db.relationship('Files', backref='author', lazy=True)

	def __repr__(self):
		return ''.join([
			'User ID: ', str(self.id),'\r\n', 
			'Email: ', self.email, '\r\n',
			'Name: ', self.first_name, ' ', self.last_name])

class Files(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	file_name = db.Column(db.String(50), nullable=False, unique=True)
	#project = db.Column(db.String(100), nulable=False)
	character_first_name = db.Column(db.String(30), nullable=False)
	character_last_name = db.Column(db.String(30), nullable=False)
	#character_description = db.Column(db.String(10000))
	date_used = db.Column(db.DateTime, nullable=False, default=datetime.now)
	author_file = db.Column(db.String(100), nullable=False)

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __repr__(self):
		return ''.join([str(self.user_id),' ', self.file_name])


# class characterappearence(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	file_id = db.Column(db.Integer, db.ForeignKey('files.id'), nullable=False)
# 	eye_colour=db.Column(db.String(10))
# 	scars= db.Column(db.Boolean, default=False)
# 	tattoos = db.Column(db.Boolean, default=False)

# 	def__repr__(self):
# 		return ''.join([
# 			'Eye colour: ', self.eye_colour, '\r\n',
# 			'Character has scars: ', self.scars, '\r\n',
# 			'character has tattoos: ', self.tattoos])



# class characterpersonality(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	file_id = db.Column(db.Integer, db.ForeignKey('files.id'), nullable=False)
# 	pet_peeves = db.Column(db.String(10000))
# 	hobbies = db.Column(db.String(10000))
# 	alignment = db.Column(db.String(20))
# 	accent = db.Column(db.String(50))
# 	passionate = db.Column(db.String(10000))
# 	earlybird_nightowl = db.Column(db.String(50))
# 	favourite_meal = db.Column(db.String(10000))
# 	goals = db.Column(db.String(10000))
# 	music_genre = db.Column(db.String(100000))
# 	cat_person = db.Column(db.Boolean, default=False)
# 	dog_person = db.Column(db.Boolean, default=False)
# 	romantic_relationship_ideals =db.Column(db.String(100000))
# 	partial_birthday_celebration = db.Column(db.String(10))
# 	easy_appologiser = db.Column(db.String(10))
# 	bullied = db.Column(db.String(10))
# 	smarts = db.Column(db.String(20))
# 	country = db.Column(db.String(100))
# 	book_worm = db.Column(db.Boolean, default=False)
# 	fears = db.Column(db.String(100))

# 	def__repr__(self):
# 		return ''.join([
# 			'Pet-peeves: ', self.pet_peeves, '\r\n',
# 			'Hobbies: ', self.hobbies, '\r\n',
# 			'Alignment: ', self.alignment, '\r\n',
# 			'Accent: ', self.accent, '\r\n',
# 			'Characters Passion: ', self.passionate, '\r\n',
# 			'Early-bird or Night-owl: ', self.earlybird_nightowl, '\r\n',
# 			'Characters Favourite Meal: ', self.favourite_meal, '\r\n',
# 			'Characters Goals: ', self.goals, '\r\n',
# 			'Music Taste: ', self.music_genre, '\r\n',
# 			'They are a cat person: ', self.cat_person, '\r\n',
# 			'They are a dog person: ', self.dog_person, '\r\n',
# 			'How they view a relationship: ', self.romantic_relationship_ideals, '\r\n',
# 			'Birthday Celebrator: ', self.partial_birthday_celebration, '\r\n',
# 			'Apologiser: ', self.easy_appologiser, '\r\n',
# 			'Were/are they bullied: ', self.bullied, '\r\n',
# 			'Street or Book smart: ', self.smarts, '\r\n',
# 			'What country are they from: ', self.country, '\r\n',
# 			'They are a book worm: ', self.book_worm, '\r\n',
# 			'Fears: ', self.fears])

# class characterdetails(db.Model):
# 	id=db.Column(db.Integer, primary_key=True)
# 	file_id= db.Column(db.Integer, db.ForeignKey('files.id'), nullable=False)
# 	address = db.Column(db.Boolean, default=False)
# 	gender = db.Column(db.String(20))
# 	birthday = db.Column(db.String(50))
# 	health_issues = db.Column(db.String(10000))
# 	mother = db.Column(db.String(10))
# 	father = db.Column(db.String(10))
# 	relationships = db.Column(db.String(10))

# 	def__repr__(self):
# 		return ''.join([
# 			'I know the characters address: ', self.address, '\r\n',
# 			'Gender: ', self.gender, '\r\n',
# 			'Characters Birthday: ', self.birthday, '\r\n',
# 			'Health Issues: ', self.health_issues, '\r\n',
# 			'Knows Mother: ', self.mother, '\r\n',
# 			'Knows father: ', self.father, '\r\n',
# 			"There are other relationships i'd like to input: ", self.relationships])

# class characterabilities(db.Model):
# 	id =db.Column(db.Integer, primary_key=True)
# 	file_id = db.Column(db.Integer. db.ForeignKey('files.id'), nullable=False)

