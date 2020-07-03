from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.contrib.auth.hashers import check_password, make_password
from .models import HorarioTransporte,Participanteinfo, Utilizador, UtilizadorAtividade, GestoDePerfil, Atividade, Inscricao, Escola, Transporte, UtilizadorTransporte, Ementa, UtilizadorEmenta, InscrioEmenta, Local, UnidadeOrganica, Campus, Departamento, Sessao, SessaoAtividade, SessaoAtividadeInscricao, Tarefa, Edificio
from .forms import RegisterCol, LoginForm, RegisterIndiv, RegisterForm, RegisterSchool, RegisterTransporte, RegisterAlmocos, RegisterHorario
from django.views.decorators.http import require_http_methods
from django.forms import ModelForm
from django.db import connection
from django.contrib import messages

from ualgDiaAberto.settings import TABLE_JSON

import json
import sys
from datetime import datetime, timedelta
from time import sleep


def register_col(request):  # make a collective register form

	if  request.user.is_authenticated:

		if request.method == 'POST':
			form = RegisterCol(request.POST)
			form1 = RegisterSchool(request.POST)
			form2 = RegisterTransporte(request.POST)
			form3 = RegisterAlmocos(request.POST)
			form4 = RegisterHorario(request.POST)

			if form1.is_valid() and form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():

				escola = Escola(
					nome=form1.cleaned_data['nome'],
					localidade=form1.cleaned_data['localidade'],
				)
				escola.save()

				transporte = Transporte(
					tipo_transporte=form2.cleaned_data['tipo_transporte'],
				)
				transporte.save()

				hora_transporte = HorarioTransporte(

					hora_de_chegada=form4.cleaned_data['hora_de_chegada'],
					hora_de_partida=form4.cleaned_data['hora_de_partida'],
				)
				hora_transporte.save()

				utilizador_transporte = UtilizadorTransporte(
					utilizadorid=request.user,
					transporteid=transporte,
				)
				utilizador_transporte.save()

				ementa = Ementa(
					preco_normal=form3.cleaned_data['preco_normal'],
					preco_economico=form3.cleaned_data['preco_economico'],
    				preco_outro=form3.cleaned_data['preco_outro'],
    				preco_economico_outro=form3.cleaned_data['preco_economico_outro'],
				)
				ementa.save()

				utilizador_ementa = UtilizadorEmenta(
					utilizadorid=request.user,
					ementaid=ementa,
				)
				utilizador_ementa.save()

				participanteinfo = Participanteinfo(
					ano_escolar=form.cleaned_data['ano_escolar'],
					turma=form.cleaned_data['turma'],
					area=form.cleaned_data['area'],
					total_de_participantes=form.cleaned_data['total_de_participantes'],
					total_de_professores=form.cleaned_data['total_de_professores'],
					utilizadorid=request.user, #request.session.get('user')
					checkin_state=0,
					participante_type=2
				)
				participanteinfo.save();

				inscrio = Inscricao(
					escolaid=escola,
				)
				inscrio.save()
	
				inscrio_ementa = InscrioEmenta(
					inscriçãoid = inscrio,
					ementaid = ementa,
				)
				inscrio_ementa.save()

				user_atual = Utilizador.objects.get(id=request.user.id)
				user_atual.inscriçãoid = inscrio
				user_atual.save()


				all_data = request.POST.get("all_data")

				print(all_data)
				print(type(all_data))
				json_content = json.loads(all_data)

				print(json_content)

				

				c = connection.cursor()

        #query = "SELECT `id` FROM `inscricao` ORDER BY `id` DESC LIMIT 1"
        #c.execute(query)
        #last_id = c.fetchone()
				inscricao_last_id = inscrio.id

				for item in json_content:
					session_id=item['session_id']
					activity_id=item['activity_id']

					#sess_at = c.execute("SELECT ID FROM `sessão-atividade` WHERE SessãoID = 'session_id' AND AtividadeID = 'activity_id'")
					
					query_sess = "SELECT `ID` FROM `sessao_atividade` WHERE SessaoID = %s AND AtividadeID = %s"
					values = (session_id, activity_id,)
					c.execute(query_sess, values)
					sess_at = c.fetchone()

					query = "INSERT INTO `sessao_atividade_inscricao` (`InscricaoID`, `Num_alunos`, `Sessao_AtividadeID`) VALUES (%s, %s, %s)"
					values = (inscricao_last_id, item["subscribers"], sess_at)
					c.execute(query, values)



					#query = "INSERT INTO `sessão-atividade` (`SessãoID`, `AtividadeID`) VALUES (%s, %s)"
					#values = (item["session_id"], item["activity_id"],)
					#c.execute(query, values)

				#return HttpResponse("Sucess!")
				messages.info(request, 'Inscrição realizada com sucesso!')

				return redirect('/view_forms')

			else:
				return HttpResponse("Invalid fields")
		else:
			form = RegisterCol()
			form1 = RegisterSchool()
			form2 = RegisterTransporte()
			form3 = RegisterAlmocos()
			form4 = RegisterHorario()
			table_json = {}

			data = []
			activity_kind_list = []
			campus_list = []
			eo_list = []

			atividades = Atividade.objects.all()

			for a in atividades:
				local = Local.objects.get(id=a.localid.id)
				edicifio = Edificio.objects.get(id=local.edicifioid.id)
				campus = Campus.objects.get(id=local.campusid.id)
				eo = UnidadeOrganica.objects.get(id=a.unidadeorganicaid.id)
				utilizador = Utilizador.objects.get(id=a.utilizadorid.id)

				
				dep = Departamento.objects.get(id=utilizador.departamentoid.id)
				
				#print(a.id)
				sessao_atividade = SessaoAtividade.objects.get(atividadeid=a.id)
				sessao = Sessao.objects.get(id=sessao_atividade.sessaoid.id)

				session_id = sessao.id


				start_hour = sessao.hora_de_inicio.strftime("%H:%M")
				s = sessao.hora_de_inicio.strftime("%Y-%m-%d %H:%M")
				t = datetime.strptime(s, '%Y-%m-%d %H:%M')
				end_hour = t + timedelta(minutes=a.duracao)
				end_hour = end_hour.time().strftime("%H:%M")

				build = edicifio.num_edificio
				floor = local.andar
				room = local.sala

				schedule = "{start_hour} - {end_hour}".format(start_hour=start_hour, end_hour=end_hour)

				place = "Ed.{build} Sala {room}.{floor}".format(build=build, room=room, floor=floor)

				data.append([a.nome, a.tipo_atividade, campus.nome, eo.nome, dep.nome, a.descricao, utilizador.nome, start_hour, a.duracao, a.limite_de_participantes, schedule, place, session_id, a.id])

				activity_kind_list.append(a.tipo_atividade)
				campus_list.append(campus.nome)
				eo_list.append(eo.nome)

				dict1 = {

					"name": a.nome,
					"kind": a.tipo_atividade,
					"campus": campus.nome,
					"eo": eo.nome,
					"dep": dep.nome,
					"desc": a.descricao,
					"resp": utilizador.nome,
					"hour": start_hour,
					"end_hour": end_hour,
					"duration": a.duracao,
					"vacancies": a.limite_de_participantes,
					"schedule": schedule,
					"place": place,
					"session_id": session_id,
					"activity_id": a.id
		        }

				table_json.setdefault("data", []).append(dict1)

			with open(TABLE_JSON, 'w', encoding='utf-8') as outfile2:
				json.dump(table_json, outfile2, ensure_ascii=False, indent=2, sort_keys=False)


			template = loader.get_template("register_col.html")
			return HttpResponse(template.render({'form1': form1, 'form': form, 'form2': form2,
			'form3': form3, 'form4': form4, 'post_redirect': 'main:view_forms', 'atividades': data,
			"activity_kind_list": set(activity_kind_list), "campus_list": set(campus_list),
			"eo_list": set(eo_list)}, request))









