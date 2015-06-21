from chronos.tests.test import Test
from chronos.features.register_user_feature import RegisterUserFeature
from chronos.data.entities import User


class UserTest(Test):

    @classmethod
    def setUpClass(self):
        super(UserTest, self).setUpClass()
        feature = RegisterUserFeature()
        self.admin = feature.register_user('admin@chronos.com', '123456')
        self.employee = feature.register_user('employee@chronos.com', '123456')

    @classmethod
    def tearDownClass(self):
        super(UserTest, self).tearDownClass()
        User.delete().execute()
