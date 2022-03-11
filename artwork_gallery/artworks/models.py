from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.fields.CharField(max_length=100)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.fields.CharField(max_length=255)
    birthday = models.fields.CharField(max_length=20, null=True, blank=True)
    deathday = models.fields.CharField(max_length=20, null=True, blank=True)
    image = models.fields.TextField(null=True, blank=True)

    def __str__(self):
        return self.name