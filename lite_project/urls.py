"""
URL configuration for lite_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django_distill import distill_path

from lite_front_page.models import BlogPost
from lite_front_page.views import blog_index, blog_detail

def get_blog_posts():
    for post in BlogPost.objects.all():
        yield {'id': post.id}

urlpatterns = [
    distill_path('post/<int:id>/', blog_detail, name='blog_detail', distill_func=get_blog_posts),
    distill_path('post/', blog_index, name='blog_index'),
]