from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from structure import bcrypt, login_manager
from structure.model import Users


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
    file_name = StringField('File Name: ',
		validators=[
			DataRequired(),
			Length(min=2)
		])
    project = StringField('For which project: ',
        validators=[
            DataRequired(),
            Length(min=5, max=100)
        ])
    character_first_name = StringField('Characters First Name: ',
		validators=[
			DataRequired(),
			Length(min=2)
		])
    character_last_name = StringField('Characters Last Name: ',
		validators=[
			DataRequired(),
			Length(min=2)
		])
    character_description = StringField('Short description of character: ',
        validators=[
            Length(min=2, max=10000)
        ])
    submit = SubmitField('Create File')


class CharacterForm(FlaskForm):
    eye_colour= SelectField('Characters Eye Colour',
            choices=[
            	('other', 'Other'),
                ('blue', 'Blue'),
                ('black', 'Black'),
                ('green', 'Green'),
                ('brown', 'Brown'),
                ('purple', 'Purple'),
                ('magenta', 'Magenta'),
                ('red', 'Red'),
                ('grey', 'Grey'),
                ('cyan', 'Cyan'),
                ('teal', 'Teal'),
                ('turquoise', 'Turquoise'),
                ('dark blue', 'Dark Blue'),
                ('yellow', 'Yellow')
            ])
    #eye_shape
    #lip_colour
    #lip_shape
    #nose_size
    #hair_colour
    #hair_style
    #hair_length
    scars = BooleanField('Tick here if your character has any scars')
    scars_number = IntegerField('How many scars?',
            validators=[
                DataRequired()
            ])
    scars_what=StringField('What does the scar look like?',
            validators=[
            	DataRequired()
            ])
    scars_where=StringField('Where on the body is the scar?',
            validators=[
                DataRequired()
            ])
    scars_why=StringField("What's the story behind the scar",
            validators=[
                DataRequired()
            ])

    tattoos = BooleanField('Tick if your charcter has tattoos?')
    tattoos_number = IntegerField('How many tattoos does your character have?',
            validators=[
                DataRequired()
            ])
    tattoos_what = StringField('What is the tattoo?',
            validators=[
                DataRequired()
            ])
    tattoos_where = StringField('Where is the tattoo on the body?',
	        validators=[
                DataRequired()
            ])
    #Accessories
    pet_peeves = StringField('What pet-peeves does your character have?')
    hobbies = StringField('What hobbies does your character have?')
    alignment = SelectField('What Alignement is your character?',
        choices=[
            ('lawful_good','Lawful Good'),
            ('lawful_neutral','Lawful Neutral'),
            ('lawful_evil','Lawful Evil'),
            ('neutral_good','Neutral Good'),
            ('true_neutral','True Neutral'),
            ('neutral_evil','Neutral Evil'),
            ('chaotic_good','Chaotic Good'),
            ('chaotic_neutral','Chaotic Neutral'),
            ('chaotic_evil','Chaotic Evil')
        ])
    accent = StringField('What accent does your character have?')
    #introvert_extrovert_scale #scale
    passionate = StringField('What is your character passionate about?')
    earlybird_nightowl = SelectField('Is your character an earlybird or a nightowl?',
        choices=[
            ('earlybird','Earlybird'),
            ('nightowl','Nightowl')
        ])
    favourite_meal = StringField('Whats your characters favourite meal?')
    goals = StringField('What does your character strive to achieve?')
    #pushover_controlfreak #scale
    music_genre = StringField('What genre of music does your character generally listen to?')
    #popularity
    cat_person = BooleanField('Cat Person') 
    dog_person = BooleanField('Dog Person')
    romantic_relationship_ideals = StringField('How does your character view relationships?')
    partial_birthday_celebration = SelectField('Does your character like to celebrate their birthday?',
        choices=[
        ('yes','Yes'),
        ('no','No')
    ])
    # if partial_birthday_celebration == 'no':
    #     birthday_why = StringField("Why doesn't your character like to celebrate their birthday?",
    #         validator=[
    #             DataRequired()
    #         ])
    easy_appologiser = SelectField('Does your character find it easy to applogise?',
        choices=[
            ('yes','Yes'),
            ('no','No')
        ])
    bullied = SelectField('Was/is your character bullied at school?',
        choices=[
            ('yes','Yes'),
            ('no','No')
        ]) 
    # if bullied=='yes':
    #     bullied_stopped = SelectField('Has the bullying stopped?',
    #     choices=[
    #         ('yes','Yes'),
    #         ('no','No')
    #     ])
        # if bullied_stopped=='yes':
        #     bully_effect = StringField('How does it affect your character and the way they act?')
    smarts = SelectField('Is your character have street smart or book smart?',
        choices=[
            ('street_smart','Street Smart'),
            ('book_smart','Book Smart')
        ])
    country = StringField('What country is your character from?')
    book_worm= BooleanField('Book worm')
    fears = StringField('What is your character greatest fear?')
    address = BooleanField ('Tick if you want to write your characters address')
    gender = SelectField('what is their gender?',
                choices=[
                    ('male','Male'),
                    ('female','Female'),
                    ('gender_fluid','Gender Fluid')
                ])
    birthday = StringField('Characters Birthday: ')
    health_issues = StringField('Does your character have any health issues?')
    mother = SelectField('Does your character know their biological mother?',
        choices=[
                ('yes','Yes'),
                ('No','No')
            ])
    father= SelectField('Does your character know their biological father?',
        choices=[
                ('yes','Yes'),
                ('No','No')
            ])
    relationships = SelectField('Are there any other types of relationships?',
            choices=[
                ('yes','Yes'),
                ('No','No')
            ])
    skills_number = IntegerField('How many skills does your character have?',
            validators=[
                DataRequired()
            ])
    magical_abilities = BooleanField('Tick here if your character has magical abilities')
    improvements = StringField('What skills does your character need to improve on?')
    submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
    yes = SubmitField('Yes')


