from django.db import models
import datetime

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, verbose_name='заголовок', db_index=True)
    description = models.TextField(max_length=1500, verbose_name='описание', default='описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', db_index=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    public_date = models.DateTimeField(default=datetime.datetime.today(), verbose_name='Дата публикации')
    over_date = models.DateTimeField(default=datetime.datetime.today(),
                                     verbose_name='Дата окончания публикации')
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements', verbose_name="статус")
    author = models.ForeignKey('AuthorContact', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advauthor', verbose_name="Автор")
    region = models.ManyToManyField('AdvertisementRegion',
                                    related_name='advregion')
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                             related_name='advtype')
    heading = models.ForeignKey('AdvertisementHeading', default=None, null=True, on_delete=models.CASCADE,
                                related_name='advheading')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisement'
        ordering = ['title']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=1500, verbose_name='Статус')

    def __str__(self):
        return self.name


class AdvertisementRegion(models.Model):
    regions = models.CharField(max_length=1500, verbose_name='Регион')

    def __str__(self):
        return self.regions


class AdvertisementType(models.Model):
    type = models.CharField(max_length=1500, verbose_name='Тип объявления')

    def __str__(self):
        return self.type


class AuthorContact(models.Model):
    name = models.CharField(max_length=1500, verbose_name='Имя')
    email = models.CharField(max_length=1500, verbose_name='Электронная почта')
    phone = models.CharField(max_length=15, verbose_name='Телефон')

    def __str__(self):
        return self.name


class AdvertisementHeading(models.Model):
    heading = models.CharField(max_length=1500, verbose_name='Наименование')

    def __str__(self):
        return self.heading


