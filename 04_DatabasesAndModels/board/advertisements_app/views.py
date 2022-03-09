from django.shortcuts import render
from django.views.generic import ListView, DetailView
from advertisements_app.models import Advertisement

class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = "advertisement_list"
    queryset = Advertisement.objects.all()


class AdvertisementDetailView(DetailView):
    model = Advertisement
