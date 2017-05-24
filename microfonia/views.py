from django.shortcuts import render


def index(request):
    return render(request, 'barty/index.html')

def videos(request):
	return render(request, 'david/index.html')

def descricao(request):
	return render(request, 'bortolotti/index.html')

