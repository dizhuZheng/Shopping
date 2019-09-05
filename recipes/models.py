from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    pic_path = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Dish(models.Model):
    """A dish the user is getting"""
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    difficulty = models.IntegerField()

    def __str__(self):
        """return a string repre of the model."""
        return '%s,% s,%d,%d' % (self.name, self.owner, self.rating, self.difficulty)


class Entry(models.Model):
    """something specific learned about a topic"""
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """return a string representation of the model"""
        return self.text[:50] + "..."


class IMG(models.Model):
    """users can add pic to each dish"""
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)
