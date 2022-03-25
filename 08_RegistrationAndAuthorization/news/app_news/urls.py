from django.urls import path, include
from app_news.views import NewsListView, NewsDetailView, NewsCreateView, \
                            NewsUpdateView, UserLoginView, UserLogoutView, \
                            register_view, profile_detail_view, NewsModeratorUpdateView

urlpatterns = [
    path('news/addnews/', NewsCreateView.as_view(), name='add'),
    path('news/<int:pk>/',  NewsDetailView.as_view(), name='news-detail'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/editmod/<int:pk>/', NewsModeratorUpdateView.as_view(), name="newsmod-edit"),
    path('news/edit/<int:pk>/', NewsUpdateView.as_view(), name="news-edit"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile_page/', profile_detail_view, name='profile_page'),


]
