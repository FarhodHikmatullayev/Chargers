from django.urls import path

from apps.chargers.views import CompaniesListCreateApiView, ChargersListApiView, \
    ChargersRetrieveUpdateDestroyAPIView, \
    CompanyChargersListApiView, CompanyRetrieveUpdateDestroyAPIView, ChargerCreateApiView

app_name = 'chargers'

urlpatterns = [
    path('companies/list-create/', CompaniesListCreateApiView.as_view(), name='companies_list_create'),
    path('list/', ChargersListApiView.as_view(), name='chargers_list'),
    path('create/', ChargerCreateApiView.as_view(), name='chargers_create'),
    path('<int:pk>/retrieve-update-destroy/', ChargersRetrieveUpdateDestroyAPIView.as_view(),
         name='charger_retrieve_update_destroy'),
    path('company/<int:pk>/retrieve-update-destroy/', CompanyRetrieveUpdateDestroyAPIView.as_view(),
         name='company_retrieve_update_destroy'),
    path('company/<int:pk>/chargers/list/', CompanyChargersListApiView.as_view(), name='company_chargers'),
]
