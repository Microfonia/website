from django.shortcuts import render
from django.http import HttpResponse
from .models import Episode, Serie



def videos(request, seriename=None):
	all_episodes = Episode.objects.all()
	all_series = Serie.objects.all()
	for series in all_series:
		series.episodes = Episode.objects.filter(serie__name=series.name)
	context = {
		'all_episodes': all_episodes,
		'all_series': all_series,
	}
	return render(request, 'videos.html', context)


def descricao(request):
	first_epi = Episode.objects.first()

	return render(request, 'descricao.html', { 'epi': first_epi })

def aboutus(request):
	return render(request, 'aboutus.html')

def contact(request):
	return render(request, 'contact.html')
