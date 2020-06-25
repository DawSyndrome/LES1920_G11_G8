from django.contrib import admin

from .models import Transporte, Ementa, HorarioTransporte, Rota

# Register your models here.

admin.site.register(Transporte)
admin.site.register(HorarioTransporte)
admin.site.register(Rota)
admin.site.register(Ementa)
