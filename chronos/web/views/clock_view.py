from flask import render_template, request, redirect
from .view import View

from chronos.features.clock_feature import ClockFeature


class ClockView(View):

    def get(self):
        clock_feature = ClockFeature(self.current_user)
        clock_is_open = clock_feature.clock_is_open()
        clocks = clock_feature.get_clocks().limit(20)
        return render_template('dashboard/clock.html', **locals())

    def start_clock(self):
        clock = ClockFeature(self.current_user)
        try:
            clock.start_clock()
        except ClockFeature.ClockAlreadyStarted:
            self.error_message('Clock was already started')
        return redirect('/clock')

    def stop_clock(self):
        clock = ClockFeature(self.current_user)
        try:
            clock.stop_clock()
        except ClockFeature.UnstartedClock:
            self.error_message('Clock was not started')
        return redirect('/clock')
