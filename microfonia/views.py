from django.shortcuts import render
from .models import Person
from .models import Episode


def videos(request):
    people = Person.objects.all()

    return render(request, 'videos.html', { 'people': people })

# def descricao(request):
#     my_person = Person.objects.first()

#     return render(request, 'descricao.html', { 'person': my_person })

def descricao(request):
	first_epi = Episode.objects.first()

	return render(request, 'descricao.html', { 'epi': first_epi })

