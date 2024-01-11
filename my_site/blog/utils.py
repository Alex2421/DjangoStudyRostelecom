from django.db.models import Q

#счетчик уникальных просмотров
def get_client_ip(request):
    """
    Получение IP адреса
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


from .models import ViewCount
class ViewCountMixin:
    def get_object(self):
        #получаем объект из родительского класса
        obj = super().get_object()
        ip_address = get_client_ip(self.request)
        #Если такой счетчик уже создан - выполнится get - получение
        #если его еще не было - выполнится Create
        ViewCount.objects.get_or_create(post=obj, ip_address=ip_address)
        return obj


# def searchPost(request):
#
#     search_query = ''
#
#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')
#
#     tags = Tag.objects.filter(name__icontains=search_query)
#
#     projects = Project.objects.distinct().filter(
#         Q(title__icontains=search_query) |
#         Q(description__icontains=search_query) |
#         Q(owner__name__icontains=search_query) |
#         Q(tags__in=tags)
#     )
#     return projects, search_query