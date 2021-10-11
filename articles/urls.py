from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit/', ArticleEditView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('my-articles/', MyArticlesView.as_view(), name='my_articles'),
    path('my-comments/', MyCommentsView.as_view(), name='my_comments'),
]