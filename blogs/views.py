from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q
from django.contrib import messages
from .forms import CreateBlog


# def blogs_list(request):
#     blogs = Blog.objects.all().order_by('pub_date')
#     return render(request, 'blogs/blogs_list.html', {'blog_details': blogs})

def blogs_list(request):
    query = request.GET.get("q", "")
    field = request.GET.get("field", "")

    if query and field:
        if field == "title":
            blogs = Blog.objects.filter(Q(title__icontains=query)).order_by('pub_date')
        elif field == "body":
            blogs = Blog.objects.filter(Q(body__icontains=query)).order_by('pub_date')
        elif field == "author":
            blogs = Blog.objects.filter(Q(author__username__icontains=query)).order_by('pub_date')
        else:  # No filter case or empty string case
            blogs = Blog.objects.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(author__username__icontains=query)
            ).order_by('pub_date')
    else:
        blogs = Blog.objects.all().order_by('pub_date')

    # Annotate each blog with the count of likes
    blogs = blogs.annotate(likes_count=Count('likes'))

    return render(request, 'blogs/blogs_list.html', {'blog_details': blogs, 'query': query, 'field': field})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # Retrieve the current list of recently viewed slugs from the session
    recently_viewed = request.session.get('recently_viewed', [])

    # If the slug is already in the list, remove it
    if slug in recently_viewed:
        recently_viewed.remove(slug)

    # Insert the current blog's slug at the beginning of the list
    recently_viewed.insert(0, slug)

    # Ensure the list does not exceed 5 items
    if len(recently_viewed) > 5:
        recently_viewed.pop()

    # Update the session with the modified list
    request.session['recently_viewed'] = recently_viewed

    return render(request, 'blogs/blog_detail.html', {'blog': blog})


@login_required(login_url="/accounts/login/")  # Redirect if user not logged-in
def blog_create(request):
    draft_key = 'blog_draft'
    if request.method == 'POST':
        form = CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            if 'publish' in request.POST:
                # Save the blog to the database
                blog = form.save(commit=False)
                blog.author = request.user  # Set the author to the currently logged-in user
                blog.status = 'published'
                blog.save()
                # Clear the draft from session
                if draft_key in request.session:
                    del request.session[draft_key]
                return redirect('blogs:blogs_list')
            elif 'save_draft' in request.POST:
                # Save the draft in session
                draft_data = {
                    'title': form.cleaned_data['title'],
                    'body': form.cleaned_data['body'],
                }
                # Handle the thumbnail field correctly
                thumbnail = form.cleaned_data['thumbnail']
                if thumbnail:
                    if hasattr(thumbnail, 'name'):
                        draft_data['thumbnail'] = thumbnail.name
                    else:
                        draft_data['thumbnail'] = thumbnail
                else:
                    draft_data['thumbnail'] = None

                request.session[draft_key] = draft_data
                return redirect('blogs:drafts_list')
    else:
        form = CreateBlog()
    return render(request, 'blogs/blog_create.html', {'form': form})


@login_required(login_url="/accounts/login/")  # Redirect to login page if not logged in
def recently_viewed_blogs(request):
    recently_viewed = request.session.get('recently_viewed', [])
    valid_blogs = []
    valid_slugs = []

    for slug in recently_viewed:
        try:
            blog = Blog.objects.get(slug=slug)
            valid_blogs.append(blog)
            valid_slugs.append(slug)
        except Blog.DoesNotExist:
            continue

    # Update session with only valid slugs
    request.session['recently_viewed'] = valid_slugs

    return render(request, 'blogs/recently_viewed.html', {'blogs': valid_blogs})


@login_required(login_url="/accounts/login/")  # Redirect if user not logged-in
def drafts_list(request):
    session_draft = request.session.get('blog_draft', None)
    # user_drafts = Blog.objects.filter(author=request.user, status='draft')

    return render(request, 'blogs/drafts_list.html', {
        'session_draft': session_draft,
        # 'user_drafts': user_drafts,
    })


@login_required(login_url="/accounts/login/")  # Redirect if user not logged-in
def load_draft(request):
    draft_data = request.session.get('blog_draft')

    if draft_data:
        form = CreateBlog(initial={
            'title': draft_data.get('title'),
            'body': draft_data.get('body'),
            'thumbnail': draft_data.get('thumbnail'),
        })
        return render(request, 'blogs/blog_create.html', {'form': form})
    else:
        return redirect('blogs:drafts_list')

