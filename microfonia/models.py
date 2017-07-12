from django.db import models




class Serie(models.Model):
	name = models.CharField(max_length=50)
	img = models.ImageField(upload_to='series/')
	abbrev = models.CharField(max_length=6)

	def __str__(self):
 		return self.name



class Episode(models.Model):
	name = models.CharField(max_length=20)
	season = models.CharField(max_length=2)
	serie = models.ForeignKey(Serie, on_delete = models.CASCADE)
	link_download = models.CharField(max_length=200)
	img = models.ImageField(upload_to='episodes/')
	cast = models.TextField()
	sinopsis = models.TextField()
	date = models.DateField()
	url = models.URLField()
	number = models.IntegerField()

	def __str__(self):
 		return str(self.serie) + " - " + self.name

		
	

