from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

from diaAbertoConf.models import Transporte, Rota, HorarioTransporte, Ementa, Prato, Rota_Inscricao, DiaAberto
from atividades.models import Inscricao
from diaAbertoConf.forms import TransporteForm, RotaFormSet, RotaForm, HorarioTransporteForm, RotaInscForm, RotasInscFormset, EmentaForm, PratoForm, DiaAbertoForm, formset_factory

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
def showTransportes(request):
    allTransportes = Transporte.objects.all()
    allTransportesUni_Horario = Rota.objects.all()

    paginator = Paginator(allTransportes, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { 'page_obj': page_obj,
                'rotas': allTransportesUni_Horario,}
    return render(request, 'diaAbertoConf/ShowTransportes.html', context)

#Creates new transporte
def createTransporte(request):
    
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
            
            return redirect('diaAbertoConf:allTransportes')
        
    return render(request, 'diaAbertoConf/AdicionarTransporte.html', {
        'transporteform' : transporteform,
        'rotaformset': rotaformset,
        'horarios': horarios,
        })

#deletes a transporteUniversidade_Horario
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
def showHorarios_Transporte(request):
    allHorarios_Transporte = HorarioTransporte.objects.all()
    context = {'allHorarios_Transporte': allHorarios_Transporte,}
    return render(request, 'diaAbertoConf/ShowHorarioTransportes.html', context)

#Creates new Horario Transporte
def createHorario_Transporte(request):

    form = HorarioTransporteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('diaAbertoConf:allHorarios')
    
    return render(request, 'diaAbertoConf/AdicionarHorarioTransporte.html', {'form': form})

#updates the fields of a spcific Horario_Transporte
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
def deleteHorario_Transporte(request, id):
    dados_Horario_Transporte = HorarioTransporte.objects.get(id = id)
    dados_Horario_Transporte.delete()
    return redirect('diaAbertoConf:allHorarios')

#--------------------------------------------------------------------------------------
#Rotas Inscrições - CRUD
#---------------------------------------------------------------------------------------

def showInscAssociada(request, id):
    dados_rota = Rota.objects.get(id=id)
    dados_rotaInsc = Rota_Inscricao.objects.filter(rotaid = dados_rota.id)

    lugaresOcupados = 0
    for rotaInsc in dados_rotaInsc:
        lugaresOcupados += rotaInsc.num_passageiros

    context = { 'dados_rota': dados_rota,
                'dados_rotaInsc': dados_rotaInsc,
                'lugaresOcupados': lugaresOcupados}

    return render(request, 'diaAbertoConf/ShowInscAssociada.html', context)

def createInscAssociada(request, id):
    dados_rota = Rota.objects.get(id=id)
    dados_rotaInsc = Rota_Inscricao.objects.filter(rotaid = dados_rota.id)

    error = ""

    lugaresOcupados = 0
    for rotaInsc in dados_rotaInsc:
        lugaresOcupados += rotaInsc.num_passageiros

    if request.method == "GET":  
        formset = RotasInscFormset(queryset=Rota_Inscricao.objects.none(), form_kwargs={'choices':[(insc.id, insc) for insc in Inscricao.objects.filter(dia = dados_rota.data)]})
    elif request.method =="POST":
        formset = RotasInscFormset(request.POST, form_kwargs={'choices':[(insc.id, insc) for insc in Inscricao.objects.filter(dia = dados_rota.data)]})        
                
        if formset.is_valid():
            num_passageiros = 0
            for form in formset:
                num_passageiros += form.cleaned_data['num_passageiros']

            if num_passageiros + lugaresOcupados > dados_rota.transporteid.capacidade:
                error = "Lugares insufecientes para o número de passageiros"
            else:
                for form in formset:
                    v = form.save(commit=False)
                    v.rotaid = dados_rota
                    v.save()
                return redirect('diaAbertoConf:showInscAssociadas', id=dados_rota.id)

    context = { 'dados_rota': dados_rota,
                'formset':formset,
                'lugaresOcupados': lugaresOcupados,
                'error':error}

    return render(request, 'diaAbertoConf/AdicionarInscAssociada.html', context)

def updateInscAssociada(request, id, idRota_Insc):
    dados_rota = Rota.objects.get(id=id)
    dadosRota_Insc = Rota_Inscricao.objects.get(id=idRota_Insc)

    error = ""

    all_rotaInsc = Rota_Inscricao.objects.filter(rotaid = dados_rota.id)
    lugaresOcupados = -dadosRota_Insc.num_passageiros
    for rotaInsc in all_rotaInsc:
        lugaresOcupados += rotaInsc.num_passageiros

    if request.method == "GET":
        form = RotaInscForm(initial={'inscricaoid': dadosRota_Insc.inscricaoid.id, 'num_passageiros': dadosRota_Insc.num_passageiros}, choices =[(insc.id, insc) for insc in Inscricao.objects.filter(dia = dados_rota.data)])   
    elif request.method == "POST":
        form = RotaInscForm(request.POST, instance=dadosRota_Insc, choices =[(insc.id, insc) for insc in Inscricao.objects.filter(dia = dados_rota.data)])
        
        if form.is_valid():
            num_passageiros = form.cleaned_data['num_passageiros']

            if num_passageiros + lugaresOcupados > dados_rota.transporteid.capacidade:
                error = "Lugares insufecientes para o número de passageiros"
            else:
                form.save()
                return redirect('diaAbertoConf:showInscAssociadas', id=dados_rota.id)
    
    context = { 'dados_rota': dados_rota,
                'dadosRota_Insc': dadosRota_Insc,
                'form': form,
                'lugaresOcupados': lugaresOcupados,
                'error': error}
    return render(request, 'diaAbertoConf/EditarInscAssociada.html', context)

def deleteInscAssociada(reques,id, idRota_Insc):
    dados_rotaInsc = Rota_Inscricao.objects.get(id = idRota_Insc)
    dados_rotaInsc.delete()
    return redirect('diaAbertoConf:showInscAssociadas', id=id)
 

#---------------------------------------------------------------------------------------
#Gestao de Ementas
#--------------------------------------------------------------------------------------

def gestaoEmentas(request):
    allEmentas = Ementa.objects.all()
    context = {'allEmentas' : allEmentas,}
    return render(request, 'diaAbertoConf/GestaoEmentas.html', context)

def deleteEmenta(request, id):
    dados_Ementa = Ementa.objects.get(id = id)
    dados_Ementa.delete()
    return HttpResponseRedirect(reverse('diaAbertoConf:gestaoEmentas'))

def newEmenta(request):
    if request.method == "POST":
        form = EmentaForm(request.POST)
        if form.is_valid():
            ementaData=form.save()
            #add later
            return HttpResponseRedirect(reverse('diaAbertoConf:showNewPratos',args=(),kwargs={'id': ementaData.id}))
        else:
            form = EmentaForm()
        #add later
        return render(request, 'diaAbertoConf/AdicionarEmenta.html')

def showNewEmenta(request):
     return render(request, 'diaAbertoConf/AdicionarEmenta.html')

def showNewPratos(request, id):
    dados_Ementa = Ementa.objects.get(id = id)
    context={ 'ementaData': dados_Ementa,}
    return render(request, 'diaAbertoConf/newPratos.html',context)

def newPrato(request,id):
    dados_Ementa = Ementa.objects.get(id = id)
    context={ 'ementaData': dados_Ementa,}
    if request.method == "POST":
        form = PratoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('diaAbertoConf:showNewPratos',args=(),kwargs={'id': id}))
        else:
            form = PratoForm()
        return render(request,'diaAbertoConf/newPratos.html',context)   


