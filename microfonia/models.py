from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)

class Episode(models.Model):
	episode_number = models.IntegerField()
	episode_season = models.IntegerField()
	episode_name = models.CharField(max_length=50)
	episode_date = models.DateField()
	episode_sinopsis = models.TextField()
	episode_cast = models.TextField()
	episode_url = models.URLField()
