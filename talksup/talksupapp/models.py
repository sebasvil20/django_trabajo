from django.db import models

# Create your models here.
class Podcast(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    cover_pic_url = models.CharField(max_length=1000)
    total_episodes = models.IntegerField()
    release_date = models.DateField()