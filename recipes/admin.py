from django.contrib import admin
from recipes.models import Category, Flavor, Sauce, Recipe, Ingredient

# Register your models here.
admin.site.register(Category)
admin.site.register(Flavor)
admin.site.register(Sauce)
admin.site.register(Ingredient)
admin.site.register(Recipe)