# Create your views here.
def homepage(request):
	return render(request = request, 
				  template_name="main/home.html", 
				  context={"dados": Participanteinfo.objects.all})


def inscricao(request):
	return render(request,
				  template_name="main/inscricao.html",
				  )




def login(request):
	
	##print("PASSWORD_MADE: " + str(make_password("kaputaze")))
	##print("PASSWORD_CHECK: " + str(check_password("kaputaze", str(make_password("kaputaze")))))
	if(request.user.is_authenticated):
		return HttpResponse("You are already logged in")

	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(request, email_p=form.cleaned_data['user_email'], password_p=form.cleaned_data['user_password'])
			if user is not None:
				django_login(request, user)
			#return HttpResponse("veri good frend" + " " + ("bigus dadas" if user is not None else "ah shitfuck"))
			return redirect('/') 
		else:
			return HttpResponse("something wrong")
	else:
		form = LoginForm()
		template = loader.get_template("login.html")
		return HttpResponse(template.render({'form': form.as_p, 'post_redirect': 'main:login'}, request))


def logout(request): 
	if request.user.is_authenticated:
		django_logout(request)
		#return HttpResponse("you have been logged out!")
		return redirect('/')
	return HttpResponse("you are not logged in")



def register(request): # User system registration form
	if request.user.is_authenticated:
		return HttpResponse("you cannot register because you are already logged in")

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			############registo
			perfil = GestoDePerfil(validação=0)
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
		return HttpResponse(template.render({'form': form.as_p, 'post_redirect': 'main:register'}, request))




