from django.db import models

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
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Locations"
        ordering = ['name']

# Create route model
class Route(models.Model):
    id = models.AutoField(primary_key=True)
    n_providers = models.IntegerField()
    avg_daily_product_income = models.IntegerField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Routes"
        ordering = ['id']

# Create route location model
class RouteLocation(models.Model):
    id = models.AutoField(primary_key=True)
    id_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    id_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Route Locations"
        ordering = ['id']
        
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
        return self.name
        
    class Meta:
        verbose_name_plural = "Persons"
        ordering = ['name']       

# Create contact info model
class ContactInfo(models.Model):
    id = models.AutoField(primary_key=True)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Contact Info"
        ordering = ['id']

# Create billing info model 
class BillingInfo(models.Model):
    id = models.AutoField(primary_key=True)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    payment_type = models.CharField(
        max_length=11,
        choices=payment_type.choices,
        default=payment_type.CASH,
    )
    bank = models.CharField(
        max_length=15,
        choices=bank.choices,
        default=bank.BANCOLOMBIA,
    )
    account_number = models.CharField(max_length=100, blank=True, null=True)
    account_type = models.CharField(max_length=100, blank=True, null=True)
    id_representative = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Billing Info"
        ordering = ['id']

# Create employee model 
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    salary = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Employees"
        ordering = ['name']
        
# Create provider model
class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    register_date = models.DateField()

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Providers"
        ordering = ['name']

# Create delivery model
class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    id_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    id_delivered_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_received_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    delivery_product_quantity = models.IntegerField()

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Deliveries"
        ordering = ['name']

# Create provider product control model
class ProviderProductControl(models.Model):
    id = models.AutoField(primary_key=True)
    id_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    id_delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    total_price = models.IntegerField()
    delivery_date = models.DateField()

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Provider Product Control"
        ordering = ['name']










        
        
        
        
        
        
        
        
        
        
        
        
