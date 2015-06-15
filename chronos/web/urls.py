from .app import app
from .views.register_user_view import RegisterUserView


@app.route('/')
def get_register_user():
    return RegisterUserView().get()

@app.route('/', methods=['POST'])
def post_register_user():
    return RegisterUserView().post()
