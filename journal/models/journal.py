from django.db import models

class Journals(models.Model):
    brand = models.CharField(max_length=100)
    paperweight = models.CharField(max_length=100)
    sizes = models.CharField(max_length=100)
    pages = models.IntegerField(default=3)