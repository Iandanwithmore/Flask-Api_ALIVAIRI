create extension pgcrypto;
CREATE SCHEMA Clinica;
COMMENT ON SCHEMA Clinica IS 'Modulo Clinica';
-- Persona
CREATE TABLE Persona (
   cNroDni  CHARACTER(8)    NOT NULL PRIMARY KEY,
   c_TipDoc CHARACTER(1)    NOT NULL,
   cNroDoc  VARCHAR(15)     NOT NULL,
   cNombre  VARCHAR(200)    NOT NULL,
   c_Genero   CHARACTER(1)    NOT NULL,
   tNacimi  DATE    	       NOT NULL DEFAULT '2020-01-01',
   _cCodDis  CHARACTER(6)   DEFAULT '040101',
   cDirecc  VARCHAR(300),
   cCorreo   VARCHAR(300),
   cNroCel  VARCHAR(24),
   cClave   CHARACTER(128)  NOT NULL,
   c_Estado CHARACTER(1)    NOT NULL DEFAULT 'A',   -- [000]
   _cUsuCod  CHARACTER(4),
   tGenera  TIMESTAMP       NOT NULL DEFAULT NOW(),
   tModifi  TIMESTAMP       NOT NULL DEFAULT NOW(),
   c_TipSeg CHARACTER(1)    DEFAULT 'N'
);
COMMENT ON TABLE Persona IS 'Maestro de Personas, alberga datos escenciales persona';
COMMENT ON COLUMN Persona.cNroDni IS 'Numero de documento unico de la persona, en caso de otros documentos se antepone el tipo y los ultimos 7 digitos de su documento';
COMMENT ON COLUMN Persona.c_TipDoc IS 'Codigo de Tipo de Documento asociado a TablaTablas[]'; --??
COMMENT ON COLUMN Persona.cNroDoc IS 'Numero de Documento';
COMMENT ON COLUMN Persona.cNombre IS 'Nombre de la persona formato APELLIDO PATERNO/APELLIDO MATERNO/NOMBRES';
COMMENT ON COLUMN Persona.c_TipSeg IS 'Codigo de Tipo de seguro asociado a TablaTablas[]';  ---??
COMMENT ON COLUMN Persona.c_Genero IS 'Codigo de Sexo asociado a TablaTablas[]';  ---??
COMMENT ON COLUMN Persona.tNacimi IS 'Numero de Documento';
COMMENT ON COLUMN Persona._cCodDis IS 'Referencia a tabla Distritos';
COMMENT ON COLUMN Persona.cDirecc IS 'Numero de Documento';
COMMENT ON COLUMN Persona.cCorreo IS 'Correos asociados a la persona separados por comas';
COMMENT ON COLUMN Persona.cNroCel IS 'Numeros asociados a la persona separados por comas';
COMMENT ON COLUMN Persona.cClave IS 'Clave en SHA512';
COMMENT ON COLUMN Persona.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Persona._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Persona.tGenera IS 'Fecha Generacion';
COMMENT ON COLUMN Persona.tModifi IS 'Fecha Modificacion';

INSERT INTO Persona(cNroDni, c_TipDoc, cNroDoc, cNombre, c_Sexo, tNacimi, _cCodDis, cDirecc, cEmail, cNroCel, cClave, c_Estado, _cUsuCod, tModifi) VALUES
    ('00000000', 'D', '00000000', 'USUARIO SIN CODIGO', 'M', NOW(), '000000', 'NINGUNA', '', '', '', 'A', '0000', NOW()),
    ('99999999', 'D', '99999999', 'SISTEMA', 'M', NOW(), '000000', 'NINGUNA', '', '', '', 'A', '9999', NOW());

