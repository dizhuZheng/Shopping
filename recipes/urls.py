from django.conf.urls import url, include
from .views import index, categories, new_dish, breakfast
from django.conf import settings

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^categories/$', categories, name='categories'),
    url(r'^categories/breakfast/$', breakfast, name='breakfast'), #from db
    url(r'^comments/', include('django_comments.urls')),
    url(r'^new_dish/$', new_dish, name='new_dish'),
]
