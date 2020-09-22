from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getPosts', views.get_posts, name='getPosts'),
    path('getLatestPosts', views.get_latest_posts, name='getLatestPosts'),
    path('getPost', views.get_post, name='getPost'),
    path('getAbout', views.get_about, name='getAbout'),
]