-- Usuario
CREATE TABLE Usuario (
   cCodUsu   CHARACTER(4)   NOT NULL PRIMARY KEY,
   _cNroDni  CHARACTER(8)   NOT NULL REFERENCES Persona (cNroDni) ON DELETE RESTRICT ON UPDATE CASCADE,
   c_Cargo   CHARACTER(3)   NOT NULL DEFAULT '000',
   c_Estado  CHARACTER(1)   NOT NULL DEFAULT 'A',
   _cUsuCod   CHARACTER(4)   NOT NULL,
   tGenera   TIMESTAMP      NOT NULL DEFAULT NOW(),
   tModifi   TIMESTAMP      NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Usuario IS 'Maestro de Usuaios, Usuarios del Sistema';
COMMENT ON COLUMN Usuario.cCodUsu IS 'Codigo del usuario';
COMMENT ON COLUMN Usuario._cNroDni IS 'Referencia a la tabla Persona';
COMMENT ON COLUMN Usuario.c_Cargo IS 'Codigo de Cargo asociado a TablaTablas[]'; --??
COMMENT ON COLUMN Usuario.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Usuario._cUsuCod IS 'Usuario que registra';
COMMENT ON COLUMN Usuario.tGenera IS 'Fecha Generacion';
COMMENT ON COLUMN Usuario.tModifi IS 'Fecha Modificacion';
INSERT INTO Usuario(cCodUsu, _cNroDni, c_Cargo, c_estado, _cUsuCod, tModifi) VALUES
('0000', '00000000', '000', 'A', '0000', NOW()),
('9999', '99999999', '000', 'A', '9999', NOW());


ALTER TABLE Persona 
   ADD CONSTRAINT fk_Usuario
   FOREIGN KEY (_cUsuCod)
   REFERENCES Usuario(cCodUsu)
   ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE Persona 
   ADD CONSTRAINT fk_Distrito
   FOREIGN KEY (_cCodDis)
   REFERENCES Distrito(cCodDis)
   ON DELETE RESTRICT ON UPDATE CASCADE;

CREATE TABLE App(
   nIdApp   SMALLINT PRIMARY KEY,
   cDescri   CHARACTER(100)  NOT NULL,
   cVersio   CHARACTER(10)   NOT NULL,
   c_Estado  CHARACTER(1)    NOT NULL DEFAULT 'A',
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE App IS 'Tabla Aplicaciones que usan la base de datos';
COMMENT ON COLUMN App.nIdApp IS 'codigo de la aplicacion que usa la base de datos';
COMMENT ON COLUMN App.cDescri IS 'Descripcion';
COMMENT ON COLUMN App.cVersio IS 'Version de la aplicacion';
COMMENT ON COLUMN App.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN App._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN App.tModifi IS 'Fecha Modificacion';

INSERT INTO App(nIdApp, cDescri, cVersio, c_Estado, _cUsuCod, tModifi) VALUES 
(1, 'PHP CLANAD:Rayos x y Labortorio','0.1', 'A', '0000', NOW()),
(2, 'PHP CLANAD:RESULTADOS','0.1', 'A', '0000', NOW()),
(3, 'FLASK CLANAD:Salud Ocupacional','0.1', 'A', '0000', NOW());

CREATE TABLE Empresa (
   cNroRuc   CHARACTER(11)   NOT NULL PRIMARY KEY,
   cDescri   VARCHAR(200)    NOT NULL,
   _cCodDis   CHARACTER(8) DEFAULT '000000',
   cDirecc   VARCHAR(300) ,
   cClave   CHARACTER(128)  NOT NULL,
   cConSul  VARCHAR(90),
   c_Estado  CHARACTER(1)    NOT NULL DEFAULT 'A',
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Empresa IS 'Maestro Empresas';
COMMENT ON COLUMN Empresa.cNroRuc IS 'Numero de RUC de la empresa'; 
COMMENT ON COLUMN Empresa.cDescri IS 'Nombre comercial'; 
COMMENT ON COLUMN Empresa._cCodDis IS 'Referencia a tabla Distrito';
COMMENT ON COLUMN Empresa.cDirecc IS 'Direccion fisica'; 
COMMENT ON COLUMN Empresa.cClave IS 'Clave en SHA512';
COMMENT ON COLUMN Empresa.cConSul IS 'Grupo de RUC separados por coma para poder realizar la consulta';
COMMENT ON COLUMN Empresa.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Empresa._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Empresa.tModifi IS 'Fecha Modificacion'; 

CREATE TABLE TablaTablas (
   nSerial SERIAL         NOT NULL UNIQUE,
   cCodTab CHARACTER(3)   NOT NULL,
   cTblFld VARCHAR(100)   NOT NULL,
   cCodigo VARCHAR(8)     NOT NULL,
   nOrden  SMALLINT       NOT NULL,
   c_TipReg CHARACTER(1)  NOT NULL, 
   cDescri  VARCHAR(100)  NOT NULL,
   _cUsuCod CHARACTER(4)  NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi TIMESTAMP      NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE TablaTablas IS 'Tabla donde se guardan las opciones de los select, estados, descripciones generales';
COMMENT ON COLUMN TablaTablas.cCodTab IS 'Codigo del Arreglo';
COMMENT ON COLUMN TablaTablas.cTblFld IS ' Descripcion del campo Arreglo';
COMMENT ON COLUMN TablaTablas.cCodigo IS 'Codigo dentro del Arreglo';
COMMENT ON COLUMN TablaTablas.nOrden IS 'Orden en que se muestran';
COMMENT ON COLUMN TablaTablas.c_TipReg IS 'M:cabecera MAESTRO, D: DETALLE';
COMMENT ON COLUMN TablaTablas.cDescri IS 'Descripcion del campo'; 
COMMENT ON COLUMN TablaTablas._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN TablaTablas.tModifi IS 'Fecha Modificacion';

CREATE TABLE Rol (
   cCodRol   CHARACTER(3)   NOT NULL PRIMARY KEY,
   cDescri   VARCHAR(100)   NOT NULL,
   c_Estado  CHARACTER(1)   NOT NULL DEFAULT 'A',   -- [000]
   _cUsuCod  CHARACTER(4)   NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP      NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Rol IS 'Agrupacion de Opciones';
COMMENT ON COLUMN Rol.cCodRol IS 'Codigo del Rol';
COMMENT ON COLUMN Rol.cDescri IS 'Descripcion';
COMMENT ON COLUMN Rol.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Rol._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Rol.tModifi IS 'Fecha Modificacion';

CREATE TABLE Opcion (
   cCodOpc   CHARACTER(15)   NOT NULL PRIMARY KEY,
   _nIdApp   SMALLINT       NOT NULL REFERENCES App (nIdApp) ON DELETE RESTRICT ON UPDATE CASCADE,
   cDescri   VARCHAR(100)   NOT NULL,
   cSvgPat   VARCHAR(1000),
   c_Estado  CHARACTER(1)   NOT NULL DEFAULT 'A',   -- [000]
   _cUsuCod  CHARACTER(4)   NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP      NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Opcion IS 'Opciones del Sistema';
COMMENT ON COLUMN Opcion.cCodOpc IS 'Codigo de Opcion/ Nombre de la pantalla';
COMMENT ON COLUMN Opcion._nIdApp IS 'Referencia a la tabla App';
COMMENT ON COLUMN Opcion.cDescri IS 'Descripcion';
COMMENT ON COLUMN Opcion.cSvgPat IS 'Texto svg para imagenes';
COMMENT ON COLUMN Opcion.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Opcion._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Opcion.tModifi IS 'Fecha Modificacion'; 

CREATE TABLE Rol_Opcion (
   nSerial   SERIAL         NOT NULL UNIQUE,
   _cCodOpc  CHARACTER(15)   NOT NULL REFERENCES Opcion (cCodOpc) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodRol  CHARACTER(3)   NOT NULL REFERENCES Rol (cCodRol) ON DELETE RESTRICT ON UPDATE CASCADE,
   c_Estado  CHARACTER(1)   NOT NULL DEFAULT 'A',   -- [000]
   _cUsuCod  CHARACTER(4)   NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP      NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Rol_Opcion IS 'Puente Rol Opciones del Sistema';
COMMENT ON COLUMN Rol_Opcion._cCodOpc IS 'Referencia a la tabla Opcion';
COMMENT ON COLUMN Rol_Opcion._cCodRol IS 'Referencia a la tabla Rol';
COMMENT ON COLUMN Rol_Opcion.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Rol_Opcion._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Rol_Opcion.tModifi IS 'Fecha Modificacion'; 

-- Puente Usuario-Rol
CREATE TABLE Usuario_Rol (
   nSerial   SERIAL         NOT NULL UNIQUE,
   _cCodRol  CHARACTER(3)   NOT NULL REFERENCES Rol (cCodRol) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodUsu  CHARACTER(4)   NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   c_Estado  CHARACTER(1)   NOT NULL DEFAULT 'A',   -- [000]
   _cUsuCod  CHARACTER(4)   NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP      NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Usuario_Rol IS 'Roles Asociados a los usuarios';
COMMENT ON COLUMN Usuario_Rol._cCodRol IS 'Referencia a la tabla Rol';
COMMENT ON COLUMN Usuario_Rol._cCodUsu IS 'Referencia a la tabla Usuario';
COMMENT ON COLUMN Usuario_Rol.c_Estado IS 'Referencia a la tabla TablaTablas[]'; --??
COMMENT ON COLUMN Usuario_Rol._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Usuario_Rol.tModifi IS 'Fecha Modificacion';

CREATE TABLE Empresa_CentroDistribucion (
   nSerial    SERIAL         NOT NULL UNIQUE,
   cCenDis    CHARACTER(2)    NOT NULL,
   _cNroRuc  CHARACTER(11)   NOT NULL REFERENCES Empresa (cNroRuc) ON DELETE RESTRICT ON UPDATE CASCADE,
   cDescri   VARCHAR(200)     NOT NULL,
   _cUsuCod   CHARACTER(4)    NOT NULL REFERENCES Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi    TIMESTAMP       NOT NULL DEFAULT NOW()
);
COMMENT ON TABLE Empresa_CentroDistribucion IS 'Roles Asociados a los usuarios';
COMMENT ON COLUMN Empresa_CentroDistribucion.cCenDis IS 'Codigo interno de la sub empresa o area';
COMMENT ON COLUMN Empresa_CentroDistribucion.cDescri IS 'Descripcion del area o sucursal';
COMMENT ON COLUMN Empresa_CentroDistribucion._cNroRuc IS 'Referencia a la tabla Empresa';
COMMENT ON COLUMN Empresa_CentroDistribucion._cUsuCod IS 'Referencia a la tabla Usuario, Usuario que registra';
COMMENT ON COLUMN Empresa_CentroDistribucion.tModifi IS 'Fecha Modificacion';

---??

CREATE OR REPLACE VIEW v_tablatablas_1
 AS
 SELECT t.ccodtab,
    t.ccodigo,
    t.cdescri,
    t.norden
   FROM tablatablas t
  WHERE t.c_tipreg = 'D'::bpchar
  ORDER BY t.norden, t.ccodigo;

CREATE OR REPLACE VIEW v_persona_1
 AS
 SELECT a.c_tipdoc,
    i.cdescri AS cdesdoc,
    a.cnrodoc,
    a.cnrodni,
    a.cnombre AS cnombres,
    split_part(a.cnombre::text, '/'::text, 1) AS capepat,
    split_part(a.cnombre::text, '/'::text, 2) AS capemat,
    split_part(a.cnombre::text, '/'::text, 3) AS cnombre,
    a.c_genero,
    f.cdescri AS cdessex,
    a.c_tipseg,
    g.cdescri AS cdesseg,
    a.tnacimi,
    date_part('year'::text, age(now(), a.tnacimi::timestamp with time zone)) AS nedad,
    a.cdirecc,
    a.cCorreo,
    a.cnrocel,
    a.c_estado,
    h.cdescri AS cdesest,
    b.ccoddep,
    b.cdescri AS cdesdep,
    c.ccodpro,
    c.cdescri AS cdespro,
    d.ccoddis,
    d.cdescri AS cdesdis
   FROM persona a
     LEFT JOIN departamento b ON b.ccoddep::text = "substring"(a._cCodDis::text, 1, 2)
     LEFT JOIN provincia c ON c.ccodpro::text = "substring"(a._cCodDis::text, 1, 4)
     LEFT JOIN distrito d ON d.ccoddis::text = "substring"(a._cCodDis::text, 1, 6)
     LEFT JOIN v_tablatablas_1 f ON f.ccodtab = '002'::bpchar AND btrim(f.ccodigo::text) = a.c_genero::text
     LEFT JOIN v_tablatablas_1 g ON g.ccodtab = '004'::bpchar AND btrim(g.ccodigo::text) = a.c_tipseg::text
     LEFT JOIN v_tablatablas_1 h ON h.ccodtab = '001'::bpchar AND btrim(h.ccodigo::text) = a.c_estado::text
     LEFT JOIN v_tablatablas_1 i ON i.ccodtab = '003'::bpchar AND btrim(i.ccodigo::text) = a.c_tipdoc::text;