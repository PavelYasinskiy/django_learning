from django.urls import path
from .import views


urlpatterns=[
    path('', views.advertisement_list, name="advertisement_list"),
    path('first_page', views.first_page_list, name='first_page_list')
]

