from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'municipality', MunicipalityViewSet)
router.register(r'location', LocationViewSet)
router.register(r'route', RouteViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'provider', ProviderViewSet)
router.register(r'contactinfo', ContactInfoViewSet)
router.register(r'billinginfo', BillingInfoViewSet)
router.register(r'delivery', DeliveryViewSet)
router.register(r'provider_price', ProviderPriceViewSet)
router.register(r'product_product_control', ProviderProductControlViewSet)
router.register(r'client', ClientViewSet)
router.register(r'product_dispatch', ProductDispatchViewSet)

app_name = 'product_control'
urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/', CustomAuthToken.as_view())
]

