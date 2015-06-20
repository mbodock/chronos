from flask import render_template, request, redirect, session
from .view import View
from ..forms.login_form import LoginForm
from chronos.features.login_feature import LoginFeature


class LoginView(View):

    def get(self):
        form = LoginForm.persisted() or LoginForm()
        return render_template('public/login.html', **locals())

    def login(self):
        form = LoginForm(request.form)
        if not form.is_valid():
            form.persist()
            return redirect('/login')
        form.login()
        return redirect('/dashboard')

    def logout(self):
        LoginFeature().logout(session.get('session_token'))
        return redirect('/login')
