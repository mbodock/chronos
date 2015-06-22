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
        clock.start_clock()
        return redirect('/clock')

    def stop_clock(self):
        clock = ClockFeature(self.current_user)
        clock.stop_clock()
        return redirect('/clock')
