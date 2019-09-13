from django.conf.urls import url
from .views import index, categories, dish, breakfast
from django.conf import settings

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^categories/$', categories, name='categories'),
    url(r'^categories/breakfast/$', breakfast, name='breakfast')
]