class ScarsForm(FlaskForm):
    scars_what=StringField('What does the scar look like?',
            validators=[
                DataRequired()
            ])
    scars_where=StringField('Where on the body is the scar?',
            validators=[
                DataRequired()
            ])
    scars_why=StringField("What's the story behind the scar",
            validators=[
                DataRequired()
            ])
    submit_yes= SubmitField('Yes')
    submit_no = SubmitField('No')


class TattoosForm(FlaskForm):    
    tattoos_what = StringField('What is the tattoo?',
        validators=[
            DataRequired()
        ])
    tattoos_where = StringField('Where is the tattoo on the body?',
        validators=[
            DataRequired()
        ])
    submit_yes= SubmitField('Yes')
    submit_no = SubmitField('No')

class RelationshipForm(FlaskForm):    
    relationship_type= SelectField('What type of relationship?',
            choices=[
                ('mother','Mother'),
                ('father','Father'),
                ('fatherfigure','Father Figure'),
                ('motherfigure','Mother Figure'),
                ('brother','Brother'),
                ('sister','Sister'),
                ('brother_friend','Like a Brother'),
                ('sister_friend','Like a Sister'),
                ('son','Son'),
                ('daughter','Daughter'),
                ('uncle','Uncle'),
                ('aunt','Aunt'),
                ('best_friend','best Friend'),
                ('boyfriend','Boyfriend'),
                ('girlfriend','Girlfriend'),
                ('partner','Partner'),
                ('friends_with_benefits','Friends with Benefits'),
                ('its_complicated',"It's Complicated"),
                ('aquaintance','Aquaintance'),
                ('dislike','Dislike'),
                ('enemy','Enemy')
            ])
    first_name = StringField('Whats the first name of the person?',
            validators=[
                DataRequired()
            ])
    last_name = StringField('Whats the last name of the person?',
            validators=[
                DataRequired()
            ])
    age = IntegerField('How old is the person?',
            validators=[
                DataRequired()
            ])
    length = StringField('How long has your character known this person?',
            validators=[
                DataRequired()
            ])
    gender = SelectField('what is the gender of the person?',
            choices=[
                ('male','Male'),
                ('female','Female'),
                ('gender_fluid','Gender Fluid')
            ])
    submit_yes = SubmitField('Yes')
    submit_no = SubmitField('No')


class AddressForm(FlaskForm):
    address_1 = StringField('Address Line 1: ')
    address_2 = StringField('Address Line 2: ')
    town = StringField('Town: ')
    county_state =StringField('County/State: ')
    country= StringField('Country: ')
    postcode_zipcode = StringField('Post Code/Zip Code:')
    submit = SubmitField('Submit')

class SkillsForm(FlaskForm):
    skills_what = StringField('What is the name of this skill?',
           validators= [
               DataRequired()
           ])
    skills_used = StringField('How is this skill used?',
          validators=[
               DataRequired()
           ])
    submit_yes= SubmitField('Yes')
    submit_no= SubmitField('No')

class MagicalForm(FlaskForm):
    MA_name = StringField('What is the Magical Ability?',
            validators = [
                DataRequired()
            ])
    MA_used = StringField('How does your character use this magical ability?',
            validators = [
                DataRequired()
            ])
    flaws = StringField('What are the flaws with this ability?',
            validators=[
                DataRequired()
            ])
    limitations = StringField('What are the limitaions to this ability?',
            validators=[
                DataRequired()
            ])
    price = StringField('What is the price for using this ability?',
            validators=[
                DataRequired()
            ])
    submit_yes= SubmitField('Yes')
    submit_no = SubmitField('No')


@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))