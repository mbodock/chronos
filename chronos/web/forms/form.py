from flask import flash, get_flashed_messages


class Form(object):

    fields = ()

    def __init__(self, data=None):
        self.data = {}
        self.errors = {}
        if data:
            self.fetch_data(data)

    def fetch_data(self, data):
        for field in self.fields:
            self.data[field] = data.get(field)

    def is_valid(self):
        self.validate()
        return not bool(self.errors)

    def set_error(self, field, message):
        self.errors[field] = message

    def get_error(self, field):
        return self.errors.get(field)

    def persist(self, key=None):
        key = key or self.__class__.__name__
        flash(self.__dict__, key)

    @classmethod
    def persisted(self, key=None):
        key = key or self.__name__
        flashes = get_flashed_messages(category_filter=[key])
        if not flashes:
            return None
        form = Form()
        form.__dict__.update(flashes[0])
        return form
