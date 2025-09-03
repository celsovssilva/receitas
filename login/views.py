from django.shortcuts import render
from login.forms import UserRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import login


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
          user= form.save()
          login(request, user)
          return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})