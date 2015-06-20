from flask import send_from_directory, redirect
from .app import app

from .views.before_request_view import BeforeRequestView
from .views.login_view import LoginView
from .views.register_user_view import RegisterUserView


@app.before_request
def before_request():
    return BeforeRequestView().get()

@app.route('/static/<path:path>')
def get_static(path):
    return send_from_directory('static', path)


@app.route('/')
def get_root():
    return redirect('/login')

@app.route('/login')
def get_login():
    return LoginView().get()

@app.route('/login', methods=['POST'])
def post_login():
    return LoginView().login()

@app.route('/logout')
def get_logout():
    return LoginView().logout()

@app.route('/register')
def get_register_user():
    return RegisterUserView().get()

@app.route('/register', methods=['POST'])
def post_register_user():
    return RegisterUserView().post()

@app.route('/dashboard')
def get_dashboard():
    return 'Dashboard >> <a href="/logout">Logout</a>'
