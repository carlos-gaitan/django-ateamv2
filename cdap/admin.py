from django.contrib import admin

# Register your models here.
from .models import Locacion, Empresa, Persona

admin.site.register(Locacion)
admin.site.register(Empresa)
admin.site.register(Persona)
