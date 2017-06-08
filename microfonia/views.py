from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Episode, Serie


def videos(request):
	all_episodes = Episode.objects.all()
	all_series = Serie.objects.all()
	template = loader.get_template('videos.html')
	context = {
		'all_episodes': all_episodes,
		'all_series': all_series,
	}
	return HttpResponse(template.render(context,request))
	#return render(request, 'videos.html')

def descricao(request):
	return render(request, 'descricao.html')

def episodio(request, episode_id):
	return HttpResponse("<h1>Esse é o: " + episode_id + "</h1>")
