from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=25)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)