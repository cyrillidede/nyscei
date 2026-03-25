from django.http import HttpResponse
from django.shortcuts import render, redirect 
from main.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegistrationForm, ProfileForm



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
    
def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            login(request, user)
            return redirect('account_page')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})

