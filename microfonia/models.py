from django.db import models
from django.utils.feedgenerator import Rss201rev2Feed
from django.contrib.syndication.views import Feed
import datetime




class Serie(models.Model):
	name = models.CharField(max_length=50)
	img = models.CharField(max_length=200)
	abbrev = models.CharField(max_length=6)

	def __str__(self):
 		return self.name



class Episode(models.Model):
	name = models.CharField(max_length=20)
	season = models.CharField(max_length=2)
	serie = models.ForeignKey(Serie, on_delete = models.CASCADE)
	link_download = models.CharField(max_length=200)
	img = models.CharField(max_length=200)
	cast = models.TextField()
	sinopsis = models.TextField()
	date = models.DateField()
	url = models.URLField()
	number = models.IntegerField()

	def __str__(self):
 		return str(self.serie) + " - " + self.name


class iTunesPodcastsFeedGenerator(Rss201rev2Feed):
	def rss_attributes(self):
		return {u"version": self._version, u"xmlns:atom": u"http://www.w3.org/2005/Atom", u'xmlns:itunes': u'http://www.itunes.com/dtds/podcast-1.0.dtd'}

	def add_root_elements(self, handler):
		super(iTunesPodcastsFeedGenerator, self).add_root_elements(handler)
		handler.addQuickElement(u'itunes:subtitle', self.feed['subtitle'])
		handler.addQuickElement(u'itunes:author', self.feed['author_name'])
		handler.addQuickElement(u'itunes:summary', self.feed['description'])
		handler.addQuickElement(u'itunes:explicit', self.feed['iTunes_explicit'])
		handler.startElement(u"itunes:owner", {})
		handler.addQuickElement(u'itunes:name', self.feed['iTunes_name'])
		handler.addQuickElement(u'itunes:email', self.feed['iTunes_email'])
		handler.endElement(u"itunes:owner")
		handler.addQuickElement(u'itunes:image', self.feed['iTunes_image_url'])

	def add_item_elements(self,  handler, item):
		super(iTunesPodcastsFeedGenerator, self).add_item_elements(handler, item)
		handler.addQuickElement(u'iTunes:summary',item['summary'])
		handler.addQuickElement(u'iTunes:duration',item['duration'])
		handler.addQuickElement(u'iTunes:explicit',item['explicit'])

class iTunesPodcastPost():
	def __init__(self, podcast):
		self.id = podcast.id
		self.approval_date_time = podcast.approval_date_time
		self.title = podcast.title
		self.summary = podcast.description
		self.enclosure_url = insecure_url(podcast.podcast_file.url)
		self.enclosure_length = podcast.podcast_file.size
		self.enclosure_mime_type = u'audio/mpeg'
		self.duration = podcast.duration
		self.explicit = u'no'

	def __unicode__(self):
		return "Podcast: %s" % self.title
	@permalink
	def get_absolute_url(self):
		return ('podcast_view', [str(self.id)])

class iTunesPodcastsFeed(Feed):
	 """A feed of podcasts for iTunes and other compatible podcatchers."""
	title = "Microfonia Produções"
	link = "/latest/feed"
	author_name = 'David Barenco'
	description = "A Microfonia Produções é uma produtora de conteúdo independente que resgata um excelente porém esquecido meio de se contar histórias: os áudio-dramas."
	subtitle = "Áudio dramas e podcasts para você baixar e ouvir onde quiser"
	summary = "Acompanhe nossas histórias!"
	iTunes_name = u'Microfonia Produções'
	iTunes_email = u'microfoniaproducoes@gmail.com'
	iTunes_image_url = u''
	iTunes_explicit = u'no'
	feed_type = iTunesPodcastsFeedGenerator
	feed_copyright = "Copyright %s by the Microfonia Produções." % datetime.date.today().year

	def items(self):
		"""Returns a list of items to publish in this feed."""
		stop = datetime.datetime.now()
		start = stop - datetime.timedelta(hours=72)
		posts = Podcast.objects.filter(approval_date_time__range=(start,stop)).order_by('-approval_date_time','id')
		posts = [iTunesPodcastPost(item) for item in posts]
		return posts

	def feed_extra_kwargs(self, obj):
		extra = {}
		extra['iTunes_name'] = self.iTunes_name
		extra['iTunes_email'] = self.iTunes_email
		extra['iTunes_image_url'] = self.iTunes_image_url
		extra['iTunes_explicit'] = self.iTunes_explicit
		return extra
	
	def item_extra_kwargs(self, item):
		return {'summary':item.summary, 'duration':item.duration, 'explicit':item.explicit}
	
	def item_pubdate(self, item):
		return item.approval_date_time
	
	def item_enclosure_url(self, item):
		return item.enclosure_url
	
	def item_enclosure_length(self, item):
		return item.enclosure_length
	
	def item_enclosure_mime_type(self, item):
		return item.enclosure_mime_type
	
	def item_description(self, item):
		return item.summary
