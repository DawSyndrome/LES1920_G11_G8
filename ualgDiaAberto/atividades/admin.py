from django.contrib import admin

from .models import Edificio, Campus, Departamento, Local, Atividade

# Register your models here.

admin.site.register(Edificio)
admin.site.register(Campus)
admin.site.register(Departamento)
admin.site.register(Local)
admin.site.register(Atividade)
