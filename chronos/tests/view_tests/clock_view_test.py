from chronos.tests.user_test import UserTest
from chronos.web.app import app
from chronos.features.clock_feature import ClockFeature
from chronos.data.entities import Clock


class ClockViewTest(UserTest):

    def setUp(self):
        self.client = app.test_client()
        self.client.post('/login', data={
            'email': self.employee.email,
            'password': '123456',
        })

    def tearDown(self):
        Clock.delete().execute()

    def test_can_access_clock(self):
        response = self.client.get('/clock')
        self.assertEqual(response.status_code, 200)

    def test_can_start_clock(self):
        response = self.client.post('/clock/start')
        self.assertEqual(response.status_code, 302)
        clock = Clock.get()
        self.assertIsNone(clock.stop)

    def test_can_stop_clock(self):
        self.client.post('/clock/start')
        response = self.client.post('/clock/stop')
        self.assertEqual(response.status_code, 302)
        clock = Clock.get()
        self.assertIsNotNone(clock.stop)

    def test_starting_twice_results_in_redirect(self):
        self.client.post('/clock/start')
        response = self.client.post('/clock/start')
        self.assertEqual(response.status_code, 302)

    def test_stopping_unstarted_results_in_redirect(self):
        response = self.client.post('/clock/stop')
        self.assertEqual(response.status_code, 302)
