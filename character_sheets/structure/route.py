from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from structure import app, db, bcrypt, login_manager, LoginManager
from structure.model import Alignment, Users, Files, CharacterFile, Scars, Tattoos, CharacterAddress, Relationships, Skills, Magical 
from structure.form import SearchForm, ScarsForm, TattoosForm, AddressForm, RegistrationForm, LoginForm, UpdateAccountForm, FilesForm, CharacterForm,  MagicalForm, DeleteForm, SkillsForm, RelationshipForm

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
	form= SearchForm()
	cycle = []
	for field in form:
		if field.type == 'SelectField':
			field.choices = cycle
	for file in fileData:
		cycle.append((file.file_name, file.file_name))
	form.listed.choices = cycle
	if form.go.data:
		print(form.listed.data)
		print('//////////////////////////')
		temp=Files.query.filter_by(file_name=str(form.listed.data)).first()
		file_id=temp.id
		return redirect(url_for('search', file_id=file_id))
	return render_template('account.html', title = 'Account', file=fileData, form=form)

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
		print(form.errors)
	return render_template('characterform.html', title ='Character Form', form=form)


@app.route('/account/file/<int:file_id>')
@login_required
def characterpage(file_id):
	fileData = Files.query.filter_by(id=file_id)
	characterData = CharacterFile.query.filter_by(file_id=file_id).first()
	scars= Scars.query.filter_by(file_id=file_id).all()
	tattoos= Tattoos.query.filter_by(file_id=file_id).all()
	address= CharacterAddress.query.filter_by(file_id=file_id).first()
	skill = Skills.query.filter_by(file_id=file_id).all()
	magic = Magical.query.filter_by(file_id=file_id).all()
	relationship= Relationships.query.filter_by(file_id=file_id).all()
	alignment = Alignment.query.filter_by(name=characterData.alignment).first()
	return render_template('characterpage.html', title="Charater page",a=alignment, scars=scars, tattoos=tattoos, address=address, skills=skill, magical=magic, relationships=relationship,file1=characterData, file=fileData)

@app.route('/account/delete', methods=['GET','POST'])
@login_required
def deleteaccount():
	form = DeleteForm()
	if form.validate_on_submit():
		files =Files.query.filter_by(user_id=current_user.id).all()
		for i in files:
			scars = Scars.query.filter_by(file_id=i.id)
			for scar in scars:
				db.session.delete(scar)
			tattoos= Tattoos.query.filter_by(file_id=i.id)
			for tattoo in tattoos:
				db.session.delete(tattoo)
			skills= Skills.query.filter_by(file_id=i.id)
			for skill in skills:
				db.session.delete(skill)
			magical= Magical.query.filter_by(file_id=i.id)
			for magic in magical:
				db.session.delete(magic)
			R= Relationships.query.filter_by(file_id=i.id)
			for j in R:
				db.session.delete(j)
			address = CharacterAddress.query.filter_by(file_id=i.id)
			for a in address:
				db.session.delete(a)
			chara = CharacterFile.query.filter_by(file_id=i.id)
			for c in chara:
				db.session.delete(c)
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
	file= Files.query.filter_by(id=file_id).first()
	if form.yes.data:
		i= Files.query.filter_by(id=file_id).first()
		scars = Scars.query.filter_by(file_id=i.id)
			for scar in scars:
				db.session.delete(scar)
			tattoos= Tattoos.query.filter_by(file_id=i.id)
			for tattoo in tattoos:
				db.session.delete(tattoo)
			skills= Skills.query.filter_by(file_id=i.id)
			for skill in skills:
				db.session.delete(skill)
			magical= Magical.query.filter_by(file_id=i.id)
			for magic in magical:
				db.session.delete(magic)
			R= Relationships.query.filter_by(file_id=i.id)
			for j in R:
				db.session.delete(j)
			address = CharacterAddress.query.filter_by(file_id=i.id)
			for a in address:
				db.session.delete(a)
			chara = CharacterFile.query.filter_by(file_id=i.id)
			for c in chara:
				db.session.delete(c)
		db.session.delete(i)
		db.session.commit()
		return redirect(url_for('account'))	
	return render_template('deletefile.html',title='Delete File Page', form=form)

