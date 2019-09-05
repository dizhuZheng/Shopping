from django.contrib import admin
from recipes.models import Dish, Entry, Category

# Register your models here.
admin.site.register(Dish)
admin.site.register(Entry)
admin.site.register(Category)
