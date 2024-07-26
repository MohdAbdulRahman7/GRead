from django.http import HttpResponse
from django.shortcuts import render  # this is used to render templates when view function is invoked
from datetime import datetime, timedelta
from django.contrib.auth import get_user


def homepage(request):
    user = get_user(request)
    cookie_consent = request.COOKIES.get(f'cookie_consent_{user.id}')

    # Fetch the first 7 members
    members = Member.objects.all()[:7]
    # Predefined tags -- for decoration (NO USE)
    tags = ["Storytelling", "Business", "Creative", "Design", "Modeling", "Fashion", "Acting", "Influencer",
            "Education"]

    # Assign a random tag to each member
    member_tags = []
    for member in members:
        random_tag = random.choice(tags)
        member_tags.append({'member': member, 'tag': random_tag})

    # Initial context
    context = {
        'user': request.user,
        'cookie_exists': False,
        'latest_blogs': [],
        'most_liked_blogs': [],
        'events_titles': [],
        'member_tags': member_tags,
    }

    if user.is_authenticated and cookie_consent == 'accepted':
        user_id = user.id
        visits_cookie_name = f'visits_{user_id}'
        last_visit_cookie_name = f'last_visit_{user_id}'
        cookie_exists = f'cookie_consent_{user.id}' in request.COOKIES
        context['cookie_exists'] = cookie_exists

        visits = int(request.COOKIES.get(visits_cookie_name, '0'))
        last_visit = request.COOKIES.get(last_visit_cookie_name, None)

        try:
            if last_visit:
                last_visit_time = datetime.strptime(last_visit, "%Y-%m-%d %H:%M:%S")
                if (datetime.now() - last_visit_time) > timedelta(seconds=30):
                    visits += 1
                    context['visits'] = visits
                    response = render(request, 'homepage.html', context)
                    response.set_cookie(visits_cookie_name, visits)
                    response.set_cookie(last_visit_cookie_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    return response
            else:
                context['visits'] = visits + 1
                response = render(request, 'homepage.html', context)
                response.set_cookie(last_visit_cookie_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                response.set_cookie(visits_cookie_name, visits + 1)
                return response
        except ValueError:
            context['visits'] = 1
            response = render(request, 'homepage.html', context)
            response.set_cookie(last_visit_cookie_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            response.set_cookie(visits_cookie_name, 1)
            return response

    # Fetch the latest 2 blogs
    context['latest_blogs'] = Blog.objects.filter(status='published').order_by('-pub_date')[:2]

    # Fetch the top 3 most liked blogs
    context['most_liked_blogs'] = Blog.objects.filter(status='published').annotate(like_count=Count('likes')).order_by(
        '-like_count')[:3]

    # Fetch the 4 most recent upcoming events
    context['recent_events'] = Event.objects.filter(datetime__gt=timezone.now()).order_by('datetime')[:4]

    # Render the response with context if no cookies are set
    response = render(request, 'homepage.html', context)
    return response


def about(request):
    return render(request, 'about.html')


