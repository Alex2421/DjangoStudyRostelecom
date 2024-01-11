from django.contrib import admin
from .models import Post
from .models import ViewCount
from django.db.models.functions import Length

#new image
# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ['title','article','image_tag']



#счетчик уникальных просмотров
@admin.register(ViewCount)
class ViewCountAdmin(admin.ModelAdmin):
      list_display = ['post','ip_address','view_data']






# class PostFilter(admin.SimpleListFilter):
#     title = 'По длине новости'
#     parameter_name = 'text'
#
#     def lookups(self, request, model_admin):
#         return [('S',("Короткие, <100 зн.")),
#                 ('M',("Средние, 100-500 зн.")),
#                 ('L',("Длинные, >500 зн.")),]
#
#     def queryset(self, request, queryset):
#         if self.value() == 'S':
#             return queryset.annotate(text_len=Length('text')).filter(text_len__lt=100)
#         elif self.value() == 'M':
#             return queryset.annotate(text_len=Length('text')).filter(text_len__lt=500,
#                                                                      text_len__gte=100)
#         elif self.value() == 'L':
#             return queryset.annotate(text_len=Length('text')).filter(text_len__gt=500)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted']
    list_filter  = [ 'author', 'date_posted']
    # list_display_links = ('date',)
    # search_fields = ['title__startswith', 'tags__title']
    # list_per_page = 5

admin.site.register(Post, PostAdmin)

#комментарии
#@admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'post', 'created', 'active')
#     list_filter = ('active', 'created', 'updated')
#     search_fields = ('name', 'email', 'body')

# class ViewCountAdmin(admin.ModelAdmin):
#     list_display = ['article','ip_address','view_date']
# #admin.site.register(ViewCount,ViewCountAdmin)