import datetime, json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.forms import formset_factory
from django.db.models.functions import Lower

from tarefas.models import Tarefa, ColaboradorTarefa, InscricaoTarefa
from atividades.models import UnidadeOrganica, SessaoAtividade, Inscricao, SessaoAtividadeInscricao, Utilizador
from tarefas.forms import TarefaForm, TarefaAtividadeForm, TarefaTransporteForm, TarefaGruposForm, TarefaGruposFormset, \
    ColaboradorTarefaForm


# Create your views here.

# ---------------------------------------------------------
# Tarefas CRUD- Create Read Update Delete
# ----------------------------------------------------------

def createTarefa(request):
    if request.method == 'GET':
        formTarefa = TarefaForm()
        # Change later so that id equals the UO of the autheticated Coordenador
        formTarefaAtividade = TarefaAtividadeForm(request.GET or None, uoId=UnidadeOrganica.objects.get(id=1))
        formTarefaTransporte = TarefaTransporteForm(request.GET or None)
        formSetTarefaGrupos = TarefaGruposFormset(request.GET or None)
    elif request.method == 'POST':
        formTarefa = TarefaForm(request.POST)
        formTarefaAtividade = TarefaAtividadeForm(request.POST, uoId=UnidadeOrganica.objects.get(id=1))
        formTarefaTransporte = TarefaTransporteForm(request.POST)
        formSetTarefaGrupos = TarefaGruposFormset(request.POST)

        if formTarefa.is_valid() and formTarefaTransporte.is_valid() and formSetTarefaGrupos.is_valid():
            t = formTarefa.save(commit=False)
            t.estado = False
            # Change for logged in user
            t.utilizadorid = Utilizador.objects.get(id=1)
            t.sessao_atividadeid_destino = SessaoAtividade.objects.get(
                id=formTarefaTransporte.cleaned_data['sessaoAtividade_destino'])
            t.sessao_atividadeid_origem = SessaoAtividade.objects.get(
                id=formTarefaTransporte.cleaned_data['sessaoAtividade_origem'])
            t.origem = formTarefaTransporte.cleaned_data['origem']
            t.destino = formTarefaTransporte.cleaned_data['destino']
            t.horario = formTarefaTransporte.cleaned_data['horario']
            t.data = formTarefaTransporte.cleaned_data['dia']

            t.save()

            for form in formSetTarefaGrupos:
                InscTarefa = InscricaoTarefa(inscricaoid=Inscricao.objects.get(id=form.cleaned_data['inscricao']),
                                             tarefaid=t)
                InscTarefa.save()

        elif formTarefa.is_valid() and formTarefaAtividade.is_valid():
            t = formTarefa.save(commit=False)
            t.estado = False
            # Change for logged in user
            t.utilizadorid = Utilizador.objects.get(id=1)
            t.sessao_atividadeid = SessaoAtividade.objects.get(id=formTarefaAtividade.cleaned_data['sessaoAtividade'])
            t.horario = t.sessao_atividadeid.sessaoid.hora_de_inicio
            t.data = t.sessao_atividadeid.data
            t.save()

        return redirect('tarefas:showTarefas')

    context = {'formTarefa': formTarefa,
               'formTarefaAtividade': formTarefaAtividade,
               'formTarefaTransporte': formTarefaTransporte,
               'formSetTarefaGrupos': formSetTarefaGrupos,
               }

    return render(request, 'tarefas/AdicionarTarefa.html', context)

