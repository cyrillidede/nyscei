from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    service_no = forms.CharField(max_length=50)
    course = forms.CharField(max_length=100)
    year_of_discharge = forms.CharField(max_length=50)
    employment_status = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2',
            'phone', 'service_no', 'course', 'year_of_discharge', 'employment_status'
        )

    def save(self, commit=True):   # <-- Step 2 goes here
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                phone=self.cleaned_data['phone'],
                service_no=self.cleaned_data['service_no'],
                course=self.cleaned_data['course'],
                year_of_discharge=self.cleaned_data['year_of_discharge'],
                employment_status=self.cleaned_data['employment_status']
            )
        return user