from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.user_model import User

@app.route('/')
def index():

    return render_template('index.html', users = User.get_all_users())

@app.route('/new/user')
def new_user():
    return render_template('new_user.html')

@app.route('/create/user', methods = ['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.create_user(data)
    return redirect('/')

@app.route('/edit/user/<int:id>')
def edit_user(id):
    data = {
        'id': id
    }
    return render_template('edit_user.html', user = User.get_user_id(data))

@app.route('/update/user', methods = ['POST'])
def update_user():
    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect('/')

@app.route('/delete/user/<int:id>')
def delete_user(id):
    User.delete({'id': id})
    return redirect('/')

