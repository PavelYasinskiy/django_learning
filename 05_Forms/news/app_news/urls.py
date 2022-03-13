from django.urls import path, include
from app_news.views import NewsFormView, CommentsFormView, NewsEditFormView, NewsListView, NewsDetailView, NewsView

urlpatterns = [
    path('news/addnews/', NewsFormView.as_view()),
    path('news/<int:pk>/', NewsView.as_view(), name='news'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:new_id>/edit/', NewsEditFormView.as_view()),
]

