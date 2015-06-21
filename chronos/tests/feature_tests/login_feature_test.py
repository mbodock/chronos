from chronos.tests.test import Test

from chronos.features.register_user_feature import RegisterUserFeature
from chronos.features.login_feature import LoginFeature

from chronos.data.entities import User, Session


class LoginFeatureTest(Test):

    def setUp(self):
        self.feature = LoginFeature()

    def tearDown(self):
        Session.delete().execute()
        User.delete().execute()

    def register_example_user(self):
        RegisterUserFeature().register_user('foo@bar.com', '123456')

    def test_can_login_with_valid_credentials(self):
        self.register_example_user()
        token = self.feature.login('foo@bar.com', '123456')
        self.assertTrue(self.feature.is_logged(token))

    def test_cannot_login_with_inexistent_user(self):
        with self.assertRaises(LoginFeature.UserDoesNotExist):
            self.feature.login('foo@bar.com', '123456')

    def test_cannot_login_with_invalid_password(self):
        self.register_example_user()
        with self.assertRaises(LoginFeature.InvalidPassword):
            self.feature.login('foo@bar.com', '1234567')

    def test_can_get_current_user(self):
        self.register_example_user()
        token = self.feature.login('foo@bar.com', '123456')
        user = self.feature.get_current_user(token)
        self.assertEquals(user.email, 'foo@bar.com')

    def test_cannot_get_current_user_without_login(self):
        self.register_example_user()
        user = self.feature.get_current_user('invalid_token')
        self.assertIsNone(user)

    def test_can_logout(self):
        self.register_example_user()
        token = self.feature.login('foo@bar.com', '123456')
        self.feature.logout(token)
        self.assertFalse(self.feature.is_logged(token))
        self.assertIsNone(self.feature.get_current_user(token))
