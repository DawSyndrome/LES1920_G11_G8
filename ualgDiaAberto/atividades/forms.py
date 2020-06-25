from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Select, Textarea, modelformset_factory, formset_factory, MultipleChoiceField, DateField
from atividades.models import Edificio, Campus, Departamento, Local, Atividade, UnidadeOrganica, Tematica, Material, AtividadeTematica, AtividadeMaterial, SessaoAtividade, Sessao
from diaAbertoConf.models import DiaAberto
import datetime

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields =    '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nome_edificio = cleaned_data.get("nome_edificio")
        campusid = cleaned_data.get("campusid")
        if self.instance.id:
            for edificio in Edificio.objects.all():
                if nome_edificio.lower() == edificio.nome_edificio.lower() and self.instance.id != edificio.id:
                    if  campusid == edificio.campusid:
                        raise forms.ValidationError(
                            ('O edifício que pretende editar já existe'),
                        code='invalid'
                        )
        else:
            for edificio in Edificio.objects.all():
                if nome_edificio.lower() == edificio.nome_edificio.lower():
                    if  campusid == edificio.campusid:
                        raise forms.ValidationError(
                            ('O edifício que pretende criar já existe'),
                        code='invalid'
                        )

class CampusForm(ModelForm):
    class Meta:
        model = Campus
        fields =    '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get("nome")
        if self.instance.id:
            for campus in Campus.objects.all():
                try:
                    if nome.lower() == campus.nome.lower() and self.instance.id != campus.id:
                        raise forms.ValidationError(
                            ('O campus que pretende editar já existe'),
                        code='invalid'
                        )
                except AttributeError:
                    pass
        else:
            for campus in Campus.objects.all():
                if nome.lower() == campus.nome.lower():
                    raise forms.ValidationError(
                        ('O campus que pretende criar já existe'),
                    code='invalid'
                    )

class UnidadeOrganicaForm(ModelForm):
    class Meta:
        model = UnidadeOrganica
        fields =    '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get("nome")
        if self.instance.id:
            for unidade_organica in UnidadeOrganica.objects.all():
                if nome.lower() == unidade_organica.nome.lower() and self.instance.id != unidade_organica.id:
                    raise forms.ValidationError(
                        ('A unidade orgânica que pretende editar já existe'),
                    code='invalid'
                    )
        else:
            for unidade_organica in UnidadeOrganica.objects.all():
                if nome.lower() == unidade_organica.nome.lower():
                    raise forms.ValidationError(
                        ('A unidade orgânica que pretende criar já existe'),
                    code='invalid'
                    )

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields =    '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get("nome")
        if self.instance.id:
            for departamento in Departamento.objects.all():
                if nome.lower() == departamento.nome.lower() and self.instance.id != departamento.id:
                    raise forms.ValidationError(
                        ('O departamento que pretende editar já existe'),
                    code='invalid'
                    )
        else:
            for departamento in Departamento.objects.all():
                if nome.lower() == departamento.nome.lower():
                    raise forms.ValidationError(
                        ('O departamento que pretende criar já existe'),
                    code='invalid'
                    )

class LocalForm(ModelForm):
    class Meta:
        model = Local
        fields =    ['campusid', 'indoor', 'descricao', 'sala', 'andar', 'mapa_sala', 'edicifioid', 'nome_local_exterior']

    def clean(self):
        cleaned_data = super().clean()
        campusid = cleaned_data.get("campusid")
        edicifioid = cleaned_data.get("edicifioid")
        andar = cleaned_data.get("andar")
        sala = cleaned_data.get("sala")
        indoor = cleaned_data.get("indoor")
        nome_exterior = cleaned_data.get("nome_local_exterior")

        if indoor:
            if self.instance.id:
                for local in Local.objects.all():
                    if campusid.id == local.campusid.id and self.instance.id != local.id:
                        try:
                            if edicifioid.id == local.edicifioid.id and self.instance.id != local.id:
                                if andar == local.andar and self.instance.id != local.id:
                                    if sala == local.sala and self.instance.id != local.id:
                                        raise forms.ValidationError(
                                            ('O local que pretende editar já existe'),
                                        code='invalid'
                                        )
                        except AttributeError:
                            pass
            else:
                for local in Local.objects.all():
                    if campusid.id == local.campusid.id:
                        try:
                            if edicifioid.id == local.edicifioid.id:
                                if andar == local.andar:
                                    if sala == local.sala:
                                        raise forms.ValidationError(
                                            ('O local que pretende criar já existe'),
                                        code='invalid'
                                        )
                        except AttributeError:
                            pass
        else:
            if self.instance.id:
                for local in Local.objects.all():
                    if campusid.id == local.campusid.id and self.instance.id != local.id:
                            if nome_exterior == local.nome_local_exterior:
                                raise forms.ValidationError(
                                            ('O local que pretende editar já existe'),
                                        code='invalid'
                                        )
            else:
                for local in Local.objects.all():
                    if campusid.id == local.campusid.id:
                            if nome_exterior == local.nome_local_exterior:
                                raise forms.ValidationError(
                                            ('O local que pretende criar já existe'),
                                        code='invalid'
                                        )
                       


