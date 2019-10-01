from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, equalTo, ValidationError
from flask_login import current_user
from character_sheets import bcrypt
from character_sheets.model import Users


class RegistrationForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=2, max=100)
		])
	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=2, max=100)
		])
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired(),
			Length(min=4)
		])
	confirm_password = PasswordField('Confirm Password',
		validators=[
			DataRequired(),
			EqualTo('password')
		])
	submit =SubmitField('Sign Up')

	def validate_email(self,email):
		user =Users.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already in use!')


class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired()
		])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

	def validate_email(self, email):
		user=Users.query.filter_by(email=self.email.data).first()
		if not user:
			raise ValidationError('Unknown email')
	
	def validate_password(self, password):
		user=Users.query.filter_by(email=self.email.data).first()
		if user: 
			if not bcrypt.check_password_hash(user.password,self.password.data):
				raise ValidationError('Invalid password')
			

class UpdateAccountForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=2, max=100)
		])
	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=2, max=100)
		])
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	submit = SubmitField('Update')

	def validate_email(self,email):
		if email.data != current_user.email:	
			user =Users.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use - Please choose another')


class FilesForm(FlaskForm):
	file_name = StringField('File Name'
		validators=[
			DataRequired(),
			Length(min=5)
		])
	character_first_name = StringField('Characters First Name'
		validators=[
			DataRequired(),
			Length(min=2)
		])
	character_last_name = StringField('Characters Last Name'
		validators=[
			DataRequired()
			length(min=2)
		])
	submit = SubmitField('Create File')


# class CApperenceForm(FlaskForm):
#     eye_colour= SelectField('Characters Eye Colour'
#             choices=[
#                 ('blue','blue'),
#                 ('black','black'),
#                 ('green','green'),
#                 ('brown','brown'),
#                 ('purple','purple'),
#                 ('magenta','magenta'),
#                 ('red','red'),
#                 ('grey','grey'),
#                 ('syan','syan'),
#                 ('teal','teal'),
#                 ('turquoise','turquoise'),
#                 ('dark bule','dark blue'),
#                 ('yellow','yellow')
#             ])
#     eye_shape
#     lip_colour
#     lip_shape
#     nose_size
#     hair_colour
#     hair_style
#     hair_length
#     scars = BooleanField('Tick here if your character has anty scars')
#     if scars == True:
#         scars_number = IntegerField('How many scars?'
#                 validation=[
#                     DataRequired()
#                 ])
#         for i in scars_number:
#             scars_what=StringField('What does the scar look like?'
#                     validation=[
#                         DataRequired()
#                     ])
#             scars_where=StringField('Where on the body is the scar?'
#                     validation=[
#                         DataRequired()
#                     ])
#             scars_why=StringField("What's the story behind the scar"
#                     validation=[
#                         DataRequired()
#                     ])
#     tattoos = BooleanField('Tick if your charcter has tattoos?')
#     if tattoos == True:
#         tattoos_number = IntegerField('How many tattoos does your character have?'
#                 validation=[
#                     DataRequired()
#                 ])
#         for i in tattoos_number:
#             tattoos_what = StringField('What is the tattoo?'
#                     validation=[
#                         DataRequired()
#                     ])
#             tattoos_where = StringField('Where is the tattoo on the body?'
#                     validation=[
#                         DataRequired()
#                     ])
#     Accessories



# class CPersonalityForm(FlaskForm):
#     pet_peeves
#     hobbies
#     alignment
#     accent
#     introvert_extrovert_scale
#     passionate
#     earlybird_nightowl
#     favourite_meal
#     goals
#     pushover_controlfreak
#     music_genre
#     popularity
#     cat_person
#     dog_person
#     romantic_relationship_ideals
#     partial_birthday_celebration
#     easy_appologiser
#     bullied
#     smarts
#     country
#     book_worm
#     fears



# class CMinorDetailsForm(FlaskForm):
#     address
#     birthday
#     health_issues
#     mother
#     father
#     relationships = SelectField('Are there any other types of relationships?'
#             choices=[
#                 ('yes','Yes'),
#                 ('No','No')
#             ])
#     while relationships == 'Yes':
#         reationship_type= SelectField('What type of relationship?'
#                 choices=[
#                     ('fatherfigure','Father Figure'),
#                     ('motherfigure','Mother Figure'),
#                     ('brother','Brother'),
#                     ('sister','Sister')
#                     ('brother_friend','Like a Brother')
#                     ('sister_friend','Like a Sister')
#                     ('son','Son'),
#                     ('daughter','Daughter'),
#                     ('uncle','Uncle'),
#                     ('aunt','Aunt'),
#                     ('best_friend','best Friend'),
#                     ('boyfriend','Boyfriend'),
#                     ('girlfriend','Girlfriend'),
#                     ('partner','Partner'),
#                     ('friends_with_benefits','Friends with Benefits'),
#                     ('its_complicated',~"It's Complicated"),
#                     ('aquaintance','Aquaintance'),
#                     ('dislike','Dislike'),
#                     ('enemy','Enemy')
#                 ])
#         r_first_name = StringField('Whats the first name of the person?'
#                 validation=[
#                     DataRequired()
#                 ])
#         r_last_name = StringField('Whats the last name of the person?'
#                 validation=[
#                     DataRequired()
#                 ])
#         r_age = IntegerField('How old is the person?'
#                 validation=[
#                     DataRequired()
#                 ])
#         r_length = StringField('How long has your charcter known this person?'
#                 validation=[
#                     DataRequired()
#                 ])
#         r_gender = SelectField('what is the gender of the person?'
#                 validation=[
#                     DataRequired()
#                 ])

# class CAbilitiesForm(FlaskForm):
#     skills_number = IntegerField('How many skills does your character have?'
#             validation=[
#                 DataRequired()
#             ])
#     for i in skills_number:
#         skills_what = StringField('What is the name of this skill?'
#                 validation= [
#                     DataRequired()
#                 ])
#         skills_used = StringField('How is this skill used?'
#                 validation=[
#                     DataRequired()
#                 ])
#     magical_abilities = BooleanField('Tick here if your character has magical abilities')
#     if magical_abilities == True:
#         MA_number = IntegerField('How many magiocal abilities does your character have?'
#                 validation= [
#                     DataRequired()
#                 ])
#         for i in MA_number:
#             MA_name = StringField('What is the Magical Ability?'
#                     validation = [
#                         DataRequired()
#                     ])
#             MA_used = StringField('How does your character use this magical ability?'
#                     validation = [
#                         DataRequired()
#                     ])
#             flaws = StringField('What are the flaws with this ability?'
#                     validation=[
#                         Datarequired()
#                     ])
#             limitations = StringField('What are the limitaions to this ability?'
#                     validation=[
#                         DataRequired()
#                     ])
#             price = StringField('What is the price for using this ability?'
#                     validation=[
#                         DataRequired()
#                     ])
#     improvements