@app.route('/account/file/<int(min=1):file_id>/edit_file_name', methods=['GET', 'POST'])
@login_required
def editfile(file_id):
	form = FilesForm()
	file=Files.query.filter_by(id=file_id).first()
	if form.validate_on_submit():
		file.file_name=form.file_name.data
		file.project = form.project.data
		file.character_first_name=form.character_first_name.data
		file.character_last_name= form.character_last_name.data
		file.character_description = form.character_description.data
		db.session.commit()
		return redirect(url_for('characterpage', file_id=file_id))
	return render_template('editfile.html',title='Edit file', form=form, file=file)

@app.route('/account/file/<int(min=1):file_id>/edit_character', methods=['GET', 'POST'])
@login_required
def editcharacter(file_id):
	form = CharacterForm()
	Chara = CharacterFile.query.filter_by(file_id=file_id).first()
	if form.submit.data:
		Chara.eye_colour = form.eye_colour.data
		Chara.pet_peeves = form.pet_peeves.data
		Chara.hobbies = form.hobbies.data
		Chara.alignment = form.alignment.data
		Chara.accent = form.accent.data
		Chara.passionate = form.passionate.data
		Chara.earlybird_nightowl = form.earlybird_nightowl.data
		Chara.favourite_meal = form.favourite_meal.data
		Chara.goals = form.goals.data
		Chara.music_genre = form.music_genre.data
		Chara.cat_person = form.cat_person.data
		Chara.dog_person = form.dog_person.data
		Chara.romantic_relationship_ideals = form.romantic_relationship_ideals.data
		Chara.partial_birthday_celebration = form.partial_birthday_celebration.data
		Chara.easy_appologiser = form.easy_appologiser.data
		Chara.bullied = form.bullied.data
		Chara.smarts = form.smarts.data
		Chara.country = form.country.data
		Chara.book_worm = form.book_worm.data
		Chara.fears = form.fears.data
		Chara.address = form.address.data
		Chara.gender = form.gender.data
		Chara.birthday = form.birthday.data
		Chara.health_issues = form.health_issues.data
		Chara.mother = form.mother.data
		Chara.father = form.father.data
		Chara.relationships = form.relationships.data
		Chara.skills_number = form.skills_number.data
		Chara.magical_abilities = form.magical_abilities.data
		Chara.improvements = form.improvements.data
		db.session.commit()
		return redirect(url_for('characterpage', file_id=file_id))
	return render_template('editcharacter.html', title='Edit Character', form=form, file=Chara)

@app.route('/account/file/<int(min=1):file_id>/address/edit', methods=['GET','POST'])
@login_required
def editaddress(file_id):
	form =  AddressForm()
	file = CharacterAddress.query.filter_by(file_id=file_id).first()
	if form.validate_on_submit():
		file.address_1 = form.address_1.data
		file.address_2 =  form.address_2.data
		file.town = form.town.data
		file.county = form.county.data
		file.country = form.country.data
		file.postcode_zipcode = form.postcode_zipcode.data
		db.session.commit()
		return redirect(url_for('characterpage', file_id=file_id))
	return render_template('address.html', title='Address form', form=form)

@app.route('/account/file/<int(min=1):file_id>/scar/<int(min=1):scars_id>/delete', methods=['GET','POST'])
@login_required
def deletescar(file_id, scars_id):
	form = DeleteForm()
	scar = Scars.query.filter_by(id=scars_id).first()
	if form.yes.data:
		scarData = Scars.query.filter_by(id=scars_id).first()
		db.session.delete(scarData)
		db.session.commit()
		return redirect (url_for('characterpage', file_id=file_id))
	return render_template('deletescars.html', title='Delete scar', form=form)

