from django.urls import path

from . import views


app_name =  'atividades'
urlpatterns = [
    path('', views.index, name='index'),
    path('GestaoAtividades/', views.gestaoAtividades, name='gestaoAtividades'),
    path('ShowAtividades/', views.showatividades, name='showatividades'),
    path('AdicionarAtividade/', views.adicionaratividade, name='adicionaratividade'),

    path('Atividades/', views.showAtividades, name='allAtividades'),
    path('Atividades/<int:id>', views.showDetailsAtividade, name='showDetailsAtividade'),
    path('Atividades/create', views.createAtividade, name='createAtividade'),
    path('Atividades/delete/<int:id>', views.deleteAtividade, name='deleteAtividade'),
    path('Atividades/update/<int:id>', views.updateAtividade, name='updateAtividade'),
    path('Atividades/valid/<int:id>', views.validAtividade, name='validAtividade'),
    path('Atividades/recuse/<int:id>', views.recuseAtividade, name='recuseAtividade'),
    path('Atividades/atribuir/<int:id>', views.atribuirLocal, name='atribuirLocal'),
    path('getEdificio/<int:campusid>', views.getEdificio, name='getEdificio'),
    path('getLocal/<int:edificioid>', views.getLocal, name='getLocal'),
    
    path('getEdificio/<int:campusid>', views.getEdificio, name='getEdificio'),
    path('getLocal/<int:edificioid>', views.getLocal, name='getLocal'),
    
    path('Edificios/', views.showEdificios, name='allEdificios'),
    path('Edificios/create/<int:saved>', views.showCreateEdificio, name='showCreateEdificio'),
    path('Edificios/add', views.createEdificio, name='addEdificio'),
    path('Edificios/delete/<int:id>', views.deleteEdificio, name='deleteEdificio'),
    path('Edificios/update/<int:id>', views.showUpdateEdificio, name='showUpdateEdificio'),
    path('Edificios/updates/<int:id>', views.updateEdificio, name='updateEdificio'),

    path('Campus/', views.showCampus, name='allCampus'),
    path('Campus/create/<int:saved>', views.showCreateCampus, name='showCreateCampus'),
    path('Campus/add', views.createCampus, name='addCampus'),
    path('Campus/delete/<int:id>', views.deleteCampus, name='deleteCampus'),
    path('Campus/update/<int:id>', views.showUpdateCampus, name='showUpdateCampus'),
    path('Campus/updates/<int:id>', views.updateCampus, name='updateCampus'),

    path('UnidadeOrganicas/', views.showUnidadeOrganicas, name='allUnidadeOrganicas'),
    path('UnidadeOrganicas/create/<int:saved>', views.showCreateUnidadeOrganica, name='showCreateUnidadeOrganica'),
    path('UnidadeOrganicas/add', views.createUnidadeOrganica, name='addUnidadeOrganica'),
    path('UnidadeOrganicas/delete/<int:id>', views.deleteUnidadeOrganica, name='deleteUnidadeOrganica'),
    path('UnidadeOrganicas/update/<int:id>', views.showUpdateUnidadeOrganica, name='showUpdateUnidadeOrganica'),
    path('UnidadeOrganicas/updates/<int:id>', views.updateUnidadeOrganica, name='updateUnidadeOrganica'),

    path('Departamentos/', views.showDepartamentos, name='allDepartamentos'),
    path('Departamentos/create/<int:saved>', views.showCreateDepartamento, name='showCreateDepartamento'),
    path('Departamentos/add', views.createDepartamento, name='addDepartamento'),
    path('Departamentos/delete/<int:id>', views.deleteDepartamento, name='deleteDepartamento'),
    path('Departamentos/update/<int:id>', views.showUpdateDepartamento, name='showUpdateDepartamento'),
    path('Departamentos/updates/<int:id>', views.updateDepartamento, name='updateDepartamento'),

    path('Locais/', views.showLocais, name='allLocais'),
    path('Locais/create/<int:saved>', views.showCreateLocal, name='showCreateLocal'),
    path('Locais/add', views.createLocal, name='addLocal'),
    path('Locais/delete/<int:id>', views.deleteLocal, name='deleteLocal'),
    path('Locais/update/<int:id>', views.showUpdateLocal, name='showUpdateLocal'),
    path('Locais/updates/<int:id>', views.updateLocal, name='updateLocal'),

    path('Tematicas', views.showTematicas, name='allTematicas'),
    path('Tematicas/create', views.addTematica, name='addTematica'),
    path('Tematicas/delete/<int:id>', views.deleteTematica, name='deleteTematica'),
    path('Tematicas/update/<int:id>', views.updateTematica, name='updateTematica'),

   path('Materiais/', views.showMateriais, name='allMateriais'),
    path('Materiais/create/<int:saved>', views.showCreateMaterial, name='showCreateMaterial'),
    path('Materiais/add', views.createMaterial, name='addMaterial'),
    path('Materiais/delete/<int:id>', views.deleteMaterial, name='deleteMaterial'),
    path('Materiais/update/<int:id>', views.showUpdateMaterial, name='showUpdateMaterial'),
    path('Materiais/updates/<int:id>', views.updateMaterial, name='updateMaterial'),

    path('Sessoes', views.showSessoes, name='allSessoes'),
    path('Sessoes/create', views.addSessao, name='addSessao'),
    path('Sessoes/update/<int:id>', views.updateSessao, name='updateSessao'),
    path('Sessoes/delete/<int:id>', views.deleteSessao, name="deleteSessao")
  
]