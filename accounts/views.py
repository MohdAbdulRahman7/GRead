from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, get_user


def login_view(request):
    # GET request if user hits login.html
    # POST request if user submits the login form
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Login User
            user = form.get_user()
            login(request, user)
            if not request.session.get('cookie_consent_given'):
                request.session['cookie_consent_needed'] = True  # Set session variable
            # Check if cookie consent is given
            cookie_consent = request.COOKIES.get(f'cookie_consent_{user.id}', None)
            if cookie_consent == 'accepted':
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    # Redirect to blogs list or desired page
                    return redirect('blogs:blogs_list')
            else:
                # Set session variable to show cookie consent banner
                request.session['cookie_consent_needed'] = True
                return redirect('home')  # Redirect to homepage or another page where banner is displayed
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blogs:blogs_list')