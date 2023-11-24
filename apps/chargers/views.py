from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.chargers.models import ChargerCompany, Charger
from apps.chargers.serializers import CompanySerializer, ChargerSerializer


class CompaniesListApiView(ListAPIView):
    serializer_class = CompanySerializer
    queryset = ChargerCompany.objects.all()


class CompanyRetrieveApiView(RetrieveAPIView):
    queryset = ChargerCompany.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'pk'


class ChargersListApiView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Charger.objects.all()
    serializer_class = ChargerSerializer


class ChargerDetailApiView(RetrieveAPIView):
    queryset = Charger.objects.all()
    serializer_class = ChargerSerializer
    lookup_field = 'pk'


class CompanyChargersListApiView(APIView):

    def get(self, request, pk):
        chargers = Charger.objects.filter(company_id=pk)
        serializer = ChargerSerializer(chargers, many=True)
        return Response(
            {
                'success': True,
                'data': serializer.data,
                'status': status.HTTP_200_OK
            }
        )
