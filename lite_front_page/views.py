from django.shortcuts import render, get_object_or_404
from lite_front_page.models import BlogPost

# Create your views here.

def blog_detail(request, id=None):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog_detail.html', {'post': post})

def blog_index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_index.html', {'posts': posts})