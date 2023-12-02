from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.chargers.models import ChargerCompany, Charger
from apps.chargers.serializers import CompanySerializer, ChargerSerializer, ChargerCreateSerializer
from apps.shared.pagination import CustomPagination
from apps.shared.permissions import IsAdminOrReadOnly


class CompaniesListCreateApiView(ListCreateAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = CustomPagination
    serializer_class = CompanySerializer
    queryset = ChargerCompany.objects.all()


class CompanyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = ChargerCompany.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'pk'


class ChargersListApiView(ListAPIView):
    pagination_class = CustomPagination
    permission_classes = (AllowAny,)
    queryset = Charger.objects.all()
    serializer_class = ChargerSerializer


class ChargerCreateApiView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Charger.objects.all()
    serializer_class = ChargerCreateSerializer


class ChargersRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Charger.objects.all()
    serializer_class = ChargerSerializer
    lookup_field = 'pk'


class CompanyChargersListApiView(APIView):
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination

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
