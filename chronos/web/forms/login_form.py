from flask import session
from .form import Form
from chronos.features.login_feature import LoginFeature


class LoginForm(Form):

    fields = ('email', 'password')

    def validate(self):
        self.validate_required()
        if not self.errors:
            self.validate_credentials()

    def validate_required(self):
        if not self.data.get('email'):
            self.set_error('email', 'Required')
        if not self.data.get('password'):
            self.set_error('password', 'Required')

    def validate_credentials(self):
        feature = LoginFeature()
        email = self.data.get('email')
        password = self.data.get('password')
        try:
            feature.validate_credentials(email, password)
        except (LoginFeature.UserDoesNotExist, LoginFeature.InvalidPassword):
            self.set_error('global', 'Invalid credentials')

    def login(self):
        feature = LoginFeature()
        session['session_token'] = feature.login(
            email=self.data.get('email'),
            password=self.data.get('password')
        )
