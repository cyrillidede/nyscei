from django.http import HttpResponse
from django.shortcuts import render, redirect 
from main.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login




def about(request):
    return HttpResponse('nyscei')

def homepage(request):
    return render(request, 'index.html')

def leadership(request):
    return render(request, 'leadership.html')

def leaderstable(request):
    leaders =Current_leader.objects.all()
    return render(request, 'leaderstable.html',{'leaders': leaders})

def login_view(request):
    return render(request, 'login.html')

def activities(request):
    return render(request, 'activities.html')

@login_required
def account(request):
    
    profile = request.user.profile
    return render(request, 'account.html', {'profile': profile})
    

