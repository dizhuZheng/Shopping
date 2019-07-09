from django.db import models

class Dish(models.Model):
    """A dish the user is getting"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return a string repre of the model."""
        return self.text


class Entry(models.Model):
    """something specific learned about a topic"""
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """return a string representation of the model"""
        return self.text[:50] + "..."


class Image(models.Model):
    """pictures"""
    img = models.ImageField(upload_to='img')
    time = models.DateTimeField(auto_now_add=True)
