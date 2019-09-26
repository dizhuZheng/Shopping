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

class Common(models.Model):
    name = models.CharField(max_length=200)
    amount = models.SmallIntegerField()
    UNIT_CHOICE = (
        ('g','grams'),
        ('ml','ml')
    )
    unit = models.CharField(max_length=2, choices=UNIT_CHOICE, default='g')

    class Meta:
        abstract = True

    def __str__(self):
        return '%s,%d,%s' % (self.name, self.amount,self.unit)

class Sauce(Common):
    pass

class Ingredient(Common):
    pass

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
    people = models.IntegerField(choices=PEOPLE_CHOICES, default=1)
    ingredient = models.ManyToManyField(Ingredient, related_name='recipe_ingredient', default='')
    sauce = models.ManyToManyField(Sauce, related_name='recipe_sauce', default='')
    cover_img = models.ImageField(default='media/smile.jpg')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s,%s,%s' % (self.title, self.owner, self.date_added)
