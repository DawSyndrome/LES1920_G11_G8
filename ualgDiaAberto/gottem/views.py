from django.shortcuts import render


from django.shortcuts import redirect


from django.utils import timezone

from django.contrib.auth.models import BaseUserManager


from django.http import HttpResponse
from django.template import loader

from .models import Utilizador, GestoDePerfil

from django.contrib.auth import authenticate, login as django_login, logout as django_logout

from django.contrib.auth.hashers import check_password, make_password

from .forms import * #LoginForm, RegisterForm, ChangePasswordForm, NewPasswordForm, ResetPasswordForm


from django.urls import resolve
from django.urls import reverse

#############################################################################################################################
#############################################################LOG#############################################################
#############################################################################################################################

from django.forms.utils import ErrorList

def login(request):

	if(request.user.is_authenticated):
		return redirect('home')

	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(request, email_p=form.cleaned_data['user_email'], password_p=form.cleaned_data['user_password'])
			if user is not None:
				django_login(request, user, backend='utilizadores.backends.AuthBackend')
				return redirect('home')
			form.add_error("user_email", "Bad email-password combination.")

			template = loader.get_template("login_form.html")
			return HttpResponse(template.render({'form': form, 'post_redirect': reverse('login')}, request))
		else:
			template = loader.get_template("login_form.html")
			return HttpResponse(template.render({'form': form, 'post_redirect': reverse('login')}, request))
			#return HttpResponse("bade ting frend")
	else:
		form = LoginForm()
		template = loader.get_template("login_form.html")
		return HttpResponse(template.render({'form': form, 'post_redirect': reverse('login')}, request))




def logout(request):
	if request.user.is_authenticated:
		django_logout(request)
	return redirect('home')


from django.contrib.auth.models import Permission
def register(request):
	if request.user.is_authenticated:

		if (not request.user.is_admin() or request.user.is_coordenador()) or not request.user.validado == 1:
			print("thistheone " + str(request.user.is_coordenador()))
			return redirect('home');

		if request.method == 'POST':
			form = RegisterByEntity(request.POST)

			if not form.is_valid():
				template = loader.get_template("form.html")
				return HttpResponse(template.render({'form': form, 'post_redirect': reverse('register')}, request))

			newuser = Utilizador(
				nome=form.cleaned_data['name'],
				email=form.cleaned_data['email'],
				password=make_password(form.cleaned_data['password']),
				user_type=0,
				validado=0
			)



			newuser.save()
			return redirect('index');
		else:
			form = RegisterByEntity()
			template = loader.get_template("form.html")
			return HttpResponse(template.render({'form': form, 'post_redirect': reverse('register')}, request))


	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():

			############registo
			#perfil = GestoDePerfil(validação=0)
			#perfil.save()

			utilizador = Utilizador(
				nome=form.cleaned_data['name'],
				email=form.cleaned_data['email'],
				password=make_password(form.cleaned_data['password']),
				data_de_nascimento=form.cleaned_data['date_of_birth'],
				numero_telemovel=form.cleaned_data['cellphone_number'],
				deficiencias=form.cleaned_data['deficiencias'],
				departamentoid=form.cleaned_data['departamento'],
				unidade_orgânicaid=form.cleaned_data['departamento'].unidade_organicaid,
				user_type=form.cleaned_data['user_type'],
				validado=0,
				#check_in_state=0,
				#gestão_de_perfilid=perfil
			)
			utilizador.save()
			############

			if utilizador.is_admin():
				utilizador.user_permissions.set(Permission.objects.all())
			elif utilizador.is_coordenador():
				permission_list  = []
				permission_list.append(Permission.objects.get(name='Can add atividade'))
				permission_list.append(Permission.objects.get(name='Can view atividade'))
				permission_list.append(Permission.objects.get(name='Can change atividade'))
				permission_list.append(Permission.objects.get(name='Can delete atividade'))
				permission_list.append(Permission.objects.get(codename='validates_atividade'))
				permission_list.append(Permission.objects.get(codename='atribuir_local'))
				permission_list.append(Permission.objects.get(codename='alterar_local'))

				permission_list.append(Permission.objects.get(name='Can add tarefa'))
				permission_list.append(Permission.objects.get(name='Can view tarefa'))
				permission_list.append(Permission.objects.get(name='Can change tarefa'))
				permission_list.append(Permission.objects.get(name='Can delete tarefa'))
				permission_list.append(Permission.objects.get(codename='assign_tarefa'))
				permission_list.append(Permission.objects.get(codename='remove_colab_from_tarefa'))
				utilizador.user_permissions.set(permission_list)
			elif utilizador.is_docente():
				permission_list  = []
				permission_list.append(Permission.objects.get(name='Can add atividade'))
				permission_list.append(Permission.objects.get(name='Can view atividade'))
				permission_list.append(Permission.objects.get(name='Can change atividade'))
				permission_list.append(Permission.objects.get(name='Can delete atividade'))
				utilizador.user_permissions.set(permission_list)


			#return HttpResponse("registed this new user!")
			return redirect('login')
		else:
			template = loader.get_template("form.html")
			return HttpResponse(template.render({'form': form, 'post_redirect': reverse('register')}, request))
			#return HttpResponse("something wrong")
	else:
		form = RegisterForm()
		template = loader.get_template("form.html")
		return HttpResponse(template.render({'form': form, 'post_redirect': reverse('register')}, request))