class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields =    ['nome', 'descricao', 'duracao', 'limite_de_participantes', 'tipo_atividade', 'public_alvo', 'num_colaboradores']
        choices = (('Laboratorial', 'Laboratorial'),('Prática', 'Prática'), ('Teórica', 'Teórica'),)
        widgets = {
            'nome' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza o nome da atividade',
                'required' : 'required',
                'oninvalid': "goToStep('1')",
            }),

            'descricao' : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza uma descrição da atividade',
                'required' : 'required',
                'oninvalid': "goToStep('1')",
            }),

            'duracao' : NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza a duração da atividade em minutos',
                'min' : 10,
                'required' : 'required',
                'oninvalid': "goToStep('1')",
            }),

            'limite_de_participantes' : NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza um limite de participantes',
                'min' : 1,
                'required' : 'required',
                'oninvalid': "goToStep('1')",
            }),

            'num_colaboradores' : NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza o número de colaboradores',
                'min' : 0,
                'required' : 'required',
                'oninvalid': "goToStep('1')",
            }),

            'tipo_atividade' : Select(attrs={
                'class' : 'form-control',
                'required' : 'required',
            }, choices = choices),

            'public_alvo' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza o público alvo',
                'required' : 'required',
                'oninvalid': "goToStep('1')",
            }),
        }
        labels = {
            'nome' : _('Nome'),
            'descricao' : _('Descrição'),
            'duracao' : _('Duração'),
            'limite_de_participantes' : _('Limite de participantes'),
            'tipo_atividade' : _('Tipo de atividade'),
            'public_alvo' : _('Público alvo'),
            'num_colaboradores' : _('Colaboradores')
        }

class TematicaForm(ModelForm):
    class Meta:
        model = Tematica
        fields =    '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get("nome")
        if self.instance.id:
            for tematica in Tematica.objects.all():
                if nome.lower() == tematica.nome.lower() and self.instance.id != tematica.id:
                    raise forms.ValidationError(
                        ('A temática que pretende editar já existe'),
                    code='invalid'
                    )
        else:
            for tematica in Tematica.objects.all():
                if nome.lower() == tematica.nome.lower():
                    raise forms.ValidationError(
                        ('A temática que pretende criar já existe'),
                    code='invalid'
                    )

class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields =    '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get("nome")
        if self.instance.id:
            for material in Material.objects.all():
                if nome.lower() == material.nome.lower() and self.instance.id != material.id:
                    raise forms.ValidationError(
                        ('O material que pretende editar já existe'),
                    code='invalid'
                    )
        else:
            for material in Material.objects.all():
                if nome.lower() == material.nome.lower():
                    raise forms.ValidationError(
                        ('O material que pretende criar já existe'),
                    code='invalid'
                    )

class AtividadeTematicaForm(ModelForm):

    class Meta:
        model = AtividadeTematica
        fields = ['tematicaid']
        widgets = { 
            'tematicaid': Select(
                choices= [],
                attrs= {
                    'class' : 'form-control',
                    'required': 'required',
                    'oninvalid': "goToStep('2')",
                }),
        }
        labels = {
            'tematicaid': ('Temática'),
        } 

        def __init__(self, *args, **kwargs):
            super(AtividadeTematicaForm,self).__init__(*args,**kwargs)   
            self.fields['tematicaid'].choices = [(tematica.id, tematica.nome) for tematica in Tematica.objects.all()]

AtividadeTematicaFormset = formset_factory(AtividadeTematicaForm, extra=1)

class AtividadeMaterialForm(ModelForm):

    class Meta:
        model = AtividadeMaterial
        fields = ['materialid', 'quantidade']
        widgets = { 
            'materialid': Select(
                choices= [],
                attrs= {
                    'class' : 'form-control',
                }),
            'quantidade': NumberInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Introduza a quantidade',
            'min' : 1,
            'oninvalid': "goToStep('3')"
            }),
        }
        labels = {
            'materialid': ('Material'),
            'quantidade' : ('Quantidade'),
        }

        def __init__(self, *args, **kwargs):
            super(AtividadeMaterialForm,self).__init__(*args,**kwargs)   
            self.fields['materialid'].choices = [(material.id, material.nome) for material in Material.objects.all()]

AtividadeMaterialFormset = formset_factory(AtividadeMaterialForm, extra=1)

class AtividadeSessaoForm(ModelForm):

    class Meta:
        model = SessaoAtividade
        fields = ['sessaoid', 'data']
        widgets = { 
            'sessaoid': Select(
                choices= [],
                attrs= {
                    'class' : 'form-control',
                    'required' : 'required',
                }),
            'data' : Select(attrs={
                 'class' : 'form-control',
                 'required' : 'required',
            }, choices=[]),
        }
        labels = {
            'sessaoid': ('Sessão'),
            'data' : ('Data'),
        } 

    def __init__(self, *args, **kwargs):
        super(AtividadeSessaoForm,self).__init__(*args,**kwargs)

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

        self.fields['data'].widget.choices = daysDiaAberto
        self.fields['sessaoid'].choices = [(sessao.id, sessao.hora_de_inicio.strftime("%H:%M")) for sessao in Sessao.objects.all()]

AtividadeSessaoFormset = formset_factory(AtividadeSessaoForm, extra=1)

class SessaoForm(ModelForm):
    class Meta:
        model = Sessao
        fields =    '__all__'

    def clean(self):
        cleaned_data = super().clean()
        hora_de_inicio = cleaned_data.get("hora_de_inicio")
        if self.instance.id:
            for sessao in Sessao.objects.all():
                if hora_de_inicio == sessao.hora_de_inicio and self.instance.id != sessao.id:
                    raise forms.ValidationError(
                        ('A sessão que pretende editar já existe'),
                    code='invalid'
                    )
        else:
            for sessao in Sessao.objects.all():
                if hora_de_inicio == sessao.hora_de_inicio:
                    raise forms.ValidationError(
                        ('A sessão que pretende criar já existe'),
                    code='invalid'
                    )

# class AtividadeSessaoForm(ModelForm):
#     class Meta:
#         model = SessaoAtividade
#         fields =    '__all__'

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model= Image
#         fields= ["mapa_sala"]