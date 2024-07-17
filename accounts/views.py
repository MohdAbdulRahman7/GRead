from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


def home_page(request):
    return HttpResponse("This is the home page")


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


def reset_view(request):
    return redirect('blogs:')


def clear_cookie_consent_session(request):
    if request.method == 'POST':
        if 'cookie_consent_needed' in request.session:
            del request.session['cookie_consent_needed']
            return JsonResponse({'message': 'Session variable cleared successfully'})
        else:
            return JsonResponse({'message': 'Session variable not found'}, status=404)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)
