from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Art
from .forms import ArtForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

from PIL import Image

class ArtListView(ListView):
    template_name = 'art_artist/Art_Listview.html'

    def get_queryset(self):
        return Art.objects.get_active_art()
@login_required(login_url='/login')
def add_art(request):
    add_art_form = ArtForm(request.POST or None , request.FILES)
    if add_art_form.is_valid():
        title = add_art_form.cleaned_data.get("title")
        paintistname = add_art_form.cleaned_data.get("paintistname")
        subject = add_art_form.cleaned_data.get("subject")
        about = add_art_form.cleaned_data.get("about")
        date = add_art_form.cleaned_data.get("date")
        material = add_art_form.cleaned_data.get("material")

        if  Art.objects.filter(title=title).exists():
            if not Art.objects.filter(paintistname=paintistname).exists():
                Art(title=title,date=date,paintistname=paintistname,subject=subject,about=about,
                           material=material,image=request.FILES['image'],creator_id=request.user.id).save()
            else:
                raise Http404
        else:
            Art(title=title, date=date, paintistname=paintistname, subject=subject, about=about,
                material=material, image=request.FILES['image'], creator_id=request.user.id).save()

        redirect('/add-art')

    context = {
        'add_art_form' :  add_art_form
    }
    return render(request,'art_artist/Art_Form.html',context)
