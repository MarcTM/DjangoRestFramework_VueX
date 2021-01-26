from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)
    image = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username