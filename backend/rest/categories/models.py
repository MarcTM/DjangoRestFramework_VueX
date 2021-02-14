from django.db import models
from meals.models import Meal


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    meals = models.ManyToManyField(Meal)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title