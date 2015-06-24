from chronos.tests.test import Test

from chronos.features.register_user_feature import RegisterUserFeature
from chronos.data.entities import User


class RegisterUserFeatureTest(Test):

    def setUp(self):
        self.feature = RegisterUserFeature()

    def tearDown(self):
        User.delete().execute()

    def register_foobar(self):
        return self.feature.register_user('foo@bar.com', '123456')

    def test_user_can_register(self):
        self.register_foobar()
        assert self.feature.email_taken('foo@bar.com')

    def test_password_is_encrypted(self):
        user = self.register_foobar()
        assert user.password != '123456'

    def test_cannot_register_taken_email(self):
        self.register_foobar()
        with self.assertRaises(RegisterUserFeature.EmailTaken):
            self.register_foobar()

    def test_cannot_register_invalid_email(self):
        with self.assertRaises(RegisterUserFeature.InvalidEmail):
            self.feature.register_user('foobar', '123456')

    def test_cannot_register_empty_password(self):
        with self.assertRaises(RegisterUserFeature.EmptyPassword):
            self.feature.register_user('foo@bar.com', '')

    def test_first_registered_user_is_admin(self):
        user = self.register_foobar()
        assert user.type == User.ADMIN

    def test_second_registered_user_is_employee(self):
        self.register_foobar()
        user = self.feature.register_user('bar@biz.com', '123456')
        assert user.type == User.EMPLOYEE

    def test_cannot_register_taken_email_changing_case(self):
        self.register_foobar()
        with self.assertRaises(RegisterUserFeature.EmailTaken):
            self.feature.register_user('FOO@BAR.COM', '123456')
