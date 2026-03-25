from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def account(request):
     return render(request, 'accounts/account.html', {'user': request.user})


from django.contrib.auth.models import User
from .models import Profile
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the user first
            user = form.save()

            # Create the profile linked to this user
            Profile.objects.create(
                user=user,
                # Example: pull extra fields from the form if included
                bio=form.cleaned_data.get('bio', ''),
                phone=form.cleaned_data.get('phone', ''),
                # add other profile fields here
            )

            return redirect('login')  # or wherever you want to redirect
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})