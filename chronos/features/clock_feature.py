from datetime import datetime

from chronos.data.database import database
from chronos.data.entities import Clock


class ClockFeature(object):

    class ClockAlreadyStarted(Exception): pass
    class UnstartedClock(Exception): pass

    def start_clock(self, user):
        if self.get_open_clock_from_user(user):
            raise self.ClockAlreadyStarted
        clock = Clock(user_id=user.id, start=datetime.now())
        database.add(clock)

    def stop_clock(self, user):
        clock = self.get_open_clock_from_user(user)
        if not clock:
            raise self.UnstartedClock
        clock.stop = datetime.now()

    def get_clocks_from_user(self, user):
        return database.query(Clock).order_by(Clock.id)

    def get_open_clock_from_user(self, user):
        return database.query(Clock).filter(Clock.stop == None).first()
