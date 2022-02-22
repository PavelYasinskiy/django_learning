from django.urls import path
from .import views


urlpatterns=[
    path('', views.advertisement_list, name="advertisement_list"),
    path('first_page', views.first_page_list, name='first_page_list'),
    path('second_page', views.second_page_list, name='second_page_list'),
    path('third_page', views.third_page_list, name='third_page_list'),
    path('fourth_page', views.fourth_page_list, name='fourth_page_list'),
    path('fifth_page', views.fifth_page_list, name='fifth_page_list'),
]

