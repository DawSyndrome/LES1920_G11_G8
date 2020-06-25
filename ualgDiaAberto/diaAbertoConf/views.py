import datetime

from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required, permission_required

from diaAbertoConf.models import Transporte, Rota, HorarioTransporte, Ementa, Prato, Rota_Inscricao, DiaAberto
from atividades.models import Inscricao
from diaAbertoConf.forms import TransporteForm, RotaFormSet, RotaForm, HorarioTransporteForm, RotaInscForm, EmentaForm, PratoForm, DiaAbertoForm, formset_factory, PratoFormset

from diaAbertoConf.filters import RotaFilter, TransporteFilter, HorarioTransporteFilter, InscRotaFilter

# Create your views here.
def index(request):
    #template = loader.get_template('diaAbertoConf/DiaAbertoConfMain.html')
    #return HttpResponse(template.render({}, request))
    try: 
        diaAberto_data = DiaAberto.objects.all()[0]
        context = {'diaAbertoData' : diaAberto_data}
    except IndexError:
        context ={}
    return render(request, 'diaAbertoConf/Home.html',context)

@login_required()
@permission_required('diaAbertoConf.add_diaaberto', raise_exception=True)
def editConfDiaAberto(request):
    try:
        diaAberto_data = DiaAberto.objects.all()[0]
    except IndexError:
        diaAberto_data = None
    
    form = DiaAbertoForm()

    if request.method == 'POST':
        form = DiaAbertoForm( request.POST, instance=diaAberto_data)
        if form.is_valid():
            form.save()
            return  redirect('diaAbertoConf:index')

    context = {'diaAberto_data' : diaAberto_data,
                'form' : form}

    return render(request, 'diaAbertoConf/editConfig.html',context)

#---------------------------------------------------------
#Transporte CRUD- Create Read Update Delete
#--------------------------------------------------------

