from django.urls import path
from . import views
from .views import AdvertisementListView, AdvertisementDetailView

urlpatterns = [
    # path('adv/', views.advertisement_list, name='advertisement_list'),
    # # path('about/', views.about_lst, name='about_lst'),
    # path('regions/', views.regions_lst, name='regions_lst'),
    # path('categories/', views.categories_lst, name='categories_lst'),
    # path('about/', views.About.as_view()),
    # path('region/', views.Regions.as_view()),
    path('advertisements/', AdvertisementListView.as_view(), name='advertisement'),
    path('advertisements/<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement-detail'),
    # path('contacts/', views.Contacts.as_view()),
    # path('', views.MainMenu.as_view()),
]
