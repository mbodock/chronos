from datetime import datetime
from chronos.data.entities import Clock


class ClockFeature(object):

    class ClockAlreadyStarted(Exception): pass
    class UnstartedClock(Exception): pass

    def __init__(self, user):
        self.user = user

    def start_clock(self):
        if self.clock_is_open():
            raise self.ClockAlreadyStarted
        return Clock.create(user=self.user, start=datetime.now())

    def stop_clock(self):
        clock = self.get_open_clock()
        if not clock:
            raise self.UnstartedClock
        clock.stop = datetime.now()
        clock.save()

    def get_clocks(self):
        return Clock.select().where(
            Clock.user == self.user
        ).order_by(Clock.id.desc())

    def clock_is_open(self):
        return Clock.select().where(
            Clock.user == self.user,
            Clock.stop == None,
        ).exists()

    def get_open_clock(self):
        return Clock.select().where(
            Clock.user == self.user,
            Clock.stop == None,
        ).first()
