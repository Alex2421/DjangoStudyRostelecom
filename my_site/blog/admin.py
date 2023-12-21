from django.contrib import admin
from .models import Post
admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    list_filter  = ['title', 'author', 'date',]
    list_display_links = ('date',)
    search_fields = ['title__startswith', 'tags__title']
    list_per_page = 5




# Register your models here.
class PostFilter(admin.SimpleListFilter):
    title = 'По длине новости'
    parameter_name = 'text'

    def lookups(self, request, model_admin):
        return [('S',("Короткие, <100 зн.")),
                ('M',("Средние, 100-500 зн.")),
                ('L',("Длинные, >500 зн.")),]

    def queryset(self, request, queryset):
        if self.value() == 'S':
            return queryset.annotate(text_len=Length('text')).filter(text_len__lt=100)
        elif self.value() == 'M':
            return queryset.annotate(text_len=Length('text')).filter(text_len__lt=500,
                                                                     text_len__gte=100)
        elif self.value() == 'L':
            return queryset.annotate(text_len=Length('text')).filter(text_len__gt=500)
