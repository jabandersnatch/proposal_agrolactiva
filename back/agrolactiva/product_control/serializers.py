from rest_framework import serializers
from .models import *

# Create municipality serializer class
class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = '__all__'

# Create location serializer class
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

# Create route serializer class
class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        '''
        The serializer recives all the fields from the model except the n_providers field
        set to read only
        '''
        model = Route
        fields = '__all__'
        extra_kwargs = {'n_providers': {'read_only': True}}

# Create Person serializer class
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

# Create Employee serializer class
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
# Create Provider serializer class
class ProviderSerializer(serializers.ModelSerializer):
    '''
    Every time a provider is created, the number of providers in the route is updated
    '''
    def create(self, validated_data):
        provider = Provider.objects.create(**validated_data)
        provider.id_route.n_providers += 1
        provider.id_route.save()
        return provider
    class Meta:
        model = Provider
        fields = '__all__'

# Create contact info model serializer class
class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'

# Create billing info model serializer class
class BillingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingInfo
        fields = '__all__'

# create delivery model serializer class
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

# Create provider price model serializer class
class ProviderPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderPrice
        fields = '__all__'

# Create provider product control
class ProviderProductControlSerializer(serializers.ModelSerializer):
    '''
    This serializer is used to create a new provider product Control
    calculate the payment amount
    '''
    def create(self, validated_data):
        provider_product_control = ProviderProductControl.objects.create(**validated_data)
        provider_product_control.payment_amount = provider_product_control.id_provider_price.price * provider_product_control.quantity
        provider_product_control.save()
        return provider_product_control
    class Meta:
        model = ProviderProductControl
        fields = '__all__'
        extra_kwargs = {'payment_amount': {'read_only': True}}


# Create client model serializer class
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

# Create product dispatch model serializer class
class ProductDispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDispatch
        fields = '__all__'

# Create Provider payment model serializer class
class ProviderPaymentSerializer(serializers.ModelSerializer):
    '''
    Calculate total payment amount
    
    payment_amount is not a field in the model, it is calculated fr
    '''

    def create(self, validated_data):
        provider_payment = ProviderPayment.objects.create(**validated_data)
        # Get all the deliveries that happen betwenn the payment_since and payment_util
        deliveries = Delivery.objects.filter(delivery_date__range=[provider_payment.payment_since, provider_payment.payment_until])
        # Get all the provider product controls that are related to the deliveries
        provider_product_controls = ProviderProductControl.objects.filter(id_delivery__in=deliveries)
        # Add all the payment amounts
        provider_payment.total_amount = sum([provider_product_control.payment_amount for provider_product_control in provider_product_controls])
        provider_payment.save()
        return provider_payment

    class Meta:
        model = ProviderPayment
        fields = '__all__'
        extra_kwargs = {'total_amount': {'read_only': True}}
