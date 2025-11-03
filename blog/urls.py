from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path("article_list/", views.ArticleListView.as_view(), name="article_list"),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article_create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<int:pk>/success_publication/', views.success_publication, name='article_publicate'),
]
