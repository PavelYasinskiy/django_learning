from django.urls import path, include
# from app_news.views import UserFormView, UserEditFormView
from app_news.views import NewsFormView, CommentsFormView, NewsEditFormView, NewsListView, NewsDetailView, NewsView

urlpatterns = [
    # path('profiles/register/', UserFormView.as_view()),
    # path('profiles/<int:profile_id>/edit/', UserEditFormView.as_view())
    path('news/addnews/', NewsFormView.as_view()),
    path('news/<int:pk>/', NewsView.as_view(), name='news'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:new_id>/edit/', NewsEditFormView.as_view()),
]

# список всех новостей (новости отсортированы по дате создания),
# страничку создания новости,
# страничку редактирования новости,
# детальная страница новости+комментарии к ней (с возможностью добавить новый комментарий).
