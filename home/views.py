from django.shortcuts import render


def index(request):
    """ view returns the index (home) page"""
    return render(request, 'home/index.html')
