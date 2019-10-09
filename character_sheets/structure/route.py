from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from structure import app, db, bcrypt, login_manager, LoginManager
from structure.model import Users, Files, CharacterFile 
from structure.form import RegistrationForm, LoginForm, UpdateAccountForm, FilesForm, CharacterForm #CApperenceForm, CPersonalityForm, CMinorDetailsForm, CAbilitiesForm, DeleteForm

tempFormData = ""

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title = 'Home')

@app.route('/about')
def about():
	return render_template('about.html', title = 'About')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)

@app.route("/register", methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data)
		user = Users(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			email=form.email.data,
			password=hashed_pw)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('account'))
	return render_template('register.html', title = 'Register', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/update_account', methods=['GET','POST'])
@login_required
def updateaccount():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('home'))
	elif request.method =='GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('updateaccount.html', title='Update Account', form=form)

@app.route('/account')
@login_required
def account():
	fileData=Files.query.filter_by(user_id=current_user.id)
	return render_template('account.html', title = 'Account', file=fileData)

@app.route('/account/createfile', methods=['GET','POST'])
@login_required
def createfile():
	global tempFormData
	form = FilesForm()
	if form.validate_on_submit():
		fileData = Files(
			file_name=form.file_name.data,
			project = form.project.data,
			character_first_name=form.character_first_name.data,
			character_last_name= form.character_last_name.data,
			character_description = form.character_description.data,
			author_file= current_user.first_name + " " + current_user.last_name,
			user_id= current_user.id
			)
		db.session.add(fileData)
		db.session.commit()
		data = Files.query.filter_by(file_name=form.file_name.data).first()
		tempFormData = data.id
		return redirect(url_for('characterform'))
	else:
		print(form.errors)
	return render_template('createfile.html', title= 'Create File', form=form)

	
@app.route('/account/character_form', methods=['GET','POST'])
@login_required
def characterform():
	global tempFormData
	form= CharacterForm()
	if form.submit.data:
		print('VALIDATED!!!!!!!!!!!!!!!!!! yay')
		charaData = CharacterFile(
			file_id = tempFormData,
			eye_colour = form.eye_colour.data,
			scars = form.scars.data,
			tattoos = form.tattoos.data,
			pet_peeves = form.pet_peeves.data,
			hobbies = form.hobbies.data,
			alignment = form.alignment.data,
			accent = form.accent.data,
			passionate = form.passionate.data,
			earlybird_nightowl = form.earlybird_nightowl.data,
			favourite_meal = form.favourite_meal.data,
			goals = form.goals.data,
			music_genre = form.music_genre.data,
			cat_person = form.cat_person.data,
			dog_person = form.dog_person.data,
			romantic_relationship_ideals = form.romantic_relationship_ideals.data,
			partial_birthday_celebration = form.partial_birthday_celebration.data,
			easy_appologiser = form.easy_appologiser.data,
			bullied = form.bullied.data,
			smarts = form.smarts.data,
			country = form.country.data,
			book_worm = form.book_worm.data,
			fears = form.fears.data,
			address = form.address.data,
			gender = form.gender.data,
			birthday = form.birthday.data,
			health_issues = form.health_issues.data,
			mother = form.mother.data,
			father = form.father.data,
			relationships = form.relationships.data,
			skills_number = form.skills_number.data,
			magical_abilities = form.magical_abilities.data,
			improvements = form.improvements.data
			)
		db.session.add(charaData)
		db.session.commit()
		return redirect(url_for('account'))
	else:
		print('hihihihihihihhihihihihi')
		# print(form1.errors)
		# print(form2.errors)
		# print(form3.errors)
		# print(form4.errors)
	return render_template('characterform.html', title ='Character Form', form=form)


# @app.route('/account/character_appearence_form')
# @login_required
# def appearenceform():
# 	form = CApperenceForm()
# 	if form.validate_on_submit():
# 		print('Hola padro')
# 		charaData = CharacterFile (
# 			file_id = 1,
# 			eye_colour = form.eye_colour.data,
# 			scars = form.scars.data,
# 			tattoos = form.tattoos.data,
# 			)
# 		db.session.add(charaData)
# 		db.session.commit()
# 		return redirect(url_for('personalityform'))
# 	else:
# 		print(form.errors)
# 	return render_template('characterapperenceform.html', title='File form pt.2', form=form)

