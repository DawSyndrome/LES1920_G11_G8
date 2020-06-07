from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.forms import modelformset_factory, formset_factory

from .filters import UnidadeOrganicaFilter, DepartamentoFilter, LocalFilter, CampusFilter, EdificioFilter

from atividades.models import Edificio, Campus, Departamento, Local, Atividade, UnidadeOrganica, Tematica, Utilizador, AtividadeTematica, AtividadeMaterial, Sessao, SessaoAtividade, Material

from atividades.forms import EdificioForm, CampusForm, DepartamentoForm, LocalForm, AtividadeForm, UnidadeOrganicaForm, TematicaForm, AtividadeTematicaFormset, AtividadeMaterialFormset, AtividadeTematicaForm, AtividadeMaterialForm, AtividadeSessaoForm, AtividadeSessaoFormset, SessaoForm, MaterialForm

# Create your views here.

def index(request):
    #template = loader.get_template('atividades/AtividadesMain.html')
    #return HttpResponse(template.render({}, request))
    return render(request, 'atividades/AtividadesMain.html')

def gestaoAtividades(request):
    return render(request, 'atividades/GestaoAtividades.html')

def showatividades(request):
    return render(request, 'atividades/ShowAtividades.html')

def adicionaratividade(request):
    return render(request, 'atividades/AdicionarAtividade.html')

#Creates new edificio
def createEdificio(request):
    if request.method == "POST":
        form = EdificioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atividades:showCreateEdificio', saved=1)
        else:
            form = EdificioForm()
            return render(request, 'atividades/AdicionarEdificio.html')

def showCreateEdificio(request, saved=0):
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus, 'saved' : saved}
    return render(request, 'atividades/AdicionarEdificio.html', context)

#show all edificios
def showEdificios(request):
    allEdificios = Edificio.objects.all()
    allCampus = Campus.objects.all()
    # if request.GET.get('campusid'):
    #         searchCampus = request.GET.get('campusid')
    #         campus = Campus.objects.filter(nome__icontains=searchCampus)
    #         allEdificios = []
    #         for c in campus:
    #             edificios = Edificio.objects.filter(campusid=c.id)
    #             allEdificios.extend(edificios)
    # else:
    #         myFilter = EdificioFilter(request.GET, queryset=allEdificios)
    #         allEdificios = myFilter.qs
    myFilter = EdificioFilter(request.GET, queryset=allEdificios)
    allEdificios = myFilter.qs
    paginator = Paginator(allEdificios, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nome_edificio = request.GET.get('nome_edificio')
    campusid = request.GET.get('campusid')
    context = {'allCampus' : allCampus, 'allEdificios' : allEdificios, 'page_obj': page_obj,
 'nome_edificio' : nome_edificio, 'campusid' : campusid}
    return render(request, 'atividades/ShowEdificios.html', context)

#gets a edificios with a specific id 
def getEdificio(request, id):
    dados_Edificio = Edicifio.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific edificio
def updateEdificio(request, id):
    dados_Edificio = Edificio.objects.get(id = id)
    form = EdificioForm(request.POST, instance = dados_Edificio)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('atividades:allEdificios'))
    return render(request, 'atividades/EditarEdificio.html')

def showUpdateEdificio(request, id):
    dados_Edificio = Edificio.objects.get(id = id)
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus, 'edificio' : dados_Edificio}
    return render(request, 'atividades/EditarEdificio.html', context)

#deletes a edificio
def deleteEdificio(request, id):
    dados_edificio = Edificio.objects.get(id = id)
    dados_edificio.delete()
    return HttpResponseRedirect(reverse('atividades:allEdificios'))

#Creates new campus
def createCampus(request):
    if request.method == "POST":
        form = CampusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atividades:showCreateCampus', saved=1)
        else:
            form = CampusForm()
            return render(request, 'atividades/AdicionarCampus.html')

def showCreateCampus(request, saved=0):
    context = {'saved' : saved}
    return render(request, 'atividades/AdicionarCampus.html', context)

#show all campus
def showCampus(request):#, ordena):
    allCampus = Campus.objects.all()
    myFilter = CampusFilter(request.GET, queryset=allCampus)
    allCampus = myFilter.qs
    paginator = Paginator(allCampus, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nome = request.GET.get('nome')
    localizacao = request.GET.get('localizacao')
    context = {'allCampus' : allCampus, 'page_obj': page_obj,
    'myFilter' : myFilter, 'nome' : nome, 'localizacao' : localizacao}
    return render(request, 'atividades/ShowCampus.html', context)

#gets a campus with a specific id 
def getCampus(request, id):
    dados_Campus = Campus.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific campus
def updateCampus(request, id):
    dados_Campus = Campus.objects.get(id = id)
    form = CampusForm(request.POST, instance = dados_Campus)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('atividades:allCampus'))
    return render(request, 'atividades/EditarCampus.html')

