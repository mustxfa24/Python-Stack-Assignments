from flask_app import app 

from flask import render_template, redirect, request, session, flash

from flask_app.models.model_user import User

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/controller_user/register', methods=['POST'])
def register_user():

    if not User.validate_new_user(request.form):
        print('validation fails')
        return redirect('/')

    else:
        print('validation good')
        data = {
            'username': request.form['username'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        print(data)
        User.create_new_user(data)
        flash('User registered; login with that account')
        return redirect('/')

@app.route('/users/login', methods = ['POST'])
def login_user():
    # determine if the user exists

    user = User.get_user_by_username(request.form)

    if not User.get_user_by_username(request.form):
        flash('User with givern username does not exist.')
        return redirect('/')

    # check password against database record

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')

    # user is logged in

    session['user_id'] = user.id
    session['user_email'] = user.email


    return redirect('/success')

@app.route('/success')
def success():
    if not 'user_id' in session:
        flash('Please login to view this page')
        return redirect('/')
    return render_template('success.html')

@app.route('/user/logout')
def logout():
    session.clear()
    flash('Logged out; please login again.')
    return redirect('/')
