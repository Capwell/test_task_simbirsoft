from django.urls import path

from .views import HomeView, ArticleCreateView, ArticleListView

app_name = 'notes'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/add/', ArticleCreateView.as_view(), name='add_article'),
    path('article/list/', ArticleListView.as_view(), name='articles_list'),
]
