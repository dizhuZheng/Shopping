from django.conf.urls import url
from .views import index, categories, dish, new_dish
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #Home page
    url(r'^$', index, name='index'),
    url(r'^categories/$', categories, name='categories'),
    # url(r'^authors/$')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
