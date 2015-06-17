from flask import render_template, request, redirect
from chronos.web.forms.register_user_form import RegisterUserForm
from .view import View


class RegisterUserView(View):

    def get(self):
        form = RegisterUserForm.persisted() or RegisterUserForm()
        return render_template('public/register_user.html', **locals())

    def post(self):
        form = RegisterUserForm(request.form)
        if not form.is_valid():
            form.persist()
            return redirect('/register')
        form.register_user()
        self.success_message('You are registered and ready for login!')
        return redirect('/register')
