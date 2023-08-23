from dataclasses import field, fields
from pyexpat import model
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class BlockListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_add.html'
    fields = ['title', 'author', 'body']

class PostEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')
