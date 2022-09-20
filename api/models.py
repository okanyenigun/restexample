from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=250)
    duration = models.IntegerField()
    release_date = models.DateField()
    rating = models.IntegerField()
    
    def __str__(self):
        return self.title
