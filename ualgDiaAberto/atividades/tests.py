from django.test import TestCase, Client
from utilizadores.models import Utilizador
from atividades.models import *
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import Permission
from atividades.forms import *

#Tests for UO
class LoggedInTestCase_UO(TestCase):
    def setUp(self):
        self.client = Client()

    def test_enter_showUnidadeOrganica(self):
        response = self.client.get('/GestaoAtividades/UnidadeOrganicas/')
        self.assertEqual(response.status_code, 302)

    def test_enter_allUnidadeOrganicasAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'admin@ualg.pt',nome = 'Admin',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b10000, validado=1, password = make_password('12345'))
        u.save()
        self.client.login(email_p='admin@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/UnidadeOrganicas/')
        self.assertEqual(response.status_code, 403)

#Tests for Departamentos
class LoggedInTestCase_Departamento(TestCase):
    def setUp(self):
        self.client = Client()

    def test_enter_showDepartamentos(self):
        response = self.client.get('/GestaoAtividades/Departamentos/')
        self.assertEqual(response.status_code, 302)

    def test_enter_allDepartamentosAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'admin@ualg.pt',nome = 'Admin',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b10000, validado=1, password = make_password('12345'))
        u.save()
        self.client.login(email_p='admin@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Departamentos/')
        self.assertEqual(response.status_code, 403)

#Tests for Campus
class LoggedInTestCase_Campus(TestCase):
    def setUp(self):
        self.client = Client()

    def test_enter_showCampus(self):
        response = self.client.get('/GestaoAtividades/Campus/')
        self.assertEqual(response.status_code, 302)

    def test_enter_allCampusAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'admin@ualg.pt',nome = 'Admin',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b10000, validado=1, password = make_password('12345'))
        u.save()
        self.client.login(email_p='admin@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Campus/')
        self.assertEqual(response.status_code, 403)

#Tests for Edificios
class LoggedInTestCase_Edificios(TestCase):
    def setUp(self):
        self.client = Client()

    def test_enter_showEdificios(self):
        response = self.client.get('/GestaoAtividades/Edificios/')
        self.assertEqual(response.status_code, 302)

    def test_enter_allEdificiosAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'admin@ualg.pt',nome = 'Admin',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b10000, validado=1, password = make_password('12345'))
        u.save()
        self.client.login(email_p='admin@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Edificios/')
        self.assertEqual(response.status_code, 403)

#Tests for Locais
class LoggedInTestCase_Locais(TestCase):
    def setUp(self):
        self.client = Client()

    def test_enter_showLocais(self):
        response = self.client.get('/GestaoAtividades/Locais/')
        self.assertEqual(response.status_code, 302)

    def test_enter_allLocaisAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'admin@ualg.pt',nome = 'Admin',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b10000, validado=1, password = make_password('12345'))
        u.save()
        self.client.login(email_p='admin@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Locais/')
        self.assertEqual(response.status_code, 403)

#Tests for Materiais
class LoggedInTestCase_Materiais(TestCase):
    def setUp(self):
        self.client = Client()

    def test_enter_showMateriais(self):
        response = self.client.get('/GestaoAtividades/Materiais/')
        self.assertEqual(response.status_code, 302)

    def test_enter_allMateriaisAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'admin@ualg.pt',nome = 'Admin',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b10000, validado=1, password = make_password('12345'))
        u.save()
        self.client.login(email_p='admin@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Materiais/')
        self.assertEqual(response.status_code, 403)

#Tests for Tematicas
class LoggedInTestCase_Tematicas(TestCase):
    def setUp(self):
        self.client = Client()

    def test_enter_showTematicas(self):
        response = self.client.get('/GestaoAtividades/Tematicas')
        self.assertEqual(response.status_code, 302)

    def test_enter_allTematicasAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'admin@ualg.pt',nome = 'Admin',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b10000, validado=1, password = make_password('12345'))
        u.save()
        self.client.login(email_p='admin@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Tematicas')
        self.assertEqual(response.status_code, 403)

#Tests for Sessoes
class LoggedInTestCase_Sessoes(TestCase):
    def setUp(self):
        self.client = Client()

    def test_enter_showSessoes(self):
        response = self.client.get('/GestaoAtividades/Sessoes')
        self.assertEqual(response.status_code, 302)

    def test_enter_allSessoesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'admin@ualg.pt',nome = 'Admin',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b10000, validado=1, password = make_password('12345'))
        u.save()
        self.client.login(email_p='admin@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Sessoes')
        self.assertEqual(response.status_code, 403)

