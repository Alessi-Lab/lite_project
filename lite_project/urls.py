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
from lite_front_page.views import blog_index, blog_detail, home_index, forms_index, contact_index


def get_blog_posts():
    for post in BlogPost.objects.all():
        yield {'id': post.id}

urlpatterns = [
    distill_path('', home_index, name='home_index'),
    distill_path('forms/', forms_index, name='forms_index'),
    distill_path('contact/', contact_index, name='contact_index'),
    distill_path('posts/', blog_index, name='blog_index'),
    distill_path('posts/<int:id>/', blog_detail, name='blog_detail', distill_func=get_blog_posts),
]