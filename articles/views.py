from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Article, Comment

from .forms import CommentForm

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'

class ArticleDetailView(DetailView, CreateView):
    model = Article
    template_name = 'article_detail.html'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse('article_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs['pk'])
        return super(ArticleDetailView, self).form_valid(form)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'text',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'text',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class MyArticlesView(ListView):
    model = Article
    template_name = 'my_articles.html'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

class MyCommentsView(ListView):
    model = Comment
    template_name = 'my_comments.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
