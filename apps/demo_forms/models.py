from django.db import models

import re

from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

MIN_FIELD_LENGHT = 6

def ValidarLongitudMinima(cadena):
    if len(cadena) < MIN_FIELD_LENGHT:
        raise ValidationError(
            f"{cadena} tiene deberia tener mas de {MIN_FIELD_LENGHT} caracteres"
        )

def ValidarEmail(cadena):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(cadena):  
        raise ValidationError(
            f'{cadena} no es un e-mail valido'
        )

class User(models.Model):
    name = models.CharField(max_length=45, blank = False, null =False, validators=[ValidarLongitudMinima])
    lastname = models.CharField(max_length=45, blank = True, null =True)
    email = models.CharField(max_length=50, validators=[ValidarEmail])
    password = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password) 
        super(User, self).save(*args, **kwargs)

    @staticmethod
    def authenticate(email, password):
        user = User.objects.filter(email = email)
        print ('user: ', user)
        if len(user) == 1:
            user = user[0]
            bd_password = user.password
            if check_password(password, bd_password):
                return user
        return None 


class Hobbie(models.Model):
    name = models.CharField(max_length=45)
    # 1. exterior, 2. interior, 3.ambos
    tipo = models.PositiveSmallIntegerField(
        validators = [
            validators.MinValueValidator(1, 'Debe selecionar un valor valido'),
            validators.MaxValueValidator(3)]
    )        
