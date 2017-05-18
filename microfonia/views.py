from django.shortcuts import render


def index(request):
    return render(request, 'barty/index.html')

def url_david(request):
	return render(request, 'david/index.html')

def bortolotti(request):
	return render(request, 'bortolotti/index.html')

