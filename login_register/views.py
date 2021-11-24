from django.shortcuts import render,redirect
from .forms import Login_User_Form,Register_User_Form
from django.contrib.auth import login,get_user_model,authenticate,logout
from django.contrib.auth.models import User


def login_user_page(request):

    # if request.user.is_authenticated():
    #     return redirect('/')

    login_user_form = Login_User_Form(request.POST or None)

    if login_user_form.is_valid():
        username = login_user_form.cleaned_data.get('username')
        password = login_user_form.cleaned_data.get('password')
        user  = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            redirect('/')
        else:
             login_user_form.add_error('username', 'کاربری با مشخصات وارد شده یافت نشد')
    context={
        'login_form':login_user_form
    }
    return render(request, 'login_page.html', context)



def register_user_page(request):

    # if request.user.is_authenticated():
    #     return redirect('/')

    register_form = Register_User_Form(request.POST or None)

    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(username=username,email=email,password=password)
        redirect('login/')

    context ={
        'register_form':register_form
    }
    return render(request, 'register_page.html', context)