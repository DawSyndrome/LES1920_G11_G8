from django.urls import path

from . import views


app_name =  'atividades'
urlpatterns = [
    
    path('Atividades/', views.showAtividades, name='allAtividades'),
    path('Atividades/<int:id>', views.showDetailsAtividade, name='showDetailsAtividade'),
    path('Atividades/create', views.createAtividade, name='createAtividade'),
    path('Atividades/delete/<int:id>', views.deleteAtividade, name='deleteAtividade'),
    path('Atividades/update/<int:id>', views.updateAtividade, name='updateAtividade'),
    path('Atividades/recuse/<int:id>', views.recuseAtividade, name='recuseAtividade'),
    path('Atividades/atribuir/<int:id>', views.atribuirLocal, name='atribuirLocal'),
    path('Atividades/changeAtribuir/<int:id>', views.updateAtribuirLocal, name='updateAtribuirLocal'),
    
    path('getEdificio/<int:campusid>', views.getEdificio, name='getEdificio'),
    path('getEdificioCampus/<int:campusid>', views.getEdificioCampus, name='getEdificioCampus'),
    path('getLocal/<int:edificioid>', views.getLocal, name='getLocal'),
    path('getLocalExterior/<int:campusid>', views.getLocalExterior, name='getLocalExterior'),
    path('getDescricaoLocal/<int:localid>', views.getDescricaoLocal, name='getDescricaoLocal'),
    path('getLocalImage/<int:localid>', views.getLocalImage, name='getLocalImage'),

    
    path('Edificios/', views.showEdificios, name='allEdificios'),
    path('Edificios/create', views.createEdificio, name='createEdificio'),
    path('Edificios/delete/<int:id>', views.deleteEdificio, name='deleteEdificio'),
    path('Edificios/update/<int:id>', views.updateEdificio, name='updateEdificio'),

    path('Campus/', views.showCampus, name='allCampus'),
    path('Campus/create', views.createCampus, name='addCampus'),
    path('Campus/delete/<int:id>', views.deleteCampus, name='deleteCampus'),
    path('Campus/update/<int:id>', views.updateCampus, name='updateCampus'),

    path('UnidadeOrganicas/', views.showUnidadeOrganicas, name='allUnidadeOrganicas'),
    path('UnidadeOrganicas/create', views.createUnidadeOrganica, name='createUnidadeOrganica'),
    path('UnidadeOrganicas/delete/<int:id>', views.deleteUnidadeOrganica, name='deleteUnidadeOrganica'),
    path('UnidadeOrganicas/update/<int:id>', views.updateUnidadeOrganica, name='updateUnidadeOrganica'),

    path('Departamentos/', views.showDepartamentos, name='allDepartamentos'),
    path('Departamentos/create', views.createDepartamento, name='createDepartamento'),
    path('Departamentos/delete/<int:id>', views.deleteDepartamento, name='deleteDepartamento'),
    path('Departamentos/update/<int:id>', views.updateDepartamento, name='updateDepartamento'),

    path('Locais/', views.showLocais, name='allLocais'),
    path('Locais/create', views.createLocal, name='addLocal'),
    path('Locais/delete/<int:id>', views.deleteLocal, name='deleteLocal'),
    path('Locais/update/<int:id>', views.updateLocal, name='updateLocal'),

    path('Tematicas', views.showTematicas, name='allTematicas'),
    path('Tematicas/create', views.addTematica, name='addTematica'),
    path('Tematicas/delete/<int:id>', views.deleteTematica, name='deleteTematica'),
    path('Tematicas/update/<int:id>', views.updateTematica, name='updateTematica'),

    path('Materiais/', views.showMateriais, name='allMateriais'),
    path('Materiais/create', views.createMaterial, name='addMaterial'),
    path('Materiais/delete/<int:id>', views.deleteMaterial, name='deleteMaterial'),
    path('Materiais/update/<int:id>', views.updateMaterial, name='updateMaterial'),

    path('Sessoes', views.showSessoes, name='allSessoes'),
    path('Sessoes/create', views.addSessao, name='addSessao'),
    path('Sessoes/update/<int:id>', views.updateSessao, name='updateSessao'),
    path('Sessoes/delete/<int:id>', views.deleteSessao, name="deleteSessao")
  
]

