from django.db import models

class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title