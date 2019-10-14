from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    pic_path = models.CharField(max_length=100)
    url = models.URLField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'
        unique_together = (('name', 'pic_path'))

    def __str__(self):
        return self.name

class Flavor(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Common(models.Model):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    amount = models.DecimalField(max_digits=5, decimal_places=3)
    UNIT_CHOICE = (
        ('g','grams'),
        ('ml','ml'),
        ('l', 'l'),
        ('kg', 'kg')
    )
    unit = models.CharField(max_length=2, choices=UNIT_CHOICE, default='g')

    class Meta:
        abstract = True
        ordering = ['name']

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
    difficulty = models.IntegerField(validators.MaxValueValidator(limit_value=5), default=1)
    rating = models.IntegerField(validators.MaxValueValidator(limit_value=5), default=3)
    cooking_time = models.PositiveIntegerField()
    PEOPLE_CHOICES = (
        (1, '1 person'),
        (2, '2 people'),
        (3, '3 people'),
        (4, 'More')
    )
    people = models.IntegerField(choices=PEOPLE_CHOICES, default=1)
    ingredient = models.ManyToManyField(Ingredient, related_name='recipe_ingredient', default='')
    sauce = models.ManyToManyField(Sauce, related_name='recipe_sauce', default='')
    directions = models.TextField(max_length=2000, default='')
    cover_img = models.ImageField(default='media/smile.jpg')
    date_added = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-rating']
        get_latest_by = ['date-added']

    def __str__(self):
        return '%s,%s,%s' % (self.title, self.owner, self.date_added)
