from django.db import models
from datetime import timedelta
from django.utils import timezone
# Create enumeration document type model
class document_type(models.TextChoices):
    '''
    Enunmeration of document types in Colombia
    '''
    CC = 'CC', 'Cédula de ciudadanía'
    CE = 'CE', 'Cédula de extranjería'
    TI = 'TI', 'Tarjeta de identidad'
    PA = 'PA', 'Pasaporte'
    RC = 'RC', 'Registro civil'
    NIT = 'NIT', 'Número de identificación tributaria'

# Create employee type text choices
class employee_type(models.TextChoices):
    '''
    Enunmeration of employee types
    '''
    DRIVER = 'DRIVER', 'Conductor'
    ASSISTANT = 'ASSISTANT', 'Asistente'
    ADMINISTRATOR = 'ADMINISTRATOR', 'Administrador'

# Create payment type text choices
class payment_type(models.TextChoices):
    '''
    Enunmeration of payment types
    '''
    CASH = 'CASH', 'Efectivo'
    debit_card = 'DEBIT_CARD', 'Tarjeta débito'
    credit_card = 'CREDIT_CARD', 'Tarjeta crédito'
    nequi = 'NEQUI', 'Nequi'
    daviplata = 'DAVIPLATA', 'Daviplata'

# Create bank text choices
class bank(models.TextChoices):
    '''
    Enunmeration of banks in Colombia
    '''
    BANCO_AGRARIO = 'BANCO_AGRARIO', 'Banco Agrario'
    BANCO_DAVIVIENDA = 'BANCO_DAVIVIENDA', 'Banco Davivienda'
    BANCO_DE_BOGOTA = 'BANCO_DE_BOGOTA', 'Banco de Bogotá'
    BANCOLOMBIA = 'BANCOLOMBIA', 'Bancolombia'
    BBVA_COLOMBIA = 'BBVA_COLOMBIA', 'BBVA Colombia'
    NO_APLICA = 'NO_APLICA', 'No aplica'


# Create route type text TextChoices
class route_type(models.TextChoices):
    '''
    Enunmeration of route types
    '''
    MORNING_ROUTE = 'MORNING_ROUTE', 'Ruta de la mañana'
    AFTERNOON_ROUTE = 'AFTERNOON_ROUTE', 'Ruta de la tarde'
    NIGHT_ROUTE = 'NIGHT_ROUTE', 'Ruta de la noche'

# Create municipality model
class Municipality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Municipalities"
        ordering = ['name']

# Create location model
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    id_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Locations"
        ordering = ['name']

# Create route model
class Route(models.Model):
    id = models.AutoField(primary_key=True)
    locations = models.ManyToManyField(Location)
    route_type = models.CharField(
        max_length=20,
        choices=route_type.choices,
        default=route_type.MORNING_ROUTE,
    )
    n_providers = models.IntegerField(default=0)


    def __str__(self):
        # Create a string with all the codes of the different Locations

        location_codes = ''

        for location in self.locations.all():
            location_codes += location.code + ' - '


        return f'{self.id} - {self.route_type} - {location_codes}'

    class Meta:
        verbose_name_plural = "Routes"
        ordering = ['id']
        

        
# Create person model
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document_type = models.CharField(
        max_length=3,
        choices=document_type.choices,
        default=document_type.CC,
    )
    document_number = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)
        
    class Meta:
        verbose_name_plural = "Persons"

# Create contact info model
class ContactInfo(models.Model):
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id_person.first_name} {self.id_person.last_name} {self.email}'

    class Meta:
        verbose_name_plural = "Contact Info"
        ordering = ['id']

# Create billing info model 
class BillingInfo(models.Model):
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    payment_type = models.CharField(
        max_length=11,
        choices=payment_type.choices,
        default=payment_type.CASH,
    )
    bank = models.CharField(
        max_length=25,
        choices=bank.choices,
        default=bank.BANCOLOMBIA,
    )
    account_number = models.CharField(max_length=100, blank=True, null=True)
    account_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.id_person}'

    class Meta:
        verbose_name_plural = "Billing Info"
        ordering = ['id']

# Create employee model 
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    salary = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.id_person.first_name}'
        
    class Meta:
        verbose_name_plural = "Employees"
        ordering = ['start_date']
        
# Create provider model
class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    id_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    register_date = models.DateField()

    def __str__(self):
        return f'{self.id_person}'
        
    class Meta:
        verbose_name_plural = "Providers"
        ordering = ['register_date']

# Create delivery model
class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    id_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    id_delivered_by = models.ForeignKey(
            Employee,
            related_name='delivered_by',
            on_delete=models.CASCADE)
    id_received_by = models.ForeignKey(
            Employee, 
            related_name='received_by',
            on_delete=models.CASCADE)
    delivery_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.id_route} - {self.id_delivered_by} - {self.id_received_by} - {self.delivery_date} - {self.quantity}'
        
    class Meta:
        verbose_name_plural = "Deliveries"
        ordering = ['delivery_date', 'quantity']

# Create ProviderPrice
class ProviderPrice(models.Model):
    id = models.AutoField(primary_key=True)
    id_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.id_provider} - {self.price} - {self.start_date} - {self.end_date}'
        
    class Meta:
        verbose_name_plural = "Provider Prices"
        ordering = ['id_provider', 'price']

# Create provider product control model
class ProviderProductControl(models.Model):
    id = models.AutoField(primary_key=True)
    id_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    id_delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    id_provider_price = models.ForeignKey(ProviderPrice, on_delete=models.CASCADE)
    payment_amount = models.IntegerField()

    def __str__(self):
        return f'{self.id_provider} - {self.id_delivery} - {self.quantity} - {self.id_provider_price} - {self.payment_amount}'
        
    class Meta:
        verbose_name_plural = "Provider Product Control"
        ordering = ['id_provider', 'id_delivery', 'quantity', 'id_provider_price']

# Create client

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100)
    register_date = models.DateField()

    def __str__(self):
        return self.id_person.first_name + ' ' + self.id_person.last_name
        
    class Meta:
        verbose_name_plural = "Clients"
        ordering = ['register_date']

# Create product dispatch model
class ProductDispatch(models.Model):
    id = models.AutoField(primary_key=True)
    id_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    id_delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    id_dispatched_by = models.ForeignKey(
            Employee, 
            on_delete=models.CASCADE)
    id_client = models.ForeignKey(
            Client, 
            on_delete=models.CASCADE)
    dispatch_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.id_route} - {self.id_delivery} - {self.id_dispatched_by} - {self.id_client} - {self.dispatch_date} - {self.quantity}'
    class Meta:
        verbose_name_plural = "Product Dispatch"

# Provider payment model
class ProviderPayment(models.Model):
    id = models.AutoField(primary_key=True)
    id_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    payment_since = models.DateField()
    payment_until = models.DateField(default=timezone.now)
    payment_date = models.DateField(default=timezone.now)
    total_amount = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.id_provider} - {self.payment_since} - {self.payment_until} - {self.payment_date} - {self.total_amount}'
    class Meta:
        verbose_name_plural = "Provider Payment"
