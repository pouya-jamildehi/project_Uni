from django.shortcuts import render, redirect

from art_artist.models import Art


def mainpage(request):
    ax = Art.objects.get_art_id(3)
    context={
        'ax' : ax

    }
    return render(request, 'Mainpage.html', context)

def footer(request, *args, **kwargs):
    context = {


    }
    return render(request, 'shared/footer.html',context)

def hader(request, *args, **kwargs):
    context = {


    }
    return render(request, 'shared/header.html',context)