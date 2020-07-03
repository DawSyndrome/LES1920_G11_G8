from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Select, Textarea, modelformset_factory, formset_factory 
from .models import Participanteinfo, HorarioTransporte, Utilizador, Escola,  UtilizadorAtividade, Transporte, Ementa, Edificio, Campus, Departamento, Local, Atividade, UnidadeOrganica, Tematica, Material, AtividadeTematica, AtividadeMaterial, SessaoAtividade, Sessao

from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils.safestring import mark_safe

from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple, AdminDateWidget
from django.core.validators import MaxValueValidator




class RegisterCol(forms.ModelForm):

	ano_escolar = forms.IntegerField(required=True, max_value=12, min_value=1, widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "1"}))  #forms.IntegerField(label='Ano Escolar')
	turma = forms.CharField(label='Turma')
	area = forms.CharField(label='Area')
	total_de_participantes = forms.IntegerField(label='Quantos alunos pretende inscrever?', required=True, min_value=1, widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "1"}))  #forms.IntegerField(label='Quantos alunos pretende inscrever?')
	total_de_professores = forms.IntegerField(label='Quantos professores pretende que estejam presentes nas atividades?', required=True, max_value=12, min_value=1, widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "1"}))  #forms.IntegerField(label='Quantos professores pretende que estejam presentes nas atividades?')

	def clean(self):
		cleaned_data = super(RegisterCol, self).clean()

	class Meta:
		model = Participanteinfo
		fields = ('ano_escolar',
				  'turma',
				  'area',
				  'total_de_participantes',
				  'total_de_professores' )

		#Participanteinfo.utilizadorid = Utilizador.objects.get(id=1)
		
		#Participanteinfo.checkin_state = 1
		
		#if commit:
		#	Participanteinfo.save()
		#return Participanteinfo


class RegisterIndiv(forms.ModelForm):

	numero_telemovel = forms.IntegerField(validators=[MaxValueValidator(999999999)], required=True, widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "1"}))  
	cartão_cidadão = forms.IntegerField(validators=[MaxValueValidator(99999999)], required=True, widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "1"}))
	data_de_nascimento = forms.DateField()

	def clean(self):
		cleaned_data = super(RegisterIndiv, self).clean()

	class Meta:
		model = Utilizador
		fields = ('numero_telemovel',
				  'cartão_cidadão',
				  'data_de_nascimento')



class RegisterSchool(forms.ModelForm):

	nome = forms.CharField(label='Nome')
	localidade = forms.CharField(label='Localidade')

	def clean(self):
		cleaned_data = super(RegisterSchool, self).clean()

	class Meta:
		model = Escola
		fields = ('nome',
				  'localidade' )


class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def __init__(self, attrs=None):
        super(CustomCheckboxSelectMultiple, self).__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = super(CustomCheckboxSelectMultiple, self).render(name, value, attrs)

        style = self.attrs.get('style', None)
        if style:
            output = output.replace("<ul", format_html('<ul style="{0}"', style))

        return mark_safe(output)



class RegisterAtividades(forms.ModelForm):
    atividadeid = forms.ModelMultipleChoiceField(
                            queryset=Atividade.objects.all(),#Atividade.objects.filter(id=Atividade.objects.all().values('id')),
                            required=False,
                            widget=CustomCheckboxSelectMultiple)

    class Meta:
        model = UtilizadorAtividade
        fields = ('atividadeid',)

    def clean(self):
    	cleaned_data = super(RegisterAtividades, self).clean()





class TimePickerWidget(forms.TimeInput):                                                  
	def render(self, name, value, attrs=None, renderer=None):                                                
	    htmlString = u''                                                                      
	    htmlString += u'<select name="%s">' % (name)                                          
	    for i in range(24):                                                               
	            htmlString += ('<option value="%d:00">%d:00</option>' % (i,i))          
	    htmlString +='</select>'                                                              
	    return mark_safe(u''.join(htmlString))