@app.route('/account/file/<int(min=1):file_id>/tattoo/<int(min=1):tattoos_id>/delete', methods=['GET','POST'])
@login_required
def deletetattoo(file_id, tattoos_id):
	form = DeleteForm()
	tattoo = Tattoos.query.filter_by(id=tattoos_id).first()
	if form.yes.data:
		print('hellow?')
		tattooData = Tattoos.query.filter_by(id=tattoos_id).first()
		db.session.delete(tattooData)
		db.session.commit()
		return redirect (url_for('characterpage', file_id=file_id))
	return render_template('deletetattoo.html', title='Delete tattoo', form=form)

@app.route('/account/file/<int(min=1):file_id>/skill/<int(min=1):skills_id>/delete', methods=['GET','POST'])
@login_required
def deleteskill(file_id, skills_id):
	form = DeleteForm()
	skill = Skills.query.filter_by(id=skills_id).first()
	if form.yes.data:
		skillData = Skills.query.filter_by(id=skills_id).first()
		db.session.delete(skillData)
		db.session.commit()
		
		temp = Skills.query.filter_by(file_id=file_id).count()
		chara= CharacterFile.query.filter_by(id=file_id).first()
		chara.skills_number = int(temp)
		db.session.commit()
		return redirect (url_for('characterpage', file_id=file_id))
	return render_template('deleteskill.html', title='Delete skill', form=form)

@app.route('/account/file/<int(min=1):file_id>/magical_ability/<int(min=1):magic_id>/delete', methods=['GET','POST'])
@login_required
def deletemagic(file_id, magic_id):
	form = DeleteForm()
	magic = Magical.query.filter_by(id=magic_id).first()
	if form.yes.data:
		magicData = Magical.query.filter_by(id=magic_id).first()
		db.session.delete(magicData)
		db.session.commit()
		return redirect (url_for('characterpage', file_id=file_id))
	return render_template('deletemagic.html', title='Delete magical ability', form=form)

@app.route('/account/file/<int(min=1):file_id>/relationship/<int(min=1):relationship_id>/delete', methods=['GET','POST'])
@login_required
def deleterelationship(file_id, relationship_id):
	form = DeleteForm()
	relationship = Relationships.query.filter_by(id=relationship_id).first()
	if form.yes.data:
		Data = Relationships.query.filter_by(id=relationship_id).first()
		db.session.delete(Data)
		db.session.commit()
		return redirect (url_for('characterpage', file_id=file_id))
	return render_template('deleterelationship.html', title='Delete magical ability', form=form)	

@app.route('/account/file/<int(min=1):file_id>/scars_form', methods=['GET', 'POST'])
@login_required
def scars(file_id):
	form =  ScarsForm()
	if form.validate_on_submit():
		ScarsData = Scars(
			file_id = file_id,
			scars_what = form.scars_what.data,
			scars_where =  form.scars_where.data,
			scars_why = form.scars_why.data
			)
		temp = CharacterFile.query.filter_by(id=file_id).first()
		temp.scars=1
		db.session.add(ScarsData)
		db.session.commit()
		if form.submit_yes.data:
			return redirect(url_for('scars', file_id=file_id))
		if form.submit_no.data:
			return redirect(url_for('characterpage', file_id=file_id))
	return render_template('scars.html', title='Scars form', form=form)

@app.route('/account/file/<int(min=1):file_id>/tattoos_form', methods=['GET', 'POST'])
@login_required
def tattoos(file_id):
	form =  TattoosForm()
	if form.validate_on_submit():
		TattooData = Tattoos(
			file_id = file_id,
			tattoos_what = form.tattoos_what.data,
			tattoos_where =  form.tattoos_where.data
			)
		temp = CharacterFile.query.filter_by(id=file_id).first()
		temp.tattoos=1
		db.session.add(TattooData)
		db.session.commit()
		if form.submit_yes.data:
			return redirect(url_for('tattoos', file_id=file_id))
		if form.submit_no.data:
			return redirect(url_for('characterpage', file_id=file_id))
	return render_template('tattoos.html', title='Tattoos form', form=form)

