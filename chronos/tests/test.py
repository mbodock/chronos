import hashlib

from unittest import TestCase
from chronos.features.register_user_feature import RegisterUserFeature
from chronos.features.login_feature import LoginFeature


class Test(TestCase):

    @classmethod
    def setUpClass(self):
        self.remove_bcrypt()

    @classmethod
    def remove_bcrypt(self):
        RegisterUserFeature.hash_password = self.hash_password
        LoginFeature.hash_password = self.hash_password

    def hash_password(self, password, stored_password=None):
        stored_password = 'salt'
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        m.update(stored_password.encode('utf-8'))
        return m.hexdigest()
