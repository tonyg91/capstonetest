from django.db import models

class Supply(models.Model):
    brand: models.CharField(max_length=100)
    type: models.CharField(max_length=100)
    ink: models.CharField(max_length=100)