def register_ind(request):  # make an individual register form

	if  request.user.is_authenticated:

		if request.method == 'POST':
			form3 = RegisterAlmocos(request.POST)

			if form3.is_valid():

				escola = Escola(
					nome="individual",
				)
				escola.save();

				participanteinfo = Participanteinfo(
					utilizadorid=request.user, #request.session.get('user')
					ano_escolar=1,
					checkin_state=0,
					participante_type=1,
				)
				participanteinfo.save();

				
				inscrio = Inscricao(
					escolaid=escola,
				)
				inscrio.save()

				user_atual = Utilizador.objects.get(id=request.user.id)
				user_atual.inscriçãoid = inscrio
				user_atual.save()

				all_data = request.POST.get("all_data")

				print(all_data)
				print(type(all_data))
				json_content = json.loads(all_data)

				print(json_content)

				

				c = connection.cursor()

        #query = "SELECT `id` FROM `inscricao` ORDER BY `id` DESC LIMIT 1"
        #c.execute(query)
        #last_id = c.fetchone()
				inscricao_last_id = inscrio.id

				for item in json_content:
					session_id=item['session_id']
					activity_id=item['activity_id']

					#sess_at = c.execute("SELECT ID FROM `sessão-atividade` WHERE SessãoID = 'session_id' AND AtividadeID = 'activity_id'")
					
					query_sess = "SELECT `ID` FROM `sessao_atividade` WHERE SessaoID = %s AND AtividadeID = %s"
					values = (session_id, activity_id,)
					c.execute(query_sess, values)
					sess_at = c.fetchone()

					query = "INSERT INTO `sessao_atividade_inscricao` (`InscricaoID`, `Num_alunos`, `Sessao_AtividadeID`) VALUES (%s, %s, %s)"
					values = (inscricao_last_id, item["subscribers"], sess_at)
					c.execute(query, values)



					#query = "INSERT INTO `sessão-atividade` (`SessãoID`, `AtividadeID`) VALUES (%s, %s)"
					#values = (item["session_id"], item["activity_id"],)
					#c.execute(query, values)

				#return HttpResponse("Sucess!")
				messages.info(request, 'Inscrição realizada com sucesso!')

				return redirect('/view_forms')

			else:
				return HttpResponse("Invalid fields")
		else:
			form3 = RegisterAlmocos()
			table_json = {}

			data = []
			activity_kind_list = []
			campus_list = []
			eo_list = []

			atividades = Atividade.objects.all()

			for a in atividades:
				local = Local.objects.get(id=a.localid.id)
				edicifio = Edificio.objects.get(id=local.edicifioid.id)
				campus = Campus.objects.get(id=local.campusid.id)
				eo = UnidadeOrganica.objects.get(id=a.unidadeorganicaid.id)
				utilizador = Utilizador.objects.get(id=a.utilizadorid.id)

				
				dep = Departamento.objects.get(id=utilizador.departamentoid.id)
				
				#print(a.id)
				sessao_atividade = SessaoAtividade.objects.get(atividadeid=a.id)
				sessao = Sessao.objects.get(id=sessao_atividade.sessaoid.id)

				session_id = sessao.id


				start_hour = sessao.hora_de_inicio.strftime("%H:%M")
				s = sessao.hora_de_inicio.strftime("%Y-%m-%d %H:%M")
				t = datetime.strptime(s, '%Y-%m-%d %H:%M')
				end_hour = t + timedelta(minutes=a.duracao)
				end_hour = end_hour.time().strftime("%H:%M")

				build = edicifio.num_edificio
				floor = local.andar
				room = local.sala

				schedule = "{start_hour} - {end_hour}".format(start_hour=start_hour, end_hour=end_hour)

				place = "Ed.{build} Sala {room}.{floor}".format(build=build, room=room, floor=floor)

				data.append([a.nome, a.tipo_atividade, campus.nome, eo.nome, dep.nome, a.descricao, utilizador.nome, start_hour, a.duracao, a.limite_de_participantes, schedule, place, session_id, a.id])

				activity_kind_list.append(a.tipo_atividade)
				campus_list.append(campus.nome)
				eo_list.append(eo.nome)

				dict1 = {

					"name": a.nome,
					"kind": a.tipo_atividade,
					"campus": campus.nome,
					"eo": eo.nome,
					"dep": dep.nome,
					"desc": a.descricao,
					"resp": utilizador.nome,
					"hour": start_hour,
					"end_hour": end_hour,
					"duration": a.duracao,
					"vacancies": a.limite_de_participantes,
					"schedule": schedule,
					"place": place,
					"session_id": session_id,
					"activity_id": a.id
		        }

				table_json.setdefault("data", []).append(dict1)

			with open(TABLE_JSON, 'w', encoding='utf-8') as outfile2:
				json.dump(table_json, outfile2, ensure_ascii=False, indent=2, sort_keys=False)


			template = loader.get_template("register_ind.html")
			return HttpResponse(template.render({'form3': form3, 'post_redirect': 'main:view_forms', 'atividades': data,
			"activity_kind_list": set(activity_kind_list), "campus_list": set(campus_list),
			"eo_list": set(eo_list)}, request))




