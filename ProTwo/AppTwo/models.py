from django.db import models

# Create your models here.
class User (models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    Email = models.CharField(max_length=264)

    def __str__(self):
        return self.last_name
