from flask import flash


class View(object):

    def success_message(self, message):
        flash(message, 'success_message')