def update_col(request, pk): # update collective registration information
	
	part = Participanteinfo.objects.get(participanteinfoid=pk)

	insc = Inscricao.objects.get(id=part.utilizadorid.inscriçãoid.id)
	escola = Escola.objects.get(id=insc.escolaid.id)

	ut_transporte = UtilizadorTransporte.objects.get(utilizadorid=request.user.id)
	transporte = Transporte.objects.get(id=ut_transporte.transporteid.id)

	ut_ementa = UtilizadorEmenta.objects.get(utilizadorid=request.user.id)
	ementa = Ementa.objects.get(id=ut_ementa.ementaid.id)

	form = RegisterCol(instance=part)
	form1 = RegisterSchool(instance=escola)
	form2 = RegisterTransporte(instance=transporte)
	form3 = RegisterAlmocos(instance=ementa)

	if request.method == 'POST':
		form = RegisterCol(request.POST, instance=part)
		form1 = RegisterSchool(request.POST, instance=escola)
		form2 = RegisterTransporte(request.POST, instance=transporte)
		form3 = RegisterAlmocos(request.POST, instance=ementa)

		if form1.is_valid() and form.is_valid() and form2.is_valid() and form3.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form, 'form1': form1, 'form2': form2,	'form3': form3,  }
	return render(request, 'main/register_col.html', context)



def apagar_col(request, pk):  # delete a collective registration
	

	act = Participanteinfo.objects.get(participanteinfoid=pk)
	insc = Inscricao.objects.get(id=act.utilizadorid.inscriçãoid.id)
	u_ementa = UtilizadorEmenta.objects.get(utilizadorid=request.user.id)
	ementa = InscrioEmenta.objects.get(ementaid=u_ementa.ementaid.id)


	#local = Local.objects.get(id=a.localid.id)
	#edicifio = Edificio.objects.get(id=local.edicifioid.id)
	if  request.user.is_authenticated:
		if request.method == "POST":
			ementa.delete()
			insc.delete()
			act.delete()
			return redirect('/view_forms')
		
	context = {'info':act}
	return render(request, 'main/apagar_col.html', context)





