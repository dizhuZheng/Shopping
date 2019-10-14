from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/(?P<id>\d+)/$', views.sub_category, name='sub_category'),
    # url(r'^categories/breakfast/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', breakfast_details, name='breakfast_details'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^new_dish/$', views.new_dish, name='new_dish'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
