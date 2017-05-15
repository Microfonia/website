from django.shortcuts import render


def index(request):
    return render(request, 'barty/index.html')

def bortolotti(request):
	return render(request, 'bortolotti/index.html')