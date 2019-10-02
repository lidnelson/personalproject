from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from structure import app, db, bcrypt
from structure.model import Users, Files
from structure.form import RegistrationForm, LoginForm, UpdateAccountForm, FilesForm, CApperenceForm#, CPersonalityForm, CMinorDetailsForm, CAbilitiesForm

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
	return render_template('account.html', title = 'Account')

@app.route('/account/createfile', methods=['GET','POST'])
@login_required
def createfile():
	form = FilesForm()
	if form.validate_on_submit():
		fileData = Files(
			file_name=form.file_name.data,
			character_first_name=form.character_first_name.data,
			character_last_name= form.character_last_name.data,
			author_file= current_user.first_name + " " + current_user.last_name,
			user_id= current_user.id
			)
		db.session.add(fileData)
		db.session.commit()
		return redirect(url_for('appearenceform'))
	else:
		print(form.errors)
	return render_template('createfile.html', title= 'Create File', form=form)
	
@app.route('/account/character_appearence_form')
@login_required
def appearenceform():
	form = CApperenceForm()
	if form.validate_on_submit():
		return redirect(url_for('home'))
	# else:
	# 	print(form.errors)
	return render_template('characterapperenceform.html', title='File form pt.2')#, form=form)
# CApperenceForm
# CPersonalityForm
# CMinorDetailsForm
# CAbilitiesForm