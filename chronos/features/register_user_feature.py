import bcrypt
import re

from chronos.data.entities import User


class RegisterUserFeature(object):

    class InvalidEmail(Exception): pass
    class EmailTaken(Exception): pass
    class EmptyPassword(Exception): pass

    def register_user(self, email, password):
        self.validate_data(email, password)
        hashed_password = self.hash_password(password)
        type = User.ADMIN if not self.there_are_users() else User.EMPLOYEE
        return User.create(email=email, password=hashed_password, type=type)

    def validate_data(self, email, password):
        if not self.email_valid(email):
            raise self.InvalidEmail
        if self.email_taken(email):
            raise self.EmailTaken
        if not password:
            raise self.EmptyPassword

    def hash_password(self, password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')

    def email_valid(self, email):
        pattern = '^[^@]+@[^@]+\.[^@]+$'
        return bool(re.match(pattern, email))

    def email_taken(self, email):
        return User.select().where(User.email == email).exists()

    def there_are_users(self):
        return User.select().exists()
