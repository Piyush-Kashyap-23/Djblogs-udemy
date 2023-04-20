from django.urls import path
from .views import HomeView, DetailPostView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', DetailPostView.as_view(), name='post_detail'),
    path('post/create/', CreatePostView.as_view(), name='post_create'),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='post_delete'),
]
