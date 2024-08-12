from django.shortcuts import render, redirect
from .models import News_post
from . forms import News_postForm

def home(request):
	films = News_post.objects.all()
	return render(request, 'admin_pan/news.html' , {'films': films})


def create_film(request):
	if request.method == 'POST':
		form = News_postForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('films')
		else:
			print(form.errors)  # Это поможет увидеть ошибки валидации в консоли
	else:
		form = News_postForm()
	return render(request, 'admin_pan/add_film.html', {'form': form})
