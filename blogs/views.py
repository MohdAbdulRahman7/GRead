from django.shortcuts import render

from blogs.models import Blog

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

