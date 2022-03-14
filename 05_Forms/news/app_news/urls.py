from django.urls import path, include
from app_news.views import NewsFormView,  NewsEditFormView, NewsListView, NewsDetailView

urlpatterns = [
    path('news/addnews/', NewsFormView.as_view()),
    path('news/<int:pk>/',  NewsDetailView.as_view(), name='news'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/edit/', NewsEditFormView.as_view()),
]

