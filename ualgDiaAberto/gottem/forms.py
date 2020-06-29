from django import forms

from .models import *

from django.db.models import Q

from django.forms import ModelForm

class CustomModelChoiceField(forms.ModelChoiceField):
	name_function = staticmethod(lambda obj: obj)

	def __init__(self, name_function, *args, **kwargs):
		if not name_function is None: self.name_function = name_function
		super(CustomModelChoiceField, self).__init__(*args, **kwargs)

	def label_from_instance(self, obj):
         return self.name_function(obj);



class IndexForm(forms.Form):
	admin = forms.BooleanField(			label='Administrador', 	initial=True, required=False)
	participante = forms.BooleanField(	label='Participante', 	initial=True, required=False)
	docente = forms.BooleanField(		label='Docente', 		initial=True, required=False)
	colaborador = forms.BooleanField(	label='Colaborador', 	initial=True, required=False)
	coordenador = forms.BooleanField(	label='Coordenador', 	initial=True, required=False)

	def clean(self):
		cleaned_data = super(IndexForm, self).clean()

		admin 		 = Utilizador.USER_TYPES.Administrador 	if cleaned_data.get("admin")	 	else 0
		participante = Utilizador.USER_TYPES.Participante 	if cleaned_data.get("participante") else 0
		docente 	 = Utilizador.USER_TYPES.Docente 		if cleaned_data.get("docente")	 	else 0
		colaborador  = Utilizador.USER_TYPES.Colaborador 	if cleaned_data.get("colaborador") 	else 0
		coordenador  = Utilizador.USER_TYPES.Coordenador 	if cleaned_data.get("coordenador") 	else 0

		self.cleaned_data['flag'] = admin | participante | docente | colaborador | coordenador


class LoginForm(forms.Form):

	user_email = forms.EmailField(label='Your Email')
	user_password = forms.CharField(label='Your Password', widget=forms.PasswordInput)
	#user_password_confirm = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

	#def clean(self):
	#	cleaned_data = super(LoginForm, self).clean()
	#	password = cleaned_data.get("user_password")
	#	confirm_password = cleaned_data.get("user_password_confirm")
	#
	#	if password != confirm_password:
	#		raise forms.ValidationError({
	#			'user_password_confirm': "This password doesn't match with the other one."
	#		})

class ResetPasswordForm(forms.Form):

	email = forms.EmailField(label='Your Email')

class RegisterForm(forms.Form):

	name = forms.CharField(label='Your Name')

	email = forms.EmailField(label='Your Email')
	confirm_email = forms.EmailField(label='Confirm Your Email')

	password = forms.CharField(label='Your Password', widget=forms.PasswordInput)
	confirm_password = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

	date_of_birth = forms.DateField(label='Your Date Of Birth', widget=forms.DateInput)

	cellphone_number = forms.IntegerField(label='Your Phone Number')

	departamento = CustomModelChoiceField(
		lambda obj: obj.unidade_organicaid.nome + ", Departamento de " + obj.nome,
		required=True,
		queryset=Departamento.objects.all().order_by("unidade_organicaid__nome"),
	)

	deficiencias = forms.CharField(label='Deficiências ou Problemas de Saude')


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
			raise forms.ValidationError({
				'confirm_password': "This password doesn't match with the other one."
			})
		if email != confirm_email:
			raise forms.ValidationError({
				'confirm_email': "This password doesn't match with the other one."
			})

		checkboxes = self.cleaned_data['user_type']
		final_usertype_bitfield = 0
		for val in checkboxes:
			final_usertype_bitfield |= int(val)
		self.cleaned_data['user_type'] = final_usertype_bitfield

class RegisterByEntity(forms.Form):
	name = forms.CharField(label='User\'s name')
	email = email = forms.EmailField(label='User\'s Email')
	password = forms.CharField(label='User\'s Password', widget=forms.PasswordInput)

