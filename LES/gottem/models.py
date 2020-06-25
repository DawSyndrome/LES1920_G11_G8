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
    localid = models.ForeignKey('Local', models.DO_NOTHING, db_column='LocalID')  # Field name made lowercase.
    utilizadorid = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID')  # Field name made lowercase.
    unidadeorganicaid = models.ForeignKey('UnidadeOrgnica', models.DO_NOTHING, db_column='UnidadeOrganicaID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descrição = models.CharField(db_column='Descrição', max_length=255, blank=True, null=True)  # Field name made lowercase.
    duração = models.IntegerField(db_column='Duração', blank=True, null=True)  # Field name made lowercase.
    limite_de_participantes = models.IntegerField(db_column='Limite_de_participantes', blank=True, null=True)  # Field name made lowercase.
    validada = models.IntegerField(db_column='Validada', blank=True, null=True)  # Field name made lowercase.
    tipo_atividade = models.CharField(db_column='Tipo_atividade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    public_alvo = models.CharField(db_column='Public_alvo', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'atividade'


class AtividadeMaterial(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='AtividadeID')  # Field name made lowercase.
    materialid = models.ForeignKey('Material', models.DO_NOTHING, db_column='MaterialID')  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'atividade-material'


class AtividadeTematica(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='AtividadeID')  # Field name made lowercase.
    temáticaid = models.ForeignKey('Temtica', models.DO_NOTHING, db_column='TemáticaID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'atividade-tematica'


class AtividadeDepartamento(models.Model):
    atividadeid = models.OneToOneField(Atividade, models.DO_NOTHING, db_column='AtividadeID', primary_key=True)  # Field name made lowercase.
    departamentoid = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='DepartamentoID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'atividade_departamento'
        unique_together = (('atividadeid', 'departamentoid'),)


class Campus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    localização = models.CharField(db_column='Localização', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'campus'


class Departamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    unidade_orgânicaid = models.ForeignKey('UnidadeOrgnica', models.DO_NOTHING, db_column='Unidade OrgânicaID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'departamento'


class DiaAberto(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descrição = models.CharField(db_column='Descrição', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.
    data_inicio = models.DateField(db_column='Data_inicio', blank=True, null=True)  # Field name made lowercase.
    data_fim = models.DateField(db_column='Data_fim', blank=True, null=True)  # Field name made lowercase.
    limite_de_inscrição_atividades = models.DateField(db_column='Limite_de_inscrição_atividades', blank=True, null=True)  # Field name made lowercase.
    limite_de_inscrição_participantes = models.DateField(db_column='Limite_de_inscrição_participantes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'dia aberto'


class DiaAbertoUtilizador(models.Model):
    dia_abertoid = models.OneToOneField(DiaAberto, models.DO_NOTHING, db_column='Dia AbertoID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    utilizadorid = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'dia aberto_utilizador'
        unique_together = (('dia_abertoid', 'utilizadorid'),)


class Edicifio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero_edificio = models.IntegerField(db_column='Numero edificio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        #managed = False
        db_table = 'edicifio'


class Ementa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dia = models.DateField(db_column='Dia', blank=True, null=True)  # Field name made lowercase.
    preço_economico_aluno = models.FloatField(db_column='Preço_economico_aluno', blank=True, null=True)  # Field name made lowercase.
    preço_normal_aluno = models.FloatField(db_column='Preço_normal_aluno', blank=True, null=True)  # Field name made lowercase.
    preço_economico_outro = models.FloatField(db_column='Preço_economico_outro', blank=True, null=True)  # Field name made lowercase.
    preço_outro = models.FloatField(db_column='Preço_outro', blank=True, null=True)  # Field name made lowercase.

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

    class Meta:
        #managed = False
        db_table = 'escola'


class GestoDePerfil(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    validação = models.IntegerField(db_column='Validação', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'gestão de perfil'


class Horario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora_de_partida = models.TimeField(db_column='Hora_de_partida', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'horario'


class Inscrio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    escolaid = models.ForeignKey(Escola, models.DO_NOTHING, db_column='EscolaID', blank=True, null=True)  # Field name made lowercase.
    dia = models.DateField(db_column='Dia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'inscrição'


class InscrioEmenta(models.Model):
    inscriçãoid = models.OneToOneField(Inscrio, models.DO_NOTHING, db_column='InscriçãoID', primary_key=True)  # Field name made lowercase.
    ementaid = models.ForeignKey(Ementa, models.DO_NOTHING, db_column='EmentaID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'inscrição_ementa'
        unique_together = (('inscriçãoid', 'ementaid'),)


class Local(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    edicifioid = models.ForeignKey(Edicifio, models.DO_NOTHING, db_column='EdicifioID')  # Field name made lowercase.
    andar = models.IntegerField(db_column='Andar', blank=True, null=True)  # Field name made lowercase.
    sala = models.IntegerField(db_column='Sala', blank=True, null=True)  # Field name made lowercase.
    descriçao = models.CharField(db_column='Descriçao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indoor = models.IntegerField(db_column='Indoor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'local'


class Material(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'material'


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
        managed = True
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
    ementaid = models.ForeignKey(Ementa, models.DO_NOTHING, db_column='EmentaID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descriçao = models.CharField(db_column='Descriçao', max_length=255, blank=True, null=True)  # Field name made lowercase.

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


class Sesso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora_de_inicio = models.TimeField(db_column='Hora_de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        #managed = False
        db_table = 'sessão'


class SessoAtividade(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sessãoid = models.ForeignKey(Sesso, models.DO_NOTHING, db_column='SessãoID')  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='AtividadeID')  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'sessão-atividade'


class SessoAtividadeInscrio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sessão_atividadeid = models.ForeignKey(SessoAtividade, models.DO_NOTHING, db_column='Sessão-AtividadeID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inscriçãoid = models.ForeignKey(Inscrio, models.DO_NOTHING, db_column='InscriçãoID')  # Field name made lowercase.
    num_alunos = models.IntegerField(db_column='Num_alunos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'sessão-atividade-inscrição'


class Tarefa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sessão_atividade_inscriçãoid_destino = models.ForeignKey(SessoAtividadeInscrio, models.DO_NOTHING, db_column='Sessão-Atividade-InscriçãoID_Destino', blank=True, null=True, related_name='+')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sessão_atividade_inscriçãoid_origem = models.ForeignKey(SessoAtividadeInscrio, models.DO_NOTHING, db_column='Sessão-Atividade-InscriçãoID_Origem', related_name='+')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    utilizadorid = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID')  # Field name made lowercase.
    descrição = models.CharField(db_column='Descrição', max_length=255, blank=True, null=True)  # Field name made lowercase.
    localização_do_grupo = models.CharField(db_column='Localização do grupo', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destino = models.CharField(db_column='Destino', max_length=255, blank=True, null=True)  # Field name made lowercase.
    horário = models.TimeField(db_column='Horário', blank=True, null=True)  # Field name made lowercase.
    tarefatransporte = models.IntegerField(db_column='TarefaTransporte', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tarefa'


class TarefaSessoAtividade(models.Model):
    tarefaid = models.OneToOneField(Tarefa, models.DO_NOTHING, db_column='TarefaID', primary_key=True)  # Field name made lowercase.
    sessão_atividadeid = models.ForeignKey(SessoAtividade, models.DO_NOTHING, db_column='Sessão-AtividadeID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        #managed = False
        db_table = 'tarefa_sessão-atividade'
        unique_together = (('tarefaid', 'sessão_atividadeid'),)


class Temtica(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'temática'


class Transporte(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora_de_chegada = models.DateField(db_column='Hora_de_chegada', blank=True, null=True)  # Field name made lowercase.
    hora_de_partida = models.DateField(db_column='Hora_de_partida', blank=True, null=True)  # Field name made lowercase.
    tipo_de_transporte = models.CharField(db_column='Tipo_de_transporte', max_length=255, blank=True, null=True)  # Field name made lowercase.
    capacidade = models.IntegerField(db_column='Capacidade', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'transporte'


class TransporteUniversitrioHorario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    horarioid = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioID')  # Field name made lowercase.
    transporteid = models.ForeignKey(Transporte, models.DO_NOTHING, db_column='TransporteID')  # Field name made lowercase.
    origem = models.CharField(db_column='Origem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destino = models.CharField(db_column='Destino', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'transporte_universitário-horario'


class TransporteUniversitrioHorarioInscrio(models.Model):
    transporte_universitário_horarioid = models.OneToOneField(TransporteUniversitrioHorario, models.DO_NOTHING, db_column='Transporte_Universitário-HorarioID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inscriçãoid = models.ForeignKey(Inscrio, models.DO_NOTHING, db_column='InscriçãoID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'transporte_universitário-horario_inscrição'
        unique_together = (('transporte_universitário_horarioid', 'inscriçãoid'),)


class UnidadeOrgnica(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    campusid = models.ForeignKey(Campus, models.DO_NOTHING, db_column='CampusID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'unidade orgânica'


from enum import IntEnum
class Utilizador(AbstractBaseUser):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    inscriçãoid = models.ForeignKey(Inscrio, models.DO_NOTHING, db_column='InscriçãoID', blank=True, null=True)  # Field name made lowercase.
    unidade_orgânicaid = models.ForeignKey(UnidadeOrgnica, models.DO_NOTHING, db_column='Unidade OrgânicaID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
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
    	return self.user_type & self.USER_TYPES.Administrador != 0;

    def is_participante(self):
    	return self.user_type & self.USER_TYPES.Participante != 0;

    def is_docente(self):
    	return self.user_type & self.USER_TYPES.Docente != 0;

    def is_colaborador(self):
    	return self.user_type & self.USER_TYPES.Colaborador != 0;

    def is_coordenador(self):
    	return self.user_type & self.USER_TYPES.Coordenador != 0;

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
