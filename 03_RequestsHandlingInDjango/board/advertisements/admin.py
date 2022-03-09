from django.contrib import admin
from advertisements.models import Advertisement, AuthorContact, AdvertisementStatus, AdvertisementRegion, \
    AdvertisementType, AdvertisementHeading

# Register your models here.

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass


@admin.register(AuthorContact)
class AuthorContactAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementStatus)
class StatuAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementRegion)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementType)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementHeading)
class HeadingAdmin(admin.ModelAdmin):
    pass