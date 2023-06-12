from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView

from .services import send_order_email
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from users.forms import UserForm, RegisterForm
from users.models import User


# Create your views here.
class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm

    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        send_order_email()
        return super().form_valid(form)


class ResetView(PasswordResetView):
    model = User
    template_name = 'users/resetview.html'
    email_template_name = 'users/password_reset_email.html'

    success_url = reverse_lazy('catalog:index')


class ResetDoneView(PasswordResetDoneView):
    model = User
    template_name = 'users/password_reset_done_view.html'

class ResetConfirmView(PasswordResetConfirmView):

    template_name = 'users/password_reset_confirm.html'

class ResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'