def showUpdateCampus(request, id):
    dados_Campus = Campus.objects.get(id = id)
    context = {'campus' : dados_Campus}
    return render(request, 'atividades/EditarCampus.html', context)

#deletes a campus
def deleteCampus(request, id):
    dados_campus = Campus.objects.get(id = id)
    dados_campus.delete()
    return HttpResponseRedirect(reverse('atividades:allCampus'))

#Creates new unidade
def createUnidadeOrganica(request):
    if request.method == "POST":
        form = UnidadeOrganicaForm(request.POST)
        if form.is_valid():
            form.save()
            #if 'add_next' in request.POST: 
            return redirect('atividades:showCreateUnidadeOrganica', saved=1)
            #else:
                #return HttpResponseRedirect(reverse('atividades:gestaoAtividades'))
        else:
            form = UnidadeOrganicaForm()
            return render(request, 'atividades/AdicionarUO.html')

def showCreateUnidadeOrganica(request, saved=0):
    #allCampus = Campus.objects.all()
    #context = {'allCampus' : allCampus,}
    context = {'form' : UnidadeOrganicaForm(), 'saved' : saved}
    return render(request, 'atividades/AdicionarUO.html', context)

#show all unidade
def showUnidadeOrganicas(request):
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    myFilter = UnidadeOrganicaFilter(request.GET, queryset=allUnidadeOrganicas)
    allUnidadeOrganicas = myFilter.qs
    paginator = Paginator(allUnidadeOrganicas, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nome = request.GET.get('nome')
    context = {'allUnidadeOrganicas' : allUnidadeOrganicas, 'page_obj': page_obj,
    'myFilter' : myFilter, 'nome' : nome}
    return render(request, 'atividades/ShowUO.html', context)

#gets a unidade with a specific id 
def getUnidadeOrganica(request, id):
    dados_UnidadeOrganica = UnidadeOrganica.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific unidade
def updateUnidadeOrganica(request, id):
    dados_UnidadeOrganica = UnidadeOrganica.objects.get(id = id)
    form = UnidadeOrganicaForm(request.POST, instance = dados_UnidadeOrganica)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('atividades:allUnidadeOrganicas'))
    return render(request, 'atividades/EditarUO.html')

def showUpdateUnidadeOrganica(request, id):
    dados_UnidadeOrganica = UnidadeOrganica.objects.get(id = id)
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus, 'unidadeorganica' : dados_UnidadeOrganica}
    return render(request, 'atividades/EditarUO.html', context)

#deletes a unidade
def deleteUnidadeOrganica(request, id):
    dados_unidadeorganica = UnidadeOrganica.objects.get(id = id)
    dados_unidadeorganica.delete()
    return HttpResponseRedirect(reverse('atividades:allUnidadeOrganicas'))

#Creates new departamento
def createDepartamento(request):
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atividades:showCreateDepartamento', saved=1)
        else:
            form = DepartamentoForm()
            return render(request, 'atividades/AdicionarDepartamento.html')

def showCreateDepartamento(request, saved=0):
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    context = {'allUnidadeOrganicas' : allUnidadeOrganicas, 'saved' : saved}
    return render(request, 'atividades/AdicionarDepartamento.html', context)

#show all departamntos
def showDepartamentos(request):
    allDepartamentos = Departamento.objects.all()
    myFilter = DepartamentoFilter(request.GET, queryset=allDepartamentos)
    allDepartamentos = myFilter.qs
    paginator = Paginator(allDepartamentos, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nome = request.GET.get('nome')
    unidade_organicaid = request.GET.get('unidade_organicaid')
    context = {'allDepartamentos' : allDepartamentos, 'page_obj': page_obj,
    'myFilter' : myFilter, 'nome' : nome, 'unidade_organicaid' : unidade_organicaid}
    return render(request, 'atividades/ShowDepartamentos.html', context)

#gets a departamento with a specific id 
def getDepartamento(request, id):
    dados_Departamento = Departamento.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific departamento
def updateDepartamento(request, id):
    dados_Departamento = Departamento.objects.get(id = id)
    form = DepartamentoForm(request.POST, instance = dados_Departamento)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('atividades:allDepartamentos'))
    return render(request, 'atividades/EditarDepartamento.html')

