from chronos.tests.test import Test

from chronos.features.register_user_feature import RegisterUserFeature
from chronos.features.clock_feature import ClockFeature

from chronos.data.database import database
from chronos.data.entities import User, Clock


class ClockFeatureTest(Test):

    def setUp(self):
        self.clock = ClockFeature()
        self.setup_user()

    def tearDown(self):
        database.query(Clock).delete()
        database.query(User).delete()

    def setup_user(self):
        self.register = RegisterUserFeature()
        self.user = self.register.register_user('foo@bar.com', '123456')

    def test_start_clock(self):
        self.clock.start_clock(self.user)
        clocks = self.clock.get_clocks_from_user(self.user)
        self.assertEqual(clocks.count(), 1)
        self.assertIsNone(clocks.one().stop)

    def test_stop_clock(self):
        self.clock.start_clock(self.user)
        self.clock.stop_clock(self.user)
        clock = self.clock.get_clocks_from_user(self.user).one()
        self.assertIsNotNone(clock.stop)

    def test_cannot_stop_clock_if_not_started(self):
        with self.assertRaises(ClockFeature.UnstartedClock):
            self.clock.stop_clock(self.user)

    def test_cannot_start_clock_if_already_started(self):
        self.clock.start_clock(self.user)
        with self.assertRaises(ClockFeature.ClockAlreadyStarted):
            self.clock.start_clock(self.user)