@app.route('/account/file/<int(min=1):file_id>/address_form', methods=['GET', 'POST'])
@login_required
def address(file_id):
	form =  AddressForm()
	if form.validate_on_submit():
		AddressData = CharacterAddress(
			file_id = file_id,
			address_1 = form.address_1.data,
			address_2 =  form.address_2.data,
			town = form.town.data,
			county = form.county.data,
			country = form.country.data,
			postcode_zipcode = form.postcode_zipcode.data
			)
		temp = CharacterFile.query.filter_by(id=file_id).first()
		temp.address=1
		db.session.add(AddressData)
		db.session.commit()
		return redirect(url_for('characterpage', file_id=file_id))
	return render_template('address.html', title='Address form', form=form)

@app.route('/account/file/<int(min=1):file_id>/relationship_form', methods=["GET", "POST"])
@login_required
def relationships(file_id):
	form =  RelationshipForm()
	if form.validate_on_submit():
		Data = Relationships(
			file_id = file_id,
			relationship_type = form.relationship_type.data,
			first_name =  form.first_name.data,
			last_name = form.last_name.data,
			age = form.age.data,
			length = form.length.data,
			gender = form.gender.data
			)
		temp = CharacterFile.query.filter_by(id=file_id).first()
		temp.relationships=1
		db.session.add(Data)
		db.session.commit()
		if form.submit_yes.data:
			return redirect(url_for('relationships', file_id=file_id))
		elif form.submit_no.data:
			return redirect(url_for('characterpage', file_id=file_id))
	return render_template('relationships.html', title='Relationship form', form=form)

@app.route('/account/file/<int(min=1):file_id>/skill_form', methods=['GET', 'POST'])
@login_required
def skill(file_id):
	form =  SkillsForm()
	if form.validate_on_submit():
		Data = Skills(
			file_id = file_id,
			skills_what = form.skills_what.data,
			skills_used =  form.skills_used.data
			)
		db.session.add(Data)
		db.session.commit()
		if form.submit_yes.data:
			temp = Skills.query.filter_by(file_id=file_id).count()
			chara= CharacterFile.query.filter_by(id=file_id).first()
			chara.skills_number = int(temp)
			db.session.commit()
			return redirect(url_for('skill', file_id=file_id))
		if form.submit_no.data:
			temp = Skills.query.filter_by(file_id=file_id).count()
			chara= CharacterFile.query.filter_by(id=file_id).first()
			chara.skills_number = temp
			db.session.commit()
			return redirect(url_for('characterpage', file_id=file_id))
	return render_template('skill.html', title='Skills form', form=form)

@app.route('/account/file/<int(min=1):file_id>/magical_abilities_form', methods=['GET', 'POST'])
@login_required
def magical(file_id):
	form =  MagicalForm()
	if form.validate_on_submit():
		Data = Magical(
			file_id = file_id,
			MA_name = form.MA_name.data,
			MA_used =  form.MA_used.data,
			flaws = form.flaws.data,
			limitations = form.limitations.data,
			price = form.price.data
			)
		temp = CharacterFile.query.filter_by(id=file_id).first()
		temp.magical_abilities=1
		db.session.add(Data)
		db.session.commit()
		if form.submit_yes.data:
			return redirect(url_for('magical', file_id=file_id))
		if form.submit_no.data:
			return redirect(url_for('characterpage', file_id=file_id))
	return render_template('magical.html', title='Magical Abilities form', form=form)

@app.route('/account/file/search/<int(min=1):file_id>')
@login_required
def search(file_id):
	file= Files.query.filter_by(id=file_id)
	return render_template('search.html', title='Search', file=file
		)


@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))
