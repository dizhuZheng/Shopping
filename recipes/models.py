from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    pic_path = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Flavor(models.Model):
    """flavor choices"""
    name = models.CharField(primary_key=True, max_length=100)

class Recipe(models.Model):
    """something specific learned about a topic"""
    name = models.CharField(max_length=80)
    category = models.ForeignKey(Category, related_name='recipe_category', on_delete=models.SET_NULL, null=True)
    pics = models.ImageField(null=True, blank=True, upload_to='dish_pics')
    flavor = models.ManyToManyField(Flavor, related_name='recipe_flavor',blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    difficulty = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'recipes'
        ordering=['-date_added']

    def __str__(self):
        """return a string representation of the model"""
        return "%s, %s, %d" % (self.name, self.owner, self.date_added)
