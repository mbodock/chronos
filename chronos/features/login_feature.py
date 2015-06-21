from uuid import uuid4
import bcrypt

from chronos.data.entities import User, Session


class LoginFeature(object):

    class UserDoesNotExist(Exception): pass
    class InvalidPassword(Exception): pass

    def login(self, email, password):
        user = self.validate_credentials(email, password)
        return self.create_session(user)

    def is_logged(self, token):
        return Session.select().where(Session.token == token).exists()

    def logout(self, token):
        Session.delete().where(Session.token == token).execute()

    def get_current_user(self, token):
        session = Session.select().where(Session.token == token).first()
        if session:
            return User.get(User.id == session.user_id)
        return None

    def validate_credentials(self, email, password):
        user = User.select().where(User.email == email).first()
        if not user:
            raise self.UserDoesNotExist
        if not self.password_match(user, password):
            raise self.InvalidPassword
        return user

    def create_session(self, user):
        token = self.generate_token()
        Session.create(user=user, token=token)
        return token

    def password_match(self, user, password):
        return user.password == self.hash_password(password, user.password)

    def hash_password(self, password, stored_password):
        stored_password = stored_password.encode('utf-8')
        hashed = bcrypt.hashpw(password.encode('utf-8'), stored_password)
        return hashed.decode('utf-8')

    def generate_token(self):
        return str(uuid4())
