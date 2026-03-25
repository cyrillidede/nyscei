from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def account(request):
     return render(request, 'accounts/account.html', {'user': request.user})

from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or your account page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})