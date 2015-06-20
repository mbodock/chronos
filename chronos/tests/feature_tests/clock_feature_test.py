from .user_test import UserTest
from chronos.features.clock_feature import ClockFeature
from chronos.data.database import database
from chronos.data.entities import Clock


class ClockFeatureTest(UserTest):

    def setUp(self):
        self.clock = ClockFeature()

    def tearDown(self):
        database.query(Clock).delete()

    def test_start_clock(self):
        self.clock.start_clock(self.employee)
        clocks = self.clock.get_clocks_from_user(self.employee)
        self.assertEqual(clocks.count(), 1)
        self.assertIsNone(clocks.one().stop)

    def test_stop_clock(self):
        self.clock.start_clock(self.employee)
        self.clock.stop_clock(self.employee)
        clock = self.clock.get_clocks_from_user(self.employee).one()
        self.assertIsNotNone(clock.stop)

    def test_cannot_stop_clock_if_not_started(self):
        with self.assertRaises(ClockFeature.UnstartedClock):
            self.clock.stop_clock(self.employee)

    def test_cannot_start_clock_if_already_started(self):
        self.clock.start_clock(self.employee)
        with self.assertRaises(ClockFeature.ClockAlreadyStarted):
            self.clock.start_clock(self.employee)