##	perfil = GestoDePerfil(validação=0)
##	perfil.save()
##
##	utilizador = Utilizador(
##		email="hemayl@gai.come37",
##		nome="joseca37",
##		data_de_nascimento=timezone.now(),
##		numero_telemovel=919191919,
##		deficiencias="precisa de uma ajudinha para fazer algumas coisas pfv",
##		user_type=0,
##		validado=1,
##		check_in_state=0,
##		gestão_de_perfilid=perfil
##	)
##	utilizador.save()


#############################################################################################################################
#########################################################PASSWORD############################################################
#############################################################################################################################

def changpw(request):
	if not request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		form.user = request.user

		if form.is_valid():
			request.user.password = make_password(form.cleaned_data['new_pw'])
			request.user.save()
			return redirect('home')

		template = loader.get_template("form.html")
		return HttpResponse(template.render({'form': form, 'post_redirect': reverse('changpw')}, request))

	form = ChangePasswordForm()
	template = loader.get_template("form.html")
	return HttpResponse(template.render({'form': form, 'post_redirect': reverse('changpw')}, request))


from django.core.mail import send_mail
from time import time
from urllib.parse import quote, unquote
import random
import string
def resetpw(request, uid=0, token=None):
	user = None 

	###se o método é post temos 2 opções
	if request.method == 'POST':
		if request.user.is_authenticated:				##se tiver autenticado é porque já meteu o token certo, e submeteu agora o formulário para mudar a password
			form = NewPasswordForm(request.POST)
			if form.is_valid():							#se estiver válido metemos-lhe a password nova
				request.user.password = make_password(form.cleaned_data['new_pw'])
				request.user.save()
				django_login(request, request.user, backend='utilizadores.backends.AuthBackend')
				template = loader.get_template("message.html")
				return HttpResponse(template.render({'loc': reverse('home'), 'err_msg': 'New password set successfully!'}, request))

			template = loader.get_template("form.html")	#caso contrário apresentamos-lhe o formulário para ele mudar o que tá mal
			return HttpResponse(template.render({'form': form, 'post_redirect': reverse('resetpw')}, request))
		else:											##se não tiver autenticado é porque já submeteu o formulário com o email para o qual mandar o token
			form = ResetPasswordForm(request.POST)
			form.user_objects = Utilizador.objects
			if not form.is_valid():						#se não existir ou o email estiver inválido, repete o formulário
				template = loader.get_template("form.html")
				return HttpResponse(template.render({'form': form, 'post_redirect': reverse('resetpw')}, request))
			user = Utilizador.objects.get(email=form.cleaned_data['email'])


	###se não houver token e o user não estiver logado, mostra-se o formulário
	elif token is None and not request.user.is_authenticated:
		form = ResetPasswordForm()
		template = loader.get_template("form.html")
		return HttpResponse(template.render({'form': form, 'post_redirect': reverse('resetpw')}, request))

	elif token is None and request.user.is_authenticated:
			user = request.user

	###token é true e método é get : é obviamente um link de token (ou alguém a avacalhar)
	else:

		user = Utilizador.objects.get(id=uid)						##busca-se o user cujo id foi especificado
		if check_password(unquote(token), user.password_reset_url):	##e se o token estiver bem, loga-se o user e redirecionamos para ir meter a pass nova
			django_login(request, user, backend='utilizadores.backends.AuthBackend')
			form = NewPasswordForm()
			template = loader.get_template("form.html")
			return HttpResponse(template.render({'form': form, 'post_redirect': reverse('resetpw')}, request))

		else:									##caso contrário dizemos que o token expirou
			template = loader.get_template("message.html")
			return HttpResponse(template.render({'loc': reverse('resetpw'),'err_msg': 'Sorry, this link is no longer valid, perhaps you would like to request a new one?'}, request))




	reset_token = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
	reset_url = request.build_absolute_uri(reverse('resetpw_return', kwargs={'uid': user.id, 'token': quote(reset_token)}))
	user.password_reset_url = make_password(reset_token)
	user.save()

	send_mail(
	    'Password reset!',
	    'Here is your password reset URL: ' + reset_url,
	    'erfram@diaabertogottem.com',
	    [user.email],
	    fail_silently=False,
	)

	template = loader.get_template("message.html")
	return HttpResponse(template.render({'err_msg': 'An email has been sent to yourself good sir, continue from there.'}, request))
	#	user.password =


