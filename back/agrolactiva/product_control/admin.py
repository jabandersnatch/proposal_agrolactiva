from .models import *
from django.contrib import admin

@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_filter = ('code',)
    search_fields = ('name', 'code')
    ordering = ('name',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'id_municipality')
    list_filter = ('code', 'id_municipality')
    search_fields = ('name', 'code', 'id_municipality')
    ordering = ('name',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display =  ('id', 'n_providers', 'route_type')
    list_filter =   ('id', 'n_providers',  'route_type')
    search_fields = ('id', 'n_providers', 'route_type')
    ordering = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('id_person', 'phone_number', 'email')
    list_filter = ('id_person',)
    search_fields = ('id_person', 'phone_number', 'email')
    ordering = ('id_person',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(BillingInfo)
class BillingInfoAdmin(admin.ModelAdmin):
    list_display = ('id_person', 'payment_type', 'bank', 'account_number', 'account_type')
    list_filter = ('id_person', 'payment_type', 'bank', 'account_number', 'account_type')
    search_fields = ('id_person', 'payment_type', 'bank', 'account_number', 'account_type')
    ordering = ('id_person',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_person', 'salary', 'start_date', 'end_date')
    list_filter = ('id', 'id_person', 'salary', 'start_date', 'end_date')
    search_fields = ('id', 'id_person', 'salary', 'start_date', 'end_date')
    ordering = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_person', 'id_route', 'register_date')
    list_filter = ('id', 'id_person', 'id_route', 'register_date')
    search_fields = ('id', 'id_person', 'id_route', 'register_date')
    ordering = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_route', 'id_delivered_by', 'id_received_by', 'delivery_date', 'quantity')
    list_filter = ('id', 'id_route', 'id_delivered_by', 'id_received_by', 'delivery_date', 'quantity')
    search_fields = ('id', 'id_route', 'id_delivered_by', 'id_received_by', 'delivery_date', 'quantity')
    ordering = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(ProviderPrice)
class ProviderPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_provider', 'price', 'start_date', 'end_date')
    list_filter = ('id', 'id_provider', 'price', 'start_date', 'end_date')
    search_fields = ('id', 'id_provider', 'price', 'start_date', 'end_date')
    ordering = ('id',)

@admin.register(ProviderProductControl)
class ProviderProductControlAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_provider', 'id_delivery', 'quantity', 'id_provider_price')
    list_filter = ('id', 'id_provider', 'id_delivery', 'quantity', 'id_provider_price')
    search_fields = ('id', 'id_provider', 'id_delivery', 'quantity', 'id_provider_price')
    ordering = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_person', 'organization', 'register_date')
    ordering = ('id','register_date')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(ProductDispatch)
class ProductDispatchAdmin(admin.ModelAdmin):
    list_display = ('id','id_route', 'id_dispatched_by', 'id_client', 'dispatch_date', 'quantity')
    list_filter = ('id','id_route', 'id_dispatched_by', 'id_client', 'dispatch_date', 'quantity')
    search_fields = ('id','id_route', 'id_dispatched_by', 'id_client', 'dispatch_date', 'quantity')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(ProviderPayment)
class ProviderPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_provider', 'payment_since', 'payment_until', 'payment_date', 'total_amount')
    list_filter = ('id', 'id_provider', 'payment_since', 'payment_until', 'payment_date', 'total_amount')
    search_fields = ('id', 'id_provider', 'payment_since', 'payment_until', 'payment_date', 'total_amount')
    ordering = ('id',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