class ChangePasswordForm(forms.Form):

	new_pw = forms.CharField(label='Your New Password', widget=forms.PasswordInput)
	new_pw_confirm = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)
	old_pw = forms.CharField(label='Your Old Password', widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(ChangePasswordForm, self).clean()

		new_password = cleaned_data.get("new_pw")
		confirm_new_password = cleaned_data.get("new_pw_confirm")
		old_password = cleaned_data.get("old_pw")

		if new_password != confirm_new_password:
			raise forms.ValidationError({
				'new_pw_confirm': "This password doesn't match with the other one."
			})

		if not self.user.check_password(old_password):
			raise forms.ValidationError({
				'old_pw': "Invalid password."
			})

class ResetPasswordForm(forms.Form):
	email = forms.EmailField(label='Your Email')

	def clean(self):
		cleaned_data = super(ResetPasswordForm, self).clean()
		if not self.user_objects.filter(email=cleaned_data.get('email')).exists():
			raise forms.ValidationError({
				'email': "This email doesn't exist."
			})

class NewPasswordForm(forms.Form):
	new_pw = forms.CharField(label='Your New Password', widget=forms.PasswordInput)
	new_pw_confirm = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(NewPasswordForm, self).clean()

		new_password = cleaned_data.get("new_pw")
		confirm_new_password = cleaned_data.get("new_pw_confirm")

		if new_password != confirm_new_password:
			raise forms.ValidationError({
				'new_pw_confirm': "This password doesn't match with the other one."
			})



class EditUser(ModelForm):
	unidade_orgânicaid = CustomModelChoiceField(
		lambda obj: obj.nome,
		required=False,
		queryset=UnidadeOrganica.objects.all(),
	)

	departamentoid = CustomModelChoiceField(
		lambda obj: obj.nome,
		required=False,
		queryset=Departamento.objects.all(),
	)

	registo_horárioid = CustomModelChoiceField(
		lambda obj: str(obj.hora_inicio) + " -> " + str(obj.hora_fim) + " : " + str(obj.data),
		required=False,
		queryset=RegistoHorrio.objects.all(),
	)


	class Meta:
		model = Utilizador
		fields = [
			'nome',
			'email',
			'validado',
			'numero_telemovel',
			'cartão_cidadão',
			'data_de_nascimento',
			'deficiencias',

			'unidade_orgânicaid',
			'departamentoid',
			'registo_horárioid',
		]

###################################################################
############# Diogo Lobo - Notificacoes ###########################
###################################################################

## CABULA DE FILTROS ##
## Admin - Envia a Toda a Gente ##
## Coordenador - Envia a Toda a Gente Menos Participantes ##
## Docente - Só envia a colaboradores ##
## Colaborador - Só envia a coordenadores ##
## Participante - Só recebe ##

class NotificationForm(forms.Form):

    conteudo = forms.CharField(label='Conteúdo', widget=forms.Textarea, required=True)

    utilizadorid_recebe = forms.ModelChoiceField(label='Enviar Para:',
                                                 required=True,
                                                 queryset=Utilizador.objects.all())

    CHOICES1 = (
        ('Alteração de Data', 'Alteração de Data'),
        ('Novas Vagas', 'Novas Vagas'),
        ('Cancelamento da Atividade', 'Cancelamento da Atividade'),
        ('Outro', 'Outro'),
    )

    assunto = forms.ChoiceField(label='Assunto', widget=forms.Select, required=True, choices=CHOICES1)

    CHOICES2 = (
        ('1', '1 - Urgente'),
        ('2', '2 - Aviso'),
        ('3', '3 - Lembrete'),
    )
    prioridade = forms.ChoiceField(label='Prioridade', widget=forms.Select, required=True, choices=CHOICES2)

    def __init__(self, *args, **kwargs):
        iduser = kwargs.pop('uid')
        typeuser = kwargs.pop('utype')
        uni_org = kwargs.pop('uniorg')
        super(NotificationForm, self).__init__(*args, **kwargs)
        if (typeuser == 16):#Admin
        	self.fields['utilizadorid_recebe'] = forms.ModelChoiceField(label='Enviar Para:', required=True,
				queryset=Utilizador.objects.exclude(id=iduser))
        if (typeuser == 4): #Docente
        	self.fields['utilizadorid_recebe'] = forms.ModelChoiceField(label='Enviar Para:', required=True,
				queryset=Utilizador.objects.filter((Q(user_type=1) & Q(unidade_orgânicaid=uni_org)) | Q(user_type=2)))
        if (typeuser == 1): #Coordenador
        	self.fields['utilizadorid_recebe'] = forms.ModelChoiceField(label='Enviar Para:', required=True,
				queryset=Utilizador.objects.filter(Q(user_type=1) | Q(user_type=2) | (Q(user_type=4) & Q(unidade_orgânicaid=uni_org)) | Q(user_type=16)).exclude(id=iduser))
        if (typeuser == 2): #Colaborador
        	self.fields['utilizadorid_recebe'] = forms.ModelChoiceField(label='Enviar Para:', required=True,
				queryset=Utilizador.objects.filter(user_type=1).filter(unidade_orgânicaid=uni_org))
        if (typeuser == 8): #Participante
        	self.fields['utilizadorid_recebe'] = forms.ModelChoiceField(label='Enviar Para:', required=True,
				queryset=Utilizador.objects.filter(user_type=16))
