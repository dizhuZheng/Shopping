from django.urls import re_path
from . import views

app_name = 'myaccount'
urlpatterns = [
    re_path(r'^profile/(?P<username>[\w.@+-]+)/$', views.profile, name='profile'),
    re_path(r'^profile/(?P<username>[\w.@+-]+)/updates/$', views.profile_update, name='profile_update'),
    re_path(r'^personal_space/(?P<username>[\w.@+-]+)/$', views.personal_space, name='personal_space'),
]
