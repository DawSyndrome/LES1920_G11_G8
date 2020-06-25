import datetime

from django import forms
from django.forms import ModelForm, Textarea, RadioSelect, Select, TextInput, formset_factory
from django.utils.translation import gettext_lazy as _

from tarefas.models import Tarefa
from atividades.models import Atividade, SessaoAtividade
from diaAbertoConf.models import DiaAberto

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ('descricao', 'tipoTarefa', 'nome')
        #exclude = ['utilizadorid']

        widgets= {
            'nome': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduza o nome da tarefa',
                'required': 'required',
            }),
            'descricao': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Introduza a descrição da tarefa',
                'required': 'required',
            }),
            'tipoTarefa': RadioSelect(attrs={
                'class': 'form-check-input',
                'required': 'required',
            },
                choices = (('Atividade', 'Atividade'), ('Transporte', 'Transporte'))
            )
        }

        labels= {
            'nome': _('Nome'),
            'descricao': _('Descrição'),
            'tipoTarefa': _('Tipo de Tarefa')
        }

class TarefaAtividadeForm(forms.Form):

    
    atividade = forms.CharField(
        label = 'Atividade',
        widget = Select(attrs= {
            'class' : 'form-control',
            
        },choices = [])
    )
    sessaoAtividade = forms.CharField(
        label = 'Sessão',
        widget = Select(attrs={
            'class' : 'form-control',
        },choices = [])
    )

    def __init__(self, *args, **kwargs):
        self.uoId = kwargs.pop('uoId')
        try: 
            self.selectedAtividade = kwargs.pop('sA')
        except KeyError:
            self.selectedAtividade = None
        super(TarefaAtividadeForm,self).__init__(*args,**kwargs)

        allAtividades = [(atividade.id, atividade.nome) for atividade in Atividade.objects.filter(unidadeorganicaid = self.uoId).filter(validada=1).filter(num_colaboradores__gt = 0)]
        self.fields['atividade'].widget.choices = allAtividades
        if self.selectedAtividade:
            self.fields['sessaoAtividade'].widget.choices = [(sessao.id, str(sessao)) for sessao in SessaoAtividade.objects.filter(atividadeid = self.selectedAtividade)]
        else:
            try:
                firstAtividade = next(iter(allAtividades))
                self.fields['sessaoAtividade'].widget.choices = [(sessao.id, str(sessao)) for sessao in SessaoAtividade.objects.filter(atividadeid = firstAtividade[0]).order_by('sessaoid__hora_de_inicio')]
            except StopIteration:
                self.fields['sessaoAtividade'].widget.choices = []


class TarefaTransporteForm(forms.Form):

    dia = forms.DateField(
        label = "Dia",
        widget = Select(
            attrs={
                'class' : 'form-control',
            }, 
            choices=[() ]
        )
    )
    horario = forms.TimeField(
        label = "Hora"
    )
    sessaoAtividade_origem = forms.CharField(
        label = "Sessão atividade origem",
        widget = Select(attrs={
            'class' : 'form-control',
        })
    )
    sessaoAtividade_destino = forms.CharField(
        label = "Sessão atividade destino",
        widget = Select(attrs={
            'class' : 'form-control',
        })
    )
    origem = forms.CharField(
        label= "Origem",
    )
    destino = forms.CharField(
        label= "Destino",
    )

    def __init__(self, *args, **kwargs):
        try: 
            self.sessao_o = kwargs.pop('sessao_o')
            self.sessao_d = kwargs.pop('sessao_d')
        except KeyError:
            self.sessao_o = None
            self.sessao_d = None
        super(TarefaTransporteForm,self).__init__(*args,**kwargs)

        if self.sessao_o and self.sessao_d:
            self.fields['sessaoAtividade_origem'].widget.choices = self.sessao_o
            self.fields['sessaoAtividade_destino'].widget.choices = self.sessao_d

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

        self.fields['dia'].widget.choices = daysDiaAberto


class TarefaGruposForm(forms.Form):
    inscricao = forms.CharField(
        label = "Grupo",
        widget = Select(attrs={
            'class' : 'form-control',
        })
    )

    def __init__(self, *args, **kwargs):
        try: 
            self.available_grupos = kwargs.pop('available_grupos')
        except KeyError:
            self.available_grupos = None
        super(TarefaGruposForm, self).__init__(*args, **kwargs)
        if self.available_grupos:
            self.fields['inscricao'].widget.choices = self.available_grupos

TarefaGruposFormset = formset_factory(TarefaGruposForm, extra=1)