class RegisterTransporte(forms.ModelForm):

	CHOICES = [
		('Autocarro próprio', "Autocarro Próprio"),
		('Comboio', "Comboio"),
		('Pedir à Universidade', "Pedir à Universidade"),
		('Outro', "Outro")]

	tipo_transporte = forms.ChoiceField(label='Meio de Transporte', required=True, choices=BLANK_CHOICE_DASH+CHOICES, widget=forms.Select())

	def clean(self):
		cleaned_data = super(RegisterTransporte, self).clean()

	class Meta:
		model = Transporte
		fields = ('tipo_transporte',)


class RegisterHorario(forms.ModelForm):

	hora_de_chegada = forms.TimeField(widget=TimePickerWidget(format='%I:%M %p')) #forms.DateField(label='Hora de Chegada')
	hora_de_partida = forms.TimeField(widget=TimePickerWidget(format='%I:%M %p')) #forms.DateField(label='Hora de Partida')

	def clean(self):
		cleaned_data = super(RegisterHorario, self).clean()

	class Meta:
		model = HorarioTransporte
		fields = ('hora_de_chegada',
				  'hora_de_partida')




class RegisterAlmocos(forms.ModelForm):
	CHOICES = [
		('Gambelas', "Gambelas"),
		('Penha', "Penha")]

	preco_normal = forms.FloatField(required=False, max_value=30, min_value=0, widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "1"}))  #forms.FloatField(label='Preço Normal Aluno (2,80€)')
	preco_economico = forms.FloatField(required=False, max_value=30, min_value=0, widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "1"}))  #forms.IntegerField(label='Preço Economico Aluno (2,00€)')
	preco_outro = forms.FloatField(required=False, max_value=30, min_value=0, widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "1"}))  #forms.FloatField(label='Preço Normal Outro (4,25€)')
	preco_economico_outro = forms.FloatField(required=False, max_value=30, min_value=0, widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "1"}))  #forms.FloatField(label='Preço Economico Outro (3,50€)')

	def clean(self):
		cleaned_data = super(RegisterAlmocos, self).clean()

	class Meta:
		model = Ementa
		fields = ('preco_normal',
				  'preco_economico',
				  'preco_outro',
				  'preco_economico_outro',)





class RegisterForm(forms.Form): # user registration
	name = forms.CharField(label='Your Name')

	email = forms.EmailField(label='Your Email')
	confirm_email = forms.EmailField(label='Confirm Your Email')

	password = forms.CharField(label='Your Password', widget=forms.PasswordInput)
	confirm_password = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

	date_of_birth = forms.DateField(label='Your Date Of Birth', widget=forms.DateInput)

	cellphone_number = forms.IntegerField(label='Your Phone Number')

	deficiencias = forms.CharField(label='Algumas Deficiências ou Problemas de Saude que Possa Ter')


	CHOICES = [
		(0b10000, "Administrador"),
		(0b01000, "Participante"),
		(0b00100, "Docente"),
		(0b00010, "Colaborador"),
		(0b00001, "Coordenador")
	]
	user_type = forms.MultipleChoiceField(label='A Que Roles Pertence?', required=True, choices=CHOICES, widget=forms.CheckboxSelectMultiple)

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()

		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")

		email = cleaned_data.get("email")
		confirm_email = cleaned_data.get("confirm_email")

		if password != confirm_password:
			raise forms.ValidationError(
				"password and confirm_password does not match"
			)
		if email != confirm_email:
			raise forms.ValidationError(
				"email and confirm_email does not match"
			)

		checkboxes = self.cleaned_data['user_type']
		final_usertype_bitfield = 0
		for val in checkboxes:
			final_usertype_bitfield |= int(val)
		self.cleaned_data['user_type'] = final_usertype_bitfield






class LoginForm(forms.Form):
	user_email = forms.EmailField(label='Your Email')
	user_password = forms.CharField(label='Your Password', widget=forms.PasswordInput)
	user_password_confirm = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		password = cleaned_data.get("user_password")
		confirm_password = cleaned_data.get("user_password_confirm")

		if password != confirm_password:
			raise forms.ValidationError(
				"password and confirm_password does not match"
			)
