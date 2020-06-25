import django_filters

from django_filters import DateFilter, CharFilter, NumberFilter, TimeFilter, BooleanFilter

from .models import *

class UnidadeOrganicaFilter(django_filters.FilterSet):
	nome = CharFilter(field_name='nome', lookup_expr='icontains')
	class Meta:
		model = UnidadeOrganica
		fields = '__all__'

class DepartamentoFilter(django_filters.FilterSet):
	nome = CharFilter(field_name='nome', lookup_expr='icontains')
	unidade_organicaid__nome = CharFilter(field_name='unidade_organicaid__nome', lookup_expr='icontains')
	class Meta:
		model = Departamento
		fields = '__all__'

class LocalFilter(django_filters.FilterSet):
	edicifioid__nome_edificio = CharFilter(field_name='edicifioid__nome_edificio', lookup_expr='icontains')
	campusid__nome = CharFilter(field_name='campusid__nome', lookup_expr='icontains')
	indoor = BooleanFilter(field_name='indoor')
	class Meta:
		model = Local
		fields = ['edicifioid' ,'campusid', 'indoor']

class CampusFilter(django_filters.FilterSet):
	nome = CharFilter(field_name='nome', lookup_expr='icontains')
	localizacao = CharFilter(field_name='localizacao', lookup_expr='icontains')
	class Meta:
		model = Campus
		fields = '__all__'

class EdificioFilter(django_filters.FilterSet):
	nome_edificio = CharFilter(field_name='nome_edificio', lookup_expr='icontains')
	campusid__nome = CharFilter(field_name='campusid__nome', lookup_expr='icontains')
	class Meta:
		model = Edificio
		fields = ['nome_edificio' ,'campusid__nome']

class TematicaFilter(django_filters.FilterSet):
	nome = CharFilter(field_name='nome', lookup_expr='icontains')
	class Meta:
		model = Tematica
		fields = '__all__'

class MaterialFilter(django_filters.FilterSet):
	nome = CharFilter(field_name='nome', lookup_expr='icontains')
	class Meta:
		model = Material
		fields = '__all__'

class AtividadeFilter(django_filters.FilterSet):
	nome = CharFilter(field_name='nome', lookup_expr='icontains')
	tipo_atividade = CharFilter(field_name='tipo_atividade')
	validada = NumberFilter(field_name='validada')
	localcampus = CharFilter(field_name='localid__campusid')
	localedicifio = CharFilter(field_name='localid__edicifioid')
	data = DateFilter(field_name="sessaoatividade__data", distinct=True)
	sessao_gte = TimeFilter(field_name="sessaoatividade__sessaoid__hora_de_inicio", lookup_expr='gte', distinct=True)
	sessao_lte = TimeFilter(field_name="sessaoatividade__sessaoid__hora_de_inicio", lookup_expr='lte', distinct=True)
	class Meta:
		model = Atividade
		fields = '__all__'

class SessaoFilter(django_filters.FilterSet):
	sessao_gte = TimeFilter(field_name="hora_de_inicio", lookup_expr='gte')
	sessao_lte = TimeFilter(field_name="hora_de_inicio", lookup_expr='lte')
	class Meta:
		model = Sessao
		fields = '__all__'