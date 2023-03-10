from django.contrib.auth import logout
from django.shortcuts import redirect

def kill_session(request):
    logout(request)

    return redirect('/')

def home(request): 
    return redirect('/accounts/login')