from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path("article_list/", views.ArticleListView.as_view(), name="article_list"),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
