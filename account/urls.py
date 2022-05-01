from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .views import index, signup, log_in, log_out, profile

# email test@gmail.com
# pass BXEOEgb3

urlpatterns = [
    path("", index, name="home"),
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt',
        success_url='/password_reset/done/'),
         name='password_reset'
         ),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'),
         name='password_reset_done'
         ),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
        success_url='/reset/done/'),
         name='password_reset_confirm'
         ),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'),
         name='password_reset_complete'
         ),
    path('profile/<username>/', profile, name='profile'),
]
