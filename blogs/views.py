from django.shortcuts import render, redirect
from .models import Blog
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q


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

    return render(request, 'blogs/blogs_list.html', {'blog_details': blogs, 'query': query, 'field': field})


@login_required(login_url="/accounts/login/")  # Redirect if user not logged-in
def blog_create(request):
    if request.method == 'POST':
        # request.files as .POST does not include attached files data! :(
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            # Save blog to the database
            blog_instance = form.save(commit=False)
            blog_instance.author = request.user
            blog_instance.save()
            return redirect('blogs:blogs_list')
    else:
        form = forms.CreateBlog()
    return render(request, 'blogs/blog_create.html', {'form_UI': form})



def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})

