from django.db import models

# Create your models here.

class Campus(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    localizacao = models.CharField(db_column='Localizacao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contacto = models.CharField(db_column='Contacto', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'campus'

    def __str__(self):
        return self.nome

class Edificio(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    num_edificio = models.IntegerField(db_column='Num_edificio', blank=True, null=True)  # Field name made lowercase.
    nome_edificio = models.CharField(db_column='Nome_edificio', max_length=255, blank=True, null=True)  # Field name made lowercase
    campusid = models.ForeignKey(Campus, on_delete = models.CASCADE, db_column='CampusID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'edicifio'

    def __str__(self):
        return self.nome_edificio

class UnidadeOrganica(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    #campusid = models.ForeignKey(Campus, on_delete = models.CASCADE, db_column='CampusID', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'unidade_organica'

class Departamento(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    unidade_organicaid = models.ForeignKey('UnidadeOrganica', on_delete = models.CASCADE, db_column='Unidade_OrganicaID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'

class Local(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    edicifioid = models.ForeignKey(Edificio, on_delete = models.CASCADE, db_column='EdicifioID', blank=True, null=True)  # Field name made lowercase.
    andar = models.IntegerField(db_column='Andar', blank=True, null=True)  # Field name made lowercase.
    sala = models.CharField(db_column='Sala', blank=True, null=True, max_length=255)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indoor = models.BooleanField(db_column='Indoor', blank=True, null=True)  # Field name made lowercase.
    campusid = models.ForeignKey(Campus, on_delete = models.CASCADE, db_column='CampusID', blank=True, null=True)  # Field name made lowercase.
    mapa_sala = models.ImageField(upload_to='mapas_salas', blank=True, null=True)

    def __str__ (self):
        if self.indoor:
            return str(self.campusid.nome) + "," + " " + str(self.edicifioid.nome_edificio) + "," + " " + "Andar" + " " + str(self.andar) + "," + " " + "Sala" + " " + str(self.sala)
        return str(self.campusid.nome) + " Exterior"

    class Meta:
        managed = True
        db_table = 'local'


class Utilizador(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    #inscricaoid = models.ForeignKey(Inscricao, models.DO_NOTHING, db_column='InscricaoID', blank=True, null=True)  # Field name made lowercase.
    unidade_organicaid = models.ForeignKey(UnidadeOrganica, on_delete = models.CASCADE, db_column='Unidade_OrganicaID', blank=True, null=True)  # Field name made lowercase.
    departamentoid = models.ForeignKey(Departamento, on_delete = models.CASCADE, db_column='DepartamentoID', blank=True, null=True)  # Field name made lowercase.
    #registo_horarioid = models.ForeignKey(RegistoHorario, models.DO_NOTHING, db_column='Registo_HorarioID', blank=True, null=True)  # Field name made lowercase.
    #gestao_perfilid = models.ForeignKey(GestaoPerfil, models.DO_NOTHING, db_column='Gestao_PerfilID', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_de_nascimento = models.DateField(db_column='Data_de_nascimento', blank=True, null=True)  # Field name made lowercase.
    numero_telemovel = models.IntegerField(db_column='Numero_telemovel', blank=True, null=True)  # Field name made lowercase.
    cartao_cidadao = models.IntegerField(db_column='Cartao_cidadao', blank=True, null=True)  # Field name made lowercase.
    deficiencias = models.CharField(db_column='Deficiencias', max_length=255, blank=True, null=True)  # Field name made lowercase.
    permitir_localizacao = models.IntegerField(db_column='Permitir_localizacao', blank=True, null=True)  # Field name made lowercase.
    utilizar_dados_pessoais = models.IntegerField(db_column='Utilizar_dados_pessoais', blank=True, null=True)  # Field name made lowercase.
    tema_do_website = models.IntegerField(db_column='Tema_do_website', blank=True, null=True)  # Field name made lowercase.
    user_type = models.IntegerField(db_column='User_type')  # Field name made lowercase.
    daltonico = models.IntegerField(db_column='Daltonico', blank=True, null=True)  # Field name made lowercase.
    validado = models.IntegerField(db_column='Validado')  # Field name made lowercase.
    check_in_state = models.IntegerField(db_column='Check_in_state', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilizador'

class Atividade(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    localid = models.ForeignKey('Local', on_delete = models.CASCADE, db_column='LocalID', blank=True, null=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey('Utilizador', default = "", on_delete = models.CASCADE, db_column='UtilizadorID', null=True)  # Field name made lowercase.
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
        managed = True
        db_table = 'atividade'

class Material(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'material'

    def __str__ (self): 
        return str(self.nome)

class Tematica(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tematica'

    def __str__ (self): 
        return str(self.nome)

class Sessao(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora_de_inicio = models.TimeField(db_column='Hora_de_inicio', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.hora_de_inicio)

    class Meta:
        managed = False
        db_table = 'sessao'

class AtividadeDepartamento(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, on_delete = models.CASCADE, db_column='AtividadeID')  # Field name made lowercase.
    departamentoid = models.ForeignKey('Departamento', on_delete = models.CASCADE, db_column='DepartamentoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividade_departamento'


class AtividadeMaterial(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, on_delete = models.CASCADE, db_column='AtividadeID')  # Field name made lowercase.
    materialid = models.ForeignKey('Material', on_delete = models.CASCADE, db_column='MaterialID')  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividade_material'


class AtividadeTematica(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, on_delete = models.CASCADE, db_column='AtividadeID')  # Field name made lowercase.
    tematicaid = models.ForeignKey('Tematica', on_delete = models.CASCADE, db_column='TematicaID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividade_tematica'

class SessaoAtividade(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sessaoid = models.ForeignKey(Sessao, on_delete = models.CASCADE, db_column='SessaoID')  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, on_delete = models.CASCADE, db_column='AtividadeID')  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.data) + ", " + str(self.sessaoid)

    class Meta:
        managed = False
        db_table = 'sessao_atividade'


#-----------------------------REMOVE LATER-------------------------------------------------------

class Escola(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zip = models.IntegerField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.
    localidade = models.CharField(db_column='Localidade', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.nome)

    class Meta:
        managed = False
        db_table = 'escola'

class Inscricao(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    escolaid = models.ForeignKey(Escola, models.DO_NOTHING, db_column='EscolaID', blank=True, null=True)  # Field name made lowercase.
    dia = models.DateField(db_column='Dia', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        if self.escolaid:
            return "Grupo " + str(self.id) + ", " + str(self.escolaid)
        return "Grupo" + str(self.id) + ", Individual"

    class Meta:
        managed = False
        db_table = 'inscricao'

class SessaoAtividadeInscricao(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sessao_atividadeid = models.ForeignKey(SessaoAtividade, models.DO_NOTHING, db_column='Sessao_AtividadeID')  # Field name made lowercase.
    inscricaoid = models.ForeignKey(Inscricao, models.DO_NOTHING, db_column='InscricaoID')  # Field name made lowercase.
    num_alunos = models.IntegerField(db_column='Num_alunos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sessao_atividade_inscricao'

# class Image(models.Model):
#     mapa_sala= models.FileField(upload_to='images/', null=True, verbose_name="")

#     def __str__(self):
#         return str(self.mapa_sala)