def showUpdateDepartamento(request, id):
    dados_Departamento = Departamento.objects.get(id = id)
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    context = {'allUnidadeOrganicas' : allUnidadeOrganicas, 'departamento' : dados_Departamento}
    return render(request, 'atividades/EditarDepartamento.html', context)

#deletes a departamento
def deleteDepartamento(request, id):
    dados_departamento = Departamento.objects.get(id = id)
    dados_departamento.delete()
    return HttpResponseRedirect(reverse('atividades:allDepartamentos'))

#Creates new local
def createLocal(request):
    saved = False
    allCampus = Campus.objects.all()

    try:
        allEdificios = Edificio.objects.filter(campusid = allCampus[0].id)
    except IndexError:
        allEdificios = None

    if request.method == "POST":
        form = LocalForm(request.POST, request.FILES)
        #image = ImageForm(request.POST, request.FILES)
        print(request.FILES['mapa_sala'])
        if form.is_valid():
            print("aa")
            if form.cleaned_data['indoor'] == False:
                l = Local(campusid=form.cleaned_data['campusid'],  
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
    context = {'allCampus' : allCampus, 'allEdificios' : allEdificios, 'saved' : saved}
    return render(request, 'atividades/AdicionarLocal.html', context)

def showCreateLocal(request, saved=0):
    allEdificios = Edificio.objects.all()
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus, 'allEdificios' : allEdificios, 'saved' : saved}
    return render(request, 'atividades/AdicionarLocal.html', context)

#show all local
def showLocais(request):
    allLocais = Local.objects.all()
    allCampus = Campus.objects.all()
    myFilter = LocalFilter(request.GET, queryset=allLocais)
    allLocais = myFilter.qs
    paginator = Paginator(allLocais, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    edicifioid = request.GET.get('edicifioid')
    campusid = request.GET.get('campusid')
    context = {'allCampus': allCampus, 'allLocais' : allLocais, 'page_obj': page_obj,
    'myFilter' : myFilter, 'edicifioid' : edicifioid, 'campusid' : campusid}
    return render(request, 'atividades/ShowLocais.html', context)

#gets a local with a specific id 
def getLocal(request, id):
    dados_Local = Local.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific local
def updateLocal(request, id):
    dados_Local = Local.objects.get(id = id)
    form = LocalForm(request.POST, request.FILES)
    if form.is_valid():
        if form.cleaned_data['indoor'] == True:
            dados_Local.campusid = form.cleaned_data['campusid']
            dados_Local.indoor = form.cleaned_data['indoor']
            dados_Local.descricao = form.cleaned_data['descricao']
            dados_Local.andar = form.cleaned_data['andar']
            dados_Local.sala = form.cleaned_data['sala']
            dados_Local.edicifioid = Edificio.objects.get(id=request.POST['edicifioid'])
            if form.cleaned_data['mapa_sala'] != None:
                dados_Local.mapa_sala = form.cleaned_data['mapa_sala']
        #form.save()
        else:
            dados_Local.campusid = form.cleaned_data['campusid']
            dados_Local.indoor = form.cleaned_data['indoor']
            dados_Local.descricao = form.cleaned_data['descricao']
            dados_Local.andar = None
            dados_Local.sala = None
            dados_Local.edicifioid = None
            if form.cleaned_data['mapa_sala'] != None:
                dados_Local.mapa_sala = form.cleaned_data['mapa_sala']
        dados_Local.save()
        return  HttpResponseRedirect(reverse('atividades:allLocais'))
    return render(request, 'atividades/EditarLocal.html')

def showUpdateLocal(request, id):
    dados_Local = Local.objects.get(id = id)
    allEdificios = Edificio.objects.all()
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus, 'allEdificios' : allEdificios, 'local' : dados_Local,}
    return render(request, 'atividades/EditarLocal.html', context)

#deletes a local
def deleteLocal(request, id):
    dados_local = Local.objects.get(id = id)
    dados_local.delete()
    return HttpResponseRedirect(reverse('atividades:allLocais'))

#Creates new atvidade
def createAtividade(request):

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
            utilizador = Utilizador.objects.get(id = 1)
            atividade = form.save(commit=False)
            atividade.utilizadorid = utilizador
            atividade.unidadeorganicaid = utilizador.unidade_organicaid
            atividade.validada = -1
            atividade.editavel = True
            atividade.save()
            
            for form in materialformset:
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

