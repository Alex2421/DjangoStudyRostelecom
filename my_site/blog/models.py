from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  #модуль связанный с аутентификацией класса User
from django.urls import reverse
from django.core.validators import MinLengthValidator
from django.db.models import ImageField
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe

validate_phone = RegexValidator('\+7\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}',
                                      message='Номер телефона указан некорректно')

from users.models import Profile
owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)


#счетчик уникальных просмотров
class ViewCount(models.Model):
    """
    Модель просмотров для статей
    """
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='views')
    ip_address = models.GenericIPAddressField(verbose_name='IP адрес')
    view_data = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')

    class Meta:
        ordering = ('-view_data',)
        indexes = [models.Index(fields=['-view_data'])]
        # verbose_name = 'Просмотр'
        # verbose_name_plural = 'Просмотры'

    def __str__(self):
        return self.post.title


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     imagepost = models.ImageField(default='defaultpost.jpg', upload_to='post_pics')
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('post-detail', kwargs={'pk': self.pk})

#add images
# class Image(models.Model):
#     title = models.CharField(max_length= 255, blank=False, null=False)
#     image = models.ImageField(upload_to='images/', null=True, max_length=255)

    # def __repr__(self):
    #     return 'Image(%s, %s)' % (self.title, self.image)

    # def __str__ (self):
    #     return self.title



class Post(models.Model):
    objects = None
    categories = (('O', 'Operator'),
                  ('S', 'Science'),
                  ('I', 'Internet'),
                  ('OS', 'Operation System'))
    #поля
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор')
    title = models.CharField('Название', max_length=100, default='', validators=[MinLengthValidator(10)], null=False)
    anouncement = models.TextField('Аннотация', max_length=500, default='', validators=[MinLengthValidator(10)], null=False)
    content = models.TextField('Статья', max_length=100000, default='', validators=[MinLengthValidator(10)], null=False)
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    category = models.CharField(max_length=50, choices=categories)
#    imagepost = models.ImageField(default='defaultpost.jpg', upload_to='post_pics')


    def get_absolute_url(self):
     return f'/post/{self.id}'

    def __str__(self):
        return self.title

    def get_views(self):
        return self.views.count()

# изображения
    def image_tag(self):
        image = Image.objects.filter(post=self)
        print('!!!!', image)
        if image:
                return mark_safe(f'<img src="{image[0].image.url}" height="50px" width="auto" />')
        else:
                return '(no image)'


    class Meta:
        ordering = ['title', 'date_posted']
        verbose_name= 'Новость'
        verbose_name_plural= 'Новости'



class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='post_images/',null=True,blank=True) #лучше добавить поле default !!!

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image is not None:
            return mark_safe(f'<img src="{self.image.url}" height="50px" width="auto" />')
        else:
            return '(no image)'







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

#     class Meta:
#         ordering = ('created',)
#
#     def __str__(self):
#         return 'Comment by {} on {}'.format(self.name, self.post)
#
#
# class Resume:
#     pass


#
# #like
# class Favorite_Taste(models.Model):
#     user_id_favorite = models.ForeignKey(User, on_delete=models.CASCADE, default='')
#     post_id_favorite = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
#     favorite_choices = models.BooleanField()
#
#     class Meta:
#         unique_together = ('user_id_favorite', 'post_id_favorite')
