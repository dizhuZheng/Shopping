from django.conf.urls import url
from .views import index, categories, dish
from django.conf import settings

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^categories/$', categories, name='categories'),
]
