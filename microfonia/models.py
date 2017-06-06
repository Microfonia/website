from django.db import models

#class Episode(object):
#	def __init__(self, arg):
#		super(Episode, self).__init__()
#		self.arg = arg

class Serie(models.Model):
	name = models.CharField(max_length=50)
	img = models.CharField(max_length=200)

	def __str__(self):
 		return self.name



class Episode(models.Model):
	episode = models.CharField(max_length=20)
	season = models.CharField(max_length=2)
	serie = models.ForeignKey(Serie, on_delete = models.CASCADE)
	download = models.CharField(max_length=200)
	img = models.CharField(max_length=200)
	

	def __str__(self):
 		return str(self.serie) + " - " + self.episode
