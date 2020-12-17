from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import ArticleCreateForm
from .models import Article
from .apps import NotesConfig


class HomeView(TemplateView):
    template_name = 'notes/home.html'

    def get_context_data(self, **kwargs):
        kwargs['articles_count'] = Article.objects.articles_by_author_count()
        kwargs['app_name'] = NotesConfig.verbose_name
        return super(HomeView, self).get_context_data(**kwargs)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'notes/add_article.html'
    model = Article
    form_class = ArticleCreateForm
    success_url = reverse_lazy('notes:home')


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'notes/articles_list.html'
    model = Article

    def get_queryset(self):
        return Article.objects.articles_by_author()
