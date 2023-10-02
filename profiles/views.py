from django.shortcuts import render


def profile(request):
    """ Show Users profile """
    context = {

    }
    return render(request, 'profiles/profile.html', context)
