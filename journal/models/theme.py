from django.db import models

class Theme(models.Model):
    image: models.CharField(max_length=300)
    pagelayout: models.CharField(max_length=100)
    creator: models.CharField(max_length=100)