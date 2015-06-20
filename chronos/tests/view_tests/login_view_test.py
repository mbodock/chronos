from chronos.tests.test import Test

from chronos.web.app import app

from chronos.features.register_user_feature import RegisterUserFeature
from chronos.features.login_feature import LoginFeature

from chronos.data.database import database
from chronos.data.entities import User, Session


class LoginViewTest(Test):

    def setUp(self):
        self.feature = LoginFeature()
        self.client = app.test_client()
        self.user = RegisterUserFeature().register_user('foo@bar.com', '123456')

    def tearDown(self):
        database.query(Session).delete()
        database.query(User).delete()

    def test_login_is_reachable(self):
        response = self.client.get('/login')
        self.assertEquals(response.status_code, 200)

    def test_user_can_login(self):
        response = self.client.post('/login', data={
            'email': self.user.email,
            'password': '123456',
        })
        self.assertEquals(response.status_code, 302)
        session = database.query(Session).filter(Session.user_id == self.user.id).one()
        self.assertTrue(self.feature.is_logged(session.token))

    def test_user_can_logout(self):
        response = self.client.post('/login', data={
            'email': self.user.email,
            'password': '123456',
        })
        self.assertEquals(response.status_code, 302)
        session = database.query(Session).filter(Session.user_id == self.user.id).one()
        self.feature.logout(session.token)
        self.assertFalse(self.feature.is_logged(session.token))
