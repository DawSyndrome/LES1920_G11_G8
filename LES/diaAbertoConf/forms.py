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
        label = 'Data'
    )

    def __init__(self, *args, **kwargs):
        super(RotaForm, self).__init__(*args, **kwargs)
        self.fields['horarioid'].choices = [(horario.id, horario) for horario in HorarioTransporte.objects.all()]  

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
                _('Hora de partida deve ser inferior a hora de chegada'),
                code='invalid'
            )

class RotaInscForm(ModelForm):


    class Meta:
        model = Rota_Inscricao
        fields = ['inscricaoid', 'num_passageiros']

        widgets = { 
            'inscricaoid': Select(
                choices= [],
                attrs= {
                    'class' : 'form-control',
                    'required' : 'required',
                }),
            'num_passageiros': NumberInput(
                attrs= {
                    'class' : 'form-control',
                    'required' : 'required',
                    'placeholder': 'Introduza o número de passageiros',
                    'min': '0',
                }),
        }
        labels = {
            'inscricaoid': _('Grupo'),
            'num_passageiros': _('Número de Passageiros'),
        } 

    def __init__(self, *args, choices, **kwargs):
        
        super(RotaInscForm, self).__init__(*args, **kwargs)
        self.fields['inscricaoid'].choices = choices


RotasInscFormset = modelformset_factory(Rota_Inscricao, RotaInscForm, extra=1)


class EmentaForm(ModelForm):
    class Meta:
        model = Ementa
        fields =    '__all__'

class PratoForm(ModelForm):
    class Meta:
        model = Prato
        fields =    '__all__'
        
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
                ('Data de fim deve ser depois ou no mesmo dia da data de inicio'),
                code='invalid'
            )   

        if dInicInsc >= dFimInsc:
            raise forms.ValidationError(
                ('Data de fim do período de inscricao deve de ser depois  da data de inico do período de inscricao'),
                code='invalid'
            )  

        if dIpropAtiv >= dFpropAtiv:
            raise forms.ValidationError(
                ('Data de fim do período de proposta de atividades deve de ser depois da data de inico do período de proposta de atividades'),
                code='invalid'
            )  

        if dInicInsc < dIpropAtiv:
            raise forms.ValidationError(
                ('Data de incio do período de inscricao deve de ser depois  da data  de fim do período de proposta de atividades'),
                code='invalid'
            )                          
