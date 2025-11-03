from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.filter(publication=True)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article_detail'

    def get(self, request, pk):
        article = get_object_or_404(Article, id=pk)
        article.count_views()  # Увеличиваем количество просмотров
        return render(request, 'blog/article_detail.html', {'article': article})


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('blog:article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ('title', 'content', 'image')

    def get_success_url(self):
        pk = self.object.pk
        return reverse('blog:article_detail', kwargs={'pk': pk})


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('blog:article_list')


def success_publication(request, pk):
    article = get_object_or_404(Article, id=pk)
    article.publication = True
    article.save()
    return redirect('blog:article_list')