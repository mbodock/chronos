from chronos.tests.test import Test

from chronos.web.app import app
from chronos.features.register_user_feature import RegisterUserFeature
from chronos.data.entities import User


class RegisterUserViewTest(Test):

    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        User.delete().execute()

    def test_register_page_is_accessible(self):
        response = self.client.get('/register')
        assert response.status_code == 200

    def test_can_register_user(self):
        response = self.client.post('/register', data={
            'email': 'foo@bar.com',
            'password1': '123456',
            'password2': '123456'
        })
        assert response.status_code == 302
        assert RegisterUserFeature().email_taken('foo@bar.com')

    def test_failing_register_attempt_redirects_back(self):
        response = self.client.post('/register', data={
            'email': 'foo@bar.com',
            'password1': '123456',
            'password2': '1234567'
        })
        assert response.status_code == 302
        assert not RegisterUserFeature().email_taken('foo@bar.com')
