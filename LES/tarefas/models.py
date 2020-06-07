from django.db import models

# Create your models here.

class Tarefa(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sessao_atividadeid_destino = models.ForeignKey("atividades.SessaoAtividade", related_name='destino', on_delete=models.SET_NULL, db_column='Sessao_AtividadeID_Destino', blank=True, null=True)  # Field name made lowercase.
    sessao_atividadeid_origem = models.ForeignKey("atividades.SessaoAtividade", related_name='origem', on_delete=models.SET_NULL, db_column='Sessao_AtividadeID_Origem', blank=True, null=True)  # Field name made lowercase.
    sessao_atividadeid = models.ForeignKey("atividades.SessaoAtividade", related_name='TarefaSessaoAtividade', on_delete=models.CASCADE, db_column='SessaoAtividadeID', blank=True, null=True)
    utilizadorid = models.ForeignKey("atividades.Utilizador", models.DO_NOTHING, db_column='UtilizadorID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipoTarefa = models.CharField(db_column='TipoTarefa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    origem = models.CharField(db_column='Origem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destino = models.CharField(db_column='Destino', max_length=255, blank=True, null=True)  # Field name made lowercase.
    horario = models.TimeField(db_column='Horario', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tarefa'

class ColaboradorTarefa(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey("atividades.Utilizador", on_delete=models.CASCADE, db_column='UtilizadorID')  # Field name made lowercase.
    tarefaid = models.ForeignKey(Tarefa, on_delete=models.CASCADE, db_column='TarefaID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilizador_tarefa'

class InscricaoTarefa(models.Model):
    inscricaoid = models.ForeignKey("atividades.Inscricao", on_delete=models.CASCADE, db_column='InscricaoID', blank=True, null=True)
    tarefaid = models.ForeignKey(Tarefa, on_delete=models.CASCADE, db_column='TarefaID', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inscricao_tarefa'