#############################################################################################################################
#########################################################CONSULTA############################################################
#############################################################################################################################


def index(request, page=0):

	if not ( request.user.is_authenticated and ( request.user.is_admin() or request.user.is_coordenador() ) and request.user.validado == 1 ):
		return redirect('home')


	
	filter_form = IndexForm(request.POST) if request.method == 'POST' else IndexForm()

	amount_per_page = 10
	paging_start = page*amount_per_page
	paging_end = paging_start+amount_per_page

	total_users = 0#Utilizador.objects.all().count()

	query_set = None
	if request.method == 'POST':
		filter_form.is_valid()
		query_set = Utilizador.objects.extra(where=['user_type & ' + str(filter_form.cleaned_data['flag']) + ' <> 0']).order_by('nome')
		total_users = query_set.count()
		query_set = query_set[paging_start:paging_end]
	else:
		query_set = Utilizador.objects.order_by('nome')
		total_users = query_set.count()
		query_set = query_set[paging_start:paging_end]
	query_result = list(query_set)

###	html = ""
###
###	for entry in query_result:
###		html += "NAME: " + entry.nome + " ;;; " + "EMAIL: " + entry.email + " ;;; " + "PHONE NR: " + str(entry.numero_telemovel) + "<br><br>"

	template = loader.get_template("user_management.html")
	template_context = {

		'me': request.user,

		'lista_de_utilizadores': query_result,

		'post_redirect': reverse("index"),
		'form': filter_form,


		'curr_page': page,
		'prev_page': None if page == 0 else {
			'path_name': "index" if (page == 1) else "index_paged",
			'param': page-1
		},
		'next_page': None if paging_end >= total_users else {
			'path_name': "index_paged",
			'param': page+1
		},
	}

	return HttpResponse(
		template.render(template_context, request)
	)



def edit_user(request, id):
	#return HttpResponse("hue" + str(id));
	if not request.user.is_authenticated or not ( request.user.is_admin() or request.user.is_coordenador() ) or not request.user.validado == 1:
		return redirect('home')

	user = Utilizador.objects.filter(id=id).first()

	if user is None:
		template = loader.get_template("message.html")
		return HttpResponse(template.render({
			'me': request.user,

			'back': 'javascript: history.go(-1)',
			'err_msg': 'The user you\'re trying to edit no longer exists.'
		}, request))

	if (user.is_admin() and not request.user.is_admin()) or request.user.validado != 1:
		template = loader.get_template("message.html")
		return HttpResponse(template.render({
			'me': request.user,

			'back': 'javascript: history.go(-1)',
			'err_msg': 'You do not have permission to edit this user.'
		}, request))


	if request.method == 'POST':
		#if form.user_type & Utilizador.USER_TYPES.Administrador != 0 and not request.user

		form = EditUser(request.POST, instance=user);
		form.save()
		return redirect("index");

	form = EditUser(instance=user)
	template = loader.get_template("form.html")
	return HttpResponse(template.render({'form': form, 'post_redirect': reverse('edit_user', args=[id])}, request))

	return HttpResponse("hue" + str(id));


