from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    categories = (('O', 'Operator'),
                  ('S', 'Science'),
                  ('I', 'Internet'),
                  ('OS', 'Operation System'))
    title = models.CharField(max_length=200, verbose_name='Название')
    content = models.TextField('Статья')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