#Tests for Atividades
class LoggedInTestCase_Atividades(TestCase):
    def setUp(self):
        self.client = Client()

    #show atividades
    def test_enter_showAtividades(self):
        response = self.client.get('/GestaoAtividades/Atividades/')
        self.assertEqual(response.status_code, 302)

    def test_enter_allAtividadesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'docente@ualg.pt',nome = 'Docente',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00100, validado=1, password = make_password('12345'))
        u.save()
        self.client.login(email_p='docente@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/')
        self.assertEqual(response.status_code, 403)

    def test_enter_allAtividadesAuthenticatedPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'docente@ualg.pt',nome = 'Docente',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00100, validado=1, password = make_password('12345'))
        u.save()
        u.user_permissions.add(Permission.objects.get(name='Can view atividade'))
        self.client.login(email_p='docente@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/')
        self.assertEqual(response.status_code, 200)

    #add atividade
    def test_enter_addAtividades(self):
        response = self.client.get('/GestaoAtividades/Atividades/create')
        self.assertEqual(response.status_code, 302)

    def test_enter_addAtividadesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'docente@ualg.pt',nome = 'Docente',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00100, validado=1, password = make_password('12345'))
        u.save()
        self.client.login(email_p='docente@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/create')
        self.assertEqual(response.status_code, 403)

    def test_enter_addAtividadesAuthenticatedPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'docente@ualg.pt',nome = 'Docente',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00100, validado=1, password = make_password('12345'))
        u.save()
        da = DiaAberto(data_inicio_propor_atividades='2020-06-25', data_fim_propor_atividades='2020-07-25', data_inicio='2020-10-02', data_fim='2020-10-03')
        da.save()
        u.user_permissions.add(Permission.objects.get(name='Can add atividade'))
        self.client.login(email_p='docente@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/create')
        self.assertEqual(response.status_code, 200)

    #delete atividade
    def test_enter_deleteAtividades(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'docente@ualg.pt',nome = 'Docente',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00100, validado=1, password = make_password('12345'))
        u.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        response = self.client.get('/GestaoAtividades/Atividades/delete/' + str(a.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_deleteAtividadesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'docente@ualg.pt',nome = 'Docente',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00100, validado=1, password = make_password('12345'))
        u.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        self.client.login(email_p='docente@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/delete/' + str(a.id))
        self.assertEqual(response.status_code, 403)

    def test_enter_deleteAtividadesAuthenticatedPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'docente@ualg.pt',nome = 'Docente',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00100, validado=1, password = make_password('12345'))
        u.save()
        da = DiaAberto(data_inicio_propor_atividades='2020-06-25', data_fim_propor_atividades='2020-07-25', data_inicio='2020-10-02', data_fim='2020-10-03')
        da.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        u.user_permissions.add(Permission.objects.get(name='Can delete atividade'))
        self.client.login(email_p='docente@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/delete/' + str(a.id))
        self.assertEqual(response.status_code, 302)

    #update atividade
    def test_enter_updateAtividades(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'docente@ualg.pt',nome = 'Docente',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00100, validado=1, password = make_password('12345'))
        u.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        response = self.client.get('/GestaoAtividades/Atividades/update/' + str(a.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_updateAtividadesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'docente@ualg.pt',nome = 'Docente',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00100, validado=1, password = make_password('12345'))
        u.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        self.client.login(email_p='docente@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/update/' + str(a.id))
        self.assertEqual(response.status_code, 403)

    def test_enter_updateAtividadesAuthenticatedPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'docente@ualg.pt',nome = 'Docente',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00100, validado=1, password = make_password('12345'))
        u.save()
        da = DiaAberto(data_inicio_propor_atividades='2020-06-25', data_fim_propor_atividades='2020-07-25', data_inicio='2020-10-02', data_fim='2020-10-03')
        da.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save() 
        u.user_permissions.add(Permission.objects.get(name='Can change atividade'))
        self.client.login(email_p='docente@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/update/' + str(a.id))
        self.assertEqual(response.status_code, 200)

    #recusar atividade
    def test_enter_recuseAtividades(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenador@ualg.pt',nome = 'Coordenador',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        response = self.client.get('/GestaoAtividades/Atividades/recuse/' + str(a.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_recuseAtividadesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenador@ualg.pt',nome = 'Coordenador',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        self.client.login(email_p='coordenador@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/recuse/' + str(a.id))
        self.assertEqual(response.status_code, 403)

    def test_enter_recuseAtividadesAuthenticatedPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenador@ualg.pt',nome = 'Coordenador',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        da = DiaAberto(data_inicio_propor_atividades='2020-06-25', data_fim_propor_atividades='2020-07-25', data_inicio='2020-10-02', data_fim='2020-10-03')
        da.save()
        campus = Campus(nome='Campus de Gambelas', localizacao='Gambelas')
        campus.save()
        e = Edificio(nome_edificio='Faculdade de Ciências e Tecnologias', num_edificio='1', campusid=campus)
        e.save()
        local = Local(campusid=campus, edicifioid=e, indoor="True", sala="1.63", andar="1")
        local.save()
        u.user_permissions.add(Permission.objects.get(name='Can validate atividade'))
        self.client.login(email_p='coordenador@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/recuse/' + str(a.id))
        self.assertEqual(response.status_code, 302)

    #atruibuir local
    def test_enter_atribuirLocalAtividades(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenador@ualg.pt',nome = 'Coordenador',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        response = self.client.get('/GestaoAtividades/Atividades/atribuir/' + str(a.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_atribuirLocalAtividadesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenador@ualg.pt',nome = 'Coordenador',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can atribuir local atividade'))
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        self.client.login(email_p='coordenador@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/atribuir/' + str(a.id))
        self.assertEqual(response.status_code, 403)

    def test_enter_atribuirLocalAtividadesAuthenticatedPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenador@ualg.pt',nome = 'Coordenador',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        da = DiaAberto(data_inicio_propor_atividades='2020-06-25', data_fim_propor_atividades='2020-07-25', data_inicio='2020-10-02', data_fim='2020-10-03')
        da.save()
        campus = Campus(nome='Campus de Gambelas', localizacao='Gambelas')
        campus.save()
        e = Edificio(nome_edificio='Faculdade de Ciências e Tecnologias', num_edificio='1', campusid=campus)
        e.save()
        local = Local(campusid=campus, edicifioid=e, indoor="True", sala="1.63", andar="1")
        local.save()
        u.user_permissions.add(Permission.objects.get(name='Can atribuir local da atividade'))
        self.client.login(email_p='coordenador@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/atribuir/' + str(a.id))
        self.assertEqual(response.status_code, 200)

    #alterar local
    def test_enter_alterarLocalAtividades(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenador@ualg.pt',nome = 'Coordenador',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        response = self.client.get('/GestaoAtividades/Atividades/changeAtribuir/' + str(a.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_alterarLocalAtividadesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenador@ualg.pt',nome = 'Coordenador',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u)
        a.save()
        self.client.login(email_p='coordenador@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/changeAtribuir/' + str(a.id))
        self.assertEqual(response.status_code, 403)

    def test_enter_alterarLocalAtividadesAuthenticatedPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenador@ualg.pt',nome = 'Coordenador',data_de_nascimento =  '1999-10-05', numero_telemovel= 912912912, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        da = DiaAberto(data_inicio_propor_atividades='2020-06-25', data_fim_propor_atividades='2020-07-25', data_inicio='2020-10-02', data_fim='2020-10-03')
        da.save()
        campus = Campus(nome='Campus de Gambelas', localizacao='Gambelas')
        campus.save()
        e = Edificio(nome_edificio='Faculdade de Ciências e Tecnologias', num_edificio='1', campusid=campus)
        e.save()
        local = Local(campusid=campus, edicifioid=e, indoor="True", sala="1.63", andar="1")
        local.save()
        a = Atividade(unidadeorganicaid = uo, utilizadorid = u, localid=local)
        a.save()
        u.user_permissions.add(Permission.objects.get(name='Can alterar local da atividade'))
        self.client.login(email_p='coordenador@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoAtividades/Atividades/changeAtribuir/' + str(a.id))
        self.assertEqual(response.status_code, 200)

class FormErrors_TestCase(TestCase):

    def test_errors_SameUnidadeOrganica(self):
        uo_1 = UnidadeOrganica(nome='FCT')
        uo_1.save()
        form = UnidadeOrganicaForm({'nome' : "FCT"})
        self.assertFalse(form.is_valid())

    def test_errors_DifferentUnidadeOrganica(self):
        uo_1 = UnidadeOrganica(nome='FCT')
        uo_1.save()
        form = UnidadeOrganicaForm({'nome' : "FE"})
        self.assertTrue(form.is_valid())

    def test_errors_Atividade_1(self):
        form = AtividadeForm({'nome' : "Programar", 'tipo_atividade' : "Prática", 'descricao' : "vamos programas", 'duracao' : "50", 'limite_de_participantes' : "15", 'public_alvo' : "Estudantes", 'num_colaboradores' : "1"})
        self.assertTrue(form.is_valid())

    def test_errors_Atividade_2(self):
        form = AtividadeForm({'nome' : "Programar", 'tipo_atividade' : "Prática", 'descricao' : "vamos programas", 'duracao' : "oi", 'limite_de_participantes' : "15", 'public_alvo' : "Estudantes", 'num_colaboradores' : "1"})
        self.assertFalse(form.is_valid())

    def test_errors_SameDepartamento(self):
        uo = UnidadeOrganica(nome='Faculdade de Ciências e Tecnologias')
        uo.save()
        d_1 = Departamento(nome='FCT', unidade_organicaid=uo)
        d_1.save()
        form = DepartamentoForm({'nome' : "FCT", 'unidade_organicaid' : uo.id})
        self.assertFalse(form.is_valid())

    def test_errors_DifferentDepartamento(self):
        uo = UnidadeOrganica(nome='Faculdade de Ciências e Tecnologias')
        uo.save()
        d_1 = Departamento(nome='FCT', unidade_organicaid=uo)
        d_1.save()
        form = DepartamentoForm({'nome' : "DEEI", 'unidade_organicaid' : uo.id})
        self.assertTrue(form.is_valid())

    def test_errors_SameCampus(self):
        campus_1 = Campus(nome='Campus de Gambelas', localizacao='Gambelas')
        campus_1.save()
        form = CampusForm({'nome' : "Campus de Gambelas", 'localizacao' : "Gambelas"})
        self.assertFalse(form.is_valid())

    def test_errors_DifferentCampus(self):
        campus_1 = Campus(nome='Campus de Gambelas', localizacao='Gambelas')
        campus_1.save()
        form = CampusForm({'nome' : "Campus da Penha", 'localizacao' : "Penha"})
        self.assertTrue(form.is_valid())

    def test_errors_SameEdifico(self):
        campus = Campus(nome='Campus de Gambelas', localizacao='Gambelas')
        campus.save()
        e = Edificio(nome_edificio='Faculdade de Ciências e Tecnologias', num_edificio='1', campusid=campus)
        e.save()
        form = EdificioForm({'nome_edificio' : "Faculdade de Ciências e Tecnologias", 'num_edificio' : "1", 'campusid' : campus.id})
        self.assertFalse(form.is_valid())

    def test_errors_DifferentEdificio(self):
        campus = Campus(nome='Campus de Gambelas', localizacao='Gambelas')
        campus.save()
        e = Edificio(nome_edificio='Faculdade de Ciências e Tecnologias', num_edificio='1', campusid=campus)
        e.save()
        form = EdificioForm({'nome_edificio' : "Faculdade de Economia", 'num_edificio' : "9", 'campusid' : campus.id})
        self.assertTrue(form.is_valid())

    def test_errors_SameLocal(self):
        campus = Campus(nome='Campus de Gambelas', localizacao='Gambelas')
        campus.save()
        e = Edificio(nome_edificio='Faculdade de Ciências e Tecnologias', num_edificio='1', campusid=campus)
        e.save()
        local = Local(campusid=campus, edicifioid=e, indoor="True", sala="1.63", andar="1")
        local.save()
        form = LocalForm({'campusid' : campus.id, 'edicifioid' : e.id, 'indoor' : "True", 'sala' : "1.63", 'andar' : "1"})
        self.assertFalse(form.is_valid())

    def test_errors_DifferentLocal(self):
        campus = Campus(nome='Campus de Gambelas', localizacao='Gambelas')
        campus.save()
        e = Edificio(nome_edificio='Faculdade de Ciências e Tecnologias', num_edificio='1', campusid=campus)
        e.save()
        local = Local(campusid=campus, edicifioid=e, indoor="True", sala="1.63", andar="1")
        local.save()
        form = LocalForm({'campusid' : campus.id, 'edicifioid' : e.id, 'indoor' : "True", 'sala' : "2.1", 'andar' : "2"})
        self.assertTrue(form.is_valid())

    def test_errors_SameMaterial(self):
        material = Material(nome="Caneta")
        material.save()
        form = MaterialForm({'nome' : "Caneta"})
        self.assertFalse(form.is_valid())

    def test_errors_DifferentMaterial(self):
        material = Material(nome="Caneta")
        material.save()
        form = MaterialForm({'nome' : "Computador"})
        self.assertTrue(form.is_valid())

    def test_errors_SameTematica(self):
        tematica = Tematica(nome="Matemática")
        tematica.save()
        form = TematicaForm({'nome' : "Matemática"})
        self.assertFalse(form.is_valid())

    def test_errors_DifferentTematica(self):
        tematica = Tematica(nome="Matemática")
        tematica.save()
        form = TematicaForm({'nome' : "Desporto"})
        self.assertTrue(form.is_valid())

    def test_errors_SameSessao(self):
        sessao = Sessao(hora_de_inicio="09:00")
        sessao.save()
        form = SessaoForm({'hora_de_inicio' : "09:00"})
        self.assertFalse(form.is_valid())

    def test_errors_DifferentSessao(self):
        sessao = Sessao(hora_de_inicio="09:00")
        sessao.save()
        form = SessaoForm({'hora_de_inicio' : "10:00"})
        self.assertTrue(form.is_valid())
