from django.test import TestCase, Client
from django.contrib.auth.models import Permission
from utilizadores.models import Utilizador
from atividades.models import *
from tarefas.models import *
from django.contrib.auth.hashers import check_password, make_password

# Create your tests here.
class LoggedInTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_enter_showTarefas(self):
        response = self.client.get('/Tarefas/')
        self.assertEqual(response.status_code, 302)
    
    def test_enter_showTarefasAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can view tarefa'))
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/Tarefas/')
        self.assertEqual(response.status_code, 403)

    def test_enter_createTarefas(self):
        response = self.client.get('/Tarefas/create')
        self.assertEqual(response.status_code, 302)
    
    def test_enter_createTarefasAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can add tarefa'))
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/Tarefas/create')
        self.assertEqual(response.status_code, 403)


    def test_enter_updateTarefas(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        
        t = Tarefa(utilizadorid=u)
        t.save()
        
        response = self.client.get('/Tarefas/update/' + str(t.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_updateTarefasAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can change tarefa'))

        t = Tarefa(utilizadorid=u)
        t.save()
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/Tarefas/update/' + str(t.id))
        self.assertEqual(response.status_code, 403)

    def test_enter_deleteTarefas(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        
        t = Tarefa(utilizadorid=u)
        t.save()
        
        response = self.client.get('/Tarefas/delete/' + str(t.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_deleteTarefasAuthenticated(self):
        uo = UnidadeOrganica(nome='FE')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='A')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFE@ualg.pt',nome = 'CoordenadorFE',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can delete tarefa'))

        t = Tarefa(utilizadorid=u)
        t.save()
        
        self.client.login(email_p='coordenadorFE@ualg.pt', password_p= '12345')
        response = self.client.get('/Tarefas/delete/' + str(t.id))
        self.assertEqual(response.status_code, 403)

class PermissionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_enter_showTarefasPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        u.user_permissions.add(Permission.objects.get(name='Can view tarefa'))
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/Tarefas/')
        self.assertEqual(response.status_code, 200)
    
    def test_enter_createTarefasPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        u.user_permissions.add(Permission.objects.get(name='Can add tarefa'))
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/Tarefas/create')
        self.assertEqual(response.status_code, 200)


    def test_enter_updateTarefasPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        u.user_permissions.add(Permission.objects.get(name='Can change tarefa'))

        t = Tarefa(utilizadorid=u)
        t.save()
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/Tarefas/update/' + str(t.id))
        self.assertEqual(response.status_code, 200)


    def test_enter_deleteTarefasPermission(self):
        uo = UnidadeOrganica(nome='FE')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='A')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFE@ualg.pt',nome = 'CoordenadorFE',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        u.user_permissions.add(Permission.objects.get(name='Can delete tarefa'))

        t = Tarefa(utilizadorid=u)
        t.save()
        
        self.client.login(email_p='coordenadorFE@ualg.pt', password_p= '12345')
        response = self.client.get('/Tarefas/delete/' + str(t.id))
        self.assertEqual(response.status_code, 302)


class Colaboradores_AvailableTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_colaborador_busy(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        u.user_permissions.add(Permission.objects.get(codename='assign_tarefa'))

        t1 = Tarefa(utilizadorid=u, estado=True, horario= '09:00:00', data= '2021-02-10')
        t1.save()

        t2 = Tarefa(utilizadorid=u, estado=True, horario= '09:00:00', data= '2021-02-10')
        t2.save()
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')

        result = []
        for x in range(5):
            colab = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'colabFCT' + str(x) + '@ualg.pt',nome = 'ColabFCT' + str(x) ,data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00010, validado=1, password = make_password('12345'))
            colab.save()
            if x == 0:
                t1.colaboradores.add(colab)
            elif x > 0:
                result.append(colab)

        response = self.client.get('/Tarefas/atribuirColab/' + str(t2.id))
        self.assertEqual(response.context['colaboradores'], result)

    def test_colaborador_free(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        u.user_permissions.add(Permission.objects.get(codename='assign_tarefa'))

        t1 = Tarefa(utilizadorid=u, estado=True, horario= '09:00:00', data= '2021-02-10')
        t1.save()

        t2 = Tarefa(utilizadorid=u, estado=True, horario= '09:00:00', data= '2021-02-10')
        t2.save()
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')

        result = []
        for x in range(5):
            colab = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'colabFCT' + str(x) + '@ualg.pt',nome = 'ColabFCT' + str(x) ,data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00010, validado=1, password = make_password('12345'))
            colab.save()
            result.append(colab)

        response = self.client.get('/Tarefas/atribuirColab/' + str(t2.id))
        self.assertEqual(response.context['colaboradores'], result)
    
 
