from django.db import models
    class MyWatchList(models.Model):
        watched = models.BooleanField(max_length=50)
        title = models.TextField(max_length=50)
        rating = models.FloatField()
        release_date = models.DateField()
        review = models.TextField()
# Create your models here.
