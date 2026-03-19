from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserUpdateForm

@login_required
def account(request):
     return render(request, 'accounts/account.html', {'user': request.user})