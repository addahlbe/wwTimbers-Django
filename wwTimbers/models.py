from django.db import models

# Create your models here.


class Image(models.Model):
    path = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
