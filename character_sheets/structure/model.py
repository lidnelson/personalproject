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
	project = db.Column(db.String(100), nullable=False)
	character_first_name = db.Column(db.String(30), nullable=False)
	character_last_name = db.Column(db.String(30), nullable=False)
	character_description = db.Column(db.String(10000))
	date_used = db.Column(db.DateTime, nullable=False, default=datetime.now)
	author_file = db.Column(db.String(100), nullable=False)

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	details = db.relationship('CharacterFile', backref='details', lazy=True)
	

	def __repr__(self):
		return ''.join([str(self.user_id),' ', self.file_name])


class CharacterFile(db.Model):
 	id = db.Column(db.Integer, primary_key=True)
 	file_id = db.Column(db.Integer, db.ForeignKey('files.id'), nullable=False)
 	eye_colour=db.Column(db.String(10))
 	scars= db.Column(db.Boolean, default=False)
 	tattoos = db.Column(db.Boolean, default=False)
 	pet_peeves = db.Column(db.String(10000))
	hobbies = db.Column(db.String(10000))
	alignment = db.Column(db.String(20))
	accent = db.Column(db.String(50))
	passionate = db.Column(db.String(10000))
	earlybird_nightowl = db.Column(db.String(50))
	favourite_meal = db.Column(db.String(10000))
	goals = db.Column(db.String(10000))
	music_genre = db.Column(db.String(100000))
	cat_person = db.Column(db.Boolean, default=False)
	dog_person = db.Column(db.Boolean, default=False)
	romantic_relationship_ideals =db.Column(db.String(100000))
	partial_birthday_celebration = db.Column(db.String(10))
	easy_appologiser = db.Column(db.String(10))
	bullied = db.Column(db.String(10))
	smarts = db.Column(db.String(20))
	country = db.Column(db.String(100))
	book_worm = db.Column(db.Boolean, default=False)
	fears = db.Column(db.String(100))
	address = db.Column(db.Boolean, default=False)
	gender = db.Column(db.String(20))
	birthday = db.Column(db.String(50))
	health_issues = db.Column(db.String(10000))
	mother = db.Column(db.String(10))
	father = db.Column(db.String(10))
	relationships = db.Column(db.String(10))
	skills_number = db.Column(db.Integer, default=0)
	magical_abilities= db.Column(db.Boolean, default=False)
	improvements = db.Column(db.String(1000))

 	def __repr__(self):
 		return ''.join([
 			'Eye colour: ', str(self.eye_colour), '\r\n',
 			'Character has scars: ', self.scars, '\r\n',
 			'character has tattoos: ', self.tattoos,
			'Pet-peeves: ', self.pet_peeves, '\r\n',
			'Hobbies: ', self.hobbies, '\r\n',
			'Alignment: ', str(self.alignment), '\r\n',
			'Accent: ', self.accent, '\r\n',
			'Characters Passion: ', self.passionate, '\r\n',
			'Early-bird or Night-owl: ', str(self.earlybird_nightowl), '\r\n',
			'Characters Favourite Meal: ', self.favourite_meal, '\r\n',
			'Characters Goals: ', self.goals, '\r\n',
			'Music Taste: ', self.music_genre, '\r\n',
			'They are a cat person: ', self.cat_person, '\r\n',
			'They are a dog person: ', self.dog_person, '\r\n',
			'How they view a relationship: ', self.romantic_relationship_ideals, '\r\n',
			'Birthday Celebrator: ', str(self.partial_birthday_celebration), '\r\n',
			'Apologiser: ', str(self.easy_appologiser), '\r\n',
			'Were/are they bullied: ', str(self.bullied), '\r\n',
			'Street or Book smart: ', str(self.smarts), '\r\n',
			'What country are they from: ', self.country, '\r\n',
			'They are a book worm: ', self.book_worm, '\r\n',
			'Fears: ', self.fears, '\r\n',
			'I know the characters address: ', self.address, '\r\n',
			'Gender: ', str(self.gender), '\r\n',
			'Characters Birthday: ', self.birthday, '\r\n',
			'Health Issues: ', self.health_issues, '\r\n',
			'Knows Mother: ', str(self.mother), '\r\n',
			'Knows father: ', str(self.father), '\r\n',
			"There are other relationships i'd like to input: ", str(self.relationships), '\r\n',
			"Number of skills: ", self.skills_number, '\r\n',
			"Magical abilities: ", self.magical_abilities,'\r\n',
			"Skill Imporvements: ", self.improvements])

class Scars(FlaskForm):
	id = db.Column(db.Integer, primary_key=True)
	file_id = db.Column(db.Integer, db.ForeignKey('files.id'), nullable=False)
	scars_what = db.Column(db.String(200), nullable=False)
	scars_where = db.Column(db.String(50), nullable=False)
	scars_why = db.Column(db.String(200))

	def __repr__(self):
		return ''.join([
			"File ID: ", self.file_id, '\r\n',
			"What the scar if from: ", self.scars_what, '\r\n',
			"Where the scar is: ", self.scars_where, '\r\n',
			"How they got the scar: ", self.scars_why
			])


class Tattoos(FlaskForm):
	id= db.Column(db.Integer, primary_key=True)
	file_id = db.Column(db.Integer, db.ForeignKey('files.id'), nullable=False)
	tattoos_what = db.Column(db.String(200), nullable=False)
	tattoos_where = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		return ''.join([
			"File ID: ", self.file_id, '\r\n',
			"What the tattoo is of: "])


class CharacterAddress(FlaskForm):
	id= db.Column(db.Integer, primary_key=True)
	file_id = db.Column(db.Integer, db.ForeignKey('files.id'), nullable=False)
	address_1 = db.Column(db.String(100),nullable=False)
	address_2 = db.Column(db.String(100))
	town = db.Column(db.String(100), nullable=False)
	county = db.Column(db.String(100),nullable=False)
	country= db.Column(db.String(100),nullable=False)
	postcode_zipcode = db.Column(db.String(10))

	def __repr__(self):
		return ''.join([])


class Relationships(FlaskForm):
	id= db.Column(db.Integer, primary_key=True)
	file_id = db.Column(db.Integer, db.ForeignKey('files.id'), nullable=False)
	relationship_type = db.Column(db.String(30), nullable=False)
	first_name = db.Column(db.String(50), nullable=False)
	last_name = db.Column(db.String(50), nullable=False)
	age = db.Column(db.Integer)
	length = db.Column(db.Integer)
	gender = db.Column(db.String(30), nullable=False)

	def __repr__(self):
		return ''.join([])



class Skills(FlaskForm):
	id= db.Column(db.Integer, primary_key=True)
	file_id = db.Column(db.Integer, db.ForeignKey('files.id'), nullable=False)
	skills_what = db.Column(db.String(100), nullable=False)
	skills_used = db.Column(db.String(10000))

	def __repr__(self):
		return ''.join([])


class Magical(FlaskForm):
	id= db.Column(db.Integer, primary_key=True)
	file_id = db.Column(db.Integer, db.ForeignKey('files.id'), nullable=False)
	MA_name = db.Column(db.String(100), nullable=False)
	MA_used = db.Column (db.String(10000))
	flaws = db.Column(db.String(10000))
	limitations = db.Column(db.String(10000))
	price = db.Column(db.String(10000))

	def __repr__(self):
		return ''.join([])
