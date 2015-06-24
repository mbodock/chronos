from flask import session, flash
from chronos.features.login_feature import LoginFeature


class View(object):

    def __init__(self):
        self.current_user = LoginFeature().get_current_user(session.get('session_token'))

    def success_message(self, message):
        flash(message, 'success_message')

    def error_message(self, message):
        flash(message, 'error_message')
