from django.db import models

class News_post(models.Model):
	title = models.CharField('Названия фильма', max_length=50)
	short_description = models.CharField('Описание фильма', max_length=250)
	text = models.TextField('Отзыв')
	pub_date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Фильм'
		verbose_name_plural = 'Фильмы'