from django.shortcuts import render, redirect
from .forms import RegistrationForm


# Create your views here.


# register page


def register(response):
    if response.method == 'POST':

        form = RegistrationForm(response.POST)

        if form.is_valid():

            form.save()
        
        return redirect('/')
        
    else:

        form = RegistrationForm()

    return render(response, 'register.html', {'form': form})