# @app.route('/account/character_personality_form')
# @login_required
# def personalityform():
# 	form=CPersonalityForm()
# 	if form.validate_on_submit():
# 		charaData = CharacterFile(
# 			pet_peeves = form.pet_peeves.data,
# 			hobbies = form.hobbies.data,
# 			alignment = form.alignment.data,
# 			accent = form.accent.data,
# 			passionate = form.passionate.data,
# 			earlybird_nightowl = form.earlybird_nightowl.data,
# 			favourite_meal = form.favourite_meal.data,
# 			goals = form.goals.data,
# 			music_genre = form.music_genre.data,
# 			cat_person = form.cat_person.data,
# 			dog_person = form.dog_person,
# 			romantic_relationship_ideals = form.romantic_relationship_ideals.data,
# 			partial_birthday_celebration = form.partial_birthday_celebration.data,
# 			easy_appologiser = form.easy_appologiser.data,
# 			bullied = form.bullied.data,
# 			smarts = form.smarts.data,
# 			country = form.country.data,
# 			book_worm = form.book_worm.data,
# 			fears = form.fears.data
# 			)
# 		db.session.add(charaData)
# 		db.session.commit()
# 		return redirect(url_for('detailsform'))
# 	return render_template('characterpersonalityform.html', title="File form pt.3", form=form)


# @app.route('/account/character_details_form')
# @login_required
# def detailsform():
# 	form=CMinorDetailsForm()
# 	if form.validate_on_submit():
# 		charaData= CharacterFile(
# 			address = form.address.data,
# 			gender = form.gender.data,
# 			birthday = form.birthday.data,
# 			health_issues = form.health_issues.data,
# 			mother = form.mother.data,
# 			father = form.father.data,
# 			relationships = form.relationships.data
# 			)
# 		db.session.add(charaData)
# 		db.session.commit()
# 		return redirect(url_for('abilitiesform'))
# 	return render_template('characterminordetailsform.html', title="File form pt.3", form=form)

# @app.route('/account/character_abilities_form')
# @login_required
# def abilitiesform():
# 	form=CAbilitiesForm()
# 	if form4.validate_on_submit():
# 		charaData = CharacterFile(
# 			skills_number = form.skills_number.data,
# 			magical_abilities = form.magical_abilities.data,
# 			improvements = form.improvements.data
# 			)
# 		db.session.add(charaData)
# 		db.session.commit()
# 		return redirect(url_for('account'))
# 	return render_template('characterabilitiesform.html', title='File from pt.4', form=form)

@app.route('/account/file/<int(min=1):file_id>')
@login_required
def characterpage(file_id):
	fileData = Files.query.filter_by(id=file_id)
	form1 = FilesForm()
	form2 = CharacterForm()
	return render_template('characterpage.html', title="Charater page", form1=form1, form2=form2, file=fileData)

@app.route('/account/delete', methods=['GET','POST'])
@login_required
def deleteaccount():
	form = DeleteForm()
	if form.validate_on_submit():
		files =Files.query.filter_by(user_id=current_user.id).all()
		for i in files:
			db.session.delete(i)
		db.session.delete(current_user)
		db.session.commit()
		logout_user()
		return redirect(url_for('home'))
	return render_template('deleteaccount.html',title='Delete Account Page', form=form)
 
	

@app.route('/account/file/<int(min=1):file_id>/delete', methods=['GET','POST'])
@login_required
def deletecharacter(file_id):
	form= DeleteForm()
	print(file_id)
	if form.yes.data:
		fileData= Files.query.filter_by(id=file_id).first()
		print(fileData)
		db.session.delete(fileData)
		db.session.commit()
		return redirect(url_for('account'))	
	return render_template('deletefile.html',title='Delete File Page', form=form)

@app.route('/account/file/<int(min=1):file_id>/edit')
@login_required
def edit(file_id):
	fileData=Files.query.filter_by(id=file_id)
	return render_template('editfile.html',title='Edit file page')


@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))
# CApperenceForm
# CPersonalityForm
# CMinorDetailsForm
# CAbilitiesForm