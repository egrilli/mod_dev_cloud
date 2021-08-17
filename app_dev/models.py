from django.db import models
import re
from datetime import datetime, date
from app_dev.list_model import *

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['first_name']) < 3:
            errors['firstname_len'] = "nombre debe tener al menos 3 caracteres de largo";

        if len(postData['last_name']) < 2:
            errors['lastname_len'] = "apellido debe tener al menos 2 caracteres de largo";

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "correo invalido"
        
        if len(User.objects.filter(email=postData["email"])) > 0:
            errors["exists"]= "El correo ya existe"


        if not SOLO_LETRAS.match(postData['first_name']) or not SOLO_LETRAS.match(postData['last_name']):
            errors['solo_letras'] = "solo letras en nombre y apellido porfavor"

        if len(postData['password']) < 8:
            errors['password'] = "contraseña debe tener al menos 8 caracteres";

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "contraseña y confirmar contraseña no son iguales. "

        return errors




class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=70)
    rol= models.CharField(max_length=70, default="USER")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #orders_user
    objects = UserManager()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def __repr__(self):
        return f"{self.first_name} {self.last_name}" 


class CompanyManager(models.Manager):
    def validador_basico(self, postData):

        errors = {}

        if len(postData['name']) < 3:
            errors['name_len'] = "nombre debe tener al menos 3 caracteres de largo";

        if len(Company.objects.filter(name=postData["name"])) > 0:
            errors["exists"]= "La compania ya existe"

        if len(postData['rut']) < 7:
            errors['rut_len'] = "El rut debe tener mas de 7 caracteres";
        
        if len(postData['warehouse_origin']) < 1:
            errors['warehouse_origin_len'] = "No ha ingresado alguna bodega";    

        
        return errors


class Company(models.Model):
    name = models.CharField(max_length=45,choices=company)
    rut = models.CharField(max_length=45)
    warehouse_origin = models.CharField(max_length=45, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CompanyManager()
    #orders_company
    def __str__(self):
        return f"{self.name}"
    def __repr__(self):
        return f"{self.name}"


class WarehouseManager(models.Manager):
    def validador_basico(self, postData):

        errors = {}

        if len(postData['name']) < 3:
            errors['name_len'] = "nombre debe tener al menos 3 caracteres de largo";

        if len(Warehouse.objects.filter(name=postData["name"])) > 0:
            errors["exists"]= "La Bodega ya Existe"

        return errors


class Warehouse(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WarehouseManager()
    #personals
    #orders_warehouse
    
    def __str__(self):
        return f"{self.name}"
    def __repr__(self):
        return f"{self.name}"


class PersonalManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['first_name']) < 3:
            errors['firstname_len'] = "El nombre debe tener al menos 3 caracteres de largo";

        if len(postData['last_name']) < 2:
            errors['lastname_len'] = " El Apellido debe tener al menos 2 caracteres de largo";

        
        if len(postData['position']) < 1:
            errors['position_len'] = " Tiene que completar Posicion";

        if len(postData['phone']) < 1:
            errors['position_len'] = " Tiene que completar Numero Telefonico";


        if not SOLO_LETRAS.match(postData['first_name']) or not SOLO_LETRAS.match(postData['last_name']):
            errors['solo_letras'] = "Solo letras en nombre y apellido porfavor"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Formato Correo invalido"
        
        if len(Personal.objects.filter(email=postData["email"])) > 0:
            errors["exists"]= "El correo ya existe"



        return errors


class Personal(models.Model):
    rut = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birdth_date = models.DateField()
    entry_date = models.DateField()
    position = models.CharField(max_length=45)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=200, unique=True)
    warehouse_work= models.ForeignKey(Warehouse, related_name='personals', blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PersonalManager()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def __repr__(self):
        return f"{self.first_name} {self.last_name}" 



class StateDeliveryManager(models.Manager):
    def validador_basico(self, postData):

        errors = {}

        return errors



class StateDelivery(models.Model):


    beetrack_state = models.CharField(max_length=70, choices=state, default="Inicial")
    beetrack_substate  = models.CharField(max_length=70, choices=sub_state, default="Inicial")
    beetrack_comment = models.TextField()
    date_return = models.DateField( blank=True, null=True, default="2021-01-01")
    dev_state = models.CharField(max_length=70, choices=sub_state, default="Inicial")
    dev_comment = models.TextField()
    dev_reason  = models.CharField(max_length=70, choices=reason, default="Inicial")
    dev_condition  = models.CharField(max_length=70, choices=condition, default="Inicial")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = StateDeliveryManager()
    def __str__(self):
        return f"{self.beetrack_state}"
    def __repr__(self):
        return f"{self.beetrack_state}"
    



class DeliveryOrderManager(models.Manager):
    def validador_basico(self, postData):

        errors = {}


        return errors


class DeliveryOrder(models.Model):
    company_delivery = models.ForeignKey(Company, related_name='orders_company', blank=True, null=True, on_delete=models.SET_NULL)
    warehouse_delivery = models.ForeignKey(Warehouse, related_name='orders_warehouse', blank=True, null=True, on_delete=models.SET_NULL)
    warehouse_origin = models.CharField(max_length=45)
    date_issue = models.DateField(blank=True, null=True)
    origin_order = models.CharField(max_length=45)
    order_number = models.CharField(max_length=45)
    ticket_number = models.CharField(max_length=45)
    type_order = models.CharField(max_length=45)
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    number_packager = models.IntegerField()
    sku = models.CharField(max_length=45)
    record = models.JSONField()
    state = models.ForeignKey(StateDelivery, related_name='states_delivery', blank=True, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='orders_user', blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DeliveryOrderManager()
    def __str__(self):
        return f"{self.order_number}"
    def __repr__(self):
        return f"{self.order_number}"
