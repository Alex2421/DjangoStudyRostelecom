from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.shortcuts import render



# from .forms import ViewCountMixin
# from django.views.generic import DetailView
# class PostDetailView(ViewCountMixin, DetailView):



#поиск
import json
def search_auto(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        q = request.GET.get('term','')
        articles = Post.objects.filter(title__icontains=q)
        results =[]
        for a in articles:
            results.append(a.title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

# def search(request):
#     if request.method == 'POST': #пришел запрос из бокового меню
#         value = request.POST['search_input'] #находим новости
#         articles = Article.objects.filter(title__icontains=value)
#         if len(articles) == 1: #если одна- сразу открываем подробное отображение новости
#             return render(request, 'news/news_detail.html', {'article': articles[0]})
#         else:
#             #если несколько - отправляем человека в функцию index со страницей-списком новостей и фильтрами
#             #не забываем передать поисковый запрос:
#             # либо через сессии:
#             request.session['search_input'] = value
#             return redirect('news')
#             #либо через фрагмент URLссылки:
#             # но в таком случае придётся обрабатывать ссылку в Urls
#             #функция reverse из модуля Urls добавит переданные аргументы в качестве get-аргументов.
#             # return redirect(reverse('news', kwargs={'search_input':value}))
#
#             # return render(request, 'news/news_list.html', {'articles': articles})
#     else:
#         return redirect('home')


#image
def upload_images(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ImageForm

    return render(request, 'blog/images.html', {'form':form})

def upload_resume(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ImageForm

    return render(request, 'blog/images.html', {'form':form})




def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#модель счетчиков просмотров
# class ViewCount(models.Model):
#     post = models.ForeingKey('Post', on_delete=models.CASCADE,
#                              relates_name='views')
#     ip_address = models.GenericIPAddressField()
#     view_date = models.DateField(auto_now_add=True)
#     class Meta:
#         ordering = ('-view_date',)
#         indexes = [models.Index(fields=['-view_date'])]
#
#     def __str__(self):
#         return self.post.title

def post(request):
    context = {
        'posts': Post.objects.filter(author=request.user)
    }

    return render(request, 'index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post





class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'anouncement', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')
    #success_url = '/'
    template_name = 'blog/post_confirm_delete.html'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'О клубе Python RTK'})
def meeting(request):
    return render(request, 'blog/meeting.html', {'title': 'Встречи клуба'})
def form(request):
    return render(request, 'blog/form.php', {'title': 'Встречи клуба'})
def anouncement(request):
    return render(request, 'blog/anouncement.html', {'title': 'Встречи клуба'})