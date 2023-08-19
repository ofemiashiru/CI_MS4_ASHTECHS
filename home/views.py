from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    """ view returns the index (home) page"""
    return render(request, 'home/index.html')
