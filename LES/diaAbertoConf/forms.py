import datetime

from django import forms
from django.forms import ModelForm, TextInput, NumberInput, CheckboxSelectMultiple, formset_factory, modelformset_factory, Select
from django.utils.translation import gettext_lazy as _
from diaAbertoConf.models import Transporte, Rota, HorarioTransporte, Rota_Inscricao, Prato, Ementa, DiaAberto
from atividades.models import Inscricao

class TransporteForm(ModelForm):
    class Meta:
        model = Transporte
        fields =    '__all__'

        widgets = {
            'tipo_transporte' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza o tipo de transporte',
                'required' : 'required',

            }),

            'capacidade' : NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza a capacidade',
                'min' : '1',
                'required' : 'required',
            }),
        }
        labels = {
            'tipo_transporte' : _('Tipo de Transporte'),
            'capacidade' : _('Capacidade'),
        }

class RotaForm(forms.Form):
    horarioid = forms.MultipleChoiceField(
        label = 'Horario', 
        widget=forms.CheckboxSelectMultiple(),
        choices = []
        )
    origem = forms.CharField(
        label = 'Origem',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza uma origem',
                'required' : 'required',
            }
        )
    )
    destino = forms.CharField(
        label = 'Destino',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza um destino',
                'required' : 'required',
            }
        )
    )
    data = forms.DateField(
        label = 'Data',
        widget=forms.Select(
            attrs= {
                'class' : 'form-control date-Set',
                'required' : 'required',
            },
            choices=[]
        )
    )

    def __init__(self, *args, **kwargs):
        super(RotaForm, self).__init__(*args, **kwargs)

        #Gets all the dates of the diaAberto
        daysDiaAberto = []
        try:           
            diaAberto = DiaAberto.objects.all()[0]
            start_date = diaAberto.data_inicio
            end_date = diaAberto.data_fim
            current_date = start_date
            daysDiaAberto.append((start_date, start_date.strftime("%d-%m-%Y")))
            while current_date <  end_date:
                current_date += datetime.timedelta(days=1)
                daysDiaAberto.append((current_date, current_date.strftime("%d-%m-%Y")))
        except IndexError:
            pass

        my_default_errors = {
            'required': 'Tem de selecionar pelo menos um horário de transporte',
        } 

        self.fields['data'].widget.choices = daysDiaAberto
        self.fields['horarioid'].choices = [(horario.id, horario) for horario in HorarioTransporte.objects.all()]  
        self.fields['horarioid'].error_messages= my_default_errors

RotaFormSet = formset_factory(RotaForm, extra=1)

class HorarioTransporteForm(ModelForm):
    class Meta:
        model = HorarioTransporte
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        hpartida = cleaned_data.get("hora_de_partida")
        hchegada = cleaned_data.get("hora_de_chegada")

        if hpartida >= hchegada:
            raise forms.ValidationError(
                _('Hora de partida deve ser inferior à hora de chegada'),
                code='invalid'
            )

        if self.instance.id:
            for h in HorarioTransporte.objects.all():
                if h.hora_de_partida == hpartida and h.hora_de_chegada == hchegada and self.instance.id != h.id:
                    raise forms.ValidationError(
                    _('O horário que pretende editar já existe'),
                    code='invalid'
                    )
        else:
            for h in HorarioTransporte.objects.all():
                if h.hora_de_partida == hpartida and h.hora_de_chegada == hchegada:
                    raise forms.ValidationError(
                    _('O horário que pretende criar já existe'),
                    code='invalid'
                    )

class RotaInscForm(ModelForm):


    class Meta:
        model = Rota_Inscricao
        fields = ['inscricaoid', 'num_passageiros']

        widgets = { 
            'num_passageiros': NumberInput(
                attrs= {
                    'class' : 'form-control',
                    'required' : 'required',
                    'placeholder': 'Introduza o número de passageiros',
                    'min': '0',
                }),
            'inscricaoid': TextInput()
        }
        labels = {
            'num_passageiros': _('Número de passageiros'),
            'inscricaoid': _('Grupo')
        } 


class EmentaForm(ModelForm):
    class Meta:
        model = Ementa
        fields =    '__all__'


class PratoForm(ModelForm):
    class Meta:
        model = Prato
        fields = ['nome', 'tipo', 'descricao']

PratoFormset = formset_factory(PratoForm, extra=1)

class DiaAbertoForm(ModelForm):
    class Meta:
        model = DiaAberto
        fields =    '__all__'

    def clean(self):
        cleaned_data = super().clean()
        dInico = cleaned_data.get("data_inicio")
        dFim = cleaned_data.get("data_fim")
       
        dInicInsc=cleaned_data.get("data_inicio_inscricao")
        dFimInsc=cleaned_data.get("data_fim_inscricao")
        
        dIpropAtiv=cleaned_data.get("data_inicio_propor_atividades")
        dFpropAtiv=cleaned_data.get("data_fim_propor_atividades")

        if dInico > dFim:
            raise forms.ValidationError(
                ('Data de fim do Dia Aberto deve ser depois ou no mesmo dia da data de início do Dia Aberto'),
                code='invalid'
            )   

        if dInicInsc >= dFimInsc:
            raise forms.ValidationError(
                ('Data de fim do período de inscrição deve de ser depois da data de iníco do período de inscrição'),
                code='invalid'
            )  

        if dIpropAtiv >= dFpropAtiv:
            raise forms.ValidationError(
                ('Data de fim do período de proposta de atividades deve de ser depois da data de iníco do período de proposta de atividades'),
                code='invalid'
            )  

        if dInicInsc < dIpropAtiv:
            raise forms.ValidationError(
                ('Data de início do período de inscrição deve de ser depois da data de fim do período de proposta de atividades'),
                code='invalid'
            )                          
