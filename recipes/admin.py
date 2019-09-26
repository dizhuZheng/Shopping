from django.contrib import admin
from recipes.models import Category, Flavor, Ingredient, Sauce

# Register your models here.
admin.site.register(Category)
admin.site.register(Flavor)
admin.site.register(Ingredient)
admin.site.register(Sauce)
