
from django.urls import include, path

from .views import rento, tentants, landlord

urlpatterns = [
    path('', rento.home, name='home'),
    path('tenants/', include(([
        path('rent/', tentants.TenantPayRent.as_view(), name='pay_rent'),
        
    ], 'rento'), namespace='tenants')),


    
]