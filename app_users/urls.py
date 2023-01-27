from django.contrib.auth import views
from django.urls import path
from app_users.views import *

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('signup_order/', SignupWithOrder.as_view(), name='signup_order'),
    path('login/', LogInView.as_view(redirect_authenticated_user=True), name='login'),
    path('profile/', account_view, name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset/done/', ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', ResetPasswordCompleteView.as_view(), name='password_reset_complete'),
]
