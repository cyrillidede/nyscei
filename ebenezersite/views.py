from django.http import HttpResponse
from django.shortcuts import render, redirect 
from main.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm

def about(request):
    return HttpResponse('love, vickie')

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
    return render(request, 'account.html', {'user': request.user})





def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in automatically
            return redirect("home") # Redirect to your dashboard or home
    else:
        form = SignUpForm()
    
    return render(request, "signup.html", {"form": form})

