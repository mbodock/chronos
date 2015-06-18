from flask import render_template, request, redirect
from .view import View
from ..forms.login_form import LoginForm


class LoginView(View):

    def get(self):
        form = LoginForm.persisted() or LoginForm()
        return render_template('public/login.html', **locals())

    def post(self):
        form = LoginForm(request.form)
        if not form.is_valid():
            form.persist()
            return redirect('/login')
        form.login()
        return redirect('/dashboard')
