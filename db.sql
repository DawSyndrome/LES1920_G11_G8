--
-- Create model Atividade
--
CREATE TABLE `atividade` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL, `Descrição` varchar(255) NULL, `Duração` integer NULL, `Limite_de_participantes` integer NULL, `Validada` integer NULL, `Tipo_atividade` varchar(255) NULL, `Public_alvo` varchar(255) NULL);
--
-- Create model AuthGroup
--
CREATE TABLE `auth_group` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(150) NOT NULL UNIQUE);
--
-- Create model AuthUser
--
CREATE TABLE `auth_user` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `password` varchar(128) NOT NULL, `last_login` datetime(6) NULL, `is_superuser` integer NOT NULL, `username` varchar(150) NOT NULL UNIQUE, `first_name` varchar(30) NOT NULL, `last_name` varchar(150) NOT NULL, `email` varchar(254) NOT NULL, `is_staff` integer NOT NULL, `is_active` integer NOT NULL, `date_joined` datetime(6) NOT NULL);
--
-- Create model Campus
--
CREATE TABLE `campus` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL, `Localização` varchar(255) NULL, `Contacto` integer NULL);
--
-- Create model Departamento
--
CREATE TABLE `departamento` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL);
--
-- Create model DiaAberto
--
CREATE TABLE `dia aberto` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Titulo` varchar(255) NULL, `Descrição` varchar(255) NULL, `Email` varchar(255) NULL, `Contacto` integer NULL, `Data_inicio` date NULL, `Data_fim` date NULL, `Limite_de_inscrição_atividades` date NULL, `Limite_de_inscrição_participantes` date NULL);
--
-- Create model DjangoMigrations
--
CREATE TABLE `django_migrations` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `app` varchar(255) NOT NULL, `name` varchar(255) NOT NULL, `applied` datetime(6) NOT NULL);
--
-- Create model DjangoSession
--
CREATE TABLE `django_session` (`session_key` varchar(40) NOT NULL PRIMARY KEY, `session_data` longtext NOT NULL, `expire_date` datetime(6) NOT NULL);
--
-- Create model Edicifio
--
CREATE TABLE `edicifio` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Numero edificio` integer NULL);
--
-- Create model Ementa
--
CREATE TABLE `ementa` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Dia` date NULL, `Preço_economico_aluno` double precision NULL, `Preço_normal_aluno` double precision NULL, `Preço_economico_outro` double precision NULL, `Preço_outro` double precision NULL);
--
-- Create model Escola
--
CREATE TABLE `escola` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL, `Morada` varchar(255) NULL, `Zip` integer NULL, `Contacto` integer NULL, `Localidade` varchar(255) NULL);
--
-- Create model GestoDePerfil
--
CREATE TABLE `gestão de perfil` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Validação` integer NULL);
--
-- Create model Horario
--
CREATE TABLE `horario` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Hora_de_partida` time(6) NULL, `Data` date NULL);
--
-- Create model Inscrio
--
CREATE TABLE `inscrição` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Dia` date NULL, `EscolaID` integer NULL);
--
-- Create model Material
--
CREATE TABLE `material` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL);
--
-- Create model Question
--
CREATE TABLE `gottem_question` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `question_text` varchar(200) NOT NULL, `pub_date` datetime(6) NOT NULL);
--
-- Create model RegistoHorrio
--
CREATE TABLE `registo horário` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Hora_inicio` time(6) NULL, `Hora_fim` time(6) NULL, `Data` date NULL);
--
-- Create model Sesso
--
CREATE TABLE `sessão` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Hora_de inicio` time(6) NULL);
--
-- Create model SessoAtividade
--
CREATE TABLE `sessão-atividade` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Data` date NULL, `AtividadeID` integer NOT NULL, `SessãoID` integer NOT NULL);
--
-- Create model SessoAtividadeInscrio
--
CREATE TABLE `sessão-atividade-inscrição` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Num_alunos` integer NULL, `InscriçãoID` integer NOT NULL, `Sessão-AtividadeID` integer NOT NULL);
--
-- Create model Temtica
--
CREATE TABLE `temática` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL);
--
-- Create model Transporte
--
CREATE TABLE `transporte` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Hora_de_chegada` date NULL, `Hora_de_partida` date NULL, `Tipo_de_transporte` varchar(255) NULL, `Capacidade` integer NULL);
--
-- Create model TransporteUniversitrioHorario
--
CREATE TABLE `transporte_universitário-horario` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Origem` varchar(255) NULL, `Destino` varchar(255) NULL, `Data` date NULL, `HorarioID` integer NOT NULL, `TransporteID` integer NOT NULL);
--
-- Create model UnidadeOrgnica
--
CREATE TABLE `unidade orgânica` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL, `CampusID` integer NOT NULL);
--
-- Create model Utilizador
--
CREATE TABLE `utilizador` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Email` varchar(255) NULL, `Nome` varchar(255) NULL, `Data_de_nascimento` date NULL, `Numero_telemovel` integer NULL, `Cartão_cidadão` integer NULL, `Deficiencias` varchar(255) NULL, `Permitir_localização` integer NULL, `Utilizar_dados_pessoais` integer NULL, `Tema_do_website` integer NULL, `User_type` integer NOT NULL, `Daltonico` integer NULL, `Validado` integer NOT NULL, `Check_in_state` integer NOT NULL, `DepartamentoID` integer NULL, `Gestão de PerfilID` integer NOT NULL, `InscriçãoID` integer NOT NULL, `Registo HorárioID` integer NOT NULL, `Unidade OrgânicaID` integer NULL);
--
-- Create model Tarefa
--
CREATE TABLE `tarefa` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Descrição` varchar(255) NULL, `Localização do grupo` varchar(255) NULL, `Destino` varchar(255) NULL, `Horário` time(6) NULL, `TarefaTransporte` integer NULL, `Sessão-Atividade-InscriçãoID_Destino` integer NULL, `Sessão-Atividade-InscriçãoID_Origem` integer NOT NULL, `UtilizadorID` integer NOT NULL);
--
-- Create model Prato
--
CREATE TABLE `prato` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL, `Tipo` varchar(255) NULL, `Descriçao` varchar(255) NULL, `EmentaID` integer NOT NULL);
--
-- Create model Participanteinfo
--
CREATE TABLE `participanteinfo` (`ParticipanteInfoID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Ano escolar` integer NOT NULL, `Area` varchar(255) NULL, `Checkin_state` integer NOT NULL, `Participante_type` integer NULL, `Total_de_participantes` integer NULL, `Total_de_professores` integer NULL, `Turma` varchar(255) NULL, `Autorização` integer NULL, `Ficheiro_autorização` varchar(255) NULL, `Acompanhates` integer NULL, `TipoParticipante` varchar(255) NULL, `UtilizadorID` integer NOT NULL);
--
-- Create model Notificaes
--
CREATE TABLE `notificações` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Conteudo` varchar(255) NULL, `Hora_envio` time(6) NULL, `Data` date NULL, `Prioridade` integer NULL, `Assunto` varchar(255) NULL, `UtilizadorID_Envia` integer NOT NULL, `UtilizadorID_Recebe` integer NOT NULL);
--
-- Create model Local
--
CREATE TABLE `local` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Andar` integer NULL, `Sala` integer NULL, `Descriçao` varchar(255) NULL, `Indoor` integer NULL, `EdicifioID` integer NOT NULL);
--
-- Create model DjangoContentType
--
CREATE TABLE `django_content_type` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `app_label` varchar(100) NOT NULL, `model` varchar(100) NOT NULL);
--
-- Create model DjangoAdminLog
--
CREATE TABLE `django_admin_log` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `action_time` datetime(6) NOT NULL, `object_id` longtext NULL, `object_repr` varchar(200) NOT NULL, `action_flag` smallint UNSIGNED NOT NULL CHECK (`action_flag` >= 0), `change_message` longtext NOT NULL, `content_type_id` integer NULL, `user_id` integer NOT NULL);
--
-- Add field unidade_orgânicaid to departamento
--
ALTER TABLE `departamento` ADD COLUMN `Unidade OrgânicaID` integer NOT NULL , ADD CONSTRAINT `departamento_Unidade OrgânicaID_eac1b380_fk_unidade orgânica_ID` FOREIGN KEY (`Unidade OrgânicaID`) REFERENCES `unidade orgânica`(`ID`);
--
-- Create model Choice
--
CREATE TABLE `gottem_choice` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `choice_text` varchar(200) NOT NULL, `votes` integer NOT NULL, `question_id` integer NOT NULL);
--
-- Create model AuthPermission
--
CREATE TABLE `auth_permission` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(255) NOT NULL, `codename` varchar(100) NOT NULL, `content_type_id` integer NOT NULL);
--
-- Create model AtividadeTematica
--
CREATE TABLE `atividade-tematica` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `AtividadeID` integer NOT NULL, `TemáticaID` integer NOT NULL);
--
-- Create model AtividadeMaterial
--
CREATE TABLE `atividade-material` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Quantidade` integer NULL, `AtividadeID` integer NOT NULL, `MaterialID` integer NOT NULL);
--
-- Add field localid to atividade
--
ALTER TABLE `atividade` ADD COLUMN `LocalID` integer NOT NULL , ADD CONSTRAINT `atividade_LocalID_ce6b2dd9_fk_local_ID` FOREIGN KEY (`LocalID`) REFERENCES `local`(`ID`);
--
-- Add field unidadeorganicaid to atividade
--
ALTER TABLE `atividade` ADD COLUMN `UnidadeOrganicaID` integer NOT NULL , ADD CONSTRAINT `atividade_UnidadeOrganicaID_4614a1d3_fk_unidade orgânica_ID` FOREIGN KEY (`UnidadeOrganicaID`) REFERENCES `unidade orgânica`(`ID`);
--
-- Add field utilizadorid to atividade
--
ALTER TABLE `atividade` ADD COLUMN `UtilizadorID` integer NOT NULL , ADD CONSTRAINT `atividade_UtilizadorID_007a36c0_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador`(`ID`);
--
-- Create model AuthUserUserPermissions
--
CREATE TABLE `auth_user_user_permissions` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `permission_id` integer NOT NULL, `user_id` integer NOT NULL);
--
-- Create model AuthUserGroups
--
CREATE TABLE `auth_user_groups` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `group_id` integer NOT NULL, `user_id` integer NOT NULL);
--
-- Create model AuthGroupPermissions
--
CREATE TABLE `auth_group_permissions` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `group_id` integer NOT NULL, `permission_id` integer NOT NULL);
--
-- Create model UtilizadorTransporte
--
CREATE TABLE `utilizador_transporte` (`UtilizadorID` integer NOT NULL PRIMARY KEY, `TransporteID` integer NOT NULL);
--
-- Create model UtilizadorTarefa
--
CREATE TABLE `utilizador_tarefa` (`UtilizadorID` integer NOT NULL PRIMARY KEY, `TarefaID` integer NOT NULL);
--
-- Create model UtilizadorEmenta
--
CREATE TABLE `utilizador_ementa` (`UtilizadorID` integer NOT NULL PRIMARY KEY, `EmentaID` integer NOT NULL);
--
-- Create model UtilizadorAtividade
--
CREATE TABLE `utilizador_atividade` (`UtilizadorID` integer NOT NULL PRIMARY KEY, `AtividadeID` integer NOT NULL);
--
-- Create model TransporteUniversitrioHorarioInscrio
--
CREATE TABLE `transporte_universitário-horario_inscrição` (`Transporte_Universitário-HorarioID` integer NOT NULL PRIMARY KEY, `InscriçãoID` integer NOT NULL);
--
-- Create model TarefaSessoAtividade
--
CREATE TABLE `tarefa_sessão-atividade` (`TarefaID` integer NOT NULL PRIMARY KEY, `Sessão-AtividadeID` integer NOT NULL);
--
-- Create model InscrioEmenta
--
CREATE TABLE `inscrição_ementa` (`InscriçãoID` integer NOT NULL PRIMARY KEY, `EmentaID` integer NOT NULL);
--
-- Create model DiaAbertoUtilizador
--
CREATE TABLE `dia aberto_utilizador` (`Dia AbertoID` integer NOT NULL PRIMARY KEY, `UtilizadorID` integer NOT NULL);
--
-- Create model AtividadeDepartamento
--
CREATE TABLE `atividade_departamento` (`AtividadeID` integer NOT NULL PRIMARY KEY, `DepartamentoID` integer NOT NULL);
ALTER TABLE `inscrição` ADD CONSTRAINT `inscrição_EscolaID_e66e82f0_fk_escola_ID` FOREIGN KEY (`EscolaID`) REFERENCES `escola` (`ID`);
ALTER TABLE `sessão-atividade` ADD CONSTRAINT `sessão-atividade_AtividadeID_f32ff99c_fk_atividade_ID` FOREIGN KEY (`AtividadeID`) REFERENCES `atividade` (`ID`);
ALTER TABLE `sessão-atividade` ADD CONSTRAINT `sessão-atividade_SessãoID_f055d000_fk_sessão_ID` FOREIGN KEY (`SessãoID`) REFERENCES `sessão` (`ID`);
ALTER TABLE `sessão-atividade-inscrição` ADD CONSTRAINT `sessão-atividade-inscrição_InscriçãoID_2810ac0d_fk_inscrição_ID` FOREIGN KEY (`InscriçãoID`) REFERENCES `inscrição` (`ID`);
ALTER TABLE `sessão-atividade-inscrição` ADD CONSTRAINT `sessão-atividade-ins_Sessão-AtividadeID_8ca56e2c_fk_sessão-at` FOREIGN KEY (`Sessão-AtividadeID`) REFERENCES `sessão-atividade` (`ID`);
ALTER TABLE `transporte_universitário-horario` ADD CONSTRAINT `transporte_universit_HorarioID_1d5e2743_fk_horario_I` FOREIGN KEY (`HorarioID`) REFERENCES `horario` (`ID`);
ALTER TABLE `transporte_universitário-horario` ADD CONSTRAINT `transporte_universit_TransporteID_ec16a80b_fk_transport` FOREIGN KEY (`TransporteID`) REFERENCES `transporte` (`ID`);
ALTER TABLE `unidade orgânica` ADD CONSTRAINT `unidade orgânica_CampusID_0b33fb49_fk_campus_ID` FOREIGN KEY (`CampusID`) REFERENCES `campus` (`ID`);
ALTER TABLE `utilizador` ADD CONSTRAINT `utilizador_DepartamentoID_e93cd451_fk_departamento_ID` FOREIGN KEY (`DepartamentoID`) REFERENCES `departamento` (`ID`);
ALTER TABLE `utilizador` ADD CONSTRAINT `utilizador_Gestão de PerfilID_574c6ec3_fk_gestão de perfil_ID` FOREIGN KEY (`Gestão de PerfilID`) REFERENCES `gestão de perfil` (`ID`);
ALTER TABLE `utilizador` ADD CONSTRAINT `utilizador_InscriçãoID_7222ba6a_fk_inscrição_ID` FOREIGN KEY (`InscriçãoID`) REFERENCES `inscrição` (`ID`);
ALTER TABLE `utilizador` ADD CONSTRAINT `utilizador_Registo HorárioID_7c5dcb56_fk_registo horário_ID` FOREIGN KEY (`Registo HorárioID`) REFERENCES `registo horário` (`ID`);
ALTER TABLE `utilizador` ADD CONSTRAINT `utilizador_Unidade OrgânicaID_5a824940_fk_unidade orgânica_ID` FOREIGN KEY (`Unidade OrgânicaID`) REFERENCES `unidade orgânica` (`ID`);
ALTER TABLE `tarefa` ADD CONSTRAINT `tarefa_Sessão-Atividade-Ins_af18d4b0_fk_sessão-at` FOREIGN KEY (`Sessão-Atividade-InscriçãoID_Destino`) REFERENCES `sessão-atividade-inscrição` (`ID`);
ALTER TABLE `tarefa` ADD CONSTRAINT `tarefa_Sessão-Atividade-Ins_fa2eee11_fk_sessão-at` FOREIGN KEY (`Sessão-Atividade-InscriçãoID_Origem`) REFERENCES `sessão-atividade-inscrição` (`ID`);
ALTER TABLE `tarefa` ADD CONSTRAINT `tarefa_UtilizadorID_c0ca7339_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `prato` ADD CONSTRAINT `prato_EmentaID_7fa808b2_fk_ementa_ID` FOREIGN KEY (`EmentaID`) REFERENCES `ementa` (`ID`);
ALTER TABLE `participanteinfo` ADD CONSTRAINT `participanteinfo_UtilizadorID_e096f880_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `notificações` ADD CONSTRAINT `notificações_UtilizadorID_Envia_c199e052_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID_Envia`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `notificações` ADD CONSTRAINT `notificações_UtilizadorID_Recebe_4068fe33_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID_Recebe`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `local` ADD CONSTRAINT `local_EdicifioID_463cf8bc_fk_edicifio_ID` FOREIGN KEY (`EdicifioID`) REFERENCES `edicifio` (`ID`);
ALTER TABLE `django_content_type` ADD CONSTRAINT `django_content_type_app_label_model_76bd3d3b_uniq` UNIQUE (`app_label`, `model`);
ALTER TABLE `django_admin_log` ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
ALTER TABLE `django_admin_log` ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `gottem_choice` ADD CONSTRAINT `gottem_choice_question_id_cdb21ee1_fk_gottem_question_id` FOREIGN KEY (`question_id`) REFERENCES `gottem_question` (`id`);
ALTER TABLE `auth_permission` ADD CONSTRAINT `auth_permission_content_type_id_codename_01ab375a_uniq` UNIQUE (`content_type_id`, `codename`);
ALTER TABLE `auth_permission` ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
ALTER TABLE `atividade-tematica` ADD CONSTRAINT `atividade-tematica_AtividadeID_33d85a44_fk_atividade_ID` FOREIGN KEY (`AtividadeID`) REFERENCES `atividade` (`ID`);
ALTER TABLE `atividade-tematica` ADD CONSTRAINT `atividade-tematica_TemáticaID_a78a399d_fk_temática_ID` FOREIGN KEY (`TemáticaID`) REFERENCES `temática` (`ID`);
ALTER TABLE `atividade-material` ADD CONSTRAINT `atividade-material_AtividadeID_d6887694_fk_atividade_ID` FOREIGN KEY (`AtividadeID`) REFERENCES `atividade` (`ID`);
ALTER TABLE `atividade-material` ADD CONSTRAINT `atividade-material_MaterialID_a23d5ea0_fk_material_ID` FOREIGN KEY (`MaterialID`) REFERENCES `material` (`ID`);
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` UNIQUE (`user_id`, `permission_id`);
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `auth_user_groups_user_id_group_id_94350c0c_uniq` UNIQUE (`user_id`, `group_id`);
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` UNIQUE (`group_id`, `permission_id`);
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
ALTER TABLE `utilizador_transporte` ADD CONSTRAINT `utilizador_transporte_UtilizadorID_TransporteID_f5cebc21_uniq` UNIQUE (`UtilizadorID`, `TransporteID`);
ALTER TABLE `utilizador_transporte` ADD CONSTRAINT `utilizador_transporte_UtilizadorID_9f99f602_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `utilizador_transporte` ADD CONSTRAINT `utilizador_transporte_TransporteID_0fabd1b5_fk_transporte_ID` FOREIGN KEY (`TransporteID`) REFERENCES `transporte` (`ID`);
ALTER TABLE `utilizador_tarefa` ADD CONSTRAINT `utilizador_tarefa_UtilizadorID_TarefaID_511cc7f9_uniq` UNIQUE (`UtilizadorID`, `TarefaID`);
ALTER TABLE `utilizador_tarefa` ADD CONSTRAINT `utilizador_tarefa_UtilizadorID_7401137c_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `utilizador_tarefa` ADD CONSTRAINT `utilizador_tarefa_TarefaID_dbcc038a_fk_tarefa_ID` FOREIGN KEY (`TarefaID`) REFERENCES `tarefa` (`ID`);
ALTER TABLE `utilizador_ementa` ADD CONSTRAINT `utilizador_ementa_UtilizadorID_EmentaID_79fa4095_uniq` UNIQUE (`UtilizadorID`, `EmentaID`);
ALTER TABLE `utilizador_ementa` ADD CONSTRAINT `utilizador_ementa_UtilizadorID_c4bf27b7_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `utilizador_ementa` ADD CONSTRAINT `utilizador_ementa_EmentaID_5a796716_fk_ementa_ID` FOREIGN KEY (`EmentaID`) REFERENCES `ementa` (`ID`);
ALTER TABLE `utilizador_atividade` ADD CONSTRAINT `utilizador_atividade_UtilizadorID_AtividadeID_d26265cf_uniq` UNIQUE (`UtilizadorID`, `AtividadeID`);
ALTER TABLE `utilizador_atividade` ADD CONSTRAINT `utilizador_atividade_UtilizadorID_51aa2fc2_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `utilizador_atividade` ADD CONSTRAINT `utilizador_atividade_AtividadeID_4ea2e483_fk_atividade_ID` FOREIGN KEY (`AtividadeID`) REFERENCES `atividade` (`ID`);
ALTER TABLE `transporte_universitário-horario_inscrição` ADD CONSTRAINT `transporte_universitário_Transporte_Universitário_3fd0bb82_uniq` UNIQUE (`Transporte_Universitário-HorarioID`, `InscriçãoID`);
ALTER TABLE `transporte_universitário-horario_inscrição` ADD CONSTRAINT `transporte_universit_Transporte_Universit_62d9e4e2_fk_transport` FOREIGN KEY (`Transporte_Universitário-HorarioID`) REFERENCES `transporte_universitário-horario` (`ID`);
ALTER TABLE `transporte_universitário-horario_inscrição` ADD CONSTRAINT `transporte_universit_InscriçãoID_f183db79_fk_inscrição` FOREIGN KEY (`InscriçãoID`) REFERENCES `inscrição` (`ID`);
ALTER TABLE `tarefa_sessão-atividade` ADD CONSTRAINT `tarefa_sessão-atividade_TarefaID_Sessão-Atividad_bd5ec375_uniq` UNIQUE (`TarefaID`, `Sessão-AtividadeID`);
ALTER TABLE `tarefa_sessão-atividade` ADD CONSTRAINT `tarefa_sessão-atividade_TarefaID_8534a94f_fk_tarefa_ID` FOREIGN KEY (`TarefaID`) REFERENCES `tarefa` (`ID`);
ALTER TABLE `tarefa_sessão-atividade` ADD CONSTRAINT `tarefa_sessão-ativid_Sessão-AtividadeID_f6a01183_fk_sessão-at` FOREIGN KEY (`Sessão-AtividadeID`) REFERENCES `sessão-atividade` (`ID`);
ALTER TABLE `inscrição_ementa` ADD CONSTRAINT `inscrição_ementa_InscriçãoID_EmentaID_c54f3d40_uniq` UNIQUE (`InscriçãoID`, `EmentaID`);
ALTER TABLE `inscrição_ementa` ADD CONSTRAINT `inscrição_ementa_InscriçãoID_689d2185_fk_inscrição_ID` FOREIGN KEY (`InscriçãoID`) REFERENCES `inscrição` (`ID`);
ALTER TABLE `inscrição_ementa` ADD CONSTRAINT `inscrição_ementa_EmentaID_03571980_fk_ementa_ID` FOREIGN KEY (`EmentaID`) REFERENCES `ementa` (`ID`);
ALTER TABLE `dia aberto_utilizador` ADD CONSTRAINT `dia aberto_utilizador_Dia AbertoID_UtilizadorID_e00e31da_uniq` UNIQUE (`Dia AbertoID`, `UtilizadorID`);
ALTER TABLE `dia aberto_utilizador` ADD CONSTRAINT `dia aberto_utilizador_Dia AbertoID_69fc9d11_fk_dia aberto_ID` FOREIGN KEY (`Dia AbertoID`) REFERENCES `dia aberto` (`ID`);
ALTER TABLE `dia aberto_utilizador` ADD CONSTRAINT `dia aberto_utilizador_UtilizadorID_3ae8dd71_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `atividade_departamento` ADD CONSTRAINT `atividade_departamento_AtividadeID_DepartamentoID_a04939e7_uniq` UNIQUE (`AtividadeID`, `DepartamentoID`);
ALTER TABLE `atividade_departamento` ADD CONSTRAINT `atividade_departamento_AtividadeID_12042665_fk_atividade_ID` FOREIGN KEY (`AtividadeID`) REFERENCES `atividade` (`ID`);
ALTER TABLE `atividade_departamento` ADD CONSTRAINT `atividade_departamen_DepartamentoID_3e36c38b_fk_departame` FOREIGN KEY (`DepartamentoID`) REFERENCES `departamento` (`ID`);