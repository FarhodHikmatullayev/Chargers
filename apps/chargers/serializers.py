from rest_framework import serializers

from apps.chargers.models import ChargerCompany, Charger, Tariff, Image, Location


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargerCompany
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ChargerSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Charger
        fields = '__all__'


class TariffSerializer(serializers.ModelSerializer):
    charger = ChargerSerializer(read_only=True)

    class Meta:
        model = Tariff
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Image
        fields = '__all__'
