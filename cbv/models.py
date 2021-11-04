from django.db import models
from django.db.models.base import Model

class Post(models.Model):
    name = models.CharField(max_length=255)
