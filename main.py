from crypt import methods
from curses import flash
from unicodedata import category
from flask import Flask,render_template,redirect,url_for,flash,session,request
from config import *
from forms import LoginForm,SignupForm,PitchesForm
from models.user import User
from models.pitch import Pitch
from db import app, db
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_login import LoginManager,login_user,login_required,current_user
from werkzeug.security import check_password_hash,generate_password_hash

bootstrap = Bootstrap(app)
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
#db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/',methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                session["user_id"] = user.id
                session["username"] = user.username
                return redirect(url_for('pitches'))
            flash('Invalid Username or Password')
        flash('Invalid Username or Password')

    return  render_template("login.html",form = form)

@app.route('/signup',methods=['GET','POST'])
def getsignup():

    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        first_name = signup_form.first_name.data
        last_name = signup_form.last_name.data
        username = signup_form.username.data
        email = signup_form.email.data
        password = signup_form.password.data

        hashed_password = generate_password_hash(password, method="sha256")

        new_user = User(first_name=first_name,last_name=last_name,username=username,email=email,password=hashed_password)

        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully')
        return redirect(url_for('login'))

    return render_template('signup.html',signup_form=signup_form)


@app.route('/pitches',methods=['GET','POST'])
def pitches():

    pitches_form = PitchesForm()

    if pitches_form.validate_on_submit():
        if not session.get("user_id", None):
            return redirect(url_for("login"))

        new_pitch = Pitch(pitch = pitches_form.pitch.data,category = pitches_form.category.data,user_id = session["user_id"])

        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('pitches'))
    
    if not session.get("username", None):
        return redirect(url_for('login'))

    return render_template('pitches.html',pitches_form = pitches_form,username = session["username"])

@app.route('/view/pitches',methods=['GET'])
def view_pitches():
    filter = request.args.get("category", None)
    if filter:
        pitches = Pitch.query.filter_by(category=filter).all()
    else:
        pitches = Pitch.query.filter_by().all()

    return render_template('view_pitches.html', pitches=pitches)

@app.route('/logout')
def logout():
    return render_template('index.html')


@manager.shell
def make_shell_context():
    return dict(app=app,db=db)

if __name__ == '__main__':
    manager.run()