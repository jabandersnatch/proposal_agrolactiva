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
        model = Route
        fields = '__all__'

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
    class Meta:
        model = ProviderProductControl
        fields = '__all__'

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

