from flask import render_template, request, redirect
from chronos.web.forms.register_user_form import RegisterUserForm


class RegisterUserView(object):

    def get(self):
        form = RegisterUserForm.persisted() or RegisterUserForm()
        return render_template('public/register_user.html', **locals())

    def post(self):
        form = RegisterUserForm(request.form)
        if not form.is_valid():
            form.persist()
            return redirect('/')
        form.register_user()
        return 'ok'