#show all atividade
def showAtividades(request):
    # allAtividade = Atividade.objects.all()
    # if tipo == departamento:
    # 	dados_atividade = Atividades.objects.filter(departamento = filtro)
    # elif tipo == campus:
    # 	dados_atividade = Atividades.objects.filter(campus = filtro)
    # elif tipo == nome:
    # 	dados_atividade = Atividades.objects.filter(nome = filtro)
    # elif tipo == tipo_atividade:
    # 	dados_atividade = Atividades.objects.filter(tipo_atividade = filtro)
    # elif tipo == validada:
    # 	dados_atividade = Atividades.objects.filter(validada = filtro)
    # elif tipo == unidadeorganica:
    # 	dados_atividade = Atividades.objects.filter(unidadeorgaica = filtro)
    # if ordena == departamento:
    # 	dados_atividade_2 = Atividades.objets.order_by('departamento')
    # elif ordena == campus:
    # 	dados_atividade_2 = Atividades.objets.order_by('campus')
    # elif ordena == nome:
    # 	dados_atividade_2 = Atividades.objets.order_by('nome')
    # elif ordena == duracao:
    # 	dados_atividade_2 = Atividades.objets.order_by('duracao')
    # elif ordena == limite_de_particiantes:
    # 	dados_atividade_2 = Atividades.objets.order_by('limite_de_particiantes')
    allAtividades = Atividade.objects.all()
    paginator = Paginator(allAtividades, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    allTematicaAtividade = AtividadeTematica.objects.all()
    allMaterialAtividade = AtividadeMaterial.objects.all()
    allSessaoAtividade = SessaoAtividade.objects.all()
    # listTematica = []        
    # for tematica in AtividadeTematica.objects.filter(atividadeid = id):
    #         listTematica.append(tematica.tematicaid.nome)
    # listMaterial = []        
    # for material in AtividadeMaterial.objects.filter(atividadeid = id):
    #         listMaterial.append((material.materialid.nome, material.quantidade))
    context = {'allAtividades' : allAtividades, 'page_obj': page_obj,
    'listTematica' : allTematicaAtividade, 'listMaterial' : allMaterialAtividade,
    'listSessao' : allSessaoAtividade}
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

#gets a atividade with a specific id 
def getAtividade(request, id):
    dados_Atividade = Atividade.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific atividade
def updateAtividade(request, id):

    dados_Atividade = Atividade.objects.get(id = id)
    tematica = AtividadeTematica.objects.filter(atividadeid = id)
    material = AtividadeMaterial.objects.filter(atividadeid = id)
    sessao = SessaoAtividade.objects.filter(atividadeid = id)

    AtividadeTematicaFormset = formset_factory(AtividadeTematicaForm, extra=0)
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
    
#deletes a atividade
def deleteAtividade(request, id):
    dados_atividade = Atividade.objects.get(id = id)
    dados_atividade.delete()
    return HttpResponseRedirect(reverse('atividades:allAtividades'))

#request atividade
def requestAtividade(request):
	dados_atividade = atividade.objects.get(id = id)
	dados_atividade.editavel = True
	#add later
	return 0

#valid atividade
def validAtividade(request, id):
    dados_atividade = Atividade.objects.get(id = id)
    #form = AtividadeForm(request.POST, instance = dados_atividade)
    #if form.is_valid():
    #atividade = form.save(commit=False)
    dados_atividade.validada = 1 
    dados_atividade.save()
    return redirect('atividades:allAtividades')
    # dados_atividade = Atividade.objects.get(id = id)
    # dados_atividade.delete()
    # return HttpResponseRedirect(reverse('atividades:allAtividades'))

def recuseAtividade(request, id):
    dados_atividade = Atividade.objects.get(id = id)
    #form = AtividadeForm(request.POST, instance = dados_atividade)
    #if form.is_valid():
    #atividade = form.save(commit=False)
    dados_atividade.validada = 0 
    dados_atividade.save()
    return redirect('atividades:allAtividades')
    # dados_atividade = Atividade.objects.get(id = id)
    # dados_atividade.delete()
    # return HttpResponseRedirect(reverse('atividades:allAtividades'))

def atribuirLocal(request, id):
    dados_atividade = Atividade.objects.get(id = id)
    allCampus = Campus.objects.all()
    allTematicaAtividade = AtividadeTematica.objects.all()
    allMaterialAtividade = AtividadeMaterial.objects.all()
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
        dados_atividade.localid = Local.objects.get(id = request.POST.get("localid"))
        dados_atividade.validada = 1
        dados_atividade.save()
        return redirect('atividades:allAtividades')
    context = {'allLocais' : allLocais, 'allEdificios' : allEdificios, 'allCampus' : allCampus, 'atividade' : dados_atividade, 'listTematica' : allTematicaAtividade, 'listMaterial' : allMaterialAtividade, 'listSessao' : allSessaoAtividade}
    return render(request, 'atividades/AtribuirLocal.html', context)

def getEdificio(request, campusid):
    dados_edificio = [(e.id, e.nome_edificio)for e in Edificio.objects.filter(campusid = campusid)]
    return JsonResponse(dict(dados_edificio))

def getLocal(request, edificioid):
    dados_local = [(l.id, "Andar " + str(l.andar) + ", " + "Sala " + str(l.sala))for l in Local.objects.filter(edicifioid = edificioid)]
    return JsonResponse(dict(dados_local))
#-----------------------------------------------------
# Tematica CRUD- Create Read Update Delete
#----------------------------------------------------------------
#showAll
def showTematicas(request):
    allTematicas = Tematica.objects.all()
    context = {'allTematicas': allTematicas,}
    return render(request, 'atividades/ShowTematicas.html', context)

#Add tematica
def addTematica(request):
    form = AtividadeForm()
    saved = False
    if request.method == "POST":
        form = TematicaForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
    return render(request, 'atividades/AdicionarTematica.html', {'saved' : saved})

def updateTematica(request, id):
    dados = Tematica.objects.get(id = id)
    if request.method == "POST":
        form = TematicaForm(request.POST, instance = dados)
        if form.is_valid():
            form.save()
            return  redirect('atividades:allTematicas')
    
    context = {'tematica': dados,}
    return render(request, 'atividades/EditarTematica.html', context)

def deleteTematica(request, id):
    dados = Tematica.objects.get(id = id)
    dados.delete()
    return HttpResponseRedirect(reverse('atividades:allTematicas'))

#-----------------------------------------------------
# Material CRUD- Create Read Update Delete
#----------------------------------------------------------------
def createMaterial(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atividades:showCreateMaterial', saved=1)
        else:
            form = MaterialForm()
            return render(request, 'atividades/AdicionarMaterial.html')

def showCreateMaterial(request, saved=0):
    context = {'form' : MaterialForm(), 'saved' : saved}
    return render(request, 'atividades/AdicionarMaterial.html', context)

def showMateriais(request):
    allMateriais = Material.objects.all()
    paginator = Paginator(allMateriais, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'allMateriais' : allMateriais, 'page_obj': page_obj,}
    return render(request, 'atividades/ShowMateriais.html', context)

def updateMaterial(request, id):
    dados_Material = Material.objects.get(id = id)
    form = MaterialForm(request.POST, instance = dados_Material)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('atividades:allMateriais'))
    return render(request, 'atividades/EditarMaterial.html')

def showUpdateMaterial(request, id):
    dados_Material = Material.objects.get(id = id)
    context = {'material' : dados_Material}
    return render(request, 'atividades/EditarMaterial.html', context)

def deleteMaterial(request, id):
    dados_Material = Material.objects.get(id = id)
    dados_Material.delete()
    return HttpResponseRedirect(reverse('atividades:allMateriais'))

   
#-----------------------------------------------------------------------------
# Sessao CRUD - Create Read Update Delete
#-------------------------------------------------------------------------

def showSessoes(request):
    allSessoes = Sessao.objects.all()
    return render(request, 'atividades/ShowHorarioSessao.html', {'allSessoes': allSessoes})

def addSessao(request):

    if request.method == "POST":
        form = SessaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atividades:allSessoes')
    
    return render(request, 'atividades/AdicionarHorarioSessao.html')

def updateSessao(request, id):
    dados = Sessao.objects.get(id=id)

    if request.method == "POST":
        form = SessaoForm(request.POST, instance=dados)
        if form.is_valid():
            form.save()
            return redirect('atividades:allSessoes')

    return render(request,'atividades/EditarHorarioSessao.html' , {'sessao':dados})

def deleteSessao(request, id):
    dados = Sessao.objects.get(id=id)
    dados.delete()
    return redirect('atividades:allSessoes')


    