def validate_user(request, id):
	if not request.user.is_authenticated or not ( request.user.is_admin() or request.user.is_coordenador() ) or not request.user.validado == 1:
		return redirect('home')

	user = Utilizador.objects.filter(id=id).first()

	if user is None:
		template = loader.get_template("message.html")
		return HttpResponse(template.render({
			'me': request.user,

			'back': 'javascript: history.go(-1)',
			'err_msg': 'The user you\'re trying to validate no longer exists.'
		}, request))

	if (user.is_admin() and not request.user.is_admin()) or request.user.validado != 1:
		template = loader.get_template("message.html")
		return HttpResponse(template.render({
			'me': request.user,

			'back': 'javascript: history.go(-1)',
			'err_msg': 'You do not have permission to validate this user.'
		}, request))

	user.validado = 1;
	user.save()

	return redirect('index');



def delete_user(request, id):
	if not request.user.is_authenticated or not ( request.user.is_admin() or request.user.is_coordenador() ) or not request.user.validado == 1:
		return redirect('home')


	user = Utilizador.objects.filter(id=id).first()

	if user is None:
		template = loader.get_template("message.html")
		return HttpResponse(template.render({
			'me': request.user,

			'back': 'javascript: history.go(-1)',
			'err_msg': 'The user you\'re attempting to delete no longer exists.'
		}, request))

	if (user.is_admin() and not request.user.is_admin()) or request.user.validado != 1:
		template = loader.get_template("message.html")
		return HttpResponse(template.render({
			'me': request.user,

			'back': 'javascript: history.go(-1)',
			'err_msg': 'You do not have permission to delete this user.'
		}, request))

	if resolve(request.path_info).url_name == "delete_user_confirm":
		user.delete()
		return redirect(
			'index'
		)

	#if id == request.user.id:
	#	return HttpResponse("You cannot erase your own user!!!!!!!!!!!!!")

	template = loader.get_template("message.html")
	return HttpResponse(template.render({
		'me': request.user,

		'back': 'javascript: history.go(-1)',
		'loc': reverse('delete_user_confirm', args=[id]),
		'err_msg': 'Do you really want to delete ' + Utilizador.objects.get(id=id).nome + '?'
	}, request))









#############################################################################################################################
############################################################HOME#############################################################
#############################################################################################################################

def home(request):
	template = loader.get_template("Home.html")
	return HttpResponse(template.render({}, request))


###################################################################
############# Diogo Lobo - Notificacoes ###########################
###################################################################

def notificacoes(request):
	if not request.user.is_authenticated:
		return redirect('home')
	return render(request,
                  "main/notificacoes.html")


def notificacoesRecebidas(request):
	if not (request.user.is_authenticated):
		return redirect('home')

	notf = Notificacao.objects.all()
	info = list(Notificacao.objects.filter(utilizadorid_recebe=request.user.id))

	return render(request,
                  "main/notificacoesRcb.html",
                  {"notificacoes": notf, "info": info})

def notificacoesEnviadas(request):
	if not (request.user.is_authenticated):
		return redirect('home')

	if (request.user.is_admin() or request.user.is_coordenador() or request.user.is_docente() or request.user.user_type == 2 ):
		notf = Notificacao.objects.all()
		info = list(Notificacao.objects.filter(utilizadorid_envia=request.user.id))

		return render(request,
                  "main/notificacoesEnv.html",
                  {"notificacoes": notf, "info": info})



def createNotf(request):
	if not (request.user.is_authenticated):
		return redirect('home')
	if request.method == 'POST':
		form = NotificationForm(request.POST, uid=request.user.id, utype=request.user.user_type)
		if form.is_valid():
			notificacao = Notificacao(
				utilizadorid_envia=Utilizador.objects.get(id=request.user.id),
				utilizadorid_recebe=form.cleaned_data['utilizadorid_recebe'],
				assunto=form.cleaned_data['assunto'],
				conteudo=form.cleaned_data['conteudo'],
				prioridade=form.cleaned_data['prioridade'],
			)
			notificacao.save()

			return redirect('home')
		else:
			return render(request,
							"main/enviarnotf.html",
							messages.error(request, f"Necessário Preencher Todos Os Campos"))
	else:
		form = NotificationForm(uid=request.user.id, utype=request.user.user_type)
		return render(request,
						"main/enviarnotf.html",
    					{'form': form.as_ul})


def deleteNotfRecebida(request, pk):
    Notificacao.objects.filter(id=pk).delete()
    return redirect("notificacoesRcb")


def deleteNotfEnviada(request, pk):
	if (request.user.is_admin() or request.user.is_coordenador() or request.user.is_docente()):
		Notificacao.objects.filter(id=pk).delete()
		return redirect("notificacoesEnv")
