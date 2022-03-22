from django.urls import path, include
from app_news.views import NewsListView, NewsDetailView, NewsCreateView, \
                            NewsUpdateView, UserLoginView, UserLogoutView

urlpatterns = [
    path('news/addnews/', NewsCreateView.as_view(), name='add'),
    path('news/<int:pk>/',  NewsDetailView.as_view(), name='news-detail'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/edit/<int:pk>/', NewsUpdateView.as_view(), name="news-edit"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

]