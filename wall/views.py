from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Wall
from django.contrib.auth.decorators import login_required
from .forms import Add_Wall_form
from .models import Wall

class ArtListView(ListView):
    template_name = 'wall/wall_listview.html'

    def get_queryset(self):
        return  Wall.objects.get_active_wall(

        )

@login_required(login_url='/login')
def add_wall(request):
    add_wall_form = Add_Wall_form(request.POST or None , request.FILES)
    if add_wall_form.is_valid():
        owner = add_wall_form.cleaned_data.get('owner')
        location = add_wall_form.cleaned_data.get('location')
        start_date = add_wall_form.cleaned_data.get('start_date')
        end_date = add_wall_form.cleaned_data.get('end_date')
        space_count = add_wall_form.cleaned_data.get('space_count')
        price = add_wall_form.cleaned_data.get('price')

        if not Wall.objects.filter(location=location).exists()  :
            Wall(owner=owner,location=location,start_date=start_date,end_date=end_date,space_count=space_count
                ,price=price,creator_id=request.user.id).save()

        redirect('/')

    context = {
         'add_wall_form':add_wall_form
    }
    return render(request,'wall/Wall_Form.html',context)