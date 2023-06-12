from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import ProfileUpdateView, RegisterView, ResetView, ResetDoneView, ResetConfirmView, \
    ResetCompleteView

app_name = UsersConfig.name
urlpatterns = [

    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('reset/', ResetView.as_view(), name='reset'),
    path('reset/done/', ResetDoneView.as_view(), name='reset_done'),
    path('reset/<uidb64>/<token>/', ResetConfirmView.as_view(), name='password_confirm'),
    path('reset/compete/', ResetCompleteView.as_view(), name='confirm')



]