from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Login, Records

def login_page(request):
    return render(request, 'main/login.html', locals())

@csrf_protect
def is_logged(request):
    if request.POST:
        try:
            Login.objects.get(passwd=request.POST.get('passwd'))
            try:
                Records.objects.get(name_team=request.POST.get('name_team'))
            except:
                new_team = Records(name_team=request.POST.get('name_team'))
                new_team.save()
            return render(request, 'main/index.html', locals())
        except:
            return redirect('/')