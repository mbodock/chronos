from flask import redirect
from .app import app

from .views.login_view import LoginView
from .views.register_user_view import RegisterUserView
from .views.clock_view import ClockView


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

@app.route('/clock')
def get_clock():
    return ClockView().get()

@app.route('/clock/start', methods=['POST'])
def post_start_clock():
    return ClockView().start_clock()

@app.route('/clock/stop', methods=['POST'])
def post_stop_clock():
    return ClockView().stop_clock()