def showEditEmenta(request, id):
    diaAberto_data = DiaAberto.objects.get(id=1)
    dados_Ementa = Ementa.objects.get(id = id)
    dados_Pratos = Prato.objects.filter(ementaid = id)
    context = {'ementa' : dados_Ementa, 'pratos' : dados_Pratos, 'diaAbertoData' : diaAberto_data}
    return render(request, 'diaAbertoConf/editEmenta.html', context)        

def editEmenta(request, id):
    diaAberto_data = DiaAberto.objects.get(id=1)
    dados_Ementa = Ementa.objects.get(id = id)
    dados_Pratos = Prato.objects.filter(ementaid = dados_Ementa.id)
    form = EmentaForm(request.POST, instance = dados_Ementa)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('diaAbertoConf:gestaoEmentas'))
    context = {'ementa' : dados_Ementa, 'pratos' : dados_Pratos,'diaAbertoData' : diaAberto_data}
    return render(request, 'diaAbertoConf/editEmenta.html', context)

def editPrato(request,id):
    dados_Prato= Prato.objects.get(id = id)
    form = PratoForm(request.POST, instance=dados_Prato)
    if form.is_valid():
        form.save()
        dados_Ementa = Ementa.objects.get(id=dados_Prato.ementaid)
        dados_Pratos_Ementa = Prato.objects.filter(ementaid = dados_Ementa.id)
        context = {'ementa' : dados_Ementa, 'pratos' : dados_Pratos_Ementa}  
        return render(request, 'diaAbertoConf/editEmenta.html', context)
    else:
       return  HttpResponseRedirect(reverse('diaAbertoConf:gestaoEmentas')) 

def deletePrato(request, id):
    diaAberto_data = DiaAberto.objects.get(id=1)
    dados_Prato = Prato.objects.get(id = id)
    dados_Ementa = Ementa.objects.get(id=dados_Prato.ementaid.id)
    dados_Prato.delete()
    dados_Pratos_Ementa = Prato.objects.filter(ementaid = dados_Ementa.id)
    context = {'ementa' : dados_Ementa, 'pratos' : dados_Pratos_Ementa, 'diaAbertoData' : diaAberto_data}  
    return render(request, 'diaAbertoConf/editEmenta.html', context)
        
