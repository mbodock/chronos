from datetime import datetime
from chronos.data.entities import Clock


class ClockFeature(object):

    class ClockAlreadyStarted(Exception): pass
    class UnstartedClock(Exception): pass

    def start_clock(self, user):
        if self.user_has_open_clock(user):
            raise self.ClockAlreadyStarted
        return Clock.create(user=user, start=datetime.now())

    def stop_clock(self, user):
        clock = self.get_open_clock_from_user(user)
        if not clock:
            raise self.UnstartedClock
        clock.stop = datetime.now()
        clock.save()

    def user_has_open_clock(self, user):
        return Clock.select().where(Clock.stop == None).exists()

    def get_open_clock_from_user(self, user):
        return Clock.select().where(Clock.stop == None).first()
