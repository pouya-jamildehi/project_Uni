from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model,authenticate,logout


@login_required(login_url='/login')
def user_profile(request):#,args,**kwargs):
    #selected_id = kwargs['Id']
    user = get_user_model().objects.filter(id=request.user.id)

    # print(user)

    context = {
        #'selected_id': selected_id,
        'user': user
    }
#    return render(request, 'reservation/user_page.html', context)


    return render(request,'user_profile/user_profile.html',context)