from django.shortcuts import render


def user_profile(request):

    context = {


    }
    return render(request,'user_profile/user_profile.html',context)