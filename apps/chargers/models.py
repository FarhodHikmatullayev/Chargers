from django.core.validators import FileExtensionValidator
from django.db import models


class Location(models.Model):
    latitude = models.FloatField(max_length=221)
    longitude = models.FloatField(max_length=221)


class ChargerCompany(models.Model):
    name = models.CharField(max_length=221)
    website = models.CharField(max_length=500)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class Image(models.Model):
    company = models.ForeignKey(ChargerCompany, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='Company/', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'heif', 'heic'])
    ])

    def __str__(self):
        return f"{self.company.name}'s image({self.id})"


class Charger(models.Model):
    title = models.CharField(max_length=221)
    description = models.TextField(null=True, blank=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='charger')
    image = models.ImageField(upload_to='chargers/', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'heif', 'heic'])])
    company = models.ForeignKey(ChargerCompany, on_delete=models.CASCADE, related_name='chargers')

    def __str__(self):
        return self.title


class Tariff(models.Model):
    charger = models.ForeignKey(Charger, on_delete=models.CASCADE, related_name='tariffs')
    volt = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    time = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.charger.title}'s tariff ({self.id})"
