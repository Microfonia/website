from django.shortcuts import render



def videos(request):
	return render(request, 'videos.html')

def descricao(request):
	return render(request, 'descricao.html')

