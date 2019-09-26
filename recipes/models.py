from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.template.defaultfilters import slugify

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    pic_path = models.CharField(max_length=100)
    url = models.URLField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Flavor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    amount = models.SmallIntegerField()

    def __str__(self):
        return '%s,%d' % (name, amount)

class Sauce(models.Model):
    name = models.CharField(max_length=200)
    amount = models.SmallIntegerField()

    def __str__(self):
        return '%s,%d' % (name, amount)

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    flavor = models.ManyToManyField(Flavor, blank=True, default='')
    difficulty = models.IntegerField()
    rating = models.IntegerField()
    cooking_time = models.IntegerField()
    PEOPLE_CHOICES = (
        (1, '1 person'),
        (2, '2 people'),
        (3, '3 people'),
        (4, 'More')
    )
    people = models.IntegerField(max_length=2, choices=PEOPLE_CHOICES, default=1)
    ingredient = models.ManyToManyField(Ingredient, help_text='such as; rice')
    sauce = models.ManyToManyField(Ingredient, help_text='such as: slat')
    cover_img = models.ImageField(default='')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s,%d' % (name, amount)
