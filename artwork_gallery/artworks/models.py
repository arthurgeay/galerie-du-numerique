from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.fields.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.fields.CharField(max_length=255, unique=True)
    birthday = models.fields.CharField(max_length=20, null=True, blank=True)
    deathday = models.fields.CharField(max_length=20, null=True, blank=True)
    image = models.fields.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Artwork(models.Model):
    title = models.fields.CharField(max_length=255, unique=True)
    description = models.fields.TextField(null=True, blank=True)
    image = models.fields.TextField(null=True, blank=True)
    released_at = models.fields.CharField(max_length=4, null=True, blank=True)
    width = models.fields.CharField(max_length=10, null=True, blank=True)
    height = models.fields.CharField(max_length=10, null=True, blank=True)
    location = models.fields.CharField(max_length=255, null=True, blank=True)
    artist = models.ForeignKey(Artist, null=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    votes = models.ManyToManyField(User)

    class Meta:
        permissions = (("can_vote", "Can vote for an artwork"),)

    def __str__(self):
        return self.title
