from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts_list'

class DetailPostView(DetailView):
    model = Post
    template_name = 'postDetail.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'postCreate.html'
    fields = ['title', 'body', 'author']

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'postUpdate.html'
    fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'postDelete.html'
    success_url = reverse_lazy('home')