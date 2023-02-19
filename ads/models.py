from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=5000)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    cost = models.IntegerField()