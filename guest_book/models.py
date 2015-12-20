from django.db import models


class Entry(models.Model):
    username = models.CharField(max_length=50)
    text = models.CharField(max_length=10000)
    email = models.CharField(max_length=300)
    homepage = models.CharField(max_length=100)
