from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from datetime import datetime

# Create your models here.


# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

class Atividade(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    localid = models.ForeignKey('Local', on_delete = models.DO_NOTHING, db_column='LocalID', blank=True, null=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey("Utilizador", default = "", on_delete = models.CASCADE, db_column='UtilizadorID', null=True)  # Field name made lowercase.
    unidadeorganicaid = models.ForeignKey('UnidadeOrganica', default = "", on_delete = models.CASCADE, db_column='UnidadeOrganicaID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    duracao = models.IntegerField(db_column='Duracao', blank=True, null=True)  # Field name made lowercase.
    limite_de_participantes = models.IntegerField(db_column='Limite_de_participantes', blank=True, null=True)  # Field name made lowercase.
    validada = models.IntegerField(db_column='Validada', blank=True, null=True)  # Field name made lowercase.
    tipo_atividade = models.CharField(db_column='Tipo_atividade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    public_alvo = models.CharField(db_column='Public_alvo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    editavel = models.BooleanField(db_column='Editavel', blank=True, null=True)  # Field name made lowercase.
    num_colaboradores = models.IntegerField(db_column='Num_Colaboradores', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'atividade'
        permissions = [
            ("validates_atividade", "Can validate atividade"),
            ("atribuir_local", "Can atribuir local da atividade"),
            ("alterar_local", "Can alterar local da atividade")
            ]


class AtividadeMaterial(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, on_delete = models.CASCADE, db_column='AtividadeID')  # Field name made lowercase.
    materialid = models.ForeignKey('Material', on_delete = models.CASCADE, db_column='MaterialID')  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'atividade_material'


class AtividadeTematica(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, on_delete = models.CASCADE, db_column='AtividadeID')  # Field name made lowercase.
    tematicaid = models.ForeignKey('Tematica', on_delete = models.CASCADE, db_column='TematicaID')  # Field name made lowercase.

    class Meta:
        #managed = False        
        db_table = 'atividade_tematica'


class AtividadeDepartamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, on_delete = models.CASCADE, db_column='AtividadeID')  # Field name made lowercase.
    departamentoid = models.ForeignKey('Departamento', on_delete = models.CASCADE, db_column='DepartamentoID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'atividade_departamento'


class Campus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    localizacao = models.CharField(db_column='Localizacao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contacto = models.CharField(db_column='Contacto', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'campus' 

    def __str__(self):
        return str(self.nome)



class Departamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    unidade_organicaid = models.ForeignKey('UnidadeOrganica', on_delete = models.CASCADE, db_column='Unidade_OrganicaID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'departamento'


class DiaAberto(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.
    data_inicio = models.DateField(db_column='Data_inicio', blank=True, null=True)  # Field name made lowercase.
    data_fim = models.DateField(db_column='Data_fim', blank=True, null=True)  # Field name made lowercase.
    # limite_de_inscricao_atividades = models.DateField(db_column='Limite_de_inscricao_atividades', blank=True, null=True)  # Field name made lowercase.
    # limite_de_inscricao_participantes = models.DateField(db_column='Limite_de_inscricao_participantes', blank=True, null=True)  # Field name made lowercase.
    data_inicio_inscricao = models.DateField(db_column='Data_inicio_inscricao', blank=True, null=True)
    data_fim_inscricao = models.DateField(db_column='Data_fim_inscricao', blank=True, null=True)
    data_inicio_propor_atividades = models.DateField(db_column='Data_inicio_propor_atividades', blank=True, null=True)
    data_fim_propor_atividades = models.DateField(db_column='Data_fim_propor_atividades', blank=True, null=True)
    preco_aluno= models.FloatField(db_column='Preco_aluno', blank=True, null=True)
    preco_professor= models.FloatField(db_column='Preco_professor', blank=True, null=True)


    class Meta:
        #managed = False
        db_table = 'dia_aberto'


class DiaAbertoUtilizador(models.Model):
    dia_abertoid = models.OneToOneField(DiaAberto, models.DO_NOTHING, db_column='Dia AbertoID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    utilizadorid = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'dia aberto_utilizador'
        unique_together = (('dia_abertoid', 'utilizadorid'),)


class Edificio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    num_edificio = models.IntegerField(db_column='Num_edificio', blank=True, null=True)  # Field name made lowercase.
    nome_edificio = models.CharField(db_column='Nome_edificio', max_length=255, blank=True, null=True)  # Field name made lowercase
    campusid = models.ForeignKey(Campus, on_delete = models.CASCADE, db_column='CampusID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'edicifio'

    def __str__(self):
        return self.nome_edificio


class Ementa(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dia = models.DateField(db_column='Dia', blank=True, null=True)  # Field name made lowercase.
    #preco_economico = models.FloatField(db_column='Preco_economico_aluno', blank=True, null=True)  # Field name made lowercase.
    #preco_normal = models.FloatField(db_column='Preco_normal_aluno', blank=True, null=True)  # Field name made lowercase.
    #preco_economico_outro = models.FloatField(db_column='Preco_economico_outro', blank=True, null=True)  # Field name made lowercase.
    #preco_outro = models.FloatField(db_column='Preco_outro', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return "Ementa " + str(self.id)

    class Meta:
        #managed = False
        db_table = 'ementa'


class Escola(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zip = models.IntegerField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.
    localidade = models.CharField(db_column='Localidade', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        if self.nome:
            return str(self.nome)
        else:
            return 'Individual'

    class Meta:
        #managed = False
        db_table = 'escola'


class GestoDePerfil(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    validação = models.IntegerField(db_column='Validação', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'gestão de perfil'


class HorarioTransporte(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora_de_partida = models.TimeField(db_column='Hora_de_partida', blank=True, null=True)  # Field name made lowercase.
    hora_de_chegada = models.TimeField(db_column='Hora_de_chegada', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.hora_de_partida.strftime("%H:%M") + " - " + self.hora_de_chegada.strftime("%H:%M")

    class Meta:
        #managed = False
        db_table = 'horario'


class Inscricao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    escolaid = models.ForeignKey(Escola, models.DO_NOTHING, db_column='EscolaID', blank=True, null=True)  # Field name made lowercase.
    dia = models.DateField(db_column='Dia', blank=True, null=True)  # Field name made lowercase.
    hora_chegada = models.TimeField(db_column='Hora_chegada', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        if self.escolaid:
            return "Grupo " + str(self.id) + ", " + str(self.escolaid)
        return "Grupo" + str(self.id) + ", Individual"

    class Meta:
        #managed = False
        db_table = 'inscricao'


class InscrioEmenta(models.Model):
    inscriçãoid = models.OneToOneField(Inscricao, models.DO_NOTHING, db_column='InscriçãoID', primary_key=True)  # Field name made lowercase.
    ementaid = models.ForeignKey(Ementa, models.DO_NOTHING, db_column='EmentaID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'inscrição_ementa'
        unique_together = (('inscriçãoid', 'ementaid'),)


class Local(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    edicifioid = models.ForeignKey(Edificio, on_delete = models.CASCADE, db_column='EdicifioID', blank=True, null=True)  # Field name made lowercase.
    andar = models.IntegerField(db_column='Andar', blank=True, null=True)  # Field name made lowercase.
    sala = models.CharField(db_column='Sala', blank=True, null=True, max_length=255)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indoor = models.BooleanField(db_column='Indoor', blank=True, null=True)  # Field name made lowercase.
    campusid = models.ForeignKey(Campus, on_delete = models.CASCADE, db_column='CampusID', blank=True, null=True)  # Field name made lowercase.
    mapa_sala = models.ImageField(upload_to='mapas_salas', blank=True, null=True)
    nome_local_exterior = models.CharField(db_column='nome_local_exterior', blank=True, null=True, max_length=255)

    def __str__ (self):
        if self.indoor:
            return str(self.campusid.nome) + ", " + str(self.edicifioid.nome_edificio) + ", " + "Andar" + " " + str(self.andar) + ", " + "Sala" + " " + str(self.sala)
        return str(self.campusid.nome) + ", " + str(self.nome_local_exterior)

    class Meta:
        #managed = False
        db_table = 'local'


class Material(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'material'

    def __str__ (self): 
        return str(self.nome)


## Notificacao ##
class Notificacao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    utilizadorid_envia = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_Envia',
                                           related_name='idEnvia')  # Field name made lowercase.
    utilizadorid_recebe = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_Recebe',
                                            related_name='idRecebe', blank=True, null=True)
    conteudo = models.CharField(db_column='Conteudo', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    hora_envio = models.TimeField(db_column='Hora_envio', default=datetime.now, blank=True,
                                  null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', default=timezone.now, blank=True, null=True)  # Field name made lowercase.
    prioridade = models.IntegerField(db_column='Prioridade', blank=True, null=True)  # Field name made lowercase.
    assunto = models.CharField(db_column='Assunto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    visto = models.BooleanField(db_column='Visto', default=0, null=False)

    class Meta:
        #managed = False
        db_table = 'notificações'


class Participanteinfo(models.Model):
    participanteinfoid = models.AutoField(db_column='ParticipanteInfoID', primary_key=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID')  # Field name made lowercase.
    ano_escolar = models.IntegerField(db_column='Ano escolar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    area = models.CharField(db_column='Area', max_length=255, blank=True, null=True)  # Field name made lowercase.
    checkin_state = models.IntegerField(db_column='Checkin_state')  # Field name made lowercase.
    participante_type = models.IntegerField(db_column='Participante_type', blank=True, null=True)  # Field name made lowercase.
    total_de_participantes = models.IntegerField(db_column='Total_de_participantes', blank=True, null=True)  # Field name made lowercase.
    total_de_professores = models.IntegerField(db_column='Total_de_professores', blank=True, null=True)  # Field name made lowercase.
    turma = models.CharField(db_column='Turma', max_length=255, blank=True, null=True)  # Field name made lowercase.
    autorização = models.IntegerField(db_column='Autorização', blank=True, null=True)  # Field name made lowercase.
    ficheiro_autorização = models.CharField(db_column='Ficheiro_autorização', max_length=255, blank=True, null=True)  # Field name made lowercase.
    acompanhates = models.IntegerField(db_column='Acompanhates', blank=True, null=True)  # Field name made lowercase.
    tipoparticipante = models.CharField(db_column='TipoParticipante', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'participanteinfo'


class Prato(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ementaid = models.ForeignKey(Ementa, on_delete=models.CASCADE, db_column='EmentaID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'prato'


class RegistoHorrio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora_inicio = models.TimeField(db_column='Hora_inicio', blank=True, null=True)  # Field name made lowercase.
    hora_fim = models.TimeField(db_column='Hora_fim', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'registo horário'


class Sessao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora_de_inicio = models.TimeField(db_column='Hora_de_inicio', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.hora_de_inicio.strftime("%I:%M")

    class Meta:
        #managed = False
        db_table = 'sessao'


class SessaoAtividade(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sessaoid = models.ForeignKey(Sessao, on_delete = models.CASCADE, db_column='SessaoID')  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, on_delete = models.CASCADE, db_column='AtividadeID')  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.data.strftime("%d-%m-%Y") + ", " + str(self.sessaoid)

    class Meta:
        #managed = False
        db_table = 'sessao_atividade'


class SessaoAtividadeInscricao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sessao_atividadeid = models.ForeignKey(SessaoAtividade, on_delete=models.CASCADE, db_column='Sessao_AtividadeID')  # Field name made lowercase.
    inscricaoid = models.ForeignKey(Inscricao, on_delete=models.CASCADE, db_column='InscricaoID')  # Field name made lowercase.
    num_alunos = models.IntegerField(db_column='Num_alunos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'sessao_atividade_inscricao'


class Tarefa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sessao_atividadeid_destino = models.ForeignKey("SessaoAtividade", related_name='destino', on_delete=models.SET_NULL, db_column='Sessao_AtividadeID_Destino', blank=True, null=True)  # Field name made lowercase.
    sessao_atividadeid_origem = models.ForeignKey("SessaoAtividade", related_name='origem', on_delete=models.SET_NULL, db_column='Sessao_AtividadeID_Origem', blank=True, null=True)  # Field name made lowercase.
    sessao_atividadeid = models.ForeignKey("SessaoAtividade", related_name='TarefaSessaoAtividade', on_delete=models.CASCADE, db_column='SessaoAtividadeID', blank=True, null=True)
    utilizadorid = models.ForeignKey("Utilizador", related_name='tarefa_coordenador', on_delete=models.DO_NOTHING, db_column='UtilizadorID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipoTarefa = models.CharField(db_column='TipoTarefa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    origem = models.CharField(db_column='Origem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destino = models.CharField(db_column='Destino', max_length=255, blank=True, null=True)  # Field name made lowercase.
    horario = models.TimeField(db_column='Horario', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)
    colaboradores = models.ManyToManyField("Utilizador", related_name='tarefa_colaborador')

    class Meta:
        #managed = False
        db_table = 'tarefa'
        permissions = [
            ("assign_tarefa", "Can assign a tarefa to a colaborador "),
            ("remove_colab_from_tarefa", "Can remove a colaborador from a tarefa"),
        ]


class TarefaSessoAtividade(models.Model):
    tarefaid = models.OneToOneField(Tarefa, models.DO_NOTHING, db_column='TarefaID', primary_key=True)  # Field name made lowercase.
    sessão_atividadeid = models.ForeignKey(SessaoAtividade, models.DO_NOTHING, db_column='Sessão-AtividadeID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        #managed = False
        db_table = 'tarefa_sessão-atividade'
        unique_together = (('tarefaid', 'sessão_atividadeid'),)


class Tematica(models.Model):
    #d = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tematica'

    def __str__ (self): 
        return str(self.nome)


class Transporte(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo_transporte = models.CharField(db_column='Tipo_de_transporte', max_length=255, blank=True, null=True)  # Field name made lowercase.
    capacidade = models.IntegerField(db_column='Capacidade', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.tipo_transporte)

    class Meta:
        #managed = False
        db_table = 'transporte'


class Rota(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    transporteid = models.ForeignKey(Transporte, on_delete = models.CASCADE, db_column='TransporteID')  # Field name made lowercase.
    horarioid = models.ForeignKey(HorarioTransporte, on_delete = models.CASCADE, db_column='HorarioID', blank=True, null=True)  # Field name made lowercase.
    origem = models.CharField(db_column='Origem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destino = models.CharField(db_column='Destino', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'transporte_universitario_horario'


class Rota_Inscricao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rotaid = models.ForeignKey(Rota, on_delete= models.CASCADE, db_column='Transporte_Universitario_HorarioID', null=True, blank=True)  # Field name made lowercase.
    inscricaoid = models.ForeignKey("Inscricao", on_delete= models.CASCADE, db_column='InscricaoID', null=True, blank=True)  # Field name made lowercase.
    num_passageiros = models.IntegerField(db_column='Num_passageiros', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'transporte_universitario_horario_inscricao'


class UnidadeOrganica(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    #campusid = models.ForeignKey(Campus, on_delete = models.CASCADE, db_column='CampusID', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'unidade_organica'


from enum import IntEnum
class Utilizador(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    inscriçãoid = models.ForeignKey(Inscricao, models.DO_NOTHING, db_column='InscriçãoID', blank=True, null=True)  # Field name made lowercase.
    unidade_orgânicaid = models.ForeignKey(UnidadeOrganica, models.DO_NOTHING, db_column='Unidade OrgânicaID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    departamentoid = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='DepartamentoID', blank=True, null=True)  # Field name made lowercase.
    registo_horárioid = models.ForeignKey(RegistoHorrio, models.DO_NOTHING, db_column='Registo HorárioID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True, unique=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_de_nascimento = models.DateField(db_column='Data_de_nascimento', blank=True, null=True)  # Field name made lowercase.
    numero_telemovel = models.IntegerField(db_column='Numero_telemovel', blank=True, null=True)  # Field name made lowercase.
    cartão_cidadão = models.IntegerField(db_column='Cartão_cidadão', blank=True, null=True)  # Field name made lowercase.
    deficiencias = models.CharField(db_column='Deficiencias', max_length=255, blank=True, null=True)  # Field name made lowercase.
    permitir_localização = models.IntegerField(db_column='Permitir_localização', blank=True, null=True)  # Field name made lowercase.
    utilizar_dados_pessoais = models.IntegerField(db_column='Utilizar_dados_pessoais', blank=True, null=True)  # Field name made lowercase.
    tema_do_website = models.IntegerField(db_column='Tema_do_website', blank=True, null=True)  # Field name made lowercase.

    user_type = models.IntegerField(db_column='User_type')  # Field name made lowercase.

    daltonico = models.IntegerField(db_column='Daltonico', blank=True, null=True)  # Field name made lowercase.
    validado = models.IntegerField(db_column='Validado')  # Field name made lowercase.
    #check_in_state = models.IntegerField(db_column='Check_in_state')  # Field name made lowercase.

    password_reset_url = models.CharField(db_column='Password_reset_url', max_length=500, blank=True, null=True);
    password = models.CharField(db_column='Password', max_length=500);

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    class USER_TYPES(IntEnum):
        Administrador = 0b10000
        Participante  = 0b01000
        Docente       = 0b00100
        Colaborador   = 0b00010
        Coordenador   = 0b00001

    def is_admin(self):
        return (self.user_type & self.USER_TYPES.Administrador) != 0;

    def is_participante(self):
        return (self.user_type & self.USER_TYPES.Participante) != 0;

    def is_docente(self):
        return (self.user_type & self.USER_TYPES.Docente) != 0;

    def is_colaborador(self):
        return (self.user_type & self.USER_TYPES.Colaborador) != 0;

    def is_coordenador(self):
        return (self.user_type & self.USER_TYPES.Coordenador) != 0;

    class Meta:
        #managed = False
        db_table = 'utilizador'


class UtilizadorAtividade(models.Model):
    utilizadorid = models.OneToOneField(Utilizador, models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='AtividadeID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'utilizador_atividade'
        unique_together = (('utilizadorid', 'atividadeid'),)


class UtilizadorEmenta(models.Model):
    utilizadorid = models.OneToOneField(Utilizador, models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.
    ementaid = models.ForeignKey(Ementa, models.DO_NOTHING, db_column='EmentaID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'utilizador_ementa'
        unique_together = (('utilizadorid', 'ementaid'),)


class UtilizadorTarefa(models.Model):
    utilizadorid = models.OneToOneField(Utilizador, models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.
    tarefaid = models.ForeignKey(Tarefa, models.DO_NOTHING, db_column='TarefaID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'utilizador_tarefa'
        unique_together = (('utilizadorid', 'tarefaid'),)


class UtilizadorTransporte(models.Model):
    utilizadorid = models.OneToOneField(Utilizador, models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.
    transporteid = models.ForeignKey(Transporte, models.DO_NOTHING, db_column='TransporteID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'utilizador_transporte'
        unique_together = (('utilizadorid', 'transporteid'),)

class InscricaoTarefa(models.Model):
    inscricaoid = models.ForeignKey("Inscricao", on_delete=models.CASCADE, db_column='InscricaoID', blank=True, null=True)
    tarefaid = models.ForeignKey(Tarefa, on_delete=models.CASCADE, db_column='TarefaID', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'inscricao_tarefa'

