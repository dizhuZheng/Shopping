from django.db import models
from django.contrib.auth.models import User

class Dish(models.Model):
    """A dish the user is getting"""
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """return a string repre of the model."""
        return self.text


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
