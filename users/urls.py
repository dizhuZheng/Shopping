"""Define URL patterns for users"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetCompleteView,PasswordResetDoneView,PasswordResetConfirmView,PasswordChangeView
from . import views

urlpatterns = [
    #login page
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'),
        name='login'),
    #logout page
    url(r'^logout/$', views.logout_view, name='logout'),

    #reset password
    url(r'^password_reset/$', PasswordResetView.as_view(template_name='users/password_reset_form.html'),name='password_reset_form'),

    #reset done
    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name='password_reset_done'),

    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),

    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    #registration page
    url(r'^register/$', views.register, name='register')
]
