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
    #project = StringField('What porject is this for: ')
    #character_description = StringField('Short description of character: ',
        # validators=[
        #     Length(min=2, max=10000)])

	submit = SubmitField('Create File')


class CApperenceForm(FlaskForm):
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
    submit = SubmitField('Next page')
    

    # if scars == True:
    #     scars_number = IntegerField('How many scars?',
    #             validation=[
    #                 DataRequired()
    #             ])
    #     for i in scars_number:
    #         scars_what=StringField('What does the scar look like?',
    #                 validation=[
    #                     DataRequired()
    #                 ])
    #         scars_where=StringField('Where on the body is the scar?',
    #                 validation=[
    #                     DataRequired()
    #                 ])
    #         scars_why=StringField("What's the story behind the scar",
    #                 validation=[
    #                     DataRequired()
    #                 ])
    # if tattoos == True:
    #     tattoos_number = IntegerField('How many tattoos does your character have?',
    #             validators=[
    #                 DataRequired()
    #             ])
    #     for i in tattoos_number:
    #         tattoos_what = StringField('What is the tattoo?',
    #             validator=[
    #                 DataRequired()
    #             ])
    #         tattoos_where = StringField('Where is the tattoo on the body?',
    #             validator=[
    #                 DataRequired()
    #             ])
    #Accessories



class CPersonalityForm(FlaskForm):
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
    submit = SubmitField('Next page')



class CMinorDetailsForm(FlaskForm):
    address = BooleanField ('Tick if you want to write your characters address')
    # if address == True:
    #     address_1 = StringField('Address Line 1: ')
    #     address_2 = StringField('Address Line 2: ')
    #     town = StringField('Town: ')
    #     county_state =StringField('County/State: ')
    #     country= StringField('Country: ')
    #     postcode_zipcode = StringField('Post Code/Zip Code:')
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
    # if mother == 'yes':
    #     mother_first_name = StringField('Whats the mothers first name?',
    #             validators=[
    #                 DataRequired()
    #             ])
    #     mother_last_name = StringField('Whats the mothers last name?',
    #             validators=[
    #                 DataRequired()
    #             ])
    #     mother_age = IntegerField('How old is their mother?',
    #             validators=[
    #                 DataRequired()
    #             ])
    #     mother_gender = SelectField('what is the gender of their mother?',
    #             choices=[
    #                 ('male','Male'),
    #                 ('female','Female'),
    #                 ('gender_fluid','Gender Fluid')
    #             ])
    father= SelectField('Does your character know their biological father?',
        choices=[
                ('yes','Yes'),
                ('No','No')
            ])
    # if father == 'yes':
    #     father_first_name = StringField('Whats the fathers first name?',
    #             validators=[
    #                 DataRequired()
    #             ])
    #     father_last_name = StringField('Whats the fathers last name?',
    #             validators=[
    #                 DataRequired()
    #             ])
    #     father_age = IntegerField('How old is their father',
    #             validators=[
    #                 DataRequired()
    #             ])
    #     father_gender = SelectField('what is the gender of their father?',
    #             choices=[
    #                 ('male','Male'),
    #                 ('female','Female'),
    #                 ('gender_fluid','Gender Fluid')
    #             ])
    relationships = SelectField('Are there any other types of relationships?',
            choices=[
                ('yes','Yes'),
                ('No','No')
            ])
    # while relationships == 'Yes':
    #     reationship_type= SelectField('What type of relationship?',
    #             choices=[
    #                 ('fatherfigure','Father Figure'),
    #                 ('motherfigure','Mother Figure'),
    #                 ('brother','Brother'),
    #                 ('sister','Sister')
    #                 ('brother_friend','Like a Brother')
    #                 ('sister_friend','Like a Sister')
    #                 ('son','Son'),
    #                 ('daughter','Daughter'),
    #                 ('uncle','Uncle'),
    #                 ('aunt','Aunt'),
    #                 ('best_friend','best Friend'),
    #                 ('boyfriend','Boyfriend'),
    #                 ('girlfriend','Girlfriend'),
    #                 ('partner','Partner'),
    #                 ('friends_with_benefits','Friends with Benefits'),
    #                 ('its_complicated',~"It's Complicated"),
    #                 ('aquaintance','Aquaintance'),
    #                 ('dislike','Dislike'),
    #                 ('enemy','Enemy')
    #             ])
    #     r_first_name = StringField('Whats the first name of the person?',
    #             validators=[
    #                 DataRequired()
    #             ])
    #     r_last_name = StringField('Whats the last name of the person?',
    #             validators=[
    #                 DataRequired()
    #             ])
    #     r_age = IntegerField('How old is the person?',
    #             validators=[
    #                 DataRequired()
    #             ])
    #     r_length = StringField('How long has your character known this person?',
    #             validators=[
    #                 DataRequired()
    #             ])
    #     r_gender = SelectField('what is the gender of the person?',class deleteform(FlaskForm):
    yes = SubmitField('Yes')
    
    #             choices=[
    #                 ('male','Male'),
    #                 ('female','Female'),
    #                 ('gender_fluid','Gender Fluid')
    #             ])
    submit = SubmitField('Next page')


class CAbilitiesForm(FlaskForm):
    skills_number = IntegerField('How many skills does your character have?',
            validators=[
                DataRequired()
            ])
    #for i in skills_number:
        #skills_what = StringField('What is the name of this skill?',
        #        validators= [
        #            DataRequired()
        #        ])
        #skills_used = StringField('How is this skill used?',
        #       validators=[
        #            DataRequired()
        #        ])
    magical_abilities = BooleanField('Tick here if your character has magical abilities')
    # if magical_abilities == True:
    #     MA_number = IntegerField('How many magiocal abilities does your character have?',
    #             validators= [
    #                 DataRequired()
    #             ])
    #     for i in MA_number:
    #         MA_name = StringField('What is the Magical Ability?',
    #                 validators = [
    #                     DataRequired()
    #                 ])
    #         MA_used = StringField('How does your character use this magical ability?',
    #                 validators = [
    #                     DataRequired()
    #                 ])
    #         flaws = StringField('What are the flaws with this ability?',
    #                 validators=[
    #                     Datarequired()
    #                 ])
    #         limitations = StringField('What are the limitaions to this ability?',
    #                 validators=[
    #                     DataRequired()
    #                 ])
    #         price = StringField('What is the price for using this ability?',
    #                 validators=[
    #                     DataRequired()
    #                 ])
    improvements = StringField('What skills does your character need to improve on?')
    submit = SubmitField('Next page')

class DeleteForm(FlaskForm):
    yes = SubmitField('Yes')
    

@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))