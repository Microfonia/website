from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Episode, Serie
from .forms import ContactForm




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
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name','')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
                })
            content = template.render(context)
            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
                )
            email.send()
            return redirect('contact')
    return render(request, 'contact.html', {'form': form_class,})


