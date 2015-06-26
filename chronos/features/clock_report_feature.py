import calendar
from datetime import datetime, timedelta

from chronos.data.entities import Clock


class ClockReportFeature(object):

    def __init__(self, user):
        self.user = user

    def get_worked_time(self, start, stop):
        clocks = Clock.select().where(
            (Clock.start >= start) &
            (Clock.stop <= stop)
        )
        total = timedelta(0)
        for clock in clocks:
            total += clock.stop - clock.start
        return total

    def get_worked_time_in_day(self, date):
        start = datetime(date.year, date.month, date.day)
        stop = datetime(date.year, date.month, date.day, 23, 59, 59)
        return self.get_worked_time(start, stop)

    def get_worked_time_in_week(self, date):
        sunday = date.replace(day=date.day-date.isoweekday())
        start = datetime(sunday.year, sunday.month, sunday.day)
        stop_day = start.day + 7
        stop = start.replace(day=stop_day, hour=23, minute=59, second=59)
        return self.get_worked_time(start, stop)

    def get_worked_time_in_month(self, date):
        firt_day_of_month = date.replace(day=1)
        last_day_of_month = date.replace(
            day=calendar.monthrange(date.year, date.month)[1]
        )
        start = self.date_to_datetime(firt_day_of_month)
        stop = self.date_to_datetime(last_day_of_month)
        stop = stop.replace(hour=23, minute=59, second=59)
        return self.get_worked_time(start, stop)

    def date_to_datetime(self, date):
        return datetime.combine(date, datetime.min.time())
