from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'article_list'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article_detail'


class ArticleCreateView(CreateView):
    pass


class ArticleUpdateView(UpdateView):
    pass


class ArticleDeleteView(DeleteView):
    pass
