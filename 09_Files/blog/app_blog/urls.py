from django.urls import path, include
from app_blog.views import UserLoginView, UserLogoutView, \
                            register_view, profile_detail_view,\
                            profile_user_edit, BlogListView,\
                            blog_add, BlogDetailView, update_blog

urlpatterns = [

    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile_page/', profile_detail_view, name='profile_page'),
    path('profile_user_edit/', profile_user_edit, name='profile_edit'),
    path('blog/addblog/', blog_add, name='add'),
    path('blog/<int:pk>/',  BlogDetailView.as_view(), name='blog-detail'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('upload_blog/', update_blog, name='update_blog'),

]