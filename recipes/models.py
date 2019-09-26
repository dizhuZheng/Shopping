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
