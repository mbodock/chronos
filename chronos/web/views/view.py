from flask import flash, get_flashed_messages


class View(object):

    def success_message(self, message):
        flash(message, 'success_message')
