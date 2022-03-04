from django.urls import path
from . import views

urlpatterns = [
    # path('', views.advertisement_list, name='advertisement_list'),
    # path('about/', views.about_lst, name='about_lst'),
    path('regions/', views.regions_lst, name='regions_lst'),
    path('categories/', views.categories_lst, name='categories_lst'),
    path('about/', views.About.as_view()),
    path('region/', views.Regions.as_view()),
    path('advertisments/', views.Advertisements.as_view()),
    path('contacts/', views.Contacts.as_view()),
    path('', views.MainMenu.as_view()),
]
