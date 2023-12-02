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
    company = CompanySerializer(read_only=True, required=False)
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Charger
        fields = '__all__'


class ChargerCreateSerializer(serializers.ModelSerializer):
    location = LocationSerializer(write_only=True)

    class Meta:
        model = Charger
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        location = validated_data.pop('location')
        location = Location.objects.create(latitude=location.get('latitude'), longitude=location.get('longitude'))
        charger = Charger.objects.create(**validated_data, location_id=location.id)
        return charger


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
