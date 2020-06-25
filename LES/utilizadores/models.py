from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from enum import Enum
class Utilizador(AbstractBaseUser, PermissionsMixin):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    #inscricaoid = models.ForeignKey(Inscrio, models.DO_NOTHING, db_column='InscriçãoID', blank=True, null=True)  # Field name made lowercase.
    unidade_organicaid = models.ForeignKey("atividades.UnidadeOrganica", models.DO_NOTHING, db_column='Unidade_OrganicaID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    departamentoid = models.ForeignKey("atividades.Departamento", models.DO_NOTHING, db_column='DepartamentoID', blank=True, null=True)  # Field name made lowercase.
    #registo_horárioid = models.ForeignKey(RegistoHorrio, models.DO_NOTHING, db_column='Registo HorárioID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    #gestão_de_perfilid = models.ForeignKey(GestoDePerfil, models.DO_NOTHING, db_column='Gestão de PerfilID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
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
    check_in_state = models.IntegerField(db_column='Check_in_state' , blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=500);

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    class USER_TYPES(Enum):
    	Administrador = 0b10000
    	Participante  = 0b01000
    	Docente       = 0b00100
    	Colaborador   = 0b00010
    	Coordenador   = 0b00001

    class Meta:
        db_table = 'utilizador'

