from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title