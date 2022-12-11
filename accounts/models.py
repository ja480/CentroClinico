import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)

class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(
        'Usuario', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'User not valid. '
                'Este campo debe contener letras, números '
                'y los siguientes carácteres: @/./+/-/_.'
                ,  'invalid'
            )
        ], help_text='Nombre corto que se utilizara'+
                    ' para indentificarse de manera unica en la plataforma.'
    )
    
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Equipo', default=False)
    is_active = models.BooleanField('Activo', default=True)
    date_joined = models.DateTimeField('Dia de Entrada', auto_now_add=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.name or self.username
    
    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(' ')[0]