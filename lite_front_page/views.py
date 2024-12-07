from django.shortcuts import render, get_object_or_404
from lite_front_page.models import BlogPost

# Create your views here.
def home_index(request):
    return render(request, 'home_index.html')

def forms_index(request):
    return render(request, 'forms_index.html')

def contact_index(request):
    return render(request, 'contact_index.html')

def blog_detail(request, id=None):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog_detail.html', {'post': post})

def blog_index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_index.html', {'posts': posts})