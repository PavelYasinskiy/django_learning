from django.shortcuts import render

class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = "advertisement_list"
    queryset = Advertisement.objects.all()


class AdvertisementDetailView(DetailView):
    model = Advertisement
