from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from . import views
from django.urls import reverse_lazy


urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
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
    path('password_change/', PasswordChangeView.as_view(
        template_name='password_change.html',
        success_url=reverse_lazy('password_change_done')),
         name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'),
         name='password_change_done'),
    path('profile/<username>/', views.profile, name='profile'),
    path('edit-profile/<username>/', views.edit_profile, name='edit_profile'),  # http://127.0.0.1:8000/edit-profile/test777/  where test777 need write username
    path('someone-profile', views.someone_profile, name='someone_profile'),
    path('add-profile/', views.add_profile, name='add_profile'),
]
