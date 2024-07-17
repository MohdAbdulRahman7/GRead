from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        # request.POST here is the data flowing from UI to this function
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_name = form.save()  # Save the form data to the database
            # Log User In
            login(request, user_name)
            # Cookie CONSENT
            request.session['cookie_consent_needed'] = True  # Set session variable
            messages.info(request, "Welcome! Please review and accept our cookie policy.")

            return redirect('blogs:blogs_list')  # appname: named url value
    else:  # Get Method Called
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


