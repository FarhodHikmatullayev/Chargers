from django.urls import path

from apps.chargers.views import CompaniesListApiView, ChargersListApiView, ChargerDetailApiView, \
    CompanyRetrieveApiView, CompanyChargersListApiView

app_name = 'chargers'

urlpatterns = [
    path('companies/list/', CompaniesListApiView.as_view(), name='companies_list'),
    path('list/', ChargersListApiView.as_view(), name='chargers_list'),
    path('<int:pk>/detail/', ChargerDetailApiView.as_view(), name='charger_detail'),
    path('company/<int:pk>/detail/', CompanyRetrieveApiView.as_view(), name='company_detail'),
    path('company/<int:pk>/chargers/list/', CompanyChargersListApiView.as_view(), name='company_chargers'),

]
