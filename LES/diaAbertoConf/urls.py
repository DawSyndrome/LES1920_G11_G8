from django.urls import path

from . import views


app_name =  'diaAbertoConf'
urlpatterns = [
    path('', views.index, name='index'),
    path('DiaAbertoConf/', views.editConfDiaAberto, name='editConfig'),
    
    path('Transportes/', views.showTransportes, name='allTransportes'),
    path('Transportes/create', views.createTransporte, name='createTransporte'),
    path('Transportes/delete/<int:id>', views.deleteTransporte, name= 'deleteTransporte'),
    path('Transportes/update/<int:id>', views.updateTransporte, name='updateTransporte'),

    path('Transportes/HorariosTransporte/', views.showHorarios_Transporte, name='allHorarios'),
    path('Transportes/HorariosTransporte/create', views.createHorario_Transporte, name='createHorarioTransporte'),
    path('Transportes/HorariosTransporte/delete/<int:id>', views.deleteHorario_Transporte, name= 'deleteHorarioTransporte'),
    path('Transportes/HorariosTransporte/update/<int:id>', views.updateHorario_Transporte, name='updateHorarioTransporte'),

    path('Transportes/<int:id>/InscriçãoAssociada/', views.showInscAssociada, name= 'showInscAssociadas'),
    path('Transportes/<int:id>/InscriçãoAssociada/create', views.createInscAssociada, name= 'createInscAssociadas'),
    path('Transportes/<int:id>/InscriçãoAssociada/update/<int:idRota_Insc>', views.updateInscAssociada, name='updateInscAssociadas'),
    path('Transportes/<int:id>/InscriçãoAssociada/delete/<int:idRota_Insc>', views.deleteInscAssociada, name= 'deleteInscAssociadas'),


    path('GestaoEmentas/',views.gestaoEmentas, name='gestaoEmentas'),
    path('GestaoEmentas/delete/<int:id>',views.deleteEmenta, name='deleteEmenta'),
    path('GestaoEmentas/create',views.showNewEmenta, name='showNewEmenta'),
    path('GestaoEmentas/add', views.newEmenta, name='newEmenta'),
    path('GestaoEmentas/create/createPratos/<int:id>',views.showNewPratos, name='showNewPratos'),
    path('GestaoEmentas/create/addPratos/<int:id>', views.newPrato, name='newPratos'),
    path('GestaoEmentas/update/<int:id>', views.showEditEmenta, name='showEditEmenta'),
    path('GestaoEmentas/updates/<int:id>', views.editEmenta, name= 'editEmenta'),
    path('GestaoEmentas/update/update_Prato/<int:id>', views.editPrato, name= 'editPrato'),
    path('GestaoEmentas/update/delete_Prato/<int:id>', views.deletePrato, name= 'deletePrato'),
    

]   
