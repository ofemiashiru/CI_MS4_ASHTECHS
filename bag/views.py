from django.shortcuts import render


# Create your views here.
def see_shopping_bag(request):
    """ view returns the shopping bag page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    pass
