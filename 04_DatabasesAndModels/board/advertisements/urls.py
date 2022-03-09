from django.urls import path

urlpatterns = [
    path('advertisements/', AdvertisementListView.as_view(), name='advertisement'),
    path('advertisements/<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement-detail'),

]
