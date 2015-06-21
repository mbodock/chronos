from flask import request, redirect, session
from chronos.features.login_feature import LoginFeature


class BeforeRequestView(object):

    public_endpoints = (
        'get_login',
        'post_login',
        'get_register_user',
        'post_register_user',
    )

    def get(self):
        if request.endpoint == 'static':
            return
        if self.should_redirect_to_login():
            return redirect('/login')
        if self.should_redirect_to_dashboard():
            return redirect('/dashboard')

    def should_redirect_to_login(self):
        login = LoginFeature()
        return (
            not login.is_logged(session.get('session_token')) and
            request.endpoint not in self.public_endpoints
        )

    def should_redirect_to_dashboard(self):
        login = LoginFeature()
        return (
            login.is_logged(session.get('session_token')) and
            request.endpoint in self.public_endpoints
        )
