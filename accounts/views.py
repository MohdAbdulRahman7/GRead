from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib import messages

def home_page(request):
    return HttpResponse("This is the home page")


def login_view(request):
    # GET request if user hits login.html
    # POST request if user submits the login form
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Login User
            user = form.get_user()
            # messages.success(request, "You are now logged in.")
            login(request, user)
            return redirect('accounts:home')  # Redirect to homepage or another page where banner is displayed
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

