from chronos.tests.user_test import UserTest
from chronos.features.clock_feature import ClockFeature
from chronos.data.entities import Clock


class ClockFeatureTest(UserTest):

    def setUp(self):
        self.clock = ClockFeature(self.employee)

    def tearDown(self):
        Clock.delete().execute()

    def tick(self):
        self.clock.start_clock()
        self.clock.stop_clock()

    def test_start_clock(self):
        self.clock.start_clock()
        clocks = self.employee.clocks
        self.assertEqual(clocks.count(), 1)
        self.assertIsNone(clocks.first().stop)

    def test_stop_clock(self):
        self.clock.start_clock()
        self.clock.stop_clock()
        clock = self.employee.clocks.first()
        self.assertIsNotNone(clock.stop)

    def test_cannot_stop_clock_if_not_started(self):
        with self.assertRaises(ClockFeature.UnstartedClock):
            self.clock.stop_clock()

    def test_cannot_start_clock_if_already_started(self):
        self.clock.start_clock()
        with self.assertRaises(ClockFeature.ClockAlreadyStarted):
            self.clock.start_clock()

    def test_users_have_independent_clocks(self):
        admin_clock = ClockFeature(self.admin)
        employee_clock = ClockFeature(self.employee)
        admin_clock.start_clock()
        with self.assertRaises(ClockFeature.UnstartedClock):
            employee_clock.stop_clock()
        employee_clock.start_clock()
        employee_clock.stop_clock()
        admin_clock.stop_clock()

    def test_can_get_clocks_from_user(self):
        self.tick()
        self.tick()
        clocks = self.clock.get_clocks()
        self.assertEqual(clocks.count(), 2)

    def test_get_clocks_is_ordered_backwards(self):
        self.tick()
        self.tick()
        c1 = self.clock.get_clocks()[0]
        c2 = self.clock.get_clocks()[1]
        assert c1.stop > c2.stop
