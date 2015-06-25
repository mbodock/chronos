from flask import render_template
from .view import View


class ClockReportView(View):

    def get(self):
        return render_template('dashboard/clock_report.html')
