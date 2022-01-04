from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import get_user_model,authenticate,logout
from art_artist.models import Art
from wall.models import Wall
from .models import Reserv
from .forms import ArticleForm
import qrcode
#class base view
# class ReservListview(ListView):
#     template_name = 'reservation/reservation_list.html'
#
#     def get_queryset(self):
#         return Reserv.objects.get_active_reserv()

def reservation_detail(request,*args,**kwargs):

    reservation = Reserv.objects.get_reserv_id(1)
    if reservation is None :
        raise Http404('محصول مورد نظر یاقت نشد')
    wall = Art.objects.get_queryset().filter(reserv__art__reserv__id=2).distinct()
    context = {
        'reservation': reservation,
        'wall': wall,
    }
    return render(request,'reservation/reservation_pic.html',context)

def user_page(request,*args,**kwargs):
    selected_id = kwargs['Id']
    user = get_user_model().objects.filter(id=selected_id)

    #print(user)

    context={
        'selected_id' : selected_id,
        'user' : user
    }
    return render(request,'reservation/user_page.html',context)
@login_required(login_url='/login')
def add_reserv(request):
    add_reserv_form = ArticleForm(request.POST or None, request.FILES)
    if add_reserv_form.is_valid():
        if not Reserv.objects.filter(wall=add_reserv_form.data.get('wall')):
            add_reserv_form.save()
            #reserv = Reserv.objects.get(creator_id=0).update(creator_id=request.user.id)
            Reserv.objects.filter(creator_id=0).update(creator_id=request.user.id)
            return redirect('/get-qrcode')
        else:

            raise Http404('دیوار اشغال است')
    context={
        'add_reserv_form':add_reserv_form
    }

    return render(request,'reservation/add-reserv.html',context)

def get_qrcode(request,*args,**kwargs):
    text = "https://quera.ir"
    qr = qrcode.make(text)
    qr.save("my_qrcode.png")

    context={

    }
    return render(request,'reservation/ger_qrcode.html',context)