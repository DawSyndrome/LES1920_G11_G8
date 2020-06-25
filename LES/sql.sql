--
-- Create model Atividade
--
CREATE TABLE `atividade` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL, `Descri��o` varchar(255) NULL, `Dura��o` integer NULL, `Limite_de_participantes` integer NULL, `Validada` integer NULL, `Tipo_atividade` varchar(255) NULL, `Public_alvo` varchar(255) NULL);
--
-- Create model Campus
--
CREATE TABLE `campus` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL, `Localiza��o` varchar(255) NULL, `Contacto` integer NULL);
--
-- Create model Departamento
--
CREATE TABLE `departamento` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL);
--
-- Create model DiaAberto
--
CREATE TABLE `dia aberto` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Titulo` varchar(255) NULL, `Descri��o` varchar(255) NULL, `Email` varchar(255) NULL, `Contacto` integer NULL, `Data_inicio` date NULL, `Data_fim` date NULL, `Limite_de_inscri��o_atividades` date NULL, `Limite_de_inscri��o_participantes` date NULL);
--
-- Create model Edicifio
--
CREATE TABLE `edicifio` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Numero edificio` integer NULL);
--
-- Create model Ementa
--
CREATE TABLE `ementa` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Dia` date NULL, `Pre�o_economico_aluno` double precision NULL, `Pre�o_normal_aluno` double precision NULL, `Pre�o_economico_outro` double precision NULL, `Pre�o_outro` double precision NULL);
--
-- Create model Escola
--
CREATE TABLE `escola` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL, `Morada` varchar(255) NULL, `Zip` integer NULL, `Contacto` integer NULL, `Localidade` varchar(255) NULL);
--
-- Create model GestoDePerfil
--
CREATE TABLE `gest�o de perfil` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Valida��o` integer NULL);
--
-- Create model Horario
--
CREATE TABLE `horario` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Hora_de_partida` time(6) NULL, `Data` date NULL);
--
-- Create model Inscrio
--
CREATE TABLE `inscri��o` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Dia` date NULL, `EscolaID` integer NULL);
--
-- Create model Material
--
CREATE TABLE `material` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL);
--
-- Create model RegistoHorrio
--
CREATE TABLE `registo hor�rio` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Hora_inicio` time(6) NULL, `Hora_fim` time(6) NULL, `Data` date NULL);
--
-- Create model Sesso
--
CREATE TABLE `sess�o` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Hora_de inicio` time(6) NULL);
--
-- Create model SessoAtividade
--
CREATE TABLE `sess�o-atividade` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Data` date NULL, `AtividadeID` integer NOT NULL, `Sess�oID` integer NOT NULL);
--
-- Create model SessoAtividadeInscrio
--
CREATE TABLE `sess�o-atividade-inscri��o` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Num_alunos` integer NULL, `Inscri��oID` integer NOT NULL, `Sess�o-AtividadeID` integer NOT NULL);
--
-- Create model Temtica
--
CREATE TABLE `tem�tica` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL);
--
-- Create model Transporte
--
CREATE TABLE `transporte` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Hora_de_chegada` date NULL, `Hora_de_partida` date NULL, `Tipo_de_transporte` varchar(255) NULL, `Capacidade` integer NULL);
--
-- Create model TransporteUniversitrioHorario
--
CREATE TABLE `transporte_universit�rio-horario` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Origem` varchar(255) NULL, `Destino` varchar(255) NULL, `Data` date NULL, `HorarioID` integer NOT NULL, `TransporteID` integer NOT NULL);
--
-- Create model UnidadeOrgnica
--
CREATE TABLE `unidade org�nica` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL, `CampusID` integer NOT NULL);
--
-- Create model Utilizador
--
CREATE TABLE `utilizador` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Email` varchar(255) NULL, `Nome` varchar(255) NULL, `Data_de_nascimento` date NULL, `Numero_telemovel` integer NULL, `Cart�o_cidad�o` integer NULL, `Deficiencias` varchar(255) NULL, `Permitir_localiza��o` integer NULL, `Utilizar_dados_pessoais` integer NULL, `Tema_do_website` integer NULL, `User_type` integer NOT NULL, `Daltonico` integer NULL, `Validado` integer NOT NULL, `Check_in_state` integer NOT NULL, `DepartamentoID` integer NULL, `Gest�o de PerfilID` integer NOT NULL, `Inscri��oID` integer NOT NULL, `Registo Hor�rioID` integer NOT NULL, `Unidade Org�nicaID` integer NULL);
--
-- Create model Tarefa
--
CREATE TABLE `tarefa` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Descri��o` varchar(255) NULL, `Localiza��o do grupo` varchar(255) NULL, `Destino` varchar(255) NULL, `Hor�rio` time(6) NULL, `TarefaTransporte` integer NULL, `Sess�o-Atividade-Inscri��oID_Destino` integer NULL, `Sess�o-Atividade-Inscri��oID_Origem` integer NOT NULL, `UtilizadorID` integer NOT NULL);
--
-- Create model Prato
--
CREATE TABLE `prato` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Nome` varchar(255) NULL, `Tipo` varchar(255) NULL, `Descri�ao` varchar(255) NULL, `EmentaID` integer NOT NULL);
--
-- Create model Participanteinfo
--
CREATE TABLE `participanteinfo` (`ParticipanteInfoID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Ano escolar` integer NOT NULL, `Area` varchar(255) NULL, `Checkin_state` integer NOT NULL, `Participante_type` integer NULL, `Total_de_participantes` integer NULL, `Total_de_professores` integer NULL, `Turma` varchar(255) NULL, `Autoriza��o` integer NULL, `Ficheiro_autoriza��o` varchar(255) NULL, `Acompanhates` integer NULL, `TipoParticipante` varchar(255) NULL, `UtilizadorID` integer NOT NULL);
--
-- Create model Notificaes
--
CREATE TABLE `notifica��es` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Conteudo` varchar(255) NULL, `Hora_envio` time(6) NULL, `Data` date NULL, `Prioridade` integer NULL, `Assunto` varchar(255) NULL, `UtilizadorID_Envia` integer NOT NULL, `UtilizadorID_Recebe` integer NOT NULL);
--
-- Create model Local
--
CREATE TABLE `local` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Andar` integer NULL, `Sala` integer NULL, `Descri�ao` varchar(255) NULL, `Indoor` integer NULL, `EdicifioID` integer NOT NULL);
--
-- Add field unidade_org�nicaid to departamento
--
ALTER TABLE `departamento` ADD COLUMN `Unidade Org�nicaID` integer NOT NULL , ADD CONSTRAINT `departamento_Unidade Org�nicaID_eac1b380_fk_unidade org�nica_ID` FOREIGN KEY (`Unidade Org�nicaID`) REFERENCES `unidade org�nica`(`ID`);
--
-- Create model AtividadeTematica
--
CREATE TABLE `atividade-tematica` (`ID` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `AtividadeID` integer NOT NULL, `Tem�ticaID` integer NOT NULL);
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
ALTER TABLE `atividade` ADD COLUMN `UnidadeOrganicaID` integer NOT NULL , ADD CONSTRAINT `atividade_UnidadeOrganicaID_4614a1d3_fk_unidade org�nica_ID` FOREIGN KEY (`UnidadeOrganicaID`) REFERENCES `unidade org�nica`(`ID`);
--
-- Add field utilizadorid to atividade
--
ALTER TABLE `atividade` ADD COLUMN `UtilizadorID` integer NOT NULL , ADD CONSTRAINT `atividade_UtilizadorID_007a36c0_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador`(`ID`);
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
CREATE TABLE `transporte_universit�rio-horario_inscri��o` (`Transporte_Universit�rio-HorarioID` integer NOT NULL PRIMARY KEY, `Inscri��oID` integer NOT NULL);
--
-- Create model TarefaSessoAtividade
--
CREATE TABLE `tarefa_sess�o-atividade` (`TarefaID` integer NOT NULL PRIMARY KEY, `Sess�o-AtividadeID` integer NOT NULL);
--
-- Create model InscrioEmenta
--
CREATE TABLE `inscri��o_ementa` (`Inscri��oID` integer NOT NULL PRIMARY KEY, `EmentaID` integer NOT NULL);
--
-- Create model DiaAbertoUtilizador
--
CREATE TABLE `dia aberto_utilizador` (`Dia AbertoID` integer NOT NULL PRIMARY KEY, `UtilizadorID` integer NOT NULL);
--
-- Create model AtividadeDepartamento
--
CREATE TABLE `atividade_departamento` (`AtividadeID` integer NOT NULL PRIMARY KEY, `DepartamentoID` integer NOT NULL);
ALTER TABLE `inscri��o` ADD CONSTRAINT `inscri��o_EscolaID_e66e82f0_fk_escola_ID` FOREIGN KEY (`EscolaID`) REFERENCES `escola` (`ID`);
ALTER TABLE `sess�o-atividade` ADD CONSTRAINT `sess�o-atividade_AtividadeID_f32ff99c_fk_atividade_ID` FOREIGN KEY (`AtividadeID`) REFERENCES `atividade` (`ID`);
ALTER TABLE `sess�o-atividade` ADD CONSTRAINT `sess�o-atividade_Sess�oID_f055d000_fk_sess�o_ID` FOREIGN KEY (`Sess�oID`) REFERENCES `sess�o` (`ID`);
ALTER TABLE `sess�o-atividade-inscri��o` ADD CONSTRAINT `sess�o-atividade-inscri��o_Inscri��oID_2810ac0d_fk_inscri��o_ID` FOREIGN KEY (`Inscri��oID`) REFERENCES `inscri��o` (`ID`);
ALTER TABLE `sess�o-atividade-inscri��o` ADD CONSTRAINT `sess�o-atividade-ins_Sess�o-AtividadeID_8ca56e2c_fk_sess�o-at` FOREIGN KEY (`Sess�o-AtividadeID`) REFERENCES `sess�o-atividade` (`ID`);
ALTER TABLE `transporte_universit�rio-horario` ADD CONSTRAINT `transporte_universit_HorarioID_1d5e2743_fk_horario_I` FOREIGN KEY (`HorarioID`) REFERENCES `horario` (`ID`);
ALTER TABLE `transporte_universit�rio-horario` ADD CONSTRAINT `transporte_universit_TransporteID_ec16a80b_fk_transport` FOREIGN KEY (`TransporteID`) REFERENCES `transporte` (`ID`);
ALTER TABLE `unidade org�nica` ADD CONSTRAINT `unidade org�nica_CampusID_0b33fb49_fk_campus_ID` FOREIGN KEY (`CampusID`) REFERENCES `campus` (`ID`);
ALTER TABLE `utilizador` ADD CONSTRAINT `utilizador_DepartamentoID_e93cd451_fk_departamento_ID` FOREIGN KEY (`DepartamentoID`) REFERENCES `departamento` (`ID`);
ALTER TABLE `utilizador` ADD CONSTRAINT `utilizador_Gest�o de PerfilID_574c6ec3_fk_gest�o de perfil_ID` FOREIGN KEY (`Gest�o de PerfilID`) REFERENCES `gest�o de perfil` (`ID`);
ALTER TABLE `utilizador` ADD CONSTRAINT `utilizador_Inscri��oID_7222ba6a_fk_inscri��o_ID` FOREIGN KEY (`Inscri��oID`) REFERENCES `inscri��o` (`ID`);
ALTER TABLE `utilizador` ADD CONSTRAINT `utilizador_Registo Hor�rioID_7c5dcb56_fk_registo hor�rio_ID` FOREIGN KEY (`Registo Hor�rioID`) REFERENCES `registo hor�rio` (`ID`);
ALTER TABLE `utilizador` ADD CONSTRAINT `utilizador_Unidade Org�nicaID_5a824940_fk_unidade org�nica_ID` FOREIGN KEY (`Unidade Org�nicaID`) REFERENCES `unidade org�nica` (`ID`);
ALTER TABLE `tarefa` ADD CONSTRAINT `tarefa_Sess�o-Atividade-Ins_af18d4b0_fk_sess�o-at` FOREIGN KEY (`Sess�o-Atividade-Inscri��oID_Destino`) REFERENCES `sess�o-atividade-inscri��o` (`ID`);
ALTER TABLE `tarefa` ADD CONSTRAINT `tarefa_Sess�o-Atividade-Ins_fa2eee11_fk_sess�o-at` FOREIGN KEY (`Sess�o-Atividade-Inscri��oID_Origem`) REFERENCES `sess�o-atividade-inscri��o` (`ID`);
ALTER TABLE `tarefa` ADD CONSTRAINT `tarefa_UtilizadorID_c0ca7339_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `prato` ADD CONSTRAINT `prato_EmentaID_7fa808b2_fk_ementa_ID` FOREIGN KEY (`EmentaID`) REFERENCES `ementa` (`ID`);
ALTER TABLE `participanteinfo` ADD CONSTRAINT `participanteinfo_UtilizadorID_e096f880_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `notifica��es` ADD CONSTRAINT `notifica��es_UtilizadorID_Envia_c199e052_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID_Envia`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `notifica��es` ADD CONSTRAINT `notifica��es_UtilizadorID_Recebe_4068fe33_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID_Recebe`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `local` ADD CONSTRAINT `local_EdicifioID_463cf8bc_fk_edicifio_ID` FOREIGN KEY (`EdicifioID`) REFERENCES `edicifio` (`ID`);
ALTER TABLE `atividade-tematica` ADD CONSTRAINT `atividade-tematica_AtividadeID_33d85a44_fk_atividade_ID` FOREIGN KEY (`AtividadeID`) REFERENCES `atividade` (`ID`);
ALTER TABLE `atividade-tematica` ADD CONSTRAINT `atividade-tematica_Tem�ticaID_a78a399d_fk_tem�tica_ID` FOREIGN KEY (`Tem�ticaID`) REFERENCES `tem�tica` (`ID`);
ALTER TABLE `atividade-material` ADD CONSTRAINT `atividade-material_AtividadeID_d6887694_fk_atividade_ID` FOREIGN KEY (`AtividadeID`) REFERENCES `atividade` (`ID`);
ALTER TABLE `atividade-material` ADD CONSTRAINT `atividade-material_MaterialID_a23d5ea0_fk_material_ID` FOREIGN KEY (`MaterialID`) REFERENCES `material` (`ID`);
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
ALTER TABLE `transporte_universit�rio-horario_inscri��o` ADD CONSTRAINT `transporte_universit�rio_Transporte_Universit�rio_3fd0bb82_uniq` UNIQUE (`Transporte_Universit�rio-HorarioID`, `Inscri��oID`);
ALTER TABLE `transporte_universit�rio-horario_inscri��o` ADD CONSTRAINT `transporte_universit_Transporte_Universit_62d9e4e2_fk_transport` FOREIGN KEY (`Transporte_Universit�rio-HorarioID`) REFERENCES `transporte_universit�rio-horario` (`ID`);
ALTER TABLE `transporte_universit�rio-horario_inscri��o` ADD CONSTRAINT `transporte_universit_Inscri��oID_f183db79_fk_inscri��o` FOREIGN KEY (`Inscri��oID`) REFERENCES `inscri��o` (`ID`);
ALTER TABLE `tarefa_sess�o-atividade` ADD CONSTRAINT `tarefa_sess�o-atividade_TarefaID_Sess�o-Atividad_bd5ec375_uniq` UNIQUE (`TarefaID`, `Sess�o-AtividadeID`);
ALTER TABLE `tarefa_sess�o-atividade` ADD CONSTRAINT `tarefa_sess�o-atividade_TarefaID_8534a94f_fk_tarefa_ID` FOREIGN KEY (`TarefaID`) REFERENCES `tarefa` (`ID`);
ALTER TABLE `tarefa_sess�o-atividade` ADD CONSTRAINT `tarefa_sess�o-ativid_Sess�o-AtividadeID_f6a01183_fk_sess�o-at` FOREIGN KEY (`Sess�o-AtividadeID`) REFERENCES `sess�o-atividade` (`ID`);
ALTER TABLE `inscri��o_ementa` ADD CONSTRAINT `inscri��o_ementa_Inscri��oID_EmentaID_c54f3d40_uniq` UNIQUE (`Inscri��oID`, `EmentaID`);
ALTER TABLE `inscri��o_ementa` ADD CONSTRAINT `inscri��o_ementa_Inscri��oID_689d2185_fk_inscri��o_ID` FOREIGN KEY (`Inscri��oID`) REFERENCES `inscri��o` (`ID`);
ALTER TABLE `inscri��o_ementa` ADD CONSTRAINT `inscri��o_ementa_EmentaID_03571980_fk_ementa_ID` FOREIGN KEY (`EmentaID`) REFERENCES `ementa` (`ID`);
ALTER TABLE `dia aberto_utilizador` ADD CONSTRAINT `dia aberto_utilizador_Dia AbertoID_UtilizadorID_e00e31da_uniq` UNIQUE (`Dia AbertoID`, `UtilizadorID`);
ALTER TABLE `dia aberto_utilizador` ADD CONSTRAINT `dia aberto_utilizador_Dia AbertoID_69fc9d11_fk_dia aberto_ID` FOREIGN KEY (`Dia AbertoID`) REFERENCES `dia aberto` (`ID`);
ALTER TABLE `dia aberto_utilizador` ADD CONSTRAINT `dia aberto_utilizador_UtilizadorID_3ae8dd71_fk_utilizador_ID` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`ID`);
ALTER TABLE `atividade_departamento` ADD CONSTRAINT `atividade_departamento_AtividadeID_DepartamentoID_a04939e7_uniq` UNIQUE (`AtividadeID`, `DepartamentoID`);
ALTER TABLE `atividade_departamento` ADD CONSTRAINT `atividade_departamento_AtividadeID_12042665_fk_atividade_ID` FOREIGN KEY (`AtividadeID`) REFERENCES `atividade` (`ID`);
ALTER TABLE `atividade_departamento` ADD CONSTRAINT `atividade_departamen_DepartamentoID_3e36c38b_fk_departame` FOREIGN KEY (`DepartamentoID`) REFERENCES `departamento` (`ID`);
