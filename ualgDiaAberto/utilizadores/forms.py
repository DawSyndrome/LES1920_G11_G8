from django import forms

class LoginForm(forms.Form):
	user_email = forms.EmailField(label='Your Email')
	user_password = forms.CharField(label='Your Password', widget=forms.PasswordInput)
	#user_password_confirm = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

	""" def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		password = cleaned_data.get("user_password")
		confirm_password = cleaned_data.get("user_password_confirm")

		if password != confirm_password:
			raise forms.ValidationError(
				"password and confirm_password does not match"
			) """

class RegisterForm(forms.Form):
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
 
