from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView, DetailView, CreateView, UpdateView,
DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#def home(request):
#	return render(request, 'posts/home.html', {'posts': Post.objects.all()})

class ListPost(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    ordering = ['-p_date']

class DetailPost(DetailView):
    model = Post

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['p_title', 'p_content']
    def form_valid(self, form):
        form.instance.p_author = self.request.user
        return super().form_valid(form)

class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['p_title', 'p_content']
    def form_valid(self, form):
        form.instance.p_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.p_author

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.p_author
    success_url = '/'
