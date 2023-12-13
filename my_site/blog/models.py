from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  #модуль связанный с аутентификацией класса User
from django.urls import reverse
from django.db.models import Count



class Post(models.Model):
    categories = (('O', 'Operator'),
                  ('S', 'Science'),
                  ('I', 'Internet'),
                  ('OS', 'Operation System'))
    #поля
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Название')
    anounc = models.TextField('Аннотация', null=True, max_length=250)
    content = models.TextField('Статья')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    category = models.CharField(max_length=50, choices=categories)








  # anouncement = models.TextField ('Аннотация', max_length=250)
  # author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')


    # text = models.TextField('Текст новости')
    #category = models.CharField(choices=categories, max_length=20, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


