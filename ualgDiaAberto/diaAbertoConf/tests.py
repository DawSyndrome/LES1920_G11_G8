from django.test import TestCase, Client
from django.contrib.auth.models import Permission
from utilizadores.models import Utilizador
from atividades.models import *
from .models import *
from django.contrib.auth.hashers import check_password, make_password
from .forms import *

# Create your tests here.
class LoggedInTestCase_Transportes(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_enter_showTransportes(self):
        response = self.client.get('/Transportes/')
        self.assertEqual(response.status_code, 302)
    
    def test_enter_showTransportesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can view tarefa'))
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/Transportes/')
        self.assertEqual(response.status_code, 403)

    def test_enter_createTransportes(self):
        response = self.client.get('/Transportes/create')
        self.assertEqual(response.status_code, 302)
    
    def test_enter_createTransportesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can add tarefa'))
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/Transportes/create')
        self.assertEqual(response.status_code, 403)


    def test_enter_updateTransportes(self):     
        t = Transporte(tipo_transporte='Autocarro', capacidade=10)
        t.save()
        
        response = self.client.get('/Transportes/update/' + str(t.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_updateTransportesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can change tarefa'))

        t = Transporte(tipo_transporte='Autocarro', capacidade=10)
        t.save()
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/Transportes/update/' + str(t.id))
        self.assertEqual(response.status_code, 403)

    def test_enter_deleteTransportes(self):
        t = Transporte(tipo_transporte='Autocarro', capacidade=10)
        t.save()
        
        response = self.client.get('/Transportes/delete/' + str(t.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_deleteTransportesAuthenticated(self):
        uo = UnidadeOrganica(nome='FE')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='A')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFE@ualg.pt',nome = 'CoordenadorFE',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can delete tarefa'))

        t = Transporte(tipo_transporte='Autocarro', capacidade=10)
        t.save()
        
        self.client.login(email_p='coordenadorFE@ualg.pt', password_p= '12345')
        response = self.client.get('/Transportes/delete/' + str(t.id))
        self.assertEqual(response.status_code, 403)

class LoggedInTestCase_HorariosTransportes(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_enter_showHorariosTransportes(self):
        response = self.client.get('/Transportes/HorariosTransporte/')
        self.assertEqual(response.status_code, 302)
    
    def test_enter_showHorariosTransportesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can view tarefa'))
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/Transportes/HorariosTransporte/')
        self.assertEqual(response.status_code, 403)

    def test_enter_createHorariosTransportes(self):
        response = self.client.get('/Transportes/HorariosTransporte/create')
        self.assertEqual(response.status_code, 302)
    
    def test_enter_createHorariosTransportesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can add tarefa'))
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/Transportes/HorariosTransporte/create')
        self.assertEqual(response.status_code, 403)


    def test_enter_updateHorariosTransportes(self):     
        t = HorarioTransporte(hora_de_chegada= '09:00:00', hora_de_partida='10:00:00')
        t.save()
        
        response = self.client.get('/Transportes/HorariosTransporte/update/' + str(t.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_updateHorariosTransportesAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can change tarefa'))

        t = HorarioTransporte(hora_de_chegada= '09:00:00', hora_de_partida='10:00:00')
        t.save()
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/Transportes/HorariosTransporte/update/' + str(t.id))
        self.assertEqual(response.status_code, 403)

    def test_enter_deleteHorariosTransportes(self):
        t = HorarioTransporte(hora_de_chegada= '09:00:00', hora_de_partida='10:00:00')
        t.save()
        
        response = self.client.get('/Transportes/HorariosTransporte/update/' + str(t.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_deleteHorariosTransportesAuthenticated(self):
        uo = UnidadeOrganica(nome='FE')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='A')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFE@ualg.pt',nome = 'CoordenadorFE',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can delete tarefa'))

        t = HorarioTransporte(hora_de_chegada= '09:00:00', hora_de_partida='10:00:00')
        t.save()

        self.client.login(email_p='coordenadorFE@ualg.pt', password_p= '12345')
        response = self.client.get('/Transportes/HorariosTransporte/update/' + str(t.id))
        self.assertEqual(response.status_code, 403)

class PermissionTestCase_Transportes(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_enter_showTransportesPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'admin@ualg.pt',nome = 'Admin',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b10000, validado=1, password = make_password('12345'))
        u.save()
        u.user_permissions.set(Permission.objects.all())
        
        self.client.login(email_p='admin@ualg.pt', password_p= '12345')
        response = self.client.get('/Transportes/')
        self.assertEqual(response.status_code, 200)
    
    def test_enter_createTransportesPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'admin@ualg.pt',nome = 'Admin',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b10000, validado=1, password = make_password('12345'))
        u.save()
        u.user_permissions.set(Permission.objects.all())
        
        self.client.login(email_p='admin@ualg.pt', password_p= '12345')
        response = self.client.get('/Transportes/create')
        self.assertEqual(response.status_code, 200)

    def test_enter_updateTransportesPermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'admin@ualg.pt',nome = 'Admin',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b10000, validado=1, password = make_password('12345'))
        u.save()
        u.user_permissions.set(Permission.objects.all())

        t = Transporte(tipo_transporte='Autocarro', capacidade=10)
        t.save()
        
        self.client.login(email_p='admin@ualg.pt', password_p= '12345')
        response = self.client.get('/Transportes/update/' + str(t.id))
        self.assertEqual(response.status_code, 200)


    def test_enter_deleteTransportePermission(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'admin@ualg.pt',nome = 'Admin',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b10000, validado=1, password = make_password('12345'))
        u.save()
        u.user_permissions.set(Permission.objects.all())

        t = Transporte(tipo_transporte='Autocarro', capacidade=10)
        t.save()
        
        self.client.login(email_p='coordenadorFE@ualg.pt', password_p= '12345')
        response = self.client.get('/Transportes/delete/' + str(t.id))
        self.assertEqual(response.status_code, 302)


class TransporteForm_TestCase(TestCase):

    def test_form_Valid(self):
        t = HorarioTransporte(hora_de_chegada= '09:00:00', hora_de_partida='10:00:00')
        t.save()
        formTransporte = TransporteForm({'tipo_transporte': "autocarro", 'capacidade': 40})
        formRota = RotaForm({'horarioid': [t.id], 'origem': "Gambelas", 'destino': "Penha", 'data': "10/02/2021"})
        self.assertEqual(formTransporte.is_valid(), formRota.is_valid())


class HorarioTransporteForm_TestCase(TestCase):
    
    def test_form_Valid(self):
        form = HorarioTransporteForm({'hora_de_partida':"09:00:00", 'hora_de_chegada':"10:00:00"})
        self.assertTrue(form.is_valid())
    
    def test_form_HoraAlreadyExists(self):
        h = HorarioTransporte(hora_de_partida="09:00:00", hora_de_chegada="10:00:00")
        h.save()
        form = HorarioTransporteForm({'hora_de_partida':"09:00:00", 'hora_de_chegada':"10:00:00"})
        self.assertFalse(form.is_valid())
    
    def test_form_ChegadaLessThanPartida(self):
        form = HorarioTransporteForm({'hora_de_partida':"11:00:00", 'hora_de_chegada':"10:00:00"})
        self.assertFalse(form.is_valid())


class LoggedInTestCase_Ementa(TestCase):

    def setUp(self):
        self.client = Client()

    def test_enter_showEmentas(self):
        response = self.client.get('/GestaoEmentas/') 
        self.assertEqual(response.status_code, 302) 

    def test_enter_showEmentas_Authenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can view tarefa'))
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoEmentas/')
        self.assertEqual(response.status_code, 403) 
    def test_enter_createEmentas(self):
        response = self.client.get('/GestaoEmentas/create')
        self.assertEqual(response.status_code, 302)
    
    def test_enter_createEmentasAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can add tarefa'))
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoEmentas/create')
        self.assertEqual(response.status_code, 403)

    def test_enter_updateEmentas(self):     
        e = Ementa(dia='2020-04-23')
        e.save()
        
        response = self.client.get('/GestaoEmentas/update/' + str(e.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_updateEmentasAuthenticated(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can change tarefa'))

        e = Ementa(dia='2020-04-23')
        e.save()
        
        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoEmentas/update/' + str(e.id))
        self.assertEqual(response.status_code, 403)

    def test_enter_deleteEmentas(self):
        e = Ementa(dia='2020-04-23')
        e.save()
        
        response = self.client.get('/GestaoEmentas/delete/' + str(e.id))
        self.assertEqual(response.status_code, 302)

    def test_enter_deleteEmentasAuthenticated(self):
        uo = UnidadeOrganica(nome='FE')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='A')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFE@ualg.pt',nome = 'CoordenadorFE',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can delete tarefa'))

        e = Ementa(dia='2020-04-23')
        e.save()
        
        self.client.login(email_p='coordenadorFE@ualg.pt', password_p= '12345')
        response = self.client.get('/GestaoEmentas/delete/' + str(e.id))
        self.assertEqual(response.status_code, 403)


class EmentaForm_TestCase(TestCase):

    def test_form_Valid(self):
        formEmenta = EmentaForm({'dia': "2020-05-31"})
        self.assertTrue(formEmenta.is_valid())

    def test_form_not_Valid(self):   
        formEmenta = EmentaForm({'dia': "Maio"})
        self.assertFalse(formEmenta.is_valid()) 

    def test_pratoForm_Valid(self):
        e = Ementa(dia='2020-05-31')
        e.save()    
        formPrato = PratoForm({'ementaid': [e.id], 'nome' : "Cenoura", 'tipo': "Sopa", 'descricao' : "F"})
        self.assertTrue(formPrato.is_valid())

    def test_pratoForm_not_Valid(self):
        e = Ementa(dia='2020-05-31')
        e.save()    
        formPrato = PratoForm({'ementaid': [e.id], 'nome' : 40, 'tipo': "Sopa", 'descricao' : "F"})
        self.assertTrue(formPrato.is_valid())    
        

class LoggedInTestCase_DiaAbertoConfig(TestCase):

    def setUP(self):
        self.client= Client()

    def test_enter_ShowConfig(self):
        response = self.client.get('/DiaAbertoConf/') 
        self.assertEqual(response.status_code, 302)

    def test_enter_ShowConfig_Authenticaded(self):
        uo = UnidadeOrganica(nome='FCT')
        uo.save()
        d = Departamento(unidade_organicaid = uo, nome='DEEI')
        d.save()
        u = Utilizador(unidade_orgânicaid = uo, departamentoid = d, email = 'coordenadorFCT@ualg.pt',nome = 'CoordenadorFCT',data_de_nascimento =  '1999-10-05', numero_telemovel= 99999, user_type= 0b00001, validado=1, password = make_password('12345'))
        u.save()
        #u.user_permissions.add(Permission.objects.get(name='Can view tarefa'))

        self.client.login(email_p='coordenadorFCT@ualg.pt', password_p= '12345')
        response = self.client.get('/DiaAbertoConf/')
        self.assertEqual(response.status_code, 403)


class DiaAbertoForm_TestCase(TestCase):

    def test_form_Valid(self):
        form = DiaAbertoForm({'titulo': "AA", 
        'descricao' : "FF", 
        'email':"DD", 
        'contacto':112, 
        'data_inicio':"2020-05-30", 'data_fim':"2020-05-31", 
        'data_inicio_inscricao': "2020-04-01",'data_fim_inscricao':"2020-04-20", 
        'data_inicio_propor_atividades' : "2020-02-15",'data_fim_propor_atividades':"2020-03-20",
        'preco_aluno':3.5,'preco_professor':5.0})
        self.assertTrue(form.is_valid())

    def test_form_dInicio_After_dFim(self):
        form = DiaAbertoForm({'titulo': "AA", 
        'descricao' : "FF", 
        'email':"DD", 
        'contacto':112, 
        'data_inicio':"2020-05-31", 'data_fim':"2020-05-30", 
        'data_inicio_inscricao': "2020-04-01",'data_fim_inscricao':"2020-04-20", 
        'data_inicio_propor_atividades' : "2020-02-15",'data_fim_propor_atividades':"2020-03-20",
        'preco_aluno':3.5,'preco_professor':5.0})
        self.assertFalse(form.is_valid()) 

    def test_form_dInicInsc_After_dFimInsc(self):
        form = DiaAbertoForm({'titulo': "AA", 
        'descricao' : "FF", 
        'email':"DD", 
        'contacto':112, 
        'data_inicio':"2020-05-30", 'data_fim':"2020-05-31", 
        'data_inicio_inscricao': "2020-04-20",'data_fim_inscricao':"2020-04-01", 
        'data_inicio_propor_atividades' : "2020-02-15",'data_fim_propor_atividades':"2020-03-20",
        'preco_aluno':3.5,'preco_professor':5.0})
        self.assertFalse(form.is_valid())

    def test_form_dIpropAtiv_After_dFpropAtiv(self):
        form = DiaAbertoForm({'titulo': "AA", 
        'descricao' : "FF", 
        'email':"DD", 
        'contacto':112, 
        'data_inicio':"2020-05-30", 'data_fim':"2020-05-31", 
        'data_inicio_inscricao': "2020-04-01",'data_fim_inscricao':"2020-04-20", 
        'data_inicio_propor_atividades' : "2020-03-20",'data_fim_propor_atividades':"2020-02-20",
        'preco_aluno':3.5,'preco_professor':5.0})
        self.assertFalse(form.is_valid()) 

    def test_form_dInicInsc_After_dIpropAtiv(self): 
        form = DiaAbertoForm({'titulo': "AA", 
        'descricao' : "FF", 
        'email':"DD", 
        'contacto':112, 
        'data_inicio':"2020-05-31", 'data_fim':"2020-05-31", 
        'data_inicio_inscricao': "2020-04-21",'data_fim_inscricao':"2020-04-01", 
        'data_inicio_propor_atividades' : "2020-03-20",'data_fim_propor_atividades':"2020-04-20",
        'preco_aluno':3.5,'preco_professor':5.0})
        self.assertFalse(form.is_valid())          

