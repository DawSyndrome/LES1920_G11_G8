from django.urls import path

from . import views


app_name =  'tarefas'
urlpatterns = [
    path('',views.showTarefas, name='showTarefas'),
    path('create', views.createTarefa, name='createTarefa'),
    path('delete/<int:id>', views.deleteTarefa, name= 'deleteTarefa'),
    path('atribuir/<int:id>', views.atribuirTarefa, name='atribuirTarefa'),
    path('update/<int:id>', views.updateTarefa, name= 'updateTarefa'),

    path('getSessoes/<int:atividadeid>', views.getSessoes, name='getSessoes'),
    path('getSessoesByDate/<str:date>', views.getSessoesBydate, name='getSessoesByDate'),
    path('getSessoesNext/<int:sessao_atividadeid>/<str:date>', views.getSessoesNext, name='getSessoesNext'),
    path('getHoraFim/<int:sessao_atividadeid>', views.getHoraFim, name='getHoraFim'),
    path('getLocal_Sessao/<int:sessao_atividadeid>', views.getLocal_Sessao, name='getLocal_Sessao'),
    path('getGrupos/<int:sessao_atividade_origem>/<int:sessao_atividade_destino>/<str:dia>', views.getGrupos, name='getGrupos'),
    
]
