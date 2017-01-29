from django.db import models

# Create your models here.
class GeoPoint(models.Model):
    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    latitude = models.DecimalField(max_digits=7, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    author = models.CharField(max_length=200)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)


class Comment(models.Model):
    geopoint = models.ForeignKey(GeoPoint, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)
    timestamp = models.DateTimeField()
    author = models.CharField(max_length=200)