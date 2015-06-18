from uuid import uuid4
import bcrypt

from chronos.data.database import database
from chronos.data.entities import User, Session


class LoginFeature(object):

    class UserDoesNotExist(Exception): pass
    class InvalidPassword(Exception): pass

    def login(self, email, password):
        user = self.validate_credentials(email, password)
        return self.create_session(user)

    def validate_credentials(self, email, password):
        user = self.get_user_by_email(email)
        if not user:
            raise self.UserDoesNotExist
        if not self.password_match(user, password):
            raise self.InvalidPassword
        return user

    def get_user_by_email(self, email):
        return database.query(User).filter(User.email == email).first()

    def password_match(self, user, password):
        return user.password == self.hash_password(password, user.password)

    def hash_password(self, password, stored_password):
        stored_password = stored_password.encode('utf-8')
        hashed = bcrypt.hashpw(password.encode('utf-8'), stored_password)
        return hashed.decode('utf-8')

    def create_session(self, user):
        token = self.generate_token()
        session = Session(user_id=user.id, token=token)
        database.add(session)
        return token

    def generate_token(self):
        return str(uuid4())

    def is_logged(self, token):
        session = self.get_session(token)
        return bool(session)

    def get_current_user(self, token):
        session = self.get_session(token)
        if session:
            return self.get_user_by_id(session.user_id)
        return None

    def get_user_by_id(self, id):
        return database.query(User).filter(User.id == id).first()

    def get_session(self, token):
        return database.query(Session).filter(Session.token == token).first()

    def logout(self, token):
        database.query(Session).filter(Session.token == token).delete()
