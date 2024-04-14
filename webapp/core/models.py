# Create your models here.

from django.db import models


class Sample(models.Model):
    attachment = models.FileField()