def ver_col(request, pk):  # see the information of a collective registration form
	
	inscr = Participanteinfo.objects.get(utilizadorid=request.user)

	return render(request, 'main/ver_col.html', 
				  {
				  # "part": Participanteinfo.objects.filter(utilizadorid=request.user, participante_type=2, participanteinfoid=pk),
				   #"insc": Inscricao.objects.filter(id=pk),
				   #"sess": SessaoAtividadeInscricao.objects.get(inscricaoid=infos.utilizadorid.inscriçãoid.id)
				   "info": Participanteinfo.objects.get(utilizadorid=request.user.id),
				   "insc": Participanteinfo.objects.get(participanteinfoid=pk),
				   "sess": SessaoAtividadeInscricao.objects.filter(inscricaoid=inscr.utilizadorid.inscriçãoid.id),
				   "ut_trans": UtilizadorTransporte.objects.get(utilizadorid=request.user.id),
				   "ut_ementa": UtilizadorEmenta.objects.get(utilizadorid=request.user.id)

				  })



def view_forms(request): # see collective registration forms, in a table, made by users

	dados_part = Participanteinfo.objects.filter(utilizadorid=request.user.id)

	#insc_part = Inscrio.objects.get(participanteinfoid=dados_part)
	for a in dados_part:
		print(a.participante_type)

	return render(request, 
				  "main/view_forms.html", 
				  {"user": Utilizador.objects.filter(id=request.user.id),
				   "dados": Participanteinfo.objects.filter(utilizadorid=request.user.id),

				   "adm": Participanteinfo.objects.all,

				   "utilizadores": Utilizador.objects.all().order_by('inscriçãoid__escolaid__id'),
				   #"insc_part": insc_part,
				   "inscricao": Inscricao.objects.all #.order_by('utilizadorid__inscriçãoid__escolaid__id')
				  })




def inscricao_col(request): # see collective registration forms, in a table, made by users

	dados_part = Participanteinfo.objects.filter(utilizadorid=request.user.id, participante_type=2)
	inscric = Inscricao.objects.all

	#insc_part = Inscrio.objects.get(participanteinfoid=dados_part)
	

	return render(request, 
				  "main/inscricao_col.html", 
				  {"user": Utilizador.objects.filter(id=request.user.id),
				   "dados": Participanteinfo.objects.filter(utilizadorid=request.user.id, participante_type=2),

				   "adm": Participanteinfo.objects.all,

				   "utilizadores": Utilizador.objects.all().order_by('inscriçãoid__escolaid__id'),
				   #"insc_part": insc_part,
				   "inscricao": Inscricao.objects.all, #.order_by('utilizadorid__inscriçãoid__escolaid__id')
				   
				   "part": Participanteinfo.objects.filter(utilizadorid=request.user),

				  })
				  


def inscricao_ind(request): # see collective registration forms, in a table, made by users

	dados_part = Participanteinfo.objects.filter(utilizadorid=request.user.id, participante_type=1)
	inscric = Inscricao.objects.all
	#insc_part = Inscrio.objects.get(participanteinfoid=dados_part)

	return render(request, 
				  "main/inscricao_ind.html", 
				  {"user": Utilizador.objects.filter(id=request.user.id),
				   "dados": Participanteinfo.objects.filter(utilizadorid=request.user.id, participante_type=1),

				   "adm": Participanteinfo.objects.all,

				   "utilizadores": Utilizador.objects.all().order_by('inscriçãoid__escolaid__id'),
				   #"insc_part": insc_part,
				   "inscricao": Inscricao.objects.all, #.order_by('utilizadorid__inscriçãoid__escolaid__id')
				   "part": Participanteinfo.objects.get(utilizadorid=request.user, participante_type=1),
				  })
				  