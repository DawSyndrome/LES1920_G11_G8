from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.forms import modelformset_factory, formset_factory
import datetime
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required, permission_required

from .filters import UnidadeOrganicaFilter, DepartamentoFilter, LocalFilter, CampusFilter, EdificioFilter, TematicaFilter, MaterialFilter, AtividadeFilter, SessaoFilter

from atividades.models import Edificio, Campus, Departamento, Local, Atividade, UnidadeOrganica, Tematica, AtividadeTematica, AtividadeMaterial, Sessao, SessaoAtividade, Material
from utilizadores.models import Utilizador

from atividades.forms import EdificioForm, CampusForm, DepartamentoForm, LocalForm, AtividadeForm, UnidadeOrganicaForm, TematicaForm, AtividadeTematicaFormset, AtividadeMaterialFormset, AtividadeTematicaForm, AtividadeMaterialForm, AtividadeSessaoForm, AtividadeSessaoFormset, SessaoForm, MaterialForm

from diaAbertoConf.models import DiaAberto
# Create your views here.

#Creates new edificio
@login_required()
@permission_required('atividades.add_edificio', raise_exception=True)
def createEdificio(request):
    allCampus = Campus.objects.all()
    form = EdificioForm(request.POST or None)
    saved = False
    if request.method == "POST":
        if form.is_valid():
            form.save()
            saved = True
            form = EdificioForm()
    context = {'form' : form, 'saved' : saved, 'allCampus' : allCampus}
    return render(request, 'atividades/AdicionarEdificio.html', context)

