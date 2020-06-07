import django_filters

from django_filters import DateFilter, CharFilter

from .models import *

class UnidadeOrganicaFilter(django_filters.FilterSet):
	class Meta:
		model = UnidadeOrganica
		fields = '__all__'

class DepartamentoFilter(django_filters.FilterSet):
	class Meta:
		model = Departamento
		fields = '__all__'

class LocalFilter(django_filters.FilterSet):
	class Meta:
		model = Local
		fields = ['edicifioid' ,'campusid']

class CampusFilter(django_filters.FilterSet):
	class Meta:
		model = Campus
		fields = '__all__'

class EdificioFilter(django_filters.FilterSet):
	nome_edificio = CharFilter(field_name='nome_edificio', lookup_expr='icontains')
	campusid__nome = CharFilter(field_name='campusid', lookup_expr='icontains')
	class Meta:
		model = Edificio
		fields = ['nome_edificio' ,'campusid__nome']