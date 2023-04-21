from django.db import models

# Create your models here.


class Destinations(models.Model):
    name = models.CharField(max_length=15)
    desc = models.CharField(max_length=300)
    distance = models.IntegerField()
    time = models.CharField(max_length=20)


class Crew(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)


class Technology(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