#show all edificios
@login_required()
@permission_required('atividades.view_edificio', raise_exception=True)
def showEdificios(request):
    allEdificios = Edificio.objects.all()
    allCampus = Campus.objects.all()
    myFilter = EdificioFilter(request.GET, queryset=allEdificios)

    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = order_by
        if direction == 'desc':
            ordering = '-{}'.format(order_by)
        allEdificios = myFilter.qs.order_by(ordering)
    else:
        allEdificios = myFilter.qs

    paginator = Paginator(allEdificios, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nome_edificio = request.GET.get('nome_edificio')
    campusid__nome = request.GET.get('campusid__nome')
    context = {
                'allCampus' : allCampus, 
                'allEdificios' : allEdificios, 
                'page_obj': page_obj,
                'nome_edificio' : nome_edificio, 
                'campusid__nome' : campusid__nome,
                'order_by' : order_by, 
                'direction' : direction
            }
    return render(request, 'atividades/ShowEdificios.html', context)

#upadates the fields of a spcific edificio
@login_required()
@permission_required('atividades.change_edificio', raise_exception=True)
def updateEdificio(request, id):
    dados_Edificio = Edificio.objects.get(id = id)
    allCampus = Campus.objects.all()
    form = EdificioForm(request.POST or None, instance = dados_Edificio)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return  redirect('atividades:allEdificios')

    context = {'allCampus' : allCampus, 'edificio' : dados_Edificio, 'form' : form}
    return render(request, 'atividades/EditarEdificio.html' ,context)

#deletes a edificio
@login_required()
@permission_required('atividades.delete_edificio', raise_exception=True)
def deleteEdificio(request, id):
    dados_edificio = Edificio.objects.get(id = id)
    dados_edificio.delete()
    return HttpResponseRedirect(reverse('atividades:allEdificios'))

#Creates new campus
@login_required()
@permission_required('atividades.add_campus', raise_exception=True)
def createCampus(request):
    form = CampusForm()
    saved = False
    if request.method == "POST":
        form = CampusForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
            form = CampusForm()
    context = {'form' : form, 'saved' : saved}
    return render(request, 'atividades/AdicionarCampus.html', context)

#show all campus
@login_required()
@permission_required('atividades.view_campus', raise_exception=True)
def showCampus(request):#, ordena):
    allCampus = Campus.objects.all()
    myFilter = CampusFilter(request.GET, queryset=allCampus)

    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = Lower(order_by)
        if direction == 'desc':
            ordering = '-{}'.format(order_by)
        allCampus = myFilter.qs.order_by(ordering)
    else:
        allCampus = myFilter.qs

    paginator = Paginator(allCampus, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nome = request.GET.get('nome')
    localizacao = request.GET.get('localizacao')

    context = {'allCampus' : allCampus, 'page_obj': page_obj,
                'myFilter' : myFilter, 'nome' : nome, 'localizacao' : localizacao,
                'order_by': order_by, 'direction': direction}
    return render(request, 'atividades/ShowCampus.html', context)

#upadates the fields of a spcific campus
@login_required()
@permission_required('atividades.change_campus', raise_exception=True)
def updateCampus(request, id):
    dados_Campus = Campus.objects.get(id = id)
    form = CampusForm(request.POST or None, instance = dados_Campus)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return  redirect('atividades:allCampus')

    return render(request, 'atividades/EditarCampus.html', {'form' : form, 'campus' : dados_Campus})

#deletes a campus
@login_required()
@permission_required('atividades.delete_campus', raise_exception=True)
def deleteCampus(request, id):
    dados_campus = Campus.objects.get(id = id)
    dados_campus.delete()
    return HttpResponseRedirect(reverse('atividades:allCampus'))

#Creates new unidade
@login_required()
@permission_required('atividades.add_unidadeorganica', raise_exception=True)
def createUnidadeOrganica(request):
    form = UnidadeOrganicaForm(request.POST or None)
    saved = False
    if request.method == "POST":
        if form.is_valid():
            form.save()
            saved = True
            form = UnidadeOrganicaForm()
    context = {'form' : form, 'saved' : saved}       

    return render(request, 'atividades/AdicionarUO.html', context)

#show all unidade
@login_required()
@permission_required('atividades.view_unidadeorganica', raise_exception=True)
def showUnidadeOrganicas(request):
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    myFilter = UnidadeOrganicaFilter(request.GET, queryset=allUnidadeOrganicas)
    
    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = Lower(order_by)
        if direction == 'desc':
            ordering = '-{}'.format(order_by)
        allUnidadeOrganicas = myFilter.qs.order_by(ordering)
    else:
        allUnidadeOrganicas = myFilter.qs

    paginator = Paginator(allUnidadeOrganicas, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nome = request.GET.get('nome')
    context = {
                'allUnidadeOrganicas' : allUnidadeOrganicas, 
                'page_obj': page_obj,
                'myFilter' : myFilter, 
                'nome' : nome,
                'order_by' : order_by, 
                'direction' : direction
                }
    return render(request, 'atividades/ShowUO.html', context)

@login_required()
@permission_required('atividades.change_unidadeorganica', raise_exception=True)
#upadates the fields of a spcific unidade
def updateUnidadeOrganica(request, id):
    dados_UnidadeOrganica = UnidadeOrganica.objects.get(id = id)
    allCampus = Campus.objects.all()
    form = UnidadeOrganicaForm(request.POST or None, instance = dados_UnidadeOrganica)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return  redirect('atividades:allUnidadeOrganicas')
    
    context = {'allCampus' : allCampus, 'unidadeorganica' : dados_UnidadeOrganica, 'form' : form}
    return render(request, 'atividades/EditarUO.html', context)

#deletes a unidade
@login_required()
@permission_required('atividades.delete_unidadeorganica', raise_exception=True)
def deleteUnidadeOrganica(request, id):
    dados_unidadeorganica = UnidadeOrganica.objects.get(id = id)
    dados_unidadeorganica.delete()
    return HttpResponseRedirect(reverse('atividades:allUnidadeOrganicas'))

#Creates new departamento
@login_required()
@permission_required('atividades.add_departamento', raise_exception=True)
def createDepartamento(request):
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    form = DepartamentoForm()
    saved = False
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
            form = DepartamentoForm()
    context = {'form' : form, 'saved' : saved, 'allUnidadeOrganicas' : allUnidadeOrganicas}

    return render(request, 'atividades/AdicionarDepartamento.html', context)


#show all departamntos
@login_required()
@permission_required('atividades.view_departamento', raise_exception=True)
def showDepartamentos(request):
    allDepartamentos = Departamento.objects.all()
    myFilter = DepartamentoFilter(request.GET, queryset=allDepartamentos)

    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = Lower(order_by)
        if direction == 'desc':
            ordering = '-{}'.format(order_by)
        allDepartamentos = myFilter.qs.order_by(ordering)
    else:
        allDepartamentos = myFilter.qs

    paginator = Paginator(allDepartamentos, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nome = request.GET.get('nome')
    unidade_organicaid__nome = request.GET.get('unidade_organicaid__nome')
    context = {
                'allDepartamentos' : allDepartamentos, 
                'page_obj': page_obj,
                'myFilter' : myFilter, 
                'nome' : nome, 
                'unidade_organicaid__nome' : unidade_organicaid__nome,
                'order_by' : order_by, 
                'direction' : direction
                }
    return render(request, 'atividades/ShowDepartamentos.html', context)

#upadates the fields of a spcific departamento
@login_required()
@permission_required('atividades.change_departamento', raise_exception=True)
def updateDepartamento(request, id):
    dados_Departamento = Departamento.objects.get(id = id)
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    form = DepartamentoForm(request.POST or None, instance = dados_Departamento)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return  redirect('atividades:allDepartamentos')

    context = {'allUnidadeOrganicas' : allUnidadeOrganicas, 'departamento' : dados_Departamento, 'form' : form}
    return render(request, 'atividades/EditarDepartamento.html', context)

#deletes a departamento
@login_required()
@permission_required('atividades.delete_departamento', raise_exception=True)
def deleteDepartamento(request, id):
    dados_departamento = Departamento.objects.get(id = id)
    dados_departamento.delete()
    return HttpResponseRedirect(reverse('atividades:allDepartamentos'))

#Creates new local
@login_required()
@permission_required('atividades.add_local', raise_exception=True)
def createLocal(request):
    form = LocalForm()
    saved = False
    allCampus = Campus.objects.all()

    try:
        allEdificios = Edificio.objects.filter(campusid = allCampus[0].id)
    except IndexError:
        allEdificios = None

    if request.method == "POST":
        form = LocalForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['indoor'] == False:
                l = Local(campusid=form.cleaned_data['campusid'], 
                    nome_local_exterior = form.cleaned_data['nome_local_exterior'], 
                    descricao=form.cleaned_data['descricao'],
                    indoor = form.cleaned_data['indoor'],
                    mapa_sala = form.cleaned_data['mapa_sala'])
                l.save()
            else:
                l = Local(campusid=form.cleaned_data['campusid'],  
                    descricao=form.cleaned_data['descricao'],
                    indoor = form.cleaned_data['indoor'],
                    edicifioid = Edificio.objects.get(id=request.POST['edicifioid']),
                    andar = form.cleaned_data['andar'],
                    sala = form.cleaned_data['sala'],
                    mapa_sala = form.cleaned_data['mapa_sala'])
                l.save()
            #form.save()
            #image.save()
            saved = True
            form = LocalForm()
    context = {'allCampus' : allCampus, 'allEdificios' : allEdificios, 'saved' : saved, 'form' : form}
    return render(request, 'atividades/AdicionarLocal.html', context)

#show all local
@login_required()
@permission_required('atividades.view_local', raise_exception=True)
def showLocais(request):
    allLocais = Local.objects.all()
    allCampus = Campus.objects.all()
    myFilter = LocalFilter(request.GET, queryset=allLocais)

    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = Lower(order_by)
        if direction == 'desc':
            ordering = '-{}'.format(order_by)
        allLocais = myFilter.qs.order_by(ordering)
    else:
        allLocais = myFilter.qs

    paginator = Paginator(allLocais, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    edicifioid__nome_edificio = request.GET.get('edicifioid__nome_edificio')
    campusid__nome = request.GET.get('campusid__nome')
    indoor = request.GET.get('indoor')
    context = {'allCampus': allCampus, 
            'allLocais' : allLocais, 
            'page_obj': page_obj,
            'myFilter' : myFilter, 
            'edicifioid__nome_edificio' : edicifioid__nome_edificio, 
            'campusid__nome' : campusid__nome,
            'localTipoSearched': indoor,
            'order_by' : order_by, 
            'direction' : direction}
    return render(request, 'atividades/ShowLocais.html', context)

#upadates the fields of a spcific local
@login_required()
@permission_required('atividades.change_local', raise_exception=True)
def updateLocal(request, id):
    dados_Local = Local.objects.get(id = id)

    form = LocalForm(request.GET or None, instance= dados_Local)

    allCampus = Campus.objects.all()
    allEdificios = Edificio.objects.filter(campusid=dados_Local.campusid.id)

    
    if request.method == "POST":    
        form = LocalForm(request.POST or None, request.FILES or None, instance= dados_Local)    
        if form.is_valid():
            form.save()
            return  redirect('atividades:allLocais')
    
    context = {'allCampus' : allCampus, 'allEdificios' : allEdificios, 'local' : dados_Local, 'form' : form}
    return render(request, 'atividades/EditarLocal.html', context)


#deletes a local
@login_required()
@permission_required('atividades.delete_local', raise_exception=True)
def deleteLocal(request, id):
    dados_local = Local.objects.get(id = id)
    atividades = Atividade.objects.filter(localid= dados_local.id)
    for a in atividades:
        a.localid = None
        a.validada = -1
        a.save()
    dados_local.delete()
    return redirect('atividades:allLocais')

#Creates new atvidade
@login_required()
@permission_required('atividades.add_atividade', raise_exception=True)
def createAtividade(request):

    try: 
        diaAberto = DiaAberto.objects.all()[0]
    except IndexError:
        diaAberto = None

    data_atual = datetime.datetime.today().strftime('%Y-%m-%d')

    if diaAberto.data_inicio_propor_atividades.strftime('%Y-%m-%d') <= data_atual and diaAberto.data_fim_propor_atividades.strftime('%Y-%m-%d') >= data_atual:
        saved = False

        form = AtividadeForm(request.GET or None)
        tematicaformset = AtividadeTematicaFormset(request.GET or None, prefix='formTematica')
        materialformset = AtividadeMaterialFormset(request.GET or None, prefix='formMaterial')
        sessaoformset = AtividadeSessaoFormset(request.GET or None, prefix='formSessao')
        
        if request.method == "POST":
            
            form = AtividadeForm(request.POST)
            tematicaformset = AtividadeTematicaFormset(request.POST, prefix='formTematica')
            materialformset = AtividadeMaterialFormset(request.POST, prefix='formMaterial')
            sessaoformset = AtividadeSessaoFormset(request.POST, prefix='formSessao') 

            if form.is_valid() and materialformset.is_valid() and tematicaformset.is_valid() and sessaoformset.is_valid():
                utilizador = request.user
                atividade = form.save(commit=False)
                atividade.utilizadorid = utilizador
                atividade.unidadeorganicaid = utilizador.unidade_organicaid
                atividade.validada = -1
                atividade.editavel = True
                atividade.save()
                
                
                for form in materialformset:
                     if form.cleaned_data.get('materialid') and form.cleaned_data.get('quantidade') and form.cleaned_data.get('quantidade')>0:
                        material = AtividadeMaterial(
                            atividadeid = atividade,
                            materialid = form.cleaned_data['materialid'],
                            quantidade = form.cleaned_data['quantidade']
                        )
                        material.save()
                for form in tematicaformset:
                    tematica = AtividadeTematica(
                        atividadeid = atividade,
                        tematicaid = form.cleaned_data['tematicaid']
                    )
                    tematica.save()
                for form in sessaoformset: 
                    sessao = SessaoAtividade(
                        atividadeid = atividade,
                        sessaoid = form.cleaned_data['sessaoid'],
                        data = form.cleaned_data['data']
                    )
                    sessao.save()
                saved = True
                
                form = AtividadeForm(request.GET or None)
                tematicaformset = AtividadeTematicaFormset(request.GET or None, prefix='formTematica')
                materialformset = AtividadeMaterialFormset(request.GET or None, prefix='formMaterial')
                sessaoformset = AtividadeSessaoFormset(request.GET or None, prefix='formSessao')
        
        context = { 'form' : form, 
                    'saved' : saved, 
                    'AtividadeTematicaFormset' : tematicaformset, 
                    'AtividadeMaterialFormset' : materialformset,
                    'AtividadeSessaoFormset' : sessaoformset,
                }  
        return render(request, 'atividades/AdicionarAtividade.html', context)
    else:
        return redirect(reverse('atividades:allAtividades'))

#show all atividade
@login_required()
@permission_required('atividades.view_atividade', raise_exception=True)
def showAtividades(request):
    if request.user.user_type == 0b10000:
        allAtividades = Atividade.objects.all()
    elif request.user.user_type == 0b00001:
        allAtividades = Atividade.objects.filter(unidadeorganicaid = request.user.unidade_organicaid)
    else:
        allAtividades = Atividade.objects.filter(utilizadorid=request.user)

    allCampus = Campus.objects.all()
    allEdificios = Edificio.objects.all()
    allTematicaAtividade = AtividadeTematica.objects.all()
    allSessaoAtividade = SessaoAtividade.objects.all()

    daysDiaAberto = []
    try:
        diaAberto = DiaAberto.objects.all()[0]
        start_date = diaAberto.data_inicio
        end_date = diaAberto.data_fim
        current_date = start_date
        daysDiaAberto.append(start_date)
        while current_date <  end_date:
            current_date += datetime.timedelta(days=1)
            daysDiaAberto.append(current_date)
    except IndexError:
        diaAberto = None

    data_atual = datetime.date.today()

    if diaAberto.data_inicio_propor_atividades <= data_atual and diaAberto.data_fim_propor_atividades >= data_atual:
        inDate = True
    else:
        inDate = False

    myFilter = AtividadeFilter(request.GET, queryset=allAtividades)
    
    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = Lower(order_by)
        if direction == 'desc':
            ordering = '-{}'.format(order_by)
        allAtividades = myFilter.qs.order_by(ordering)
    else:
        allAtividades = myFilter.qs

    paginator = Paginator(allAtividades, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    allMateriais = {}
    #Gets all materiais that are in the atividades of page_obj
    for atividade in page_obj:
        materiais = AtividadeMaterial.objects.filter(atividadeid = atividade.id)
        if materiais:
            allMateriais[atividade.id] = materiais
        

    nome = request.GET.get('nome')
    tipo_atividade = request.GET.get('tipo_atividade')
    validada = request.GET.get('validada')
    sessao_gte = request.GET.get('sessao_gte')
    sessao_lte = request.GET.get('sessao_lte')
    data = request.GET.get('data')
    
    try:
        localcampusSearched =  int(request.GET.get('localcampus'))
    except TypeError:
        localcampusSearched = None

    try:
        localedificioSearched = int(request.GET.get('localedicifio'))
    except TypeError:
        localedificioSearched = None

    print(diaAberto.data_inicio_propor_atividades)

    context = {
        'page_obj': page_obj, 
        'allCampus' : allCampus, 
        'allEdificios' : allEdificios,
        'listTematica' : allTematicaAtividade, 
        'listMaterial' : allMateriais,
        'listSessao' : allSessaoAtividade, 
        'nome' : nome, 
        'tipo_atividade' : tipo_atividade,
        'validada' : validada, 
        'localcampusSearched' : localcampusSearched,
        'localedificioSearched': localedificioSearched,
        'daysDiaAberto' : daysDiaAberto, 
        'sessao_gte' : sessao_gte, 
        'sessao_lte' : sessao_lte,
        'order_by' : order_by, 
        'direction' : direction,
        'sessao_gte' : sessao_gte,
        'sessao_lte' : sessao_lte,
        'data' : data,
        'diaAberto' : diaAberto,
        'inDate' : inDate
        }
    return render(request, 'atividades/ShowAtividades.html', context)

def showDetailsAtividade(request, id):
    allDetailsAtividade = Atividade.objects.get(id = id)
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    allLocais = Local.objects.all()
    listTematica = []        
    for tematica in AtividadeTematica.objects.filter(atividadeid = id):
            listTematica.append(tematica.tematicaid.nome)
    listMaterial = []        
    for material in AtividadeMaterial.objects.filter(atividadeid = id):
            listMaterial.append((material.materialid.nome, material.quantidade))
    context = {'allLocais' : allLocais, 'allUnidadeOrganicas' : allUnidadeOrganicas, 'atividade' : allDetailsAtividade,
    'listTematica' : listTematica, 'listMaterial' : listMaterial}
    return render(request, 'atividades/ShowDetailsAtividade.html', context)


#upadates the fields of a spcific atividade
@login_required()
@permission_required('atividades.change_atividade', raise_exception=True)
def updateAtividade(request, id):

    try: 
        diaAberto = DiaAberto.objects.all()[0]
    except IndexError:
        diaAberto = None

    data_atual = datetime.datetime.today().strftime('%Y-%m-%d')

    if diaAberto.data_inicio_propor_atividades.strftime('%Y-%m-%d') <= data_atual and diaAberto.data_fim_propor_atividades.strftime('%Y-%m-%d') >= data_atual:

        dados_Atividade = Atividade.objects.get(id = id)
        tematica = AtividadeTematica.objects.filter(atividadeid = id)
        material = AtividadeMaterial.objects.filter(atividadeid = id)
        sessao = SessaoAtividade.objects.filter(atividadeid = id)

        AtividadeTematicaFormset = formset_factory(AtividadeTematicaForm, extra=0)
        if not material:
            AtividadeMaterialFormset = formset_factory(AtividadeMaterialForm, extra=1)
        else:
             AtividadeMaterialFormset = formset_factory(AtividadeMaterialForm, extra=0)
        AtividadeSessaoFormset = formset_factory(AtividadeSessaoForm, extra=0)

        if request.method == 'GET':
            form = AtividadeForm(instance=dados_Atividade)
            tematicaformset = AtividadeTematicaFormset(initial = [{'tematicaid': t.tematicaid.id} for t in tematica], prefix='formTematica')
            materialformset = AtividadeMaterialFormset(initial = [{'materialid': m.materialid.id, 'quantidade': m.quantidade} for m in material], prefix='formMaterial')
            sessaoformset = AtividadeSessaoFormset(initial = [{'sessaoid': s.sessaoid.id, 'data': s.data} for s in sessao], prefix='formSessao')
        elif request.method == 'POST':
            form = AtividadeForm(request.POST, instance = dados_Atividade)

            tematicaformset = AtividadeTematicaFormset(request.POST, initial = [{'tematicaid': t.tematicaid.id} for t in tematica], prefix='formTematica')
            materialformset = AtividadeMaterialFormset(request.POST, initial = [{'materialid': m.materialid.id, 'quantidade': m.quantidade} for m in material], prefix='formMaterial')
            sessaoformset = AtividadeSessaoFormset(request.POST, initial = [{'sessaoid': s.sessaoid.id, 'data': s.data} for s in sessao], prefix='formSessao')

            if form.is_valid() and tematicaformset.is_valid() and materialformset.is_valid() and sessaoformset.is_valid():
                f = form.save(commit=False)
                f.validada = -1
                f.localid = None
                f.save()
                
                #Atividade Tematica
                #Save and add
                if len(tematicaformset) >= len(tematica):
                    for index, form in enumerate(tematicaformset):
                        if index < len(tematica):
                            tematica[index].tematicaid = form.cleaned_data['tematicaid']
                            tematica[index].atividadeid = f
                            tematica[index].save()
                        else:
                            new_tematica = AtividadeTematica(
                                atividadeid = f,
                                tematicaid = form.cleaned_data['tematicaid']
                            )
                            new_tematica.save()

                #Save and delete
                else:
                    for index, t in enumerate(tematica):
                        if index < len(tematicaformset):
                            t.tematicaid = tematicaformset[index].cleaned_data['tematicaid']
                            t.atividadeid = f
                            t.save()
                        else:
                            t.delete()

            #Atividade Material
            #Save and add          
                if len(materialformset) >= len(material):
                    for index, form in enumerate(materialformset):
                        if form.cleaned_data.get('materialid') and form.cleaned_data.get('quantidade') and form.cleaned_data.get('quantidade')>0:
                            if index < len(material):
                                material[index].materialid = form.cleaned_data['materialid']
                                material[index].quantidade = form.cleaned_data['quantidade']
                                material[index].atividadeid = f
                                material[index].save()
                            else:
                                new_material = AtividadeMaterial(
                                    atividadeid = f,
                                    materialid = form.cleaned_data['materialid'],
                                    quantidade = form.cleaned_data['quantidade']
                                )
                                new_material.save()
                #Save and delete
                else:
                    for index, m in enumerate(material):
                        if materialformset[index].cleaned_data.get('materialid') and form.cleaned_data.get('quantidade')>0:
                            if index < len(materialformset):
                                m.materialid = materialformset[index].cleaned_data['materialid']
                                m.quantidade = materialformset[index].cleaned_data['quantidade']
                                m.atividadeid = f
                                m.save()
                            else:
                                m.delete()
                                
                #Atividade Sessao
                #Save and add
                if len(sessaoformset) >= len(sessao):
                    for index, form in enumerate(sessaoformset):
                        if index < len(sessao):
                            sessao[index].sessaoid = form.cleaned_data['sessaoid']
                            sessao[index].data = form.cleaned_data['data']
                            sessao[index].atividadeid = f
                            sessao[index].save()
                        else:
                            new_sessao = SessaoAtividade(
                                atividadeid = f,
                                sessaoid = form.cleaned_data['sessaoid'],
                                data = form.cleaned_data['data']
                            )
                            new_sessao.save()
                #Save and delete
                else:
                    for index, s in enumerate(sessao):
                        if index < len(sessaoformset):
                            s.sessaoid = sessaoformset[index].cleaned_data['sessaoid']
                            s.data = sessaoformset[index].cleaned_data['data']
                            s.atividadeid = f
                            s.save()
                        else:
                            s.delete()

                return  redirect('atividades:allAtividades')

        context = { 'atividade' : dados_Atividade, 
                    'AtividadeForm': form,
                    'AtividadeTematicaFormset' : tematicaformset,
                    'AtividadeMaterialFormset' : materialformset,
                    'AtividadeSessaoFormset' : sessaoformset,
                }

        return render(request, 'atividades/EditarAtividade.html', context)
    else:
        return redirect(reverse('atividades:allAtividades'))
    
#deletes a atividade
@login_required()
@permission_required('atividades.delete_atividade', raise_exception=True)
def deleteAtividade(request, id):

    try: 
        diaAberto = DiaAberto.objects.all()[0]
    except IndexError:
        diaAberto = None

    data_atual = datetime.datetime.today().strftime('%Y-%m-%d')

    if diaAberto.data_inicio_propor_atividades.strftime('%Y-%m-%d') <= data_atual and diaAberto.data_fim_propor_atividades.strftime('%Y-%m-%d') >= data_atual:   
        dados_atividade = Atividade.objects.get(id = id)
        dados_atividade.delete()
        return HttpResponseRedirect(reverse('atividades:allAtividades'))
    else:
        return redirect(reverse('atividades:allAtividades'))

#request atividade
def requestAtividade(request):
	dados_atividade = atividade.objects.get(id = id)
	dados_atividade.editavel = True
	#add later
	return 0

@login_required()
@permission_required('atividades.validates_atividade', raise_exception=True)
def recuseAtividade(request, id):

    try: 
        diaAberto = DiaAberto.objects.all()[0]
    except IndexError:
        diaAberto = None

    data_atual = datetime.datetime.today().strftime('%Y-%m-%d')

    if diaAberto.data_inicio_propor_atividades.strftime('%Y-%m-%d') <= data_atual and diaAberto.data_fim_propor_atividades.strftime('%Y-%m-%d') >= data_atual:
        dados_atividade = Atividade.objects.get(id = id)
        dados_atividade.validada = 0 
        dados_atividade.save()
        return redirect('atividades:allAtividades')
    else:
        return redirect(reverse('atividades:allAtividades'))

@login_required()
@permission_required('atividades.atribuir_local', raise_exception=True)
def atribuirLocal(request, id):

    try: 
        diaAberto = DiaAberto.objects.all()[0]
    except IndexError:
        diaAberto = None

    data_atual = datetime.datetime.today().strftime('%Y-%m-%d')

    if diaAberto.data_inicio_propor_atividades.strftime('%Y-%m-%d') <= data_atual and diaAberto.data_fim_propor_atividades.strftime('%Y-%m-%d') >= data_atual:
        dados_atividade = Atividade.objects.get(id = id)
        allCampus = Campus.objects.all()
        allTematicaAtividade = AtividadeTematica.objects.all()
        allMaterialAtividade = AtividadeMaterial.objects.all()
        listMateriais = []
        for material in allMaterialAtividade:
            if material.atividadeid.id == dados_atividade.id:
                listMateriais.append(material)
        allSessaoAtividade = SessaoAtividade.objects.all()

        try:
            allEdificios = Edificio.objects.filter(campusid = allCampus[0].id)
        except IndexError:
            allEdificios = None
        
        try:
            allLocais = Local.objects.filter(edicifioid = allEdificios[0].id)
        except IndexError: 
            allLocais = None

        if request.method == 'POST':
            indoor = request.POST.get('indoor')
            if indoor == "True":
                dados_atividade.localid = Local.objects.get(id = request.POST.get("localid_interior"))
            else:
                dados_atividade.localid = Local.objects.get(id = request.POST.get("localid_exterior"))
            dados_atividade.validada = 1
            dados_atividade.save()
            return redirect('atividades:allAtividades')

        context = { 'allLocais' : allLocais, 
                    'allEdificios' : allEdificios, 
                    'allCampus' : allCampus, 
                    'atividade' : dados_atividade, 
                    'listTematica' : allTematicaAtividade, 
                    'listMaterial' : listMateriais, 
                    'listSessao' : allSessaoAtividade
                }
        return render(request, 'atividades/AtribuirLocal.html', context)
    else:
        return redirect(reverse('atividades:allAtividades'))

@login_required()
@permission_required('atividades.alterar_local', raise_exception=True)
def updateAtribuirLocal(request, id):

    try: 
        diaAberto = DiaAberto.objects.all()[0]
    except IndexError:
        diaAberto = None

    data_atual = datetime.datetime.today().strftime('%Y-%m-%d')

    if diaAberto.data_inicio_propor_atividades.strftime('%Y-%m-%d') <= data_atual and diaAberto.data_fim_propor_atividades.strftime('%Y-%m-%d') >= data_atual:
        dados_atividade = Atividade.objects.get(id = id)
        local = dados_atividade.localid
        allCampus = Campus.objects.all()
        allEdificios = Edificio.objects.filter(campusid=local.campusid)
        locais = Local.objects.filter(campusid=local.campusid).filter(edicifioid=local.edicifioid)
        locais_exterior = Local.objects.filter(campusid = local.campusid).filter(indoor=False)
        allTematicaAtividade = AtividadeTematica.objects.all()
        allMaterialAtividade = AtividadeMaterial.objects.all()
        allSessaoAtividade = SessaoAtividade.objects.all()

        if request.method == "POST":
            if form.is_valid():
                dados_atividade.localid = form.cleaned_data['localid']
                dados_atividade.save()
                return  redirect('atividades:allAtividades')

        context = { 'allLocais' : locais, 
                    'allLocaisExt': locais_exterior,
                    'allEdificios' : allEdificios, 
                    'allCampus' : allCampus, 
                    'atividade' : dados_atividade, 
                    'listTematica' : allTematicaAtividade, 
                    'listMaterial' : allMaterialAtividade, 
                    'listSessao' : allSessaoAtividade,
                    'local' : local
                }
        return render(request, 'atividades/AtribuirLocal.html', context)
    else:
        return redirect(reverse('atividades:allAtividades'))

def getEdificio(request, campusid):
    dados_edificio = [(e.id, e.nome_edificio) for e in Edificio.objects.filter(campusid = campusid)]
    return JsonResponse(dict(dados_edificio))

def getEdificioCampus(request, campusid):
    dados_edificio = [(e.id, e.nome_edificio + ", " + str(e.campusid))for e in Edificio.objects.filter(campusid = campusid)]
    return JsonResponse(dict(dados_edificio))

def getLocal(request, edificioid):
    dados_local = [(l.id, "Andar " + str(l.andar) + ", " + "Sala " + str(l.sala))for l in Local.objects.filter(edicifioid = edificioid)]
    return JsonResponse(dict(dados_local))

def getLocalExterior(request, campusid):
    dados_local = [(l.id, str(l.nome_local_exterior)) for l in Local.objects.filter(campusid = campusid).filter(indoor=False)]
    return JsonResponse(dict(dados_local))

def getDescricaoLocal(request, localid):
    l = Local.objects.get(id = localid)
    dados_local = [(l.id, str(l.descricao))]
    return JsonResponse(dict(dados_local))

def getLocalImage(request, localid):
    l = Local.objects.get(id = localid)
    dados_local = [(l.id, str(l.mapa_sala))]
    return JsonResponse(dict(dados_local))
#-----------------------------------------------------
# Tematica CRUD- Create Read Update Delete
#----------------------------------------------------------------
#showAll
@login_required()
@permission_required('atividades.view_tematica', raise_exception=True)
def showTematicas(request):
    allTematicas = Tematica.objects.all()
    myFilter = TematicaFilter(request.GET, queryset=allTematicas)
    
    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = Lower(order_by)
        if direction == 'desc':
            ordering = '-{}'.format(order_by)
        allTematicas = myFilter.qs.order_by(ordering)
    else:
        allTematicas = myFilter.qs

    paginator = Paginator(allTematicas, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nome = request.GET.get('nome')
    context = {
                'allTematicas': allTematicas, 
                'page_obj': page_obj, 
                'myFilter' : myFilter, 
                'nome' : nome,
                'order_by' : order_by, 
                'direction' : direction
                }
    return render(request, 'atividades/ShowTematicas.html', context)

@login_required()
@permission_required('atividades.add_tematica', raise_exception=True)
def addTematica(request):
    form = TematicaForm()
    saved = False
    if request.method == "POST":
        form = TematicaForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
    context = {'form' : form, 'saved' : saved}
    return render(request, 'atividades/AdicionarTematica.html', context)

@login_required()
@permission_required('atividades.change_tematica', raise_exception=True)
def updateTematica(request, id):
    dados = Tematica.objects.get(id = id)
    form = TematicaForm(request.POST or None, instance=dados)
    if request.method == "POST":
        #form = TematicaForm(request.POST, instance = dados)
        if form.is_valid():
            form.save()
            return  redirect('atividades:allTematicas')
    
    context = {'tematica': dados, 'form' : form}
    return render(request, 'atividades/EditarTematica.html', context)

@login_required()
@permission_required('atividades.delete_tematica', raise_exception=True)
def deleteTematica(request, id):
    dados = Tematica.objects.get(id = id)
    dados.delete()
    return HttpResponseRedirect(reverse('atividades:allTematicas'))

#-----------------------------------------------------
# Material CRUD- Create Read Update Delete
#----------------------------------------------------------------
@login_required()
@permission_required('atividades.add_material', raise_exception=True)
def createMaterial(request):
    form = MaterialForm()
    saved = False
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
            form = MaterialForm()
    context = {'form' : form, 'saved' : saved}
    return render(request, 'atividades/AdicionarMaterial.html', context)

@login_required()
@permission_required('atividades.view_material', raise_exception=True)
def showMateriais(request):
    allMateriais = Material.objects.all()
    myFilter = MaterialFilter(request.GET, queryset=allMateriais)

    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = Lower(order_by)
        if direction == 'desc':
            ordering = '-{}'.format(order_by)
        allMateriais = myFilter.qs.order_by(ordering)
    else:
        allMateriais = myFilter.qs

    paginator = Paginator(allMateriais, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nome = request.GET.get('nome')
    context = {'allMateriais' : allMateriais, 'page_obj': page_obj, 'myFilter' : myFilter, 
    'nome' : nome, 'order_by' : order_by, 'direction' : direction}
    return render(request, 'atividades/ShowMateriais.html', context)

@login_required()
@permission_required('atividades.change_material', raise_exception=True)
def updateMaterial(request, id):
    dados_Material = Material.objects.get(id = id)
    form = MaterialForm(request.POST or None, instance = dados_Material)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('atividades:allMateriais')

    return render(request, 'atividades/EditarMaterial.html', {'form' : form, 'material' : dados_Material})

@login_required()
@permission_required('atividades.delete_material', raise_exception=True)
def deleteMaterial(request, id):
    dados_Material = Material.objects.get(id = id)
    dados_Material.delete()
    return HttpResponseRedirect(reverse('atividades:allMateriais'))

   
#-----------------------------------------------------------------------------
# Sessao CRUD - Create Read Update Delete
#-------------------------------------------------------------------------

@login_required()
@permission_required('atividades.view_sessao', raise_exception=True)
def showSessoes(request):
    allSessoes = Sessao.objects.all()
    myFilter = SessaoFilter(request.GET, queryset=allSessoes)

    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = Lower(order_by)
        if direction == 'desc':
            ordering = '-{}'.format(order_by)
        allSessoes = myFilter.qs.order_by(ordering)
    else:
        allSessoes = myFilter.qs

    paginator = Paginator(allSessoes, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    hora_de_inicio = request.GET.get('hora_de_inicio')
    context = {
                'allSessoes' : allSessoes, 
                'page_obj': page_obj, 
                'myFilter' : myFilter, 
                'hora_de_inicio' : hora_de_inicio,
                'order_by' : order_by, 
                'direction' : direction,
                'sessao_gte' : request.GET.get('sessao_gte'),
                'sessao_lte' : request.GET.get('sessao_lte')
                }
    return render(request, 'atividades/ShowHorarioSessao.html', context)

@login_required()
@permission_required('atividades.add_sessao', raise_exception=True)
def addSessao(request):
    form = SessaoForm()
    saved = False
    if request.method == "POST":
        form = SessaoForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
            form = SessaoForm()
    context = {'form' : form, 'saved' : saved}
    return render(request, 'atividades/AdicionarHorarioSessao.html', context)

@login_required()
@permission_required('atividades.change_sessao', raise_exception=True)
def updateSessao(request, id):
    dados = Sessao.objects.get(id=id)
    form = SessaoForm(request.POST or None, instance=dados)
    if request.method == "POST":
        #form = SessaoForm(request.POST, instance=dados)
        if form.is_valid():
            form.save()
            return redirect('atividades:allSessoes')

    return render(request,'atividades/EditarHorarioSessao.html' , {'form' : form, 'sessao':dados})

@login_required()
@permission_required('atividades.delete_sessao', raise_exception=True)
def deleteSessao(request, id):
    dados = Sessao.objects.get(id=id)
    dados.delete()
    return redirect('atividades:allSessoes')


    