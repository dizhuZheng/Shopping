"""Define URL patterns for users"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetForm,PasswordResetCompleteView,PasswordResetDoneView,PasswordResetConfirmView,PasswordChangeView
from . import views

urlpatterns = [
    #login page
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'),
        name='login'),

    #registration page
    url(r'^register/$', views.register, name='register'),

    #logout page
    url(r'^logout/$', views.logout_view, name='logout'),

    #reset password
    url(r'^password_reset/$', PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset_form'),

    #reset done
    url(r'^password_reset_done/$', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),

    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm')
]
