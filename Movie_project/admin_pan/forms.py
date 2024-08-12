from .models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, URLInput

class News_postForm(ModelForm):
	class Meta:
		model = News_post
		fields = ['title', 'short_description', 'text', 'pub_date', 'image_url', 'video_url']
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
			'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
			'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв'}),
			'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
			'image_url': URLInput(attrs={'class': 'form-control', 'placeholder': 'URL изображения'}),
			'video_url': URLInput(attrs={'class': 'form-control', 'placeholder': 'URL видео'}),
		}
