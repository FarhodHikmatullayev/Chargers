from django.contrib import admin

from apps.chargers.models import ChargerCompany, Charger, Tariff, Image, Location


class ChargerInlineAdmin(admin.StackedInline):
    model = Charger
    extra = 0


class ImageInlineAdmin(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(ChargerCompany)
class ChargerCompanyAdmin(admin.ModelAdmin):
    inlines = (ChargerInlineAdmin, ImageInlineAdmin)
    list_display = ('id', 'name', 'phone')


class TariffInlineAdmin(admin.TabularInline):
    model = Tariff
    extra = 0


@admin.register(Charger)
class ChargerAdmin(admin.ModelAdmin):
    inlines = (TariffInlineAdmin,)
    list_display = ('id', 'title', 'company')


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('id', 'charger', 'volt')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'company')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude')
