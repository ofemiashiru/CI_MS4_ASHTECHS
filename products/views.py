from django.shortcuts import render, HttpResponse


# Create your views here.
def see_products(request):
    return HttpResponse('Hello')