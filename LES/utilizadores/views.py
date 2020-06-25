from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader

from .models import Utilizador

from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.hashers import check_password, make_password

from .forms import LoginForm, RegisterForm

def login(request):
	
	##print("PASSWORD_MADE: " + str(make_password("kaputaze")))
	##print("PASSWORD_CHECK: " + str(check_password("kaputaze", str(make_password("kaputaze")))))
	if(request.user.is_authenticated):
		#return HttpResponse("You are alredi logged in mayte! WOOOT")
		return redirect('diaAbertoConf:index')

	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(request, email_p=form.cleaned_data['user_email'], password_p=form.cleaned_data['user_password'])
			if user is not None:
				django_login(request, user)
				return redirect('diaAbertoConf:index')

			return render(request, 'utilizadores/login.html' ,{'form': form.as_p, 'post_redirect': 'login'})
			#return HttpResponse("veri good frend" + " " + ("bigus dadas" if user is not None else "ah shitfuck"))
		else:
			return HttpResponse("bade ting frend")
	else:
		form = LoginForm()
		#template = loader.get_template("login.html")
		#return HttpResponse(template.render({'form': form.as_p, 'post_redirect': 'login'}, request))
		return render(request, 'utilizadores/login.html' ,{'form': form.as_p, 'post_redirect': 'login'})




def logout(request):
	if request.user.is_authenticated:
		django_logout(request)

		#return HttpResponse("you have been logged out!")
	#return HttpResponse("you weren't logged in in the first place mate uwot")
	return redirect('diaAbertoConf:index')



def register(request):
	if request.user.is_authenticated:
		return HttpResponse("you cannot register because you are already logged in, soz homie")

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			############registo
			#perfil = GestoDePerfil(validação=0)
			perfil.save()

			utilizador = Utilizador(
				nome=form.cleaned_data['name'],
				email=form.cleaned_data['email'],
				password=make_password(form.cleaned_data['password']),
				data_de_nascimento=form.cleaned_data['date_of_birth'],
				numero_telemovel=form.cleaned_data['cellphone_number'],
				deficiencias=form.cleaned_data['deficiencias'],
				user_type=str(form.cleaned_data['user_type']),
				validado=0,
				check_in_state=0,
				gestão_de_perfilid=perfil
			)
			utilizador.save()

			return HttpResponse("registed this new user!")
		else:
			return HttpResponse("something wrong")
	else:
		form = RegisterForm()
		template = loader.get_template("login.html")
		return HttpResponse(template.render({'form': form.as_p, 'post_redirect': 'register'}, request))