def showTarefas(request):
    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    ordering = Lower(order_by)

    if direction == 'desc':
        ordering = '-{}'.format(order_by)

    allTarefas = Tarefa.objects.all().order_by(ordering)

    paginator = Paginator(allTarefas, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    allTarefaGrupos = {}
    allTarefaColaboradores = {}

    for tarefa in page_obj:
        insc = InscricaoTarefa.objects.filter(tarefaid = tarefa.id)
        if insc:
            allTarefaGrupos[tarefa.id] = insc
        
        colab = ColaboradorTarefa.objects.filter(tarefaid = tarefa.id)
        if colab:
            allTarefaColaboradores[tarefa.id] = colab

        
    context = { 'page_obj': page_obj,
                'order_by': order_by,
                'direction': direction,
                'allTarefaGrupos': allTarefaGrupos,
                'allTarefaColaboradores': allTarefaColaboradores,
            }
    return render(request, 'tarefas/showTarefas.html', context)


def atribuirTarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    uo_id = tarefa.utilizadorid.unidade_organicaid
    resultColaboradores = []

    # change later depending on other group user_type numeration
    colaboradores = Utilizador.objects.filter(unidade_organicaid=uo_id).filter(user_type=3)

    for colab in colaboradores:
        busy = False
        for colabTarefa in ColaboradorTarefa.objects.filter(utilizadorid=colab):
            if (colabTarefa.tarefaid.horario == tarefa.horario and colabTarefa.tarefaid.data == tarefa.data):
                busy = True
                break
        if not busy:
            resultColaboradores.append(colab)

    tarefaGrupos = None
    if tarefa.tipoTarefa == 'Transporte':
        tarefaGrupos = InscricaoTarefa.objects.filter(tarefaid=tarefa.id)

    if request.method == 'POST':
        form = ColaboradorTarefaForm(request.POST)
        if form.is_valid():
            colabT = form.save(commit=False)
            colabT.tarefaid = tarefa
            colabT.save()

            tarefa.estado = True
            tarefa.save()
            return redirect('tarefas:showTarefas')

    context = {
        'colaboradores': resultColaboradores,
        'dadosTarefa': tarefa,
        'dadosTarefaGrupos': tarefaGrupos,
    }
    return render(request, 'tarefas/AtribuirTarefa.html', context)

def deleteTarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect('tarefas:showTarefas')


def updateTarefa(request, id):
    dados_Tarefa = Tarefa.objects.get(id=id)
    formTarefaTransporte = None
    formSetTarefaGrupos = None
    formTarefaAtividade = None

    if request.method == "GET":
        formTarefa = TarefaForm(instance=dados_Tarefa)
        
        if dados_Tarefa.tipoTarefa == 'Transporte':
            
            #Get sessoes origem from getSessoesBydate and then convert jsonResponse into a list of tuples
            sessao_o = getSessoesBydate(request, dados_Tarefa.data)
            s_o = json.loads(sessao_o.content)
            dados_sessao_o = [(k, v) for k, v in s_o.items()]

            #Get sessoes destino from getSessoesNext and then convert jsonResponse into a list of tuples
            sessao_d = getSessoesNext(request, dados_Tarefa.sessao_atividadeid_origem.id, dados_Tarefa.data)
            s_d = json.loads(sessao_d.content)
            dados_sessao_d = [(k, v) for k, v in s_d.items()]

            formTarefaTransporte = TarefaTransporteForm(
                initial={
                    'dia': dados_Tarefa.data,
                    'horario': dados_Tarefa.horario,
                    'sessaoAtividade_origem': dados_Tarefa.sessao_atividadeid_origem.id,
                    'sessaoAtividade_destino': dados_Tarefa.sessao_atividadeid_destino.id,
                    'origem': dados_Tarefa.origem,
                    'destino': dados_Tarefa.destino},
                sessao_o = dados_sessao_o,
                sessao_d = dados_sessao_d
            )

            #Get available grupos from getGrupos and convert jsonResponse into a list of tuples
            json_g = getGrupos(request, dados_Tarefa.sessao_atividadeid_origem.id, dados_Tarefa.sessao_atividadeid_destino.id, dados_Tarefa.data)
            g = json.loads(json_g.content)
            available_grupos = [(k, v) for k, v in g.items()]
            
            TarefaGruposFormSet = formset_factory(TarefaGruposForm, extra=0)

            grupos = []
            for grupo in InscricaoTarefa.objects.filter(tarefaid = id):
               grupos.append({'inscricao': grupo.id}) 
            
            formSetTarefaGrupos = TarefaGruposFormSet(initial=grupos, form_kwargs = {'available_grupos': available_grupos})
            

        elif dados_Tarefa.tipoTarefa == 'Atividade':
            formTarefaAtividade = TarefaAtividadeForm(
                initial={'atividade': dados_Tarefa.sessao_atividadeid.atividadeid.id,
                         'sessaoAtividade': dados_Tarefa.sessao_atividadeid.id},
                uoId=UnidadeOrganica.objects.get(id=1),
                sA=dados_Tarefa.sessao_atividadeid.atividadeid.id
            )
    
    elif request.method == "POST":
        formTarefa = TarefaForm(request.POST, instance=dados_Tarefa)
        
        if dados_Tarefa.tipoTarefa == 'Transporte':
            formTarefaTransporte = TarefaTransporteForm(request.POST)
            formSetTarefaGrupos = TarefaGruposFormset(request.POST)
            if formTarefa.is_valid() and formTarefaTransporte.is_valid() and formSetTarefaGrupos.is_valid():
                t = formTarefa.save(commit=False)
                t.tipoTarefa = 'Transporte'
                t.estado = 'False'
                t.sessao_atividadeid_origem = SessaoAtividade.objects.get(id=formTarefaTransporte.cleaned_data['sessaoAtividade_origem'])
                t.sessao_atividadeid_destino = SessaoAtividade.objects.get(id=formTarefaTransporte.cleaned_data['sessaoAtividade_destino'])
                t.origem = formTarefaTransporte.cleaned_data['origem']
                t.destino = formTarefaTransporte.cleaned_data['destino']
                t.horario = formTarefaTransporte.cleaned_data['horario']
                t.data = formTarefaTransporte.cleaned_data['dia']
                t.save()
                
                grupos = InscricaoTarefa.objects.filter(tarefaid = id)
                #update grupos and add new
                if len(formSetTarefaGrupos) >= len(grupos):
                    for index, form in enumerate(formSetTarefaGrupos):
                        if index < len(grupos):
                            grupos[index].inscricaoid = Inscricao.objects.get(id = form.cleaned_data['inscricao'])
                            grupos[index].save()
                        else:
                            g = InscricaoTarefa(inscricaoid = Inscricao.objects.get(id = form.cleaned_data['inscricao']), tarefaid = dados_Tarefa)
                            g.save()
                #update grupos and remove 
                else:
                    for index, grupo in enumerate(grupos):
                        if index < len(formSetTarefaGrupos):
                            grupo.inscricaoid = Inscricao.objects.get(id = formSetTarefaGrupos[index].cleaned_data['inscricao'])
                            grupo.save()
                        else:
                            grupo.delete()

                #Remove colaboradores associados com a tarefa
                for colab in ColaboradorTarefa.objects.filter(tarefaid=t.id):
                    colab.delete()

                return redirect('tarefas:showTarefas')
        
        elif dados_Tarefa.tipoTarefa == 'Atividade':
            formTarefaAtividade = TarefaAtividadeForm(request.POST, uoId=UnidadeOrganica.objects.get(id=1))
            if formTarefa.is_valid() and formTarefaAtividade.is_valid():
                t = formTarefa.save(commit=False)
                t.tipoTarefa = 'Atividade'
                t.estado = 'False'
                t.sessao_atividadeid = SessaoAtividade.objects.get(id=formTarefaAtividade.cleaned_data['sessaoAtividade'])
                t.horario = t.sessao_atividadeid.sessaoid.hora_de_inicio
                t.data = t.sessao_atividadeid.data
                t.save()
                #Remove colaboradores associados com a tarefa
                for colab in ColaboradorTarefa.objects.filter(tarefaid=t.id):
                    colab.delete()

                return redirect('tarefas:showTarefas')

    context = {'formTarefa': formTarefa,
               'formTarefaAtividade': formTarefaAtividade,
               'formTarefaTransporte': formTarefaTransporte,
               'formSetTarefaGrupos': formSetTarefaGrupos,
               'tarefa': dados_Tarefa}

    return render(request, 'tarefas/EditTarefa.html', context)


# Used in Create Tarefa to dynamically get the Sessoes Atividade of a the selected Atividade
# Returns a Json Response with the data of all the SessaoAtividades that have the atividadeid equal to atividadeid
def getSessoes(request, atividadeid):
    sessoes = [(sessaoAtividade.id, str(sessaoAtividade)) for sessaoAtividade in
               SessaoAtividade.objects.filter(atividadeid=atividadeid)]
    return JsonResponse(dict(sessoes))


# Used in Create Tarefa to dynamically get the Sessoes Atividade from the selected date
# Returns a Json Response with the SessaoAtividades that have date equal to the arg date
def getSessoesBydate(request, date):
    sessoes = []
    for sessao in SessaoAtividade.objects.filter(data=date):
        # change later to authenticated user
        if sessao.atividadeid.unidadeorganicaid == Utilizador.objects.get(id=1).unidade_organicaid:
            sessoes.append((sessao.id, str(sessao.atividadeid.nome) + ", " + str(sessao.sessaoid.hora_de_inicio)))

    return JsonResponse(dict(sessoes))


# Used in Create Tarefa to dynamically get the Sessoes Atividade from the selected date and that are after the sessao_atual
# Returns a Json Response with the SessaoAtividades that have date equal to the arg date and hora_inicio greather than the hora_fim of the sessao_atual
def getSessoesNext(request, sessao_atividadeid, date):
    sessoes = []
    sessao_atual = SessaoAtividade.objects.get(id=sessao_atividadeid)

    hora_inicio = datetime.datetime.combine(sessao_atual.data, sessao_atual.sessaoid.hora_de_inicio)
    duracao = sessao_atual.atividadeid.duracao

    hora_fim = hora_inicio + datetime.timedelta(minutes=duracao)

    for sessao in SessaoAtividade.objects.filter(data=date):
        # change later to authenticated user
        if sessao.atividadeid.unidadeorganicaid == Utilizador.objects.get(id=1).unidade_organicaid:
            # gets all the sessoes within a 30 minute gap since the hora_fim of the sessao_atual
            if sessao.sessaoid.hora_de_inicio >= hora_fim.time() and sessao.sessaoid.hora_de_inicio <= (
                    hora_fim + datetime.timedelta(minutes=30)).time():
                sessoes.append((sessao.id, str(sessao.atividadeid.nome) + ", " + str(sessao.sessaoid.hora_de_inicio)))

    return JsonResponse(dict(sessoes))


def getHoraFim(request, sessao_atividadeid):
    sessao_atual = SessaoAtividade.objects.get(id=sessao_atividadeid)

    hora_inicio = datetime.datetime.combine(sessao_atual.data, sessao_atual.sessaoid.hora_de_inicio)
    duracao = sessao_atual.atividadeid.duracao
    hora_fim = hora_inicio + datetime.timedelta(minutes=duracao)

    return JsonResponse({'1': hora_fim.time()})


def getLocal_Sessao(request, sessao_atividadeid):
    sessaoAtividade = SessaoAtividade.objects.get(id=sessao_atividadeid)
    local = str(sessaoAtividade.atividadeid.localid)
    return JsonResponse({'local': local})


def getGrupos(request, sessao_atividade_origem, sessao_atividade_destino, dia):
    sessao_origem = SessaoAtividade.objects.get(id=sessao_atividade_origem)
    sessao_destino = SessaoAtividade.objects.get(id=sessao_atividade_destino)

    count = 0
    grupos = []

    for grupo in Inscricao.objects.filter(dia=dia):
        for sessaoInsc in SessaoAtividadeInscricao.objects.filter(inscricaoid=grupo):
            if sessaoInsc.sessao_atividadeid.id == sessao_origem.id:
                count += 1
            elif sessaoInsc.sessao_atividadeid.id == sessao_destino.id:
                count += 1
        if count == 2:
            grupos.append((grupo.id, str(grupo)))

    return JsonResponse(dict(grupos))


