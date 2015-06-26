from datetime import datetime, timedelta
from chronos.tests.user_test import UserTest
from chronos.data.entities import Clock
from chronos.features.clock_report_feature import ClockReportFeature


class ReportTest(UserTest):

    def setUp(self):
        self.feature = ClockReportFeature(self.employee)
        self.create_clocks()

    def tearDown(self):
        Clock.delete().execute()

    def create_clocks(self):
        self.create_clock(5, 8, 4)
        self.create_clock(5, 13, 5)
        self.create_clock(6, 8, 4)
        self.create_clock(6, 13, 5)
        self.create_clock(12, 8, 4)
        self.create_clock(12, 13, 5)

    def create_clock(self, day, hour, duration):
        Clock.create(
            user=self.employee,
            start=datetime(2015, 1, day, hour),
            stop=datetime(2015, 1, day, hour + duration)
        )

    def test_get_worked_time(self):
        start = datetime(2015, 1, 5)
        stop = datetime(2015, 1, 5, 23, 59, 59)
        worked_time = self.feature.get_worked_time(start, stop)
        self.assertEqual(timedelta(hours=9), worked_time)

    def test_get_worked_time_in_day(self):
        date = datetime(2015, 1, 5).date()
        worked_time = self.feature.get_worked_time_in_day(date)
        self.assertEqual(timedelta(hours=9), worked_time)

    def test_get_worked_time_in_week(self):
        date = datetime(2015, 1, 7).date()
        worked_time = self.feature.get_worked_time_in_week(date)
        self.assertEqual(timedelta(hours=18), worked_time)

    def test_get_worked_time_in_month(self):
        date = datetime(2015, 1, 7).date()
        worked_time = self.feature.get_worked_time_in_month(date)
        self.assertEqual(timedelta(hours=27), worked_time)
