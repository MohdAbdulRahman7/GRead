from django.http import HttpResponse
from django.shortcuts import render  # this is used to render templates when view function is invoked
from datetime import datetime, timedelta
from django.contrib.auth import get_user


def about(request):
    user = get_user(request)
    cookie_consent = request.COOKIES.get(f'cookie_consent_{user.id}')

    if user.is_authenticated and cookie_consent == 'accepted':
        user_id = user.id
        visits_cookie_name = f'visits_{user_id}'
        visits = int(request.COOKIES.get(visits_cookie_name, '0'))
        context = {'visits': visits}
    else:
        context = {'visits': None}

    return render(request, 'about.html', context)