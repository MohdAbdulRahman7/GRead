from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import JsonResponse
from accounts.models import Member
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User



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
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Skip Member check for superuser
            if user.is_superuser:
                if not request.session.get('cookie_consent_given'):
                    request.session['cookie_consent_needed'] = True  # Set session variable
                return redirect('admin:index')

            # Ensure the user has a Member instance
            if not hasattr(user, 'member'):
                Member.objects.create(user=user)

            if not request.session.get('cookie_consent_given'):
                request.session['cookie_consent_needed'] = True  # Set session variable

            cookie_consent = request.COOKIES.get(f'cookie_consent_{user.id}', None)
            if cookie_consent == 'accepted':
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('home')
            else:
                request.session['cookie_consent_needed'] = True
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blogs:blogs_list')


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
