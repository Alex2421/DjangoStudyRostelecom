from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  #модуль связанный с аутентификацией класса User
from django.urls import reverse
from django.db.models import Count

#возврат на главную
class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Post(models.Model):
    categories = (('O', 'Operator'),
                  ('S', 'Science'),
                  ('I', 'Internet'),
                  ('OS', 'Operation System'))
    #поля
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Название')
    anouncement = models.TextField('Аннотация', null=True, max_length=1000)
    content = models.TextField('Статья')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    category = models.CharField(max_length=50, choices=categories)

  #   def __str__(self):
  #      return f'{self.title} от: {str(self.date)[:16]}'

    def get_absolute_url(self):
     return f'/post/{self.id}'

    def __str__(self):
        return self.title

   # def get_absolute_url(self):
   #     return reverse('post-detail', kwargs={'pk': self.pk})


class Meta:
    ordering = ['title', 'date', 'author' ]
    verbose_name= 'Новость'
    verbose_name_plural= 'Новости'


#class Comment(models.Model):
#    post = models.ForeignKey(Post,
#                             on_delete=models.CASCADE,
#                             related_name='comments')
#    name = models.CharField(max_length=80)
#    email = models.EmailField()
#   body = models.TextField()
#   created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)
#    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)