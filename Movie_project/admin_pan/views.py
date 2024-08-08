
from django.shortcuts import render
from .models import News_post

def home(request):
	films = News_post.objects.all()
	return render(request, 'admin_pan/news.html' , {'films': films})