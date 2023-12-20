from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import signupForm

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    
    else:
        form = signupForm()
    
    return render(request, 'core/signup.html', {'form': form})
