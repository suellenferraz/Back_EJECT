from django.shortcuts import render

from blog_post.models import Blog

# Create your views here.
def blog_post(request):
    blog = Blog.objects.all() 
    print (blog)
    context = {
        'blog':blog
    }

    return render(request, 'blog_post.html', context)