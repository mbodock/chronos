from flask import send_from_directory, session
from .app import app

from chronos.features.login_feature import LoginFeature
from .views.before_request_view import BeforeRequestView


@app.before_request
def before_request():
    return BeforeRequestView().get()

@app.route('/static/<path:path>')
def get_static(path):
    return send_from_directory('static', path)

@app.context_processor
def inject_current_user():
    user = LoginFeature().get_current_user(session.get('session_token'))
    return {'current_user': user}
