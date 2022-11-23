from .models import *
from django.contrib import admin
from django.contrib.auth import get_user_model
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

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
    list_display = ('id', 'n_providers', 'avg_daily_product_income', 'route_type')
    list_filter = ('id', 'n_providers', 'avg_daily_product_income', 'route_type')
    search_fields = ('id', 'n_providers', 'avg_daily_product_income', 'route_type')
    ordering = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'document_type', 'document_number')
    list_filter = ('document_type',)
    search_fields = ('first_name', 'last_name', 'document_type', 'document_number')
    ordering = ('last_name', 'first_name')

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
    list_display = ('id', 'id_provider', 'id_delivery', 'quantity', 'id_provider_price', 'payment_amount')
    list_filter = ('id', 'id_provider', 'id_delivery', 'quantity', 'id_provider_price', 'payment_amount')
    search_fields = ('id', 'id_provider', 'id_delivery', 'quantity', 'id_provider_price', 'payment_amount')
    ordering = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_person', 'organization', 'register_date')
    list_filter = ('id', 'id_person', 'organization', 'register_date')
    search_fields = ('id', 'id_person', 'organization', 'register_date')
    ordering = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(ProductDispatch)
class ProductDispatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_route', 'id_delivery', 'id_dispatched_by', 'id_client', 'dispatch_date', 'quantity')
    list_filter = ('id', 'id_route', 'id_delivery', 'id_dispatched_by', 'id_client', 'dispatch_date', 'quantity')
    search_fields = ('id', 'id_route', 'id_delivery', 'id_dispatched_by', 'id_client', 'dispatch_date', 'quantity')
    ordering = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

