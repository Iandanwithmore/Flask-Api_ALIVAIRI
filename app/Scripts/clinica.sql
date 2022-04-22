CREATE TABLE Clinica.CIE10 (
   cCodCie     VARCHAR(8)   NOT NULL PRIMARY KEY,
   cDescri   VARCHAR(300)    NOT NULL,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.CIE10 IS 'Tabla codigos Cie10  https://www.diresatumbes.gob.pe/index.php/estadisticas-de-salud/cie-10-2013';
COMMENT ON COLUMN Clinica.CIE10.cCodCie IS 'Codigo';
COMMENT ON COLUMN Clinica.CIE10._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.CIE10.tModifi IS 'Fecha Modificacion';

CREATE TABLE Clinica.CMP (
   cCodCmp     VARCHAR(8)   NOT NULL PRIMARY KEY,
   cDescri   VARCHAR(20000)    NOT NULL,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.CMP IS 'Tabla codigos Codigos medicos procedimentuales rayos x';
COMMENT ON COLUMN Clinica.CMP.cCodCmp IS 'Codigo';
COMMENT ON COLUMN Clinica.CMP._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.CMP.tModifi IS 'Fecha Modificacion';

CREATE TABLE Clinica.Consenimiento (
   cCodigo   CHARACTER(1)   NOT NULL PRIMARY KEY,
   cDescri   VARCHAR(800)    NOT NULL,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.Consenimiento IS 'Tabla codigos Codigos medicos procedimentuales rayos x';
COMMENT ON COLUMN Clinica.Consenimiento.cCodigo IS 'Codigo';
COMMENT ON COLUMN Clinica.Consenimiento.cDescri IS 'Titulo Consentimiento';
COMMENT ON COLUMN Clinica.Consenimiento._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.Consenimiento.tModifi IS 'Fecha Modificacion';

CREATE TABLE Clinica.Examen(
   cCodExa   CHARACTER(6)    NOT NULL PRIMARY KEY,
   c_TipSer  CHARACTER(1)    NOT NULL,
   cDescri   VARCHAR(200)    NOT NULL,
   c_Certif     CHARACTER(1) DEFAULT 'N',
   cExtra      VARCHAR(900),
   c_Estado  CHARACTER(1)    NOT NULL,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
   ccodexa_asociado VARCHAR(100),
   c_Tipo CHARACTER(1) DEFAULT 'S'
);
COMMENT ON TABLE Clinica.Examen IS 'Tabla codigos Codigos medicos procedimentuales rayos x';
COMMENT ON COLUMN Clinica.Examen.cCodExa IS 'Codigo de examen en el tarifario';
COMMENT ON COLUMN Clinica.Examen.c_TipSer IS 'Referencia a la tabla tablas[]';
COMMENT ON COLUMN Clinica.Examen.cDescri IS 'Descripcion del examen';
COMMENT ON COLUMN Clinica.Examen.c_Certif IS 'Referencia a la tabla tablas[]';
COMMENT ON COLUMN Clinica.Examen.cExtra IS 'Comentarios en el imprimible';
COMMENT ON COLUMN Clinica.Examen.c_Estado IS 'Referencia a la tabla tablas[]';
COMMENT ON COLUMN Clinica.Examen._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.Examen.tModifi IS 'Fecha Modificacion';

CREATE TABLE Clinica.Perfil(
   cCodPer   CHARACTER(3)    NOT NULL PRIMARY KEY, 
   cDescri   VARCHAR(50)    NOT NULL,
   _cNroRuc  CHARACTER(11)   NOT NULL REFERENCES Empresa (cNroRuc) ON DELETE RESTRICT ON UPDATE CASCADE,
   c_Estado  CHARACTER(1)    NOT NULL,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.Perfil IS 'Maestro Perfil de una empresa';
COMMENT ON COLUMN Clinica.Perfil.cDescri IS 'Descripcion del campo'; 
COMMENT ON COLUMN Clinica.Perfil._cNroRuc IS 'Referencia a la tabla Empresa';
COMMENT ON COLUMN Clinica.Perfil.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Clinica.Perfil._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.Perfil.tModifi IS 'Fecha Modificacion';

CREATE TABLE Clinica.Perfil_Examen(
   nSerial   SERIAL          NOT NULL UNIQUE,
   _cCodPer  CHARACTER(3)    NOT NULL REFERENCES Clinica.Perfil (cCodPer) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodExa  CHARACTER(6)    NOT NULL REFERENCES Clinica.Examen (cCodExa) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.Perfil_Examen IS 'Puente Perfil examenes';
COMMENT ON COLUMN Clinica.Perfil_Examen._cCodPer IS 'Codigo Perfil'; 
COMMENT ON COLUMN Clinica.Perfil_Examen._cCodExa IS 'Codigo Examen';
COMMENT ON COLUMN Clinica.Perfil_Examen._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.Perfil_Examen.tModifi IS 'Fecha Modificacion';

CREATE TABLE Clinica.PlanActividad (
   cCodPla  CHARACTER(11)    NOT NULL PRIMARY KEY,
   c_TipPla  CHARACTER(1)    NOT NULL,
   _cVauche  CHARACTER(15),
   c_CodPue  CHARACTER(3)    NOT NULL DEFAULT '000',
   tGenera   TIMESTAMP       NOT NULL DEFAULT NOW(),
   tFinPla      TIMESTAMP,
   _cNroRuc  CHARACTER(11)   NOT NULL REFERENCES Empresa (cNroRuc) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCenDis  CHARACTER(2)    DEFAULT '00',
   c_TipEva  CHARACTER(1)     NOT NULL DEFAULT 'A',
   c_Estado  CHARACTER(1)    NOT NULL,
   _cUsuCre  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.PlanActividad IS 'Maestro Plan de Actividades, examenes por los que pasara una persona';
COMMENT ON COLUMN Clinica.PlanActividad.cCodPla IS 'Codigo del Plan el cual contiene las actividades realizadas';
COMMENT ON COLUMN Clinica.PlanActividad.c_TipPla IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Clinica.PlanActividad._cVauche IS 'Vaucher que genera el sistema de facturacion'; --??
COMMENT ON COLUMN Clinica.PlanActividad.c_CodPue IS 'Puesto al que postula';
COMMENT ON COLUMN Clinica.PlanActividad.tGenera IS 'Fecha Generacion';
COMMENT ON COLUMN Clinica.PlanActividad.tCita IS 'Fecha en la que el paciente pidio cita';
COMMENT ON COLUMN Clinica.PlanActividad.tFin IS 'Fecha fin de todas las actividades';
COMMENT ON COLUMN Clinica.PlanActividad._cNroRuc IS 'Referencia a la tabla Empresa Apoderado, empresa que puede ver los resultados de la historia clinica/ Plan Actividad';
COMMENT ON COLUMN Clinica.PlanActividad._cCenDis IS 'Centro de distribucion de la empresa';
COMMENT ON COLUMN Clinica.PlanActividad.c_TipEva IS 'Tipo de Evaluacion,Referencia a la tabla TablaTablas[]';
COMMENT ON COLUMN Clinica.PlanActividad.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Clinica.PlanActividad._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.PlanActividad.tModifi IS 'Fecha Modificacion';

CREATE TABLE Clinica.Actividad (
   cCodAct    CHARACTER(8)    NOT NULL PRIMARY KEY,
   c_TipSer  CHARACTER(1)     NOT NULL,
   tCitAct      DATE            NOT NULL DEFAULT NOW(),
   tAtenci    TIMESTAMP,
   tFinAct       TIMESTAMP,
   c_Aptitu    CHARACTER(1) DEFAULT 'X',
   _cNroDni  CHARACTER(8)    NOT NULL REFERENCES Persona (cNroDni) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodPla  CHARACTER(11)    NOT NULL REFERENCES Clinica.PlanActividad (cCodPla) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodPer  CHARACTER(3)     NOT NULL REFERENCES Clinica.Perfil (cCodPer) ON DELETE RESTRICT ON UPDATE CASCADE,
   c_Estado   CHARACTER(1)    NOT NULL,
   _cUsuCod   CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi    TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.Actividad IS 'Tabla de Actividad, detalle de actividad';
COMMENT ON COLUMN Clinica.Actividad.cCodAct IS 'Codigo de la actividad, codigo de atencion';
COMMENT ON COLUMN Clinica.Actividad.c_TipSer IS 'Referencia a la tabla tablas[]';
COMMENT ON COLUMN Clinica.Actividad.tCitAct IS 'Fecha de cita plan';
COMMENT ON COLUMN Clinica.Actividad.tAtecio IS 'Fecha de atencion del paciente';
COMMENT ON COLUMN Clinica.Actividad.tFinAct IS 'fin de la actividad';
COMMENT ON COLUMN Clinica.Actividad.c_certif IS 'Referencia a la tabla tablas[]';
COMMENT ON COLUMN Clinica.Actividad.c_Aptitu IS 'Referencia a la tabla tablas[]';
COMMENT ON COLUMN Clinica.Actividad._cNroDni IS 'Referencia a la tabla Persona';
COMMENT ON COLUMN Clinica.Actividad._cCodPla IS 'Referencia a la tabla Clinica.PlanActividad';
COMMENT ON COLUMN Clinica.Actividad.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Clinica.Actividad._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.Actividad.tModifi IS 'Fecha Modificacion';

CREATE TABLE Clinica.PlantillaActividad(
   nSerial   SERIAL          NOT NULL UNIQUE,
   _cCodAct  CHARACTER(8)    NOT NULL REFERENCES Clinica.Actividad (cCodAct) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodExa  CHARACTER(6)    NOT NULL REFERENCES Clinica.Examen (cCodExa) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.PlantillaActividad IS 'Extra en los examenes Observaciones, conclusiones, recomendaciones';
COMMENT ON COLUMN Clinica.PlantillaActividad._cCodAct IS 'Codigo Perfil'; 
COMMENT ON COLUMN Clinica.PlantillaActividad._cCodExa IS 'Funcion en la API encargada de imprimir';
COMMENT ON COLUMN Clinica.PlantillaActividad._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.PlantillaActividad.tModifi IS 'Fecha Modificacion';

CREATE TABLE Clinica.ExtraActividad(
   nSerial   SERIAL          NOT NULL UNIQUE,
   _cCodAct  CHARACTER(8)    NOT NULL REFERENCES Clinica.Actividad (cCodAct) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodPla  CHARACTER(11)    NOT NULL REFERENCES Clinica.PlanActividad (cCodPla) ON DELETE RESTRICT ON UPDATE CASCADE,
   cDescri  VARCHAR(1000)    NOT NULL,
   c_Tipo  CHARACTER(1)    NOT NULL,
   c_Estado  CHARACTER(1)    NOT NULL DEFAULT 'A',
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.ExtraActividad IS 'Extra en los examenes Observaciones, conclusiones, recomendaciones';
COMMENT ON COLUMN Clinica.ExtraActividad._cCodAct IS 'Codigo Actividad'; 
COMMENT ON COLUMN Clinica.ExtraActividad.cDescri IS 'Campo de texto sonRe la actividad';
COMMENT ON COLUMN Clinica.ExtraActividad.c_Tipo IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Clinica.ExtraActividad.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Clinica.ExtraActividad._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.ExtraActividad.tModifi IS 'Fecha Modificacion';


CREATE TABLE Clinica.AntecedentesActividad(
   nSerial   SERIAL          NOT NULL UNIQUE,
   _cCodAct  CHARACTER(8)    NOT NULL REFERENCES Clinica.Actividad (cCodAct) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodPla  CHARACTER(11)    NOT NULL REFERENCES Clinica.PlanActividad (cCodPla) ON DELETE RESTRICT ON UPDATE CASCADE,
   tIniAct   DATE   NOT NULL,
   tFinAct   DATE   NOT NULL,
   cDescri   VARCHAR(200) NOT NULL,
   cDesAct   VARCHAR(200) NOT NULL,
   nHorTra   SMALLINT NOT NULL,
   cDesAre   VARCHAR(50) NOT NULL,
   cDesPue   VARCHAR(50) NOT NULL,
   cCauRet   VARCHAR(50) NOT NULL,
   nSUBSUE   INTEGER   NOT NULL,
   nSUPERF   INTEGER   NOT NULL,
   nRRuido   SMALLINT NOT NULL,
   nRPolvo   SMALLINT NOT NULL,
   nRErgon   SMALLINT NOT NULL,
   nRVinRa   SMALLINT NOT NULL,
   nRElect   SMALLINT NOT NULL,
   nRQuimi   SMALLINT NOT NULL,
   nROtros   SMALLINT NOT NULL,
   c_Estado  CHARACTER(1)    NOT NULL DEFAULT 'A',
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.AntecedentesActividad IS 'Extra en los examenes Observaciones, conclusiones, recomendaciones';
COMMENT ON COLUMN Clinica.AntecedentesActividad._cCodAct IS 'Codigo Actividad'; 
COMMENT ON COLUMN Clinica.AntecedentesActividad.cDescri IS 'Campo de texto sonRe la actividad';
COMMENT ON COLUMN Clinica.AntecedentesActividad.c_Tipo IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Clinica.AntecedentesActividad.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Clinica.AntecedentesActividad._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.AntecedentesActividad.tModifi IS 'Fecha Modificacion';

-- CREATE TABLE Clinica.CMPActividad (
--     nSerial    SERIAL          NOT NULL UNIQUE,
--    _cCodCmp     VARCHAR(8)   NOT NULL REFERENCES Clinica.CMP (cCodCmp) ON DELETE RESTRICT ON UPDATE CASCADE,
--    _cCodAct   CHARACTER(8)   NOT NULL REFERENCES Clinica.Actividad (cCodAct) ON DELETE RESTRICT ON UPDATE CASCADE,
--    _cCodPla   CHARACTER(11)   NOT NULL REFERENCES Clinica.PlanActividad (cCodPla) ON DELETE RESTRICT ON UPDATE CASCADE,
--    _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
--    tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
-- );
-- COMMENT ON TABLE Clinica.CMPActividad IS 'Puente actividades CMP';
-- COMMENT ON COLUMN Clinica.CMPActividad._cCodCmp IS 'Codigo CMP'; 
-- COMMENT ON COLUMN Clinica.CMPActividad._cCodAct IS 'Referencia a la actividad';
-- COMMENT ON COLUMN Clinica.CMPActividad._cCodPla IS 'Referencia al Plan de la actividad'; --??
-- COMMENT ON COLUMN Clinica.CMPActividad._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
-- COMMENT ON COLUMN Clinica.CMPActividad.tModifi IS 'Fecha Modificacion';

CREATE TABLE Clinica.Cie10Actividad (
    nSerial    SERIAL          NOT NULL UNIQUE,
   _cCodCie     VARCHAR(8)   NOT NULL REFERENCES Clinica.Cie10 (cCodCie) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodAct   CHARACTER(8)   NOT NULL REFERENCES Clinica.Actividad (cCodAct) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodPla   CHARACTER(11)   NOT NULL REFERENCES Clinica.PlanActividad (cCodPla) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.Cie10Actividad IS 'Puente actividades Cie10';
COMMENT ON COLUMN Clinica.Cie10Actividad._cCodCie IS 'Codigo Cie10'; 
COMMENT ON COLUMN Clinica.Cie10Actividad._cCodAct IS 'Referencia a la actividad';
COMMENT ON COLUMN Clinica.Cie10Actividad._cCodPla IS 'Referencia al Plan de la actividad'; --??
COMMENT ON COLUMN Clinica.Cie10Actividad._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.Cie10Actividad.tModifi IS 'Fecha Modificacion';

CREATE TABLE Clinica.Indicador (
   cCodInd   CHARACTER(4)    NOT NULL PRIMARY KEY,
   c_TipReg  CHARACTER(1)    NOT NULL, 
   cDescri   VARCHAR(300)    NOT NULL,
   cImprim   VARCHAR(300)    NOT NULL,
   cValPre   VARCHAR(1)   NOT NULL DEFAULT '0',
   cRango    VARCHAR(900),
   _cCodUni  CHARACTER(2)    NOT NULL REFERENCES Clinica.Unidad (cCodUni) ON DELETE RESTRICT ON UPDATE CASCADE,
   c_Estado  CHARACTER(1)    NOT NULL,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tGenera   TIMESTAMP       NOT NULL DEFAULT NOW(),
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW(),
   cValPre CHARACTER(1) DEFAULT '0'
);
COMMENT ON TABLE Clinica.Indicador IS 'Maestro Indicador, dato dentro de la filaXcolumna e un examen';
COMMENT ON COLUMN Clinica.Indicador.cCodInd IS 'Codgio Indicador del examen';
COMMENT ON COLUMN Clinica.Indicador.c_TipReg IS 'HTML ,Referencia a la tabla TablaTablas[]';
COMMENT ON COLUMN Clinica.Indicador.cDescri IS 'Descripcion con detalle';
COMMENT ON COLUMN Clinica.Indicador.cImprim IS 'Descripcion que se muestra en el HTML y PDF';
COMMENT ON COLUMN Clinica.Indicador.cValPre IS 'Valor predeterminado';
COMMENT ON COLUMN Clinica.Indicador.cRango IS 'Referencial, Rango aceptable';
COMMENT ON COLUMN Clinica.Indicador._cCodUni IS 'Referencia a la tabla Clinica.Unidad';
COMMENT ON COLUMN Clinica.Indicador.c_Estado IS 'Referencia a la tabla Clinica.TablaTablas[]'; --??
COMMENT ON COLUMN Clinica.Indicador._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.Indicador.tGenera IS 'Fecha de Generacion'; 
COMMENT ON COLUMN Clinica.Indicador.tModifi IS 'Fecha Modificacion'; 

CREATE TABLE Clinica.DetalleActividad (
   nSerial    SERIAL          NOT NULL UNIQUE,
   _cCodInd   CHARACTER(4)    NOT NULL ,
   n_Opcion   SMALLINT        NOT NULL DEFAULT 0,
   cResult    VARCHAR(800)    NOT NULL,
   _cCodPla   CHARACTER(11)   NOT NULL REFERENCES Clinica.PlanActividad (cCodPla) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodAct   CHARACTER(8)   NOT NULL REFERENCES Clinica.Actividad (cCodAct) ON DELETE RESTRICT ON UPDATE CASCADE,
   nOrden SMALLINT DEFAULT '0',
   c_Estado   CHARACTER(1)    NOT NULL,
   _cUsuCod   CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi    TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.DetalleActividad IS 'Donde se guardan los indicadores con sus resultados';
COMMENT ON COLUMN Clinica.DetalleActividad._cCodInd IS 'Referencia a la tabla de indicadores';
COMMENT ON COLUMN Clinica.DetalleActividad.n_Opcion IS 'Seleccion  segun tablatablas de opciones del servicio';
COMMENT ON COLUMN Clinica.DetalleActividad.cResult IS 'Resultado en campo texto';
COMMENT ON COLUMN Clinica.DetalleActividad._cCodPla IS 'Refencia a la tabla codigo del plan';
COMMENT ON COLUMN Clinica.DetalleActividad.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Clinica.DetalleActividad._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.DetalleActividad.tModifi IS 'Fecha Modificacion';

????????REFERENCES Clinica.Indicador (cCodInd) ON DELETE RESTRICT ON UPDATE CASCADE


CREATE TABLE  Clinica.TablaTablas(
   nSerial SERIAL         NOT NULL UNIQUE,
   _cCodInd  CHARACTER(4)    NOT NULL REFERENCES Clinica.Indicador (cCodInd) ON DELETE RESTRICT ON UPDATE CASCADE,
   nOrden  SMALLINT       NOT NULL,
   cDescri VARCHAR(100)   NOT NULL,
   c_Estado  CHARACTER(1)    NOT NULL,
   _cUsuCod CHARACTER(4)  NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tGenera TIMESTAMP      NOT NULL DEFAULT NOW(),
   tModifi TIMESTAMP      NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.TablaTablas IS 'Tabla donde se guardan las opciones de los select, estados, descripciones generales';
COMMENT ON COLUMN Clinica.TablaTablas._cCodInd IS 'Referencia a la tabla indicadores';
COMMENT ON COLUMN Clinica.TablaTablas.nOrden IS 'Orden en que se muestra , la seleccion tambien es guradada en el detalle';
COMMENT ON COLUMN Clinica.TablaTablas.cDescri IS 'Descripcion';
COMMENT ON COLUMN Clinica.TablaTablas.c_Estado IS 'Referencia a la tabla Clinica.TablaTablas[]'; --??
COMMENT ON COLUMN Clinica.TablaTablas._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.TablaTablas.tGenera IS 'Fecha de Generacion'; 
COMMENT ON COLUMN Clinica.TablaTablas.tModifi IS 'Fecha Modificacion'; 


CREATE TABLE Clinica.DetallePlantilla(
   nSerial    SERIAL         NOT NULL UNIQUE,
   cLisEnl   VARCHAR(6)      NOT NULL,
   _cCodInd  CHARACTER(4)    NOT NULL REFERENCES Clinica.Indicador (cCodInd) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodExa  CHARACTER(6)    NOT NULL REFERENCES Clinica.Examen (cCodExa) ON DELETE RESTRICT ON UPDATE CASCADE,
   c_Estado  CHARACTER(1)    NOT NULL,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.DetallePlantilla IS 'Plantillas en donde se encuentran los grupos de los indicadores';
COMMENT ON COLUMN Clinica.DetallePlantilla._cCodInd IS 'Referencia a la tabla.Indicador';
COMMENT ON COLUMN Clinica.DetallePlantilla._cCodExa IS 'Referencia a la tabla.Examen';
COMMENT ON COLUMN Clinica.DetallePlantilla.cLisEnl IS 'Lista  enlazada que crea grupos en los indicadores';
COMMENT ON COLUMN Clinica.DetallePlantilla._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.DetallePlantilla.tModifi IS 'Fecha Modificacion';

CREATE TABLE Clinica.Subtitulos(
   nSerial    SERIAL         NOT NULL UNIQUE,
   cLisEnl   VARCHAR(6)      NOT NULL,
   cDescri VARCHAR(200)    NOT NULL,
   _cCodExa  CHARACTER(6)    NOT NULL REFERENCES Clinica.Examen (cCodExa) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Clinica.Subtitulos IS 'Subtitulos presentes en las plantillas';
COMMENT ON COLUMN Clinica.Subtitulos.cDescri IS 'Titulo';
COMMENT ON COLUMN Clinica.Subtitulos._cCodExa IS 'Referencia a la tabla.Examen';
COMMENT ON COLUMN Clinica.Subtitulos.cLisEnl IS 'Lista  enlazada que crea grupos en los indicadores';
COMMENT ON COLUMN Clinica.Subtitulos._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Clinica.Subtitulos.tModifi IS 'Fecha Modificacion';

--DROP VIEW v_actividad_1
CREATE OR REPLACE VIEW V_ACTIVIDAD_1
 AS
	SELECT 
		A._cCodExa AS cCodExa, A.cCodAct, TO_CHAR(A.tCita,'YYYY-MM-DD') AS tActCit, TO_CHAR(COALESCE(A.tAtenci, NOW()),'YYYY-MM-DD') AS tActAte,  TO_CHAR(COALESCE(A.tFin, NOW()),'YYYY-MM-DD') AS tActFin, A._cCodPla AS cCodPla, A._cUsuFir AS cUsuFir, A._cUsuCod AS cUsuCod,
		A.c_TipSer, B.cDescri AS cDesSer,
		C.cDesDoc, C.cNroDni, C.cNroDoc, C.cNomnRe, TO_CHAR(C.tNacimi,'YYYY-MM-DD') AS tNacimi, C.nEdad, C.cDesSex,
		E.cDescri AS cDesTip, F.cDescri AS cDesPue, 
		G.cNroRuc, G.cDescri AS cDesEmp, COALESCE(K.cDescri, '-') AS cDesSed,
		A.c_Aptitu, I.cDescri AS cDesApt,
		A.c_Estado, J.cDescri AS cDesEst,
		H.cDescri AS cDesPer,
		D.c_TipPla, TO_CHAR(COALESCE(D.tCita, NOW()),'YYYY-MM-DD') AS tPlaIni, TO_CHAR(COALESCE(D.tFin, NOW()),'YYYY-MM-DD') AS tPlaFin, D._cVauche AS cVauche
	FROM Clinica.Actividad A
	LEFT OUTER JOIN V_TABLATABLAS_1 B ON B.cCodTab = '014' AND TRIM(B.cCodigo) = A.c_TipSer
	INNER JOIN V_PERSONA_1 C ON C.cNroDni = A._cNroDni
	INNER JOIN Clinica.PlanActividad D ON D.cCodPla = A._cCodPla
	LEFT OUTER JOIN V_TABLATABLAS_1 E ON E.cCodTab = '007' AND TRIM(E.cCodigo) = D.c_TipPla
	LEFT OUTER JOIN V_TABLATABLAS_1 F ON F.cCodTab = '013' AND TRIM(F.cCodigo) = D.c_CodPue
	INNER JOIN Empresa G ON G.cNroRuc = D._cNroRuc
	INNER JOIN Clinica.Perfil H ON H.cCodPer = A._cCodPer
	LEFT OUTER JOIN V_TABLATABLAS_1 I ON I.cCodTab = '010' AND TRIM(I.cCodigo) = A.c_Aptitu
	LEFT OUTER JOIN V_TABLATABLAS_1 J ON J.cCodTab = '011' AND TRIM(J.cCodigo) = A.c_Estado
	LEFT OUTER JOIN Empresa_centrodistribucion K ON K.cCenDis = D._cCenDis AND K._cNroRuc = D._cNroRuc


