from django.urls import path, include
from app_news.views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView

urlpatterns = [
    path('news/addnews/', NewsCreateView.as_view(), name='add'),
    path('news/<int:pk>/',  NewsDetailView.as_view(), name='news-detail'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/edit/<int:pk>/', NewsUpdateView.as_view(), name="news-edit"),
]

