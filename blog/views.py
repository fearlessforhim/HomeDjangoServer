from django.shortcuts import render
from django.http import JsonResponse
from .models import BlogPost, AboutMePost


# Create your views here.

def index(request):
	return HttpResponse("hello, world")

def get_posts(request):
	all_posts = BlogPost.objects.filter(datePublished__isnull=False).order_by('-datePublished').values()
	post_list = list(all_posts)
	return JsonResponse(post_list, safe=False)

def get_post(request):
	print(request.GET)
	post = BlogPost.objects.filter(id=request.GET['id']).order_by('-datePublished').values()
	post_list = list(post)
	return JsonResponse(post_list[0], safe=False)

def get_about(request):
	all_posts = AboutMePost.objects.all().values()
	post_list = list(all_posts)
	return JsonResponse(post_list[0], safe=False)

def get_latest_posts(request):
	all_posts = BlogPost.objects.filter(datePublished__isnull=False).order_by('-datePublished').values()
	post_list = list(all_posts)[0:2]
	return JsonResponse(post_list, safe=False)
