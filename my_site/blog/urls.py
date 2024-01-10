from django.urls import path
#from .views import upload_resume,upload_images
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('meeting/', views.meeting, name='blog-meeting'),
    path('meeting/form', views.form, name='blog-form'),
    path('anouncement/', views.anouncement, name='blog-anouncement'),
    path('about/', views.about, name='blog-about'),
    # # path('upload_resume/',upload_resume, name = "files" ),
    # path('upload_images/',upload_images, name = "images" ),

]