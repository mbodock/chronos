from flask import send_from_directory
from .app import app
from .views.register_user_view import RegisterUserView


@app.route('/static/<path:path>')
def get_static(path):
    return send_from_directory('static', path)

@app.route('/')
def get_register_user():
    return RegisterUserView().get()

@app.route('/', methods=['POST'])
def post_register_user():
    return RegisterUserView().post()
