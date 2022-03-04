from advertisements.models import Advertisement
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = u'Создание случайного пользователя'

    def handle(self, *args, **kwargs):
        for i in range(500000):
            Advertisement.objects.all(title=f"Объявление: {i}")