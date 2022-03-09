from advertisements.models import Advertisement
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = u'Автозаполнение бд'

    def handle(self, *args, **kwargs):
        for i in range(500000):
            Advertisement.objects.create(title=f"Объявление: {i}")