#show all transporteUniversidade_Horarios
@login_required()
@permission_required('diaAbertoConf.view_transporte', raise_exception=True)
def showTransportes(request):
    allTransportes = Transporte.objects.all()
    allRotas = Rota.objects.all()

    #Filtering
    transportesFiltered = TransporteFilter(request.GET, queryset=allTransportes)
    rotasFiltered = RotaFilter(request.GET, queryset=allRotas)

    #Ordering Results
    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = Lower(order_by)
        if direction == 'desc':
            ordering = '-{}'.format(order_by)

        if order_by == 'tipo_transporte':
            transportes = transportesFiltered.qs.order_by(ordering)
            rotas = rotasFiltered.qs
        else:
            transportes = transportesFiltered.qs
            rotas = rotasFiltered.qs.order_by(ordering)
    else:
        transportes = transportesFiltered.qs
        rotas = rotasFiltered.qs

    #Pagination
    paginator = Paginator(transportes, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #Gets all the dates of the diaAberto
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
        pass

    context = { 'page_obj': page_obj,
                'rotas': rotas,
                'order_by': order_by,
                'direction': direction,
                'datasDiaAberto': daysDiaAberto,
                'tipoTransporteSearched': request.GET.get('tipo_transporte'),
                'origemSearched': request.GET.get('origem'),
                'destinoSearched': request.GET.get('destino'),
                'hora_gte_Searched': request.GET.get('hora_gte'),
                'hora_lte_Searched': request.GET.get('hora_lte'),
                'dataSearched': request.GET.get('data'),
            }

    return render(request, 'diaAbertoConf/ShowTransportes.html', context)

#Creates new transporte
@login_required()
@permission_required('diaAbertoConf.add_transporte', raise_exception=True)
def createTransporte(request):
    saved = False
    horarios = HorarioTransporte.objects.all()

    if request.method == "GET":
        transporteform = TransporteForm(request.GET or None)
        rotaformset = RotaFormSet(request.GET or None)
    elif request.method == "POST":
        transporteform = TransporteForm(request.POST)
        rotaformset = RotaFormSet(request.POST)
        if transporteform.is_valid() and rotaformset.is_valid():
            transporte = transporteform.save()
            for form in rotaformset:    
                for horario in form.cleaned_data['horarioid']:
                    result = Rota(
                        horarioid= HorarioTransporte.objects.get(id=horario),
                        transporteid = transporte,
                        origem = form.cleaned_data['origem'],
                        destino = form.cleaned_data['destino'],
                        data = form.cleaned_data['data'],
                    )
                    result.save()
            saved = True
            transporteform = TransporteForm()
            rotaformset = RotaFormSet()
            
        
    return render(request, 'diaAbertoConf/AdicionarTransporte.html', {
        'transporteform' : transporteform,
        'rotaformset': rotaformset,
        'horarios': horarios,
        'saved': saved,
        })

#deletes a transporteUniversidade_Horario
@login_required()
@permission_required('diaAbertoConf.delete_transporte', raise_exception=True)
def deleteTransporte(request, id):
    dados_Transporte = Transporte.objects.get(id = id)
    dados_Transporte.delete()
    return redirect('diaAbertoConf:allTransportes')

#updates the fields of a spcific transporte

def inEntry(rota, rotaInfo):
    for ri in rotaInfo:
        if rota.origem == ri['origem'] and rota.destino == ri['destino'] and rota.data == ri['data']:
            return True
    return False

def getTotalHorarios(rotaformset):
    result = 0
    for rota in rotaformset:
        for horario in rota.cleaned_data['horarioid']:
            result+=1
    return result

@login_required()
@permission_required('diaAbertoConf.change_transporte', raise_exception=True)
def updateTransporte(request, id):
    dados_Transporte = Transporte.objects.get(id = id)
    rotas_Transporte = Rota.objects.filter(transporteid = dados_Transporte.id)
    RotaFormSet = formset_factory(RotaForm, extra=0)

    if request.method == "GET":
        arrhorarios = []
        rotaInfo = []

        for idx, currentRota in enumerate(rotas_Transporte):
            if inEntry(currentRota, rotaInfo):
                continue
            for idy, testingRota in enumerate(rotas_Transporte, start = idx):
                if currentRota.origem == testingRota.origem and currentRota.destino == testingRota.destino and currentRota.data == testingRota.data:
                    arrhorarios.append(testingRota.horarioid.id)

            entry ={'horarioid': arrhorarios, 'origem': currentRota.origem, 'destino': currentRota.destino, 'data': currentRota.data}
            rotaInfo.append(entry)
            arrhorarios = []

        rotaformset = RotaFormSet(initial = rotaInfo)
        transporteform = TransporteForm(instance=dados_Transporte)
    elif request.method == "POST":
        transporteform = TransporteForm(request.POST, instance=dados_Transporte)
        rotaformset = RotaFormSet(request.POST)
        #print(rotaformset)
        if transporteform.is_valid() and rotaformset.is_valid():
            transporteform.save()

            totalHorarios  = getTotalHorarios(rotaformset)

            if(totalHorarios <= len(rotas_Transporte)):#if there are less rotas than before or if there is the same number
                rotaform_count = 0
                h_count = 0
                for rota in rotas_Transporte:
                    if(rotaform_count < len(rotaformset)):#Edits existing rotas
                        rotaform = rotaformset[rotaform_count]

                        rota.origem = rotaform.cleaned_data['origem']
                        rota.destino = rotaform.cleaned_data['destino']
                        rota.data = rotaform.cleaned_data['data']
                        rota.horarioid = HorarioTransporte.objects.get(id=rotaform.cleaned_data['horarioid'][h_count])
                        rota.save()
                        h_count+=1

                        if(h_count == len(rotaform.cleaned_data['horarioid'])):
                            h_count = 0
                            rotaform_count+=1

                    else:#Deletes remaning rotas
                        rota.delete()
            
            else:#if there are more rotas then before, edit existing and add new ones
                rota_count = 0
                for rotaform in rotaformset:
                    for horario in rotaform.cleaned_data['horarioid']:
                        if(rota_count < len(rotas_Transporte)):#Edit existing rotas
                            rotas_Transporte[rota_count].origem = rotaform.cleaned_data['origem']
                            rotas_Transporte[rota_count].destino = rotaform.cleaned_data['destino']
                            rotas_Transporte[rota_count].data = rotaform.cleaned_data['data']
                            rotas_Transporte[rota_count].horarioid = HorarioTransporte.objects.get(id=horario)
                            rotas_Transporte[rota_count].save()
                            rota_count+=1

                        else:#Add remaining new rotas
                            newRota = Rota(
                                transporteid = dados_Transporte, 
                                horarioid = HorarioTransporte.objects.get(id=horario),
                                origem = rotaform.cleaned_data['origem'],
                                destino= rotaform.cleaned_data['destino'],
                                data= rotaform.cleaned_data['data']
                            )
                            newRota.save()

            return  redirect('diaAbertoConf:allTransportes')
    
    
    context={'transporteform': transporteform, 
             'rotaformset': rotaformset,
             'dadosTransporte': dados_Transporte}

    return render(request, 'diaAbertoConf/EditarTransporte.html', context)

#--------------------------------------------------------------
#Horario Transporte CRUD- Create Read Update Delete
#------------------------------------------------------------

#show all Horarios Transporte
@login_required()
@permission_required('diaAbertoConf.view_horariotransporte', raise_exception=True)
def showHorarios_Transporte(request):
    allHorarios_Transporte = HorarioTransporte.objects.all()
    horariosFiltered = HorarioTransporteFilter(request.GET, queryset=allHorarios_Transporte)

    #Ordering Results
    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = Lower(order_by)
        if direction == 'desc':
            ordering = '-{}'.format(order_by)

        horarios = horariosFiltered.qs.order_by(ordering)
    else:
        horarios = horariosFiltered.qs

    #Pagination
    paginator = Paginator(horarios, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { 'page_obj': page_obj,
                'hora_de_partidaSearched': request.GET.get('hora_de_partida'),
                'hora_de_chegadaSearched': request.GET.get('hora_de_chegada'),
                'order_by': order_by,
                'direction': direction,
        }

    return render(request, 'diaAbertoConf/ShowHorarioTransportes.html', context)

#Creates new Horario Transporte
@login_required()
@permission_required('diaAbertoConf.add_horariotransporte', raise_exception=True)
def createHorario_Transporte(request):
    saved = False
    form = HorarioTransporteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            saved = True    
            form = HorarioTransporteForm()
            
    return render(request, 'diaAbertoConf/AdicionarHorarioTransporte.html', {'form': form, 'saved':saved})

#updates the fields of a spcific Horario_Transporte
@login_required()
@permission_required('diaAbertoConf.change_horariotransporte', raise_exception=True)
def updateHorario_Transporte(request, id):
    dados_Horario_Transporte = HorarioTransporte.objects.get(id = id)
    form = HorarioTransporteForm(None)
    if request.method == "POST":
        form = HorarioTransporteForm(request.POST, instance = dados_Horario_Transporte)
        if form.is_valid():
            form.save()
            return redirect('diaAbertoConf:allHorarios')
    
    context = { 'horario' : dados_Horario_Transporte,
                'form': form,}
                
    return render(request, 'diaAbertoConf/EditarHorarioTransporte.html', context)

#deletes a Horario_Transporte
@login_required()
@permission_required('diaAbertoConf.delete_horariotransporte', raise_exception=True)
def deleteHorario_Transporte(request, id):
    dados_Horario_Transporte = HorarioTransporte.objects.get(id = id)
    dados_Horario_Transporte.delete()
    return redirect('diaAbertoConf:allHorarios')

#--------------------------------------------------------------------------------------
#Rotas Inscrições - CRUD
#---------------------------------------------------------------------------------------

@login_required()
@permission_required('diaAbertoConf.view_rota_inscricao', raise_exception=True)
def showInscAssociada(request, id):
    dados_rota = Rota.objects.get(id=id)
    dados_rotaInsc = Rota_Inscricao.objects.filter(rotaid = dados_rota.id)

    lugaresOcupados = 0
    for rotaInsc in dados_rotaInsc:
        lugaresOcupados += rotaInsc.num_passageiros

    #Ordering Results
    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = order_by
        if direction == 'desc':
            ordering = '-{}'.format(order_by)

        dados_rotaInsc = dados_rotaInsc.order_by(ordering)

    context = { 'dados_rota': dados_rota,
                'dados_rotaInsc': dados_rotaInsc,
                'lugaresOcupados': lugaresOcupados,
                'lugaresDisponiveis': dados_rota.transporteid.capacidade - lugaresOcupados,
                'order_by': order_by,
                'direction': direction,
            }

    return render(request, 'diaAbertoConf/ShowInscAssociada.html', context)

@login_required()
@permission_required('diaAbertoConf.add_rota_inscricao', raise_exception=True)
def createInscAssociada(request, id):
    saved = False
    dados_rota = Rota.objects.get(id=id)
    dados_rotaInsc = Rota_Inscricao.objects.filter(rotaid = dados_rota.id)
    allInsc = Inscricao.objects.filter(dia = dados_rota.data)

    inscFiltered = InscRotaFilter(request.GET, queryset=allInsc)

    numGrupoSearched = request.GET.get("num_grupo")
    escolaSearched = request.GET.get("nome_escola")

    #Ordering Results
    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if order_by:
        ordering = order_by
        if direction == 'desc':
            ordering = '-{}'.format(order_by)

        insc = inscFiltered.qs.order_by(ordering)
    else:
        insc = inscFiltered.qs

    #Pagination
    paginator = Paginator(insc, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    error = ""

    lugaresOcupados = 0
    for rotaInsc in dados_rotaInsc:
        lugaresOcupados += rotaInsc.num_passageiros

    form = RotaInscForm(request.POST or None)  

    if request.method =="POST":            
        if form.is_valid():
            num_passageiros = form.cleaned_data['num_passageiros']
            
            if num_passageiros + lugaresOcupados > dados_rota.transporteid.capacidade:
                error = "Lugares insufecientes para o número de passageiros"
            else:
                v = form.save(commit=False)
                v.rotaid = dados_rota
                v.save()
                saved = True
                form = RotaInscForm(None) 
                lugaresOcupados += num_passageiros 

    context = { 'dados_rota': dados_rota,
                'page_obj': page_obj,
                'order_by': order_by,
                'direction': direction,
                'form':form,
                'lugaresOcupados': lugaresOcupados,
                'lugaresDisponiveis': dados_rota.transporteid.capacidade - lugaresOcupados,
                'error':error,
                'numGrupoSearched': numGrupoSearched,
                'escolaSearched': escolaSearched,
                'saved': saved,
            }

    return render(request, 'diaAbertoConf/AdicionarInscAssociada.html', context)

@login_required()
@permission_required('diaAbertoConf.change_rota_inscricao', raise_exception=True)
def updateInscAssociada(request, id, idRota_Insc):
    dados_rota = Rota.objects.get(id=id)
    dadosRota_Insc = Rota_Inscricao.objects.get(id=idRota_Insc)
    grupo = dadosRota_Insc.inscricaoid

    error = ""

    all_rotaInsc = Rota_Inscricao.objects.filter(rotaid = dados_rota.id)
    
    lugaresOcupados = -dadosRota_Insc.num_passageiros
    for rotaInsc in all_rotaInsc:
        lugaresOcupados += rotaInsc.num_passageiros

    form = RotaInscForm(request.POST or None, instance=dadosRota_Insc)

    if request.method == "POST":   
        if form.is_valid():
            num_passageiros = form.cleaned_data['num_passageiros']

            if num_passageiros + lugaresOcupados > dados_rota.transporteid.capacidade:
                error = "Lugares insufecientes para o número de passageiros"
            else:
                insc = form.save(commit=False)
                insc.inscricaoid = Rota_Inscricao.objects.get(id=idRota_Insc).inscricaoid
                insc.save()
                return redirect('diaAbertoConf:showInscAssociadas', id=dados_rota.id)
    
    context = { 'dados_rota': dados_rota,
                'dadosRota_Insc': dadosRota_Insc,
                'grupo':grupo,
                'form': form,
                'lugaresOcupados': lugaresOcupados,
                'lugaresDisponiveis': dados_rota.transporteid.capacidade - lugaresOcupados,
                'error': error}

    return render(request, 'diaAbertoConf/EditarInscAssociada.html', context)

@login_required()
@permission_required('diaAbertoConf.delete_rota_inscricao', raise_exception=True)
def deleteInscAssociada(reques,id, idRota_Insc):
    dados_rotaInsc = Rota_Inscricao.objects.get(id = idRota_Insc)
    dados_rotaInsc.delete()
    return redirect('diaAbertoConf:showInscAssociadas', id=id)
 

#---------------------------------------------------------------------------------------
#Gestao de Ementas
#--------------------------------------------------------------------------------------

@login_required()
@permission_required('diaAbertoConf.view_ementa', raise_exception=True)
def gestaoEmentas(request):
    diaAberto_data = DiaAberto.objects.get(id=1)
    allEmentas = Ementa.objects.all()
    allPratos = Prato.objects.all()
    pratosType = ['Sopa','Carne','Peixe','Vegetariano','Sobremesa']
    context = {'allEmentas' : allEmentas, 'allPratos' : allPratos, 'diaAberto':diaAberto_data, 'pratosType' : pratosType}
    return render(request, 'diaAbertoConf/GestaoEmentas.html', context)

@login_required()
@permission_required('diaAbertoConf.delete_ementa', raise_exception=True)
def deleteEmenta(request, id):
    dados_Ementa = Ementa.objects.get(id = id)
    dados_Ementa.delete()
    return HttpResponseRedirect(reverse('diaAbertoConf:gestaoEmentas'))

@login_required()
@permission_required('diaAbertoConf.add_ementa', raise_exception=True)
def createEmenta(request):
    saved=False
    if request.method == "GET":
        ementaForm = EmentaForm(request.GET or None)
        pratoFormSet=PratoFormset(request.GET or None)
    elif request.method == "POST":  
        ementaForm = EmentaForm(request.POST)
        pratoFormSet=PratoFormset(request.POST)
        if ementaForm.is_valid() and pratoFormSet.is_valid():
            ementa=ementaForm.save()
            for prato in pratoFormSet:
               newPrato = prato.save(commit=False)
               newPrato.ementaid = ementa
               newPrato.save()
            saved=True   
            

    #Gets all the dates of the diaAberto
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
        pass

    context={
        'ementaform' : ementaForm,
        'pratoformset': pratoFormSet,
        'datasDiaAberto': daysDiaAberto,
        'saved' : saved,
        }  
    return render(request, 'diaAbertoConf/AdicionarEmenta.html', context)  


@login_required()
@permission_required('diaAbertoConf.change_ementa', raise_exception=True)
def EditarEmenta(request,id):
    dados_Ementa = Ementa.objects.get(id = id)
    pratos = Prato.objects.filter(ementaid = id)

    PratoFormset = formset_factory(PratoForm, extra=0)

    if request.method == "GET":
        
        form = EmentaForm(instance=dados_Ementa) 
        pratoformset= PratoFormset(initial = [{'pratoid':p.id, 'nome': p.nome, 'tipo' : p.tipo, 'descricao':p.descricao } for p in pratos])
    
    elif request.method == "POST":
        
        form = EmentaForm(request.POST,instance=dados_Ementa)
        pratoformset= PratoFormset(request.POST, initial = [{'pratoid':p.id, 'nome': p.nome, 'tipo' : p.tipo, 'descricao':p.descricao } for p in pratos])
        
        if form.is_valid() and pratoformset.is_valid():
            ementaform=form.save()

            if len(pratoformset) >= len(pratos):
                for index, form in enumerate(pratoformset):
                    if index < len(pratos):
                        pratos[index].nome = form.cleaned_data['nome']
                        pratos[index].tipo = form.cleaned_data['tipo']
                        pratos[index].descricao = form.cleaned_data['descricao']
                        pratos[index].save()
                    else:
                        new_prato = Prato(
                            ementaid=ementaform,
                            nome=form.cleaned_data['nome'],
                            tipo=form.cleaned_data['tipo'],
                            descricao=form.cleaned_data['descricao'],
                        )
                        new_prato.save()  

            else:
                for index, p in enumerate(pratos):  
                    if index < len(pratoformset): 
                        p.nome=pratoformset[index].cleaned_data['nome']
                        p.tipo=pratoformset[index].cleaned_data['tipo']
                        p.descricao=pratoformset[index].cleaned_data['descricao']
                        p.save()
                    else:
                        p.delete()   

        return redirect('diaAbertoConf:gestaoEmentas')                 
    
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
        pass

    context= { 'ementa' : dados_Ementa,
               'datasDiaAberto': daysDiaAberto,
               'pratoformset' : pratoformset,
            }

    return render(request,'diaAbertoConf/EditarEmenta.html',context)
