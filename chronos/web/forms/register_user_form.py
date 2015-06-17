from .form import Form
from chronos.features.register_user_feature import RegisterUserFeature


class RegisterUserForm(Form):

    fields = ('email', 'password1', 'password2')

    def validate(self):
        self.validate_email()
        self.validate_passwords()

    def validate_email(self):
        feature = RegisterUserFeature()
        if not self.data.get('email'):
            self.set_error('email', 'Required')
        elif not feature.email_valid(self.data.get('email')):
            self.set_error('email', 'Invalid email address')
        elif feature.email_taken(self.data.get('email')):
            self.set_error('email', 'Email already taken')

    def validate_passwords(self):
        if not self.data.get('password1'):
            self.set_error('password1', 'Required')
        if not self.data.get('password2'):
            self.set_error('password2', 'Required')
        if self.data.get('password1') != self.data.get('password2'):
            self.set_error('password2', 'Passwords don\'t match')

    def register_user(self):
        feature = RegisterUserFeature()
        feature.register_user(
            email=self.data.get('email'),
            password=self.data.get('password1'),
        )
