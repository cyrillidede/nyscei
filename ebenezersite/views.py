from django.http import HttpResponse
from django.shortcuts import render
from main.models import *
from django.contrib.auth.decorators import login_required


def about(request):
    return HttpResponse('love, vickie')

def homepage(request):
    return render(request, 'index.html')

def leadership(request):
    return render(request, 'leadership.html')

def leaderstable(request):
    leaders =Current_leader.objects.all()
    return render(request, 'leaderstable.html',{'leaders': leaders})

def login(request):
    return render(request, 'login.html')

def activities(request):
    return render(request, 'activities.html')

@login_required
def account(request):
    return render(request, 'account.html', {'user': request.user})
