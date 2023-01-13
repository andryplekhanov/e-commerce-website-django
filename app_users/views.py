from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView

from app_users.forms import UserLoginForm, CreationUserForm, UserChangingForm, PasswordSetForm, ResetPasswordForm
from .models import User


class Signup(CreateView):
    model = User
    form_class = CreationUserForm
    template_name = 'app_users/signup.html'
    success_url = reverse_lazy('profile')

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse('profile'))
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = CreationUserForm(request.POST, request.FILES)
        self.object = None

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return HttpResponseRedirect(self.success_url)
        return self.form_invalid(form)


class LogInView(LoginView):
    template_name = 'app_users/login.html'
    authentication_form = UserLoginForm
    next_page = reverse_lazy('index')


class LogOutView(LogoutView):
    next_page = '/'


class EditProfileView(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = UserChangingForm
    model = User
    template_name = 'app_users/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        return reverse('edit_profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.info(self.request, _("Профиль успешно сохранен"))
        user = self.request.user

        if form.cleaned_data.get('password1'):
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            logout(self.request)
            user = authenticate(email=email, password=password)
            login(self.request, user)
        return super(EditProfileView, self).form_valid(form)


@login_required
def account_view(request):
    return render(request, 'app_users/profile.html', {'user': request.user})


class ResetPasswordView(PasswordResetView):
    email_template_name = 'app_users/password_reset_email.html'
    template_name = 'app_users/password_reset_form.html'
    form_class = ResetPasswordForm


class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = 'app_users/password_reset_done.html'


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'app_users/password_reset_confirm.html'
    form_class = PasswordSetForm
    post_reset_login = False

    def get_success_url(self):
        return reverse_lazy('password_reset_complete')


class ResetPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'app_users/password_reset_complete.html'
