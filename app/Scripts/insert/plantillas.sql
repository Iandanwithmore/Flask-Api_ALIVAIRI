CREATE TABLE Clinica.Triaje (
	cPA      VARCHAR(7)     NOT NULL,  --PRESION ARTERIAL
	nFR      VARCHAR(2)     NOT NULL,  --FRECUENCIA RESPITAROIA
	nFC      VARCHAR(3)     NOT NULL,  --FRECUENCIA CARDIACA
	nTemper  VARCHAR(5)     NOT NULL,
	nPeso    VARCHAR(5)     NOT NULL,
	nTalla   VARCHAR(4)     NOT NULL,
	nSat     VARCHAR(3)     NOT NULL,
	nIMC     VARCHAR(5)     NOT NULL,
	nCintur  VARCHAR(3)     NOT NULL,
	nCadera  VARCHAR(3)     NOT NULL,
	nICC     VARCHAR(4)     NOT NULL, --INDICE CINTURA CADERA
   _cCodPla   CHARACTER(11)    NOT NULL REFERENCES Clinica.PlanActividad (cCodPla) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cUsuCod   CHARACTER(4)    NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi    TIMESTAMP       NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE Clinica.Triaje IS 'Tabla de Triaje, Salud Ocupacional';
COMMENT ON COLUMN Clinica.Triaje.cPA IS 'PRESION ARTERIAL';
COMMENT ON COLUMN Clinica.Triaje.nFR IS 'FRECUENCIA RESPIRATORIA';
COMMENT ON COLUMN Clinica.Triaje.nFC IS 'FRECUENCIA CARDIACA';
COMMENT ON COLUMN Clinica.Triaje.nIMC IS 'INDICE DE MASA CORPORAL';
COMMENT ON COLUMN Clinica.Triaje.nICC IS 'INDICE CINTURA CADERA';

CREATE TABLE Clinica.Actividad_extra (
   nSerial   SERIAL         NOT NULL UNIQUE,
   cTexto    TEXT            NOT NULL,
   _cCodAct  CHARACTER(8)    NOT NULL REFERENCES Clinica.Actividad (cCodAct) ON DELETE RESTRICT ON UPDATE CASCADE,
   c_Tipo   CHARACTER(1)    NOT NULL,
	c_Estado   CHARACTER(1)    NOT NULL DEFAULT 'A',
   _cUsuCod   CHARACTER(4)    NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi    TIMESTAMP       NOT NULL DEFAULT NOW()
);

CREATE TABLE Medicina.Indicador (
   cCodInd   CHARACTER(4)    NOT NULL PRIMARY KEY,
   c_TipReg  CHARACTER(1)    NOT NULL, 
   cDescri   VARCHAR(300)    NOT NULL,
   cImprim   VARCHAR(300)    NOT NULL,
   c_Estado  CHARACTER(1)    NOT NULL,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tGenera   TIMESTAMP       NOT NULL DEFAULT NOW(),
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);

CREATE TABLE Medicina.DetalleActividad(
	nSerial    SERIAL          NOT NULL UNIQUE,
	_cCodInd   CHARACTER(4)    NOT NULL REFERENCES Medicina.Indicador (cCodInd) ON DELETE RESTRICT ON UPDATE CASCADE,
   cResult    TEXT            NOT NULL,
   nOpcion  SMALLINT NOT NULL DEFAULT 0,
   _cCodAct   CHARACTER(8)    NOT NULL REFERENCES Clinica.Actividad (cCodAct) ON DELETE RESTRICT ON UPDATE CASCADE,
   c_Estado   CHARACTER(1)    NOT NULL,
   _cUsuCod   CHARACTER(4)    NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi    TIMESTAMP       NOT NULL DEFAULT NOW()
);

CREATE TABLE Medicina.DetallePlantilla(
   nSerial    SERIAL         NOT NULL UNIQUE,
   cLisEnl   VARCHAR(6)      NOT NULL,
   _cCodExa   CHARACTER(6)   NOT NULL REFERENCES Clinica.Examen (cCodExa) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodInd  CHARACTER(4)    NOT NULL REFERENCES Medicina.Indicador (cCodInd) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);

CREATE TABLE Medicina.Subtitulos(
   _cCodExa   CHARACTER(6)   NOT NULL REFERENCES Clinica.Examen (cCodExa) ON DELETE RESTRICT ON UPDATE CASCADE,
   cLisEnl   VARCHAR(6)      NOT NULL,
   cDescri  VARCHAR(200) NOT NULL,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);

ALTER TABLE Clinica.PlanActividad
ADD COLUMN _cCodPer CHARACTER(3) NOT NULL REFERENCES Clinica.Perfil (cCodPer) ON DELETE RESTRICT ON UPDATE CASCADE DEFAULT '000'
INSERT INTO Clinica.Perfil VALUES
('000', 'SIN PERFIL', '20600633369', 'A', '9999', NOW())


--AUDIOMETRIA
INSERT INTO clinica.Examen VALUES 
('900100', 'A', 'AUDIOMETRIA', 'A', '9999', NOW(), 'S', NULL, NULL, 'S');

INSERT INTO Medicina.Indicador VALUES 
('0000', 'I', 'SIN INDICADOR', 'SIN INDICADOR', 'A', '9999', NOW(), NOW()),
('0001', 'B', 'EXPOSICION A RUIDO', 'Exposicion a Ruido', 'A', '9999', NOW(), NOW()),
('0002', 'B', 'USO DE PROTECTORES AUDITIVOS', 'Uso de Protectores Auditivos', 'A', '9999', NOW(), NOW()),
('0003', 'B', 'CONSUMO DE TABACO', 'Consumo de tabaco', 'A', '9999', NOW(), NOW()),
('0004', 'B', 'SERVICIO MILITAR', 'Servicio Militar', 'A', '9999', NOW(), NOW()),
('0005', 'B', 'HOBBIES CON EXPOSICION AL RUIDO', 'Hobbies con exposicion a ruido', 'A', '9999', NOW(), NOW()),
('0006', 'B', 'EXPOSICION LABORAL  A QUIMICOS', 'Exposicion laboral a quimicos', 'A', '9999', NOW(), NOW()),
('0007', 'B', 'INFECCION DE OIDOS', 'Infeccion de oidos', 'A', '9999', NOW(), NOW()),
('0008', 'B', 'USO DE OTOTOXICOS', 'Uso de Ototoxicos', 'A', '9999', NOW(), NOW()),
('0009', 'I', 'TIEMPO DE EXPOSICION', 'Tiempo de Exposicion', 'A', '9999', NOW(), NOW()),
('0010', 'S', 'TIPO DE PROTECTORES', 'Tipo de protectores', 'A', '9999', NOW(), NOW()),
('0011', 'S', 'SINTOMAS ACTUALES', 'Sintomas actuales', 'A', '9999', NOW(), NOW()),
('0012', 'I', 'OTROS AUDIOMETRIA', 'Otros', 'A', '9999', NOW(), NOW()),
('0013', 'S', 'OTOSCOPIA DERECHO', 'Otoscopia Derecho', 'A', '9999', NOW(), NOW()),
('0014', 'I', 'OTOSCOPIA DERECHO DETALLE', 'Otoscopia Derecho Detalle', 'A', '9999', NOW(), NOW()),
('0015', 'S', 'OTOSCOPIA IZQUIERDO', 'Otoscopia Izquierdo', 'A', '9999', NOW(), NOW()),
('0016', 'I', 'OTOSCOPIA IZQUIERDO DETALLE', 'Otoscopia Izquierdo Detalle', 'A', '9999', NOW(), NOW()),
('0017', 'I', 'OIDO DERECHO AEREA', 'Audicion derecho aerea 250', 'A', '9999', NOW(), NOW()),
('0018', 'I', 'OIDO DERECHO AEREA', 'Audicion derecho aerea 500', 'A', '9999', NOW(), NOW()),
('0019', 'I', 'OIDO DERECHO AEREA', 'Audicion derecho aerea 1000', 'A', '9999', NOW(), NOW()),
('0020', 'I', 'OIDO DERECHO AEREA', 'Audicion derecho aerea 2000', 'A', '9999', NOW(), NOW()),
('0021', 'I', 'OIDO DERECHO AEREA', 'Audicion derecho aerea 3000', 'A', '9999', NOW(), NOW()),
('0022', 'I', 'OIDO DERECHO AEREA', 'Audicion derecho aerea 4000', 'A', '9999', NOW(), NOW()),
('0023', 'I', 'OIDO DERECHO AEREA', 'Audicion derecho aerea 6000', 'A', '9999', NOW(), NOW()),
('0024', 'I', 'OIDO DERECHO AEREA', 'Audicion derecho aerea 8000', 'A', '9999', NOW(), NOW()),
('0025', 'I', 'OIDO IZQUIERDO AEREA', 'Audicion izquierda aerea 250', 'A', '9999', NOW(), NOW()),
('0026', 'I', 'OIDO IZQUIERDO AEREA', 'Audicion izquierda aerea 500', 'A', '9999', NOW(), NOW()),
('0027', 'I', 'OIDO IZQUIERDO AEREA', 'Audicion izquierda aerea 1000', 'A', '9999', NOW(), NOW()),
('0028', 'I', 'OIDO IZQUIERDO AEREA', 'Audicion izquierda aerea 2000', 'A', '9999', NOW(), NOW()),
('0029', 'I', 'OIDO IZQUIERDO AEREA', 'Audicion izquierda aerea 3000', 'A', '9999', NOW(), NOW()),
('0030', 'I', 'OIDO IZQUIERDO AEREA', 'Audicion izquierda aerea 4000', 'A', '9999', NOW(), NOW()),
('0031', 'I', 'OIDO IZQUIERDO AEREA', 'Audicion izquierda aerea 6000', 'A', '9999', NOW(), NOW()),
('0032', 'I', 'OIDO IZQUIERDO AEREA', 'Audicion izquierda aerea 8000', 'A', '9999', NOW(), NOW()),
('0033', 'I', 'OIDO DERECHO OSEA', 'Audicion derecho osea 250', 'A', '9999', NOW(), NOW()),
('0034', 'I', 'OIDO DERECHO OSEA', 'Audicion derecho osea 500', 'A', '9999', NOW(), NOW()),
('0035', 'I', 'OIDO DERECHO OSEA', 'Audicion derecho osea 1000', 'A', '9999', NOW(), NOW()),
('0036', 'I', 'OIDO DERECHO OSEA', 'Audicion derecho osea 2000', 'A', '9999', NOW(), NOW()),
('0037', 'I', 'OIDO DERECHO OSEA', 'Audicion derecho osea 3000', 'A', '9999', NOW(), NOW()),
('0038', 'I', 'OIDO DERECHO OSEA', 'Audicion derecho osea 4000', 'A', '9999', NOW(), NOW()),
('0039', 'I', 'OIDO DERECHO OSEA', 'Audicion derecho osea 6000', 'A', '9999', NOW(), NOW()),
('0040', 'I', 'OIDO DERECHO OSEA', 'Audicion derecho osea 8000', 'A', '9999', NOW(), NOW()),
('0041', 'I', 'OIDO IZQUIERDO OSEA', 'Audicion izquierda osea 250', 'A', '9999', NOW(), NOW()),
('0042', 'I', 'OIDO IZQUIERDO OSEA', 'Audicion izquierda osea 500', 'A', '9999', NOW(), NOW()),
('0043', 'I', 'OIDO IZQUIERDO OSEA', 'Audicion izquierda osea 1000', 'A', '9999', NOW(), NOW()),
('0044', 'I', 'OIDO IZQUIERDO OSEA', 'Audicion izquierda osea 2000', 'A', '9999', NOW(), NOW()),
('0045', 'I', 'OIDO IZQUIERDO OSEA', 'Audicion izquierda osea 3000', 'A', '9999', NOW(), NOW()),
('0046', 'I', 'OIDO IZQUIERDO OSEA', 'Audicion izquierda osea 4000', 'A', '9999', NOW(), NOW()),
('0047', 'I', 'OIDO IZQUIERDO OSEA', 'Audicion izquierda osea 6000', 'A', '9999', NOW(), NOW()),
('0048', 'I', 'OIDO IZQUIERDO OSEA', 'Audicion izquierda osea 8000', 'A', '9999', NOW(), NOW());

INSERT INTO Medicina.Subtitulos VALUES
('900100', '0100', 'ANTECEDENTES', '9999', NOW()),
('900100', '0200', 'DETALLAR', '9999', NOW()),
('900100', '0300', 'EXAMEN CLINICO OTOSCOPIA', '9999', NOW()),
('900100', '0400', 'AUDIOGRAMA', '9999', NOW());

INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '0101', '900100', '0001', '0000', NOW()),
(DEFAULT, '0102', '900100', '0002', '0000', NOW()),
(DEFAULT, '0103', '900100', '0003', '0000', NOW()),
(DEFAULT, '0104', '900100', '0004', '0000', NOW()),
(DEFAULT, '0105', '900100', '0005', '0000', NOW()),
(DEFAULT, '0106', '900100', '0006', '0000', NOW()),
(DEFAULT, '0107', '900100', '0007', '0000', NOW()),
(DEFAULT, '0108', '900100', '0008', '0000', NOW()),
(DEFAULT, '0201', '900100', '0009', '0000', NOW()),
(DEFAULT, '0202', '900100', '0010', '0000', NOW()),
(DEFAULT, '0203', '900100', '0011', '0000', NOW()),
(DEFAULT, '0204', '900100', '0012', '0000', NOW()),
(DEFAULT, '0301', '900100', '0013', '0000', NOW()),
(DEFAULT, '0302', '900100', '0014', '0000', NOW()),
(DEFAULT, '0303', '900100', '0015', '0000', NOW()),
(DEFAULT, '0304', '900100', '0016', '0000', NOW()),
(DEFAULT, '0401', '900100', '0017', '0000', NOW()),
(DEFAULT, '0402', '900100', '0018', '0000', NOW()),
(DEFAULT, '0403', '900100', '0019', '0000', NOW()),
(DEFAULT, '0404', '900100', '0020', '0000', NOW()),
(DEFAULT, '0405', '900100', '0021', '0000', NOW()),
(DEFAULT, '0406', '900100', '0022', '0000', NOW()),
(DEFAULT, '0407', '900100', '0023', '0000', NOW()),
(DEFAULT, '0408', '900100', '0024', '0000', NOW()),
(DEFAULT, '0501', '900100', '0025', '0000', NOW()),
(DEFAULT, '0502', '900100', '0026', '0000', NOW()),
(DEFAULT, '0503', '900100', '0027', '0000', NOW()),
(DEFAULT, '0504', '900100', '0028', '0000', NOW()),
(DEFAULT, '0505', '900100', '0029', '0000', NOW()),
(DEFAULT, '0506', '900100', '0030', '0000', NOW()),
(DEFAULT, '0507', '900100', '0031', '0000', NOW()),
(DEFAULT, '0508', '900100', '0032', '0000', NOW()),
(DEFAULT, '0601', '900100', '0033', '0000', NOW()),
(DEFAULT, '0602', '900100', '0034', '0000', NOW()),
(DEFAULT, '0603', '900100', '0035', '0000', NOW()),
(DEFAULT, '0604', '900100', '0036', '0000', NOW()),
(DEFAULT, '0605', '900100', '0037', '0000', NOW()),
(DEFAULT, '0606', '900100', '0038', '0000', NOW()),
(DEFAULT, '0607', '900100', '0039', '0000', NOW()),
(DEFAULT, '0608', '900100', '0040', '0000', NOW()),
(DEFAULT, '0701', '900100', '0041', '0000', NOW()),
(DEFAULT, '0702', '900100', '0042', '0000', NOW()),
(DEFAULT, '0703', '900100', '0043', '0000', NOW()),
(DEFAULT, '0704', '900100', '0044', '0000', NOW()),
(DEFAULT, '0705', '900100', '0045', '0000', NOW()),
(DEFAULT, '0706', '900100', '0046', '0000', NOW()),
(DEFAULT, '0707', '900100', '0047', '0000', NOW()),
(DEFAULT, '0708', '900100', '0048', '0000', NOW());

--EXAMEN OFTALMOLOGICO
INSERT INTO clinica.Examen VALUES 
('600300', 'M', 'OFTALMOLOGICO', 'A', '9999', NOW(), 'S', NULL, NULL, 'S');

INSERT INTO Medicina.Indicador VALUES 
('0049', 'B', 'ANTECEDENTES DE IMPORTANCIA DIABETES', 'Diabetes', 'A', '9999', NOW(), NOW()),
('0050', 'B', 'ANTECEDENTES DE IMPORTANCIA HTA', 'HTA', 'A', '9999', NOW(), NOW()),
('0051', 'B', 'ANTECEDENTES DE IMPORTANCIA TRAUMATISMO OCULAR', 'Traumatismo ocular', 'A', '9999', NOW(), NOW()),
('0052', 'B', 'USO DE LENTES', 'Uso de lentes', 'A', '9999', NOW(), NOW()),
('0053', 'I', 'TIPO DE LENTE', 'Tipo de lente', 'A', '9999', NOW(), NOW()),
('0054', 'I', 'ENFERMEDAD ACTUAL', 'Enfermedad actual', 'A', '9999', NOW(), NOW()),
('0055', 'I', 'VISION DE LEJOS SIN CORRECTORES', 'Vision de lejos sin correctores derecha', 'A', '9999', NOW(), NOW()),
('0056', 'I', 'VISION DE LEJOS SIN CORRECTORES', 'Vision de lejos sin correctores izquierda', 'A', '9999', NOW(), NOW()),
('0057', 'I', 'VISION DE LEJOS CON CORRECTORES', 'Vision de lejos con correctores derecha', 'A', '9999', NOW(), NOW()),
('0058', 'I', 'VISION DE LEJOS CON CORRECTORES', 'Vision de lejos con correctores izquierda', 'A', '9999', NOW(), NOW()),
('0059', 'I', 'VISION DE CERCA', 'Vision de cerca sin correctores', 'A', '9999', NOW(), NOW()),
('0060', 'I', 'VISION DE CERCA', 'Vision de cerca con correctores', 'A', '9999', NOW(), NOW()),
('0061', 'I', 'VISION BINOCULAR', 'Vision binocular sin correctores', 'A', '9999', NOW(), NOW()),
('0062', 'I', 'VISION BINOCULAR', 'Vision binocular con correctores', 'A', '9999', NOW(), NOW()),
('0063', 'I', 'REFLEJOS PUPILARES', 'Reflejos pupilares', 'A', '9999', NOW(), NOW()),
('0064', 'I', 'FILTRO UV DERECHA', 'OD', 'A', '9999', NOW(), NOW()),
('0065', 'I', 'FILTRO UV IZQUIERDA', 'OI', 'A', '9999', NOW(), NOW()),
('0066', 'I', 'VISION DE COLORES', 'Visión de colores', 'A', '9999', NOW(), NOW()),
('0067', 'I', 'VISION DE PROFUNDIDAD', 'Visión de profundidad', 'A', '9999', NOW(), NOW()),
('0068', 'I', 'FONDO DE OJO DERECHO', 'Ojo derecho', 'A', '9999', NOW(), NOW()),
('0069', 'I', 'FONDO DE OJO IZQUIERDO', 'Ojo izquierdo', 'A', '9999', NOW(), NOW()),
('0070', 'I', 'REFRACCION LEJOS ESFERICO', 'Refraccion lejos sf derecha', 'A', '9999', NOW(), NOW()),
('0071', 'I', 'REFRACCION LEJOS ESFERICO', 'Refraccion lejos sf izquierda', 'A', '9999', NOW(), NOW()),
('0072', 'I', 'REFRACCION LEJOS CILINDRICO', 'Refraccion lejos cyl derecha', 'A', '9999', NOW(), NOW()),
('0073', 'I', 'REFRACCION LEJOS CILINDRICO', 'Refraccion lejos cyl izquierda', 'A', '9999', NOW(), NOW()),
('0074', 'I', 'REFRACCION LEJOS EJE', 'Refraccion lejos eje derecha', 'A', '9999', NOW(), NOW()),
('0075', 'I', 'REFRACCION LEJOS EJE', 'Refraccion lejos eje izquierda', 'A', '9999', NOW(), NOW()),
('0076', 'I', 'REFRACCION LEJOS DIP', 'Refraccion lejos dip', 'A', '9999', NOW(), NOW()),
('0077', 'I', 'REFRACCION LEJOS AV', 'Refraccion lejos av derecha', 'A', '9999', NOW(), NOW()),
('0078', 'I', 'REFRACCION LEJOS AV', 'Refraccion lejos av izquierda', 'A', '9999', NOW(), NOW()),
('0079', 'I', 'REFRACCION CERCA ESFERICO', 'Refraccion cerca sf derecha', 'A', '9999', NOW(), NOW()),
('0080', 'I', 'REFRACCION CERCA ESFERICO', 'Refraccion cerca sf izquierda', 'A', '9999', NOW(), NOW()),
('0081', 'I', 'REFRACCION CERCA CILINDRICO', 'Refraccion cerca cyl derecha', 'A', '9999', NOW(), NOW()),
('0082', 'I', 'REFRACCION CERCA CILINDRICO', 'Refraccion cerca cyl izquierda', 'A', '9999', NOW(), NOW()),
('0083', 'I', 'REFRACCION CERCA EJE', 'Refraccion cerca eje derecha', 'A', '9999', NOW(), NOW()),
('0084', 'I', 'REFRACCION CERCA EJE', 'Refraccion cerca eje izquierda', 'A', '9999', NOW(), NOW()),
('0085', 'I', 'REFRACCION CERCA DIP', 'Refraccion cerca dip', 'A', '9999', NOW(), NOW()),
('0086', 'I', 'REFRACCION CERCA AV', 'Refraccion cerca av', 'A', '9999', NOW(), NOW());

INSERT INTO Medicina.Subtitulos VALUES
('600300', '0100', 'ANTECEDENTES DE IMPORTANCIA', '9999', NOW()),
('600300', '0200', 'EXAMEN', '9999', NOW()),
('600300', '0400', 'REFRACCION', '9999', NOW());

INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '0101', '600300', '0049', '0000', NOW()),
(DEFAULT, '0102', '600300', '0050', '0000', NOW()),
(DEFAULT, '0103', '600300', '0051', '0000', NOW()),
(DEFAULT, '0104', '600300', '0052', '0000', NOW()),
(DEFAULT, '0105', '600300', '0053', '0000', NOW()),
(DEFAULT, '0106', '600300', '0054', '0000', NOW()),
(DEFAULT, '0201', '600300', '0055', '0000', NOW()),
(DEFAULT, '0202', '600300', '0056', '0000', NOW()),
(DEFAULT, '0203', '600300', '0057', '0000', NOW()),
(DEFAULT, '0204', '600300', '0058', '0000', NOW()),
(DEFAULT, '0205', '600300', '0059', '0000', NOW()),
(DEFAULT, '0206', '600300', '0060', '0000', NOW()),
(DEFAULT, '0207', '600300', '0061', '0000', NOW()),
(DEFAULT, '0208', '600300', '0062', '0000', NOW()),
(DEFAULT, '0209', '600300', '0063', '0000', NOW()),
(DEFAULT, '0210', '600300', '0064', '0000', NOW()),
(DEFAULT, '0211', '600300', '0065', '0000', NOW()),
(DEFAULT, '0301', '600300', '0066', '0000', NOW()),
(DEFAULT, '0302', '600300', '0067', '0000', NOW()),
(DEFAULT, '0303', '600300', '0068', '0000', NOW()),
(DEFAULT, '0304', '600300', '0069', '0000', NOW()),
(DEFAULT, '0401', '600300', '0070', '0000', NOW()),
(DEFAULT, '0402', '600300', '0071', '0000', NOW()),
(DEFAULT, '0403', '600300', '0072', '0000', NOW()),
(DEFAULT, '0404', '600300', '0073', '0000', NOW()),
(DEFAULT, '0405', '600300', '0074', '0000', NOW()),
(DEFAULT, '0406', '600300', '0075', '0000', NOW()),
(DEFAULT, '0407', '600300', '0076', '0000', NOW()),
(DEFAULT, '0408', '600300', '0077', '0000', NOW()),
(DEFAULT, '0409', '600300', '0078', '0000', NOW()),
(DEFAULT, '0501', '600300', '0079', '0000', NOW()),
(DEFAULT, '0502', '600300', '0080', '0000', NOW()),
(DEFAULT, '0503', '600300', '0081', '0000', NOW()),
(DEFAULT, '0504', '600300', '0082', '0000', NOW()),
(DEFAULT, '0505', '600300', '0083', '0000', NOW()),
(DEFAULT, '0506', '600300', '0084', '0000', NOW()),
(DEFAULT, '0507', '600300', '0085', '0000', NOW()),
(DEFAULT, '0508', '600300', '0086', '0000', NOW());

--EVALUACION OSTEOARTICULAR ARTICULACIONES
INSERT INTO clinica.Examen VALUES 
('600400', 'M', 'OSTEOARTICULAR ARTICULACIONES', 'A', '9999', NOW(), 'S', NULL, NULL, 'S');

INSERT INTO Medicina.Indicador VALUES 
('0087', 'B', 'NUNCA DOCE MESES', 'Nunca', 'A', '9999', NOW(), NOW()),
('0088', 'B', 'NUNCA INCAPACITACION', 'Nunca incapacitacion', 'A', '9999', NOW(), NOW()),
('0089', 'B', 'NUNCA SIETE DIAS', 'Nunca siete dias', 'A', '9999', NOW(), NOW()),
('0090', 'B', 'HOMBRO DERECHO DOCE MESES', 'Hombro derecho', 'A', '9999', NOW(), NOW()),
('0091', 'B', 'HOMBRO DERECHO INCAPACITACION', 'Hombro derecho incapacitacion', 'A', '9999', NOW(), NOW()),
('0092', 'B', 'HOMBRO DERECHO SIETE DIAS', 'Hombro derecho siete dias', 'A', '9999', NOW(), NOW()),
('0093', 'B', 'HOMBRO IZQUIERDO DOCE MESES', 'Hombro izquierdo', 'A', '9999', NOW(), NOW()),
('0094', 'B', 'HOMBRO IZQUIERDO INCAPACITACION', 'Hombro izquierdo incapacitacion', 'A', '9999', NOW(), NOW()),
('0095', 'B', 'HOMBRO IZQUIERDO SIETE DIAS', 'Hombro izquierdo siete dias', 'A', '9999', NOW(), NOW()),
('0096', 'B', 'AMBOS HOMBROS DOCE MESES', 'Ambos hombros', 'A', '9999', NOW(), NOW()),
('0097', 'B', 'AMBOS HOMBROS INCAPACITACION', 'Ambos hombros incapacitacion', 'A', '9999', NOW(), NOW()),
('0098', 'B', 'AMBOS HOMBROS SIETE DIAS', 'Ambos hombros siete dias', 'A', '9999', NOW(), NOW()),
('0099', 'B', 'CODO DERECHO DOCE MESES', 'Codo derecho', 'A', '9999', NOW(), NOW()),
('0100', 'B', 'CODO DERECHO INCAPACITACION', 'Codo derecho incapacitacion', 'A', '9999', NOW(), NOW()),
('0101', 'B', 'CODO DERECHO SIETE DIAS', 'Codo derecho siete dias', 'A', '9999', NOW(), NOW()),
('0102', 'B', 'CODO IZQUIERDO DOCE MESES', 'Codo izquierdo', 'A', '9999', NOW(), NOW()),
('0103', 'B', 'CODO IZQUIERDO INCAPACITACION', 'Codo izquierdo incapacitacion', 'A', '9999', NOW(), NOW()),
('0104', 'B', 'CODO IZQUIERDO SIETE DIAS', 'Codo izquierdo siete dias', 'A', '9999', NOW(), NOW()),
('0105', 'B', 'AMBOS CODOS DOCE MESES', 'Ambos codos', 'A', '9999', NOW(), NOW()),
('0106', 'B', 'AMBOS CODOS INCAPACITACION', 'Ambos codos incapacitacion', 'A', '9999', NOW(), NOW()),
('0107', 'B', 'AMBOS CODOS SIETE DIAS', 'Ambos codos siete dias', 'A', '9999', NOW(), NOW()),
('0108', 'B', 'PUÑOS/MANOS DERECHA DOCE MESES', 'Derecha', 'A', '9999', NOW(), NOW()),
('0109', 'B', 'PUÑOS/MANOS DERECHA INCAPACITACION', ' Puños/Manos Derecha incapacitacion', 'A', '9999', NOW(), NOW()),
('0110', 'B', 'PUÑOS/MANOS DERECHA SIETE DIAS', 'Puños/Manos Derecha siete dias', 'A', '9999', NOW(), NOW()),
('0111', 'B', 'PUÑOS/MANOS IZQUIERDA DOCE MESES', 'Izquierda', 'A', '9999', NOW(), NOW()),
('0112', 'B', 'PUÑOS/MANOS IZQUIERDA INCAPACITACION', 'Puños/Manos Izquierda incapacitacion', 'A', '9999', NOW(), NOW()),
('0113', 'B', 'PUÑOS/MANOS IZQUIERDA SIETE DIAS', 'Puños/Manos Izquierda siete dias', 'A', '9999', NOW(), NOW()),
('0114', 'B', 'PUÑOS/MANOS AMBOS DOCE MESES', 'Ambos', 'A', '9999', NOW(), NOW()),
('0115', 'B', 'PUÑOS/MANOS AMBOS INCAPACITACION', 'Puños/Manos Ambos incapacitacion', 'A', '9999', NOW(), NOW()),
('0116', 'B', 'PUÑOS/MANOS AMBOS SIETE DIAS', 'Puños/Manos Ambos siete dias', 'A', '9999', NOW(), NOW()),
('0117', 'B', 'COLUMNA ALTA (DORSO) DOCE MESES', 'Columna alta (Dorso)', 'A', '9999', NOW(), NOW()),
('0118', 'B', 'COLUMNA ALTA (DORSO) INCAPACITACION', 'Columna alta (Dorso) incapacitacion', 'A', '9999', NOW(), NOW()),
('0119', 'B', 'COLUMNA ALTA (DORSO) SIETE DIAS', 'Columna alta (Dorso) siete dias', 'A', '9999', NOW(), NOW()),
('0120', 'B', 'COLUMNA BAJA (LUMBARES) DOCE MESES', 'Columna baja (Lumbares)', 'A', '9999', NOW(), NOW()),
('0121', 'B', 'COLUMNA BAJA (LUMBARES) INCAPACITACION', 'Columna baja (Lumbares) incapacitacion', 'A', '9999', NOW(), NOW()),
('0122', 'B', 'COLUMNA BAJA (LUMBARES) SIETE DIAS', 'Columna baja (Lumbares) siete dias', 'A', '9999', NOW(), NOW()),
('0123', 'B', 'CADERAS DERECHA DOCE MESES', 'Derecha', 'A', '9999', NOW(), NOW()),
('0124', 'B', 'CADERAS DERECHA INCAPACITACION', 'Caderas Derecha incapacitacion', 'A', '9999', NOW(), NOW()),
('0125', 'B', 'CADERAS DERECHA SIETE DIAS', 'Caderas Derecha siete dias', 'A', '9999', NOW(), NOW()),
('0126', 'B', 'CADERAS IZQUIERDA DOCE MESES', 'Izquierda', 'A', '9999', NOW(), NOW()),
('0127', 'B', 'CADERAS IZQUIERDA INCAPACITACION', 'Caderas Izquierda incapacitacion', 'A', '9999', NOW(), NOW()),
('0128', 'B', 'CADERAS IZQUIERDA SIETE DIAS', 'Caderas Izquierda siete dias', 'A', '9999', NOW(), NOW()),
('0129', 'B', 'RODILLA DERECHA DOCE MESES', 'Derecha', 'A', '9999', NOW(), NOW()),
('0130', 'B', 'RODILLA DERECHA INCAPACITACION', 'Rodilla Derecha incapacitacion', 'A', '9999', NOW(), NOW()),
('0131', 'B', 'RODILLA DERECHA SIETE DIAS', 'Rodilla Derecha siete dias', 'A', '9999', NOW(), NOW()),
('0132', 'B', 'RODILLA IZQUIERDA DOCE MESES', 'Izquierda', 'A', '9999', NOW(), NOW()),
('0133', 'B', 'RODILLA IZQUIERDA INCAPACITACION', 'Rodilla Izquierda incapacitacion', 'A', '9999', NOW(), NOW()),
('0134', 'B', 'RODILLA IZQUIERDA SIETE DIAS', 'Rodilla Izquierda siete dias', 'A', '9999', NOW(), NOW()),
('0135', 'B', 'TOBILLO/PIES DERECHO DOCE MESES', 'Derecho', 'A', '9999', NOW(), NOW()),
('0136', 'B', 'TOBILLO/PIES DERECHO INCAPACITACION', 'Tobillo/pies Derecho incapacitacion', 'A', '9999', NOW(), NOW()),
('0137', 'B', 'TOBILLO/PIES DERECHO SIETE DIAS', 'Tobillo/pies Derecho siete dias', 'A', '9999', NOW(), NOW()),
('0138', 'B', 'TOBILLO/PIES IZQUIERDO DOCE MESES', 'Izquierdo', 'A', '9999', NOW(), NOW()),
('0139', 'B', 'TOBILLO/PIES IZQUIERDO INCAPACITACION', 'Tobillo/pies Izquierdo incapacitacion', 'A', '9999', NOW(), NOW()),
('0140', 'B', 'TOBILLO/PIES IZQUIERDO SIETE DIAS', 'Tobillo/pies Izquierdo siete dias', 'A', '9999', NOW(), NOW());

INSERT INTO Medicina.Subtitulos VALUES
('600400', '0200', 'Hombros', '9999', NOW()),
('600400', '0300', 'Codos', '9999', NOW()),
('600400', '0400', 'Puños/Manos', '9999', NOW()),
('600400', '0600', 'Caderas', '9999', NOW()),
('600400', '0700', 'Rodilla', '9999', NOW()),
('600400', '0800', 'Tobillo/Pies', '9999', NOW());

INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '0101', '600400', '0087', '0000', NOW()),
(DEFAULT, '0102', '600400', '0088', '0000', NOW()),
(DEFAULT, '0103', '600400', '0089', '0000', NOW()),
(DEFAULT, '0201', '600400', '0090', '0000', NOW()),
(DEFAULT, '0202', '600400', '0091', '0000', NOW()),
(DEFAULT, '0203', '600400', '0092', '0000', NOW()),
(DEFAULT, '0204', '600400', '0093', '0000', NOW()),
(DEFAULT, '0205', '600400', '0094', '0000', NOW()),
(DEFAULT, '0206', '600400', '0095', '0000', NOW()),
(DEFAULT, '0207', '600400', '0096', '0000', NOW()),
(DEFAULT, '0208', '600400', '0097', '0000', NOW()),
(DEFAULT, '0209', '600400', '0098', '0000', NOW()),
(DEFAULT, '0301', '600400', '0099', '0000', NOW()),
(DEFAULT, '0302', '600400', '0100', '0000', NOW()),
(DEFAULT, '0303', '600400', '0101', '0000', NOW()),
(DEFAULT, '0304', '600400', '0102', '0000', NOW()),
(DEFAULT, '0305', '600400', '0103', '0000', NOW()),
(DEFAULT, '0306', '600400', '0104', '0000', NOW()),
(DEFAULT, '0307', '600400', '0105', '0000', NOW()),
(DEFAULT, '0308', '600400', '0106', '0000', NOW()),
(DEFAULT, '0309', '600400', '0107', '0000', NOW()),
(DEFAULT, '0401', '600400', '0108', '0000', NOW()),
(DEFAULT, '0402', '600400', '0109', '0000', NOW()),
(DEFAULT, '0403', '600400', '0110', '0000', NOW()),
(DEFAULT, '0404', '600400', '0111', '0000', NOW()),
(DEFAULT, '0405', '600400', '0112', '0000', NOW()),
(DEFAULT, '0406', '600400', '0113', '0000', NOW()),
(DEFAULT, '0407', '600400', '0114', '0000', NOW()),
(DEFAULT, '0408', '600400', '0115', '0000', NOW()),
(DEFAULT, '0409', '600400', '0116', '0000', NOW()),
(DEFAULT, '0501', '600400', '0117', '0000', NOW()),
(DEFAULT, '0502', '600400', '0118', '0000', NOW()),
(DEFAULT, '0503', '600400', '0119', '0000', NOW()),
(DEFAULT, '0504', '600400', '0120', '0000', NOW()),
(DEFAULT, '0505', '600400', '0121', '0000', NOW()),
(DEFAULT, '0506', '600400', '0122', '0000', NOW()),
(DEFAULT, '0601', '600400', '0123', '0000', NOW()),
(DEFAULT, '0602', '600400', '0124', '0000', NOW()),
(DEFAULT, '0603', '600400', '0125', '0000', NOW()),
(DEFAULT, '0604', '600400', '0126', '0000', NOW()),
(DEFAULT, '0605', '600400', '0127', '0000', NOW()),
(DEFAULT, '0606', '600400', '0128', '0000', NOW()),
(DEFAULT, '0701', '600400', '0129', '0000', NOW()),
(DEFAULT, '0702', '600400', '0130', '0000', NOW()),
(DEFAULT, '0703', '600400', '0131', '0000', NOW()),
(DEFAULT, '0704', '600400', '0132', '0000', NOW()),
(DEFAULT, '0705', '600400', '0133', '0000', NOW()),
(DEFAULT, '0706', '600400', '0134', '0000', NOW()),
(DEFAULT, '0801', '600400', '0135', '0000', NOW()),
(DEFAULT, '0802', '600400', '0136', '0000', NOW()),
(DEFAULT, '0803', '600400', '0137', '0000', NOW()),
(DEFAULT, '0804', '600400', '0138', '0000', NOW()),
(DEFAULT, '0805', '600400', '0139', '0000', NOW()),
(DEFAULT, '0806', '600400', '0140', '0000', NOW());

--CUESTIONARIO DE SINTOMAS MUSCULO TENDINOSOS
INSERT INTO clinica.Examen VALUES 
('600500', 'M', 'CUESTIONARIO DE SINTOMAS MUSCULO TENDINOSOS', 'A', '9999', NOW(), 'S', NULL, NULL, 'S');

INSERT INTO Medicina.Indicador VALUES 
('0141', 'B', 'CUELLO 1', 'CUELLO', 'A', '9999', NOW(), NOW()),
('0142', 'B', 'HOMBRO 1', 'HOMBRO', 'A', '9999', NOW(), NOW()),
('0143', 'S', 'HOMBRO 1 DETALLE', 'Hombro 1 detalle', 'A', '9999', NOW(), NOW()),
('0144', 'B', 'COLUMNA DORSAL 1', 'COLUMNA DORSAL', 'A', '9999', NOW(), NOW()),
('0145', 'B', 'COLUMNA LUMBAR 1', 'COLUMNA LUMBAR', 'A', '9999', NOW(), NOW()),
('0146', 'B', 'CODO O ANTEBRAZO 1', 'CODO O ANTEBRAZO', 'A', '9999', NOW(), NOW()),
('0147', 'S', 'CODO O ANTEBRAZO 1 DETALLE', 'Codo o antebrazo 1 detalle', 'A', '9999', NOW(), NOW()),
('0148', 'B', 'MUÑECA O MANO 1', 'MUÑECA O MANO', 'A', '9999', NOW(), NOW()),
('0149', 'S', 'MUÑECA O MANO 1 DETALLE', 'Muñeca o mano 1 detalle', 'A', '9999', NOW(), NOW()),
('0150', 'B', 'CADERA O MUSLO 1', 'CADERA O MUSLO', 'A', '9999', NOW(), NOW()),
('0151', 'S', 'CADERA O MUSLO 1 DETALLE', 'Cadera o muslo 1 detalle', 'A', '9999', NOW(), NOW()),
('0152', 'B', 'RODILLA 1', 'RODILLA', 'A', '9999', NOW(), NOW()),
('0153', 'S', 'RODILLA 1 DETALLE', 'Rodilla 1 detalle', 'A', '9999', NOW(), NOW()),
('0154', 'B', 'TOBILLO  O PIE 1', 'TOBILLO  O PIE', 'A', '9999', NOW(), NOW()),
('0155', 'S', 'TOBILLO  O PIE 1 DETALLE', 'Tobillo  o pie 1 detalle', 'A', '9999', NOW(), NOW()),
('0156', 'S', 'CUELLO 2', 'Cuello 2', 'A', '9999', NOW(), NOW()),
('0157', 'S', 'HOMBRO 2', 'Hombro 2', 'A', '9999', NOW(), NOW()),
('0158', 'S', 'COLUMNA DORSAL 2', 'Columna dorsal 2', 'A', '9999', NOW(), NOW()),
('0159', 'S', 'COLUMNA LUMBAR 2', 'Columna lumbar 2', 'A', '9999', NOW(), NOW()),
('0160', 'S', 'CODO O ANTEBRAZO 2', 'Codo o antebrazo 2', 'A', '9999', NOW(), NOW()),
('0161', 'S', 'MUÑECA O MANO 2', 'Muñeca o mano 2', 'A', '9999', NOW(), NOW()),
('0162', 'S', 'CADERA O MUSLO 2', 'Cadera o muslo 2', 'A', '9999', NOW(), NOW()),
('0163', 'S', 'RODILLA 2', 'Rodilla 2', 'A', '9999', NOW(), NOW()),
('0164', 'S', 'TOBILLO O PIE 2', 'Tobillo o pie 2', 'A', '9999', NOW(), NOW()),
('0165', 'B', 'CUELLO 3', 'Cuello 3', 'A', '9999', NOW(), NOW()),
('0166', 'B', 'HOMBRO 3', 'Hombro 3', 'A', '9999', NOW(), NOW()),
('0167', 'B', 'COLUMNA DORSAL 3', 'Columna dorsal 3', 'A', '9999', NOW(), NOW()),
('0168', 'B', 'COLUMNA LUMBAR 3', 'Columna lumbar 3', 'A', '9999', NOW(), NOW()),
('0169', 'B', 'CODO O ANTEBRAZO 3', 'Codo o antebrazo 3', 'A', '9999', NOW(), NOW()),
('0170', 'B', 'MUÑECA O MANO 3', 'Muñeca o mano 3', 'A', '9999', NOW(), NOW()),
('0171', 'B', 'CADERA O MUSLO 3', 'Cadera o muslo 3', 'A', '9999', NOW(), NOW()),
('0172', 'B', 'RODILLA 3', 'Rodilla 3', 'A', '9999', NOW(), NOW()),
('0173', 'B', 'TOBILLO O PIE 3', 'Tobillo o pie 3', 'A', '9999', NOW(), NOW()),
('0174', 'B', 'CUELLO 4', 'Cuello 4', 'A', '9999', NOW(), NOW()),
('0175', 'B', 'HOMBRO 4', 'Hombro 4', 'A', '9999', NOW(), NOW()),
('0176', 'B', 'COLUMNA DORSAL 4', 'Columna dorsal 4', 'A', '9999', NOW(), NOW()),
('0177', 'B', 'COLUMNA LUMBAR 4', 'Columna lumbar 4', 'A', '9999', NOW(), NOW()),
('0178', 'B', 'CODO O ANTEBRAZO 4', 'Codo o antebrazo 4', 'A', '9999', NOW(), NOW()),
('0179', 'B', 'MUÑECA O MANO 4', 'Muñeca o mano 4', 'A', '9999', NOW(), NOW()),
('0180', 'B', 'CADERA O MUSLO 4', 'Cadera o muslo 4', 'A', '9999', NOW(), NOW()),
('0181', 'B', 'RODILLA 4', 'Rodilla 4', 'A', '9999', NOW(), NOW()),
('0182', 'B', 'TOBILLO O PIE 4', 'Tobillo o pie 4', 'A', '9999', NOW(), NOW()),
('0183', 'S', 'CUELLO 5', 'Cuello 5', 'A', '9999', NOW(), NOW()),
('0184', 'S', 'HOMBRO 5', 'Hombro 5', 'A', '9999', NOW(), NOW()),
('0185', 'S', 'COLUMNA DORSAL 5', 'Columna dorsal 5', 'A', '9999', NOW(), NOW()),
('0186', 'S', 'COLUMNA LUMBAR 5', 'Columna lumbar 5', 'A', '9999', NOW(), NOW()),
('0187', 'S', 'CODO O ANTEBRAZO 5', 'Codo o antebrazo 5', 'A', '9999', NOW(), NOW()),
('0188', 'S', 'MUÑECA O MANO 5', 'Muñeca o mano 5', 'A', '9999', NOW(), NOW()),
('0189', 'S', 'CADERA O MUSLO 5', 'Cadera o muslo 5', 'A', '9999', NOW(), NOW()),
('0190', 'S', 'RODILLA 5', 'Rodilla 5', 'A', '9999', NOW(), NOW()),
('0191', 'S', 'TOBILLO O PIE 5', 'Tobillo o pie 5', 'A', '9999', NOW(), NOW()),
('0192', 'S', 'CUELLO 6', 'Cuello 6', 'A', '9999', NOW(), NOW()),
('0193', 'S', 'HOMBRO 6', 'Hombro 6', 'A', '9999', NOW(), NOW()),
('0194', 'S', 'COLUMNA DORSAL 6', 'Columna dorsal 6', 'A', '9999', NOW(), NOW()),
('0195', 'S', 'COLUMNA LUMBAR 6', 'Columna lumbar 6', 'A', '9999', NOW(), NOW()),
('0196', 'S', 'CODO O ANTEBRAZO 6', 'Codo o antebrazo 6', 'A', '9999', NOW(), NOW()),
('0197', 'S', 'MUÑECA O MANO 6', 'Muñeca o mano 6', 'A', '9999', NOW(), NOW()),
('0198', 'S', 'CADERA O MUSLO 6', 'Cadera o muslo 6', 'A', '9999', NOW(), NOW()),
('0199', 'S', 'RODILLA 6', 'Rodilla 6', 'A', '9999', NOW(), NOW()),
('0200', 'S', 'TOBILLO O PIE 6', 'Tobillo o pie 6', 'A', '9999', NOW(), NOW()),
('0201', 'S', 'CUELLO 7', 'Cuello 7', 'A', '9999', NOW(), NOW()),
('0202', 'S', 'HOMBRO 7', 'Hombro 7', 'A', '9999', NOW(), NOW()),
('0203', 'S', 'COLUMNA DORSAL 7', 'Columna dorsal 7', 'A', '9999', NOW(), NOW()),
('0204', 'S', 'COLUMNA LUMBAR 7', 'Columna lumbar 7', 'A', '9999', NOW(), NOW()),
('0205', 'S', 'CODO O ANTEBRAZO 7', 'Codo o antebrazo 7', 'A', '9999', NOW(), NOW()),
('0206', 'S', 'MUÑECA O MANO 7', 'Muñeca o mano 7', 'A', '9999', NOW(), NOW()),
('0207', 'S', 'CADERA O MUSLO 7', 'Cadera o muslo 7', 'A', '9999', NOW(), NOW()),
('0208', 'S', 'RODILLA 7', 'Rodilla 7', 'A', '9999', NOW(), NOW()),
('0209', 'S', 'TOBILLO O PIE 7', 'Tobillo o pie 7', 'A', '9999', NOW(), NOW()),
('0210', 'B', 'CUELLO 8', 'Cuello 8', 'A', '9999', NOW(), NOW()),
('0211', 'B', 'HOMBRO 8', 'Hombro 8', 'A', '9999', NOW(), NOW()),
('0212', 'B', 'COLUMNA DORSAL 8', 'Columna dorsal 8', 'A', '9999', NOW(), NOW()),
('0213', 'B', 'COLUMNA LUMBAR 8', 'Columna lumbar 8', 'A', '9999', NOW(), NOW()),
('0214', 'B', 'CODO O ANTEBRAZO 8', 'Codo o antebrazo 8', 'A', '9999', NOW(), NOW()),
('0215', 'B', 'MUÑECA O MANO 8', 'Muñeca o mano 8', 'A', '9999', NOW(), NOW()),
('0216', 'B', 'CADERA O MUSLO 8', 'Cadera o muslo 8', 'A', '9999', NOW(), NOW()),
('0217', 'B', 'RODILLA 8', 'Rodilla 8', 'A', '9999', NOW(), NOW()),
('0218', 'B', 'TOBILLO O PIE 8', 'Tobillo o pie 8', 'A', '9999', NOW(), NOW()),
('0219', 'B', 'CUELLO 9', 'Cuello 9', 'A', '9999', NOW(), NOW()),
('0220', 'B', 'HOMBRO 9', 'Hombro 9', 'A', '9999', NOW(), NOW()),
('0221', 'B', 'COLUMNA DORSAL 9', 'Columna dorsal 9', 'A', '9999', NOW(), NOW()),
('0222', 'B', 'COLUMNA LUMBAR 9', 'Columna lumbar 9', 'A', '9999', NOW(), NOW()),
('0223', 'B', 'CODO O ANTEBRAZO 9', 'Codo o antebrazo 9', 'A', '9999', NOW(), NOW()),
('0224', 'B', 'MUÑECA O MANO 9', 'Muñeca o mano 9', 'A', '9999', NOW(), NOW()),
('0225', 'B', 'CADERA O MUSLO 9', 'Cadera o muslo 9', 'A', '9999', NOW(), NOW()),
('0226', 'B', 'RODILLA 9', 'Rodilla 9', 'A', '9999', NOW(), NOW()),
('0227', 'B', 'TOBILLO O PIE 9', 'Tobillo o pie 9', 'A', '9999', NOW(), NOW()),
('0228', 'S', 'CUELLO 10', 'Cuello 10', 'A', '9999', NOW(), NOW()),
('0229', 'S', 'HOMBRO 10', 'Hombro 10', 'A', '9999', NOW(), NOW()),
('0230', 'S', 'COLUMNA DORSAL 10', 'Columna dorsal 10', 'A', '9999', NOW(), NOW()),
('0231', 'S', 'COLUMNA LUMBAR 10', 'Columna lumbar 10', 'A', '9999', NOW(), NOW()),
('0232', 'S', 'CODO O ANTEBRAZO 10', 'Codo o antebrazo 10', 'A', '9999', NOW(), NOW()),
('0233', 'S', 'MUÑECA O MANO 10', 'Muñeca o mano 10', 'A', '9999', NOW(), NOW()),
('0234', 'S', 'CADERA O MUSLO 10', 'Cadera o muslo 10', 'A', '9999', NOW(), NOW()),
('0235', 'S', 'RODILLA 10', 'Rodilla 10', 'A', '9999', NOW(), NOW()),
('0236', 'S', 'TOBILLO O PIE 10', 'Tobillo o pie 10', 'A', '9999', NOW(), NOW()),
('0237', 'S', 'CUELLO 11', 'Cuello 11', 'A', '9999', NOW(), NOW()),
('0238', 'I', 'CUELLO 11 DETALLE', 'Cuello 11 detalle', 'A', '9999', NOW(), NOW()),
('0239', 'S', 'HOMBRO 11', 'Hombro 11', 'A', '9999', NOW(), NOW()),
('0240', 'I', 'HOMBRO 11 DETALLE', 'Hombro 11 detalle', 'A', '9999', NOW(), NOW()),
('0241', 'S', 'COLUMNA DORSAL 11', 'Columna dorsal 11', 'A', '9999', NOW(), NOW()),
('0242', 'I', 'COLUMNA DORSAL 11 DETALLE', 'Columna dorsal 11 detalle', 'A', '9999', NOW(), NOW()),
('0243', 'S', 'COLUMNA LUMBAR 11', 'Columna lumbar 11', 'A', '9999', NOW(), NOW()),
('0244', 'I', 'COLUMNA LUMBAR 11 DETALLE', 'Columna lumbar 11 detalle', 'A', '9999', NOW(), NOW()),
('0245', 'S', 'CODO O ANTEBRAZO 11', 'Codo o antebrazo 11', 'A', '9999', NOW(), NOW()),
('0246', 'I', 'CODO O ANTEBRAZO 11 DETALLE', 'Codo o antebrazo 11 detalle', 'A', '9999', NOW(), NOW()),
('0247', 'S', 'MUÑECA O MANO 11', 'Muñeca o mano 11', 'A', '9999', NOW(), NOW()),
('0248', 'I', 'MUÑECA O MANO 11 DETALLE', 'Muñeca o mano 11 detalle', 'A', '9999', NOW(), NOW()),
('0249', 'S', 'CADERA O MUSLO 11', 'Cadera o muslo 11', 'A', '9999', NOW(), NOW()),
('0250', 'I', 'CADERA O MUSLO 11 DETALLE', 'Cadera o muslo 11 detalle', 'A', '9999', NOW(), NOW()),
('0251', 'S', 'RODILLA 11', 'Rodilla 11', 'A', '9999', NOW(), NOW()),
('0252', 'I', 'RODILLA 11 DETALLE', 'Rodilla 11 detalle', 'A', '9999', NOW(), NOW()),
('0253', 'S', 'TOBILLO O PIE 11', 'Tobillo o pie 11', 'A', '9999', NOW(), NOW()),
('0254', 'I', 'TOBILLO O PIE 11 DETALLE', 'Tobillo o pie 11 detalle', 'A', '9999', NOW(), NOW());

INSERT INTO Medicina.Subtitulos VALUES
('600500', '0100', 'RESPONDA EN TODOS LOS CASOS', '9999', NOW()),
('600500', '0200', '1. ¿Ha tenido molestias en ... ?', '9999', NOW()),
('600500', '0300', 'Si se contesta NO a la pregunta 1, se finaliza la encuesta', '9999', NOW()),
('600500', '0400', '2. ¿Desde hace cuánto tiempo?', '9999', NOW()),
('600500', '0500', '3. ¿Ha necesitado cambiar de puesto de trabajo?', '9999', NOW()),
('600500', '0600', '4. ¿Ha tenido molestias en los ultimos 12 meses?', '9999', NOW()),
('600500', '0700', 'Si se contesta NO a la pregunta 4, se finaliza la encuesta', '9999', NOW()),
('600500', '0800', '5. ¿Cuánto tiempo ha tenido molestias en los últimos 12 meses?', '9999', NOW()),
('600500', '0900', '6. ¿Cuánto dura cada episodio?', '9999', NOW()),
('600500', '1000', '7. ¿Cuánto tiempo estas molestias le han impedido hacer su trabajo en los últimos 12 meses?', '9999', NOW()),
('600500', '1100', '8. ¿Ha recibido tratamiento por estas molestias en los últimos 12 meses?', '9999', NOW()),
('600500', '1200', '9. ¿Ha tenido molestias en los últimos 7 días?', '9999', NOW()),
('600500', '1300', '10. Pongale nota a sus molestias entre o (sin molestias) y 5 (molestias muy fuertes)', '9999', NOW()),
('600500', '1400', '11. ¿A qué atribuye estas molestias?', '9999', NOW());

INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '0201', '600500', '0141', '0000', NOW()),
(DEFAULT, '0202', '600500', '0142', '0000', NOW()),
(DEFAULT, '0203', '600500', '0143', '0000', NOW()),
(DEFAULT, '0204', '600500', '0144', '0000', NOW()),
(DEFAULT, '0205', '600500', '0145', '0000', NOW()),
(DEFAULT, '0206', '600500', '0146', '0000', NOW()),
(DEFAULT, '0207', '600500', '0147', '0000', NOW()),
(DEFAULT, '0208', '600500', '0148', '0000', NOW()),
(DEFAULT, '0209', '600500', '0149', '0000', NOW()),
(DEFAULT, '0210', '600500', '0150', '0000', NOW()),
(DEFAULT, '0211', '600500', '0151', '0000', NOW()),
(DEFAULT, '0212', '600500', '0152', '0000', NOW()),
(DEFAULT, '0213', '600500', '0153', '0000', NOW()),
(DEFAULT, '0214', '600500', '0154', '0000', NOW()),
(DEFAULT, '0215', '600500', '0155', '0000', NOW()),
(DEFAULT, '0401', '600500', '0156', '0000', NOW()),
(DEFAULT, '0402', '600500', '0157', '0000', NOW()),
(DEFAULT, '0403', '600500', '0158', '0000', NOW()),
(DEFAULT, '0404', '600500', '0159', '0000', NOW()),
(DEFAULT, '0405', '600500', '0160', '0000', NOW()),
(DEFAULT, '0406', '600500', '0161', '0000', NOW()),
(DEFAULT, '0407', '600500', '0162', '0000', NOW()),
(DEFAULT, '0408', '600500', '0163', '0000', NOW()),
(DEFAULT, '0409', '600500', '0164', '0000', NOW()),
(DEFAULT, '0501', '600500', '0165', '0000', NOW()),
(DEFAULT, '0502', '600500', '0166', '0000', NOW()),
(DEFAULT, '0503', '600500', '0167', '0000', NOW()),
(DEFAULT, '0504', '600500', '0168', '0000', NOW()),
(DEFAULT, '0505', '600500', '0169', '0000', NOW()),
(DEFAULT, '0506', '600500', '0170', '0000', NOW()),
(DEFAULT, '0507', '600500', '0171', '0000', NOW()),
(DEFAULT, '0508', '600500', '0172', '0000', NOW()),
(DEFAULT, '0509', '600500', '0173', '0000', NOW()),
(DEFAULT, '0601', '600500', '0174', '0000', NOW()),
(DEFAULT, '0602', '600500', '0175', '0000', NOW()),
(DEFAULT, '0603', '600500', '0176', '0000', NOW()),
(DEFAULT, '0604', '600500', '0177', '0000', NOW()),
(DEFAULT, '0605', '600500', '0178', '0000', NOW()),
(DEFAULT, '0606', '600500', '0179', '0000', NOW()),
(DEFAULT, '0607', '600500', '0180', '0000', NOW()),
(DEFAULT, '0608', '600500', '0181', '0000', NOW()),
(DEFAULT, '0609', '600500', '0182', '0000', NOW()),
(DEFAULT, '0801', '600500', '0183', '0000', NOW()),
(DEFAULT, '0802', '600500', '0184', '0000', NOW()),
(DEFAULT, '0803', '600500', '0185', '0000', NOW()),
(DEFAULT, '0804', '600500', '0186', '0000', NOW()),
(DEFAULT, '0805', '600500', '0187', '0000', NOW()),
(DEFAULT, '0806', '600500', '0188', '0000', NOW()),
(DEFAULT, '0807', '600500', '0189', '0000', NOW()),
(DEFAULT, '0808', '600500', '0190', '0000', NOW()),
(DEFAULT, '0809', '600500', '0191', '0000', NOW()),
(DEFAULT, '0901', '600500', '0192', '0000', NOW()),
(DEFAULT, '0902', '600500', '0193', '0000', NOW()),
(DEFAULT, '0903', '600500', '0194', '0000', NOW()),
(DEFAULT, '0904', '600500', '0195', '0000', NOW()),
(DEFAULT, '0905', '600500', '0196', '0000', NOW()),
(DEFAULT, '0906', '600500', '0197', '0000', NOW()),
(DEFAULT, '0907', '600500', '0198', '0000', NOW()),
(DEFAULT, '0908', '600500', '0199', '0000', NOW()),
(DEFAULT, '0909', '600500', '0200', '0000', NOW()),
(DEFAULT, '1001', '600500', '0201', '0000', NOW()),
(DEFAULT, '1002', '600500', '0202', '0000', NOW()),
(DEFAULT, '1003', '600500', '0203', '0000', NOW()),
(DEFAULT, '1004', '600500', '0204', '0000', NOW()),
(DEFAULT, '1005', '600500', '0205', '0000', NOW()),
(DEFAULT, '1006', '600500', '0206', '0000', NOW()),
(DEFAULT, '1007', '600500', '0207', '0000', NOW()),
(DEFAULT, '1008', '600500', '0208', '0000', NOW()),
(DEFAULT, '1009', '600500', '0209', '0000', NOW()),
(DEFAULT, '1101', '600500', '0210', '0000', NOW()),
(DEFAULT, '1102', '600500', '0211', '0000', NOW()),
(DEFAULT, '1103', '600500', '0212', '0000', NOW()),
(DEFAULT, '1104', '600500', '0213', '0000', NOW()),
(DEFAULT, '1105', '600500', '0214', '0000', NOW()),
(DEFAULT, '1106', '600500', '0215', '0000', NOW()),
(DEFAULT, '1107', '600500', '0216', '0000', NOW()),
(DEFAULT, '1108', '600500', '0217', '0000', NOW()),
(DEFAULT, '1109', '600500', '0218', '0000', NOW()),
(DEFAULT, '1201', '600500', '0219', '0000', NOW()),
(DEFAULT, '1202', '600500', '0220', '0000', NOW()),
(DEFAULT, '1203', '600500', '0221', '0000', NOW()),
(DEFAULT, '1204', '600500', '0222', '0000', NOW()),
(DEFAULT, '1205', '600500', '0223', '0000', NOW()),
(DEFAULT, '1206', '600500', '0224', '0000', NOW()),
(DEFAULT, '1207', '600500', '0225', '0000', NOW()),
(DEFAULT, '1208', '600500', '0226', '0000', NOW()),
(DEFAULT, '1209', '600500', '0227', '0000', NOW()),
(DEFAULT, '1301', '600500', '0228', '0000', NOW()),
(DEFAULT, '1302', '600500', '0229', '0000', NOW()),
(DEFAULT, '1303', '600500', '0230', '0000', NOW()),
(DEFAULT, '1304', '600500', '0231', '0000', NOW()),
(DEFAULT, '1305', '600500', '0232', '0000', NOW()),
(DEFAULT, '1306', '600500', '0233', '0000', NOW()),
(DEFAULT, '1307', '600500', '0234', '0000', NOW()),
(DEFAULT, '1308', '600500', '0235', '0000', NOW()),
(DEFAULT, '1309', '600500', '0236', '0000', NOW()),
(DEFAULT, '1401', '600500', '0237', '0000', NOW()),
(DEFAULT, '1402', '600500', '0238', '0000', NOW()),
(DEFAULT, '1403', '600500', '0239', '0000', NOW()),
(DEFAULT, '1404', '600500', '0240', '0000', NOW()),
(DEFAULT, '1405', '600500', '0241', '0000', NOW()),
(DEFAULT, '1406', '600500', '0242', '0000', NOW()),
(DEFAULT, '1407', '600500', '0243', '0000', NOW()),
(DEFAULT, '1408', '600500', '0244', '0000', NOW()),
(DEFAULT, '1409', '600500', '0245', '0000', NOW()),
(DEFAULT, '1410', '600500', '0246', '0000', NOW()),
(DEFAULT, '1411', '600500', '0247', '0000', NOW()),
(DEFAULT, '1412', '600500', '0248', '0000', NOW()),
(DEFAULT, '1413', '600500', '0249', '0000', NOW()),
(DEFAULT, '1414', '600500', '0250', '0000', NOW()),
(DEFAULT, '1415', '600500', '0251', '0000', NOW()),
(DEFAULT, '1416', '600500', '0252', '0000', NOW()),
(DEFAULT, '1417', '600500', '0253', '0000', NOW()),
(DEFAULT, '1418', '600500', '0254', '0000', NOW());

--ELECTROCARDIOGRAMA
INSERT INTO clinica.Examen VALUES 
('600600', 'M', 'ELECTROCARDIOGRAMA', 'A', '9999', NOW(), 'S', NULL, NULL, 'S');

INSERT INTO Medicina.Indicador VALUES 
('0255', 'I', 'RITMO', 'RITMO', 'A', '9999', NOW(), NOW()),
('0256', 'I', 'F.C.', 'F.C.', 'A', '9999', NOW(), NOW()),
('0257', 'I', 'INTERVALO PR', 'INTERVALO PR', 'A', '9999', NOW(), NOW()),
('0258', 'I', 'INTERVALO QRS', 'INTERVALO QRS', 'A', '9999', NOW(), NOW()),
('0259', 'I', 'INTERVALO QT', 'INTERVALO QT', 'A', '9999', NOW(), NOW()),
('0260', 'I', 'ONDA P', 'ONDA P', 'A', '9999', NOW(), NOW()),
('0261', 'I', 'ONDA Q', 'ONDA Q', 'A', '9999', NOW(), NOW()),
('0262', 'I', 'ONDA R', 'ONDA R', 'A', '9999', NOW(), NOW()),
('0263', 'I', 'ONDA S', 'ONDA S', 'A', '9999', NOW(), NOW()),
('0264', 'I', 'ONDA T', 'ONDA T', 'A', '9999', NOW(), NOW()),
('0265', 'I', 'ONDA U', 'ONDA U', 'A', '9999', NOW(), NOW()),
('0266', 'I', 'SEGMENTO ST', 'SEGMENTO ST', 'A', '9999', NOW(), NOW()),
('0267', 'I', 'EJE QRS', 'EJE QRS', 'A', '9999', NOW(), NOW());

INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '0101', '600600', '0255', '0000', NOW()),
(DEFAULT, '0102', '600600', '0256', '0000', NOW()),
(DEFAULT, '0103', '600600', '0257', '0000', NOW()),
(DEFAULT, '0104', '600600', '0258', '0000', NOW()),
(DEFAULT, '0105', '600600', '0259', '0000', NOW()),
(DEFAULT, '0106', '600600', '0260', '0000', NOW()),
(DEFAULT, '0107', '600600', '0261', '0000', NOW()),
(DEFAULT, '0108', '600600', '0262', '0000', NOW()),
(DEFAULT, '0109', '600600', '0263', '0000', NOW()),
(DEFAULT, '0110', '600600', '0264', '0000', NOW()),
(DEFAULT, '0111', '600600', '0265', '0000', NOW()),
(DEFAULT, '0112', '600600', '0266', '0000', NOW()),
(DEFAULT, '0113', '600600', '0267', '0000', NOW());

--PSICOLOGIA
INSERT INTO clinica.Examen VALUES 
('600100', 'P', 'FICHA PSICOLOGICA OCUPACIONAL', 'A', '9999', NOW(), 'S', NULL, NULL, 'S');

INSERT INTO Medicina.Indicador VALUES 
('0268', 'I', 'HISTORIA FAMILIAR', 'Historia Familiar', 'A', '9999', NOW(), NOW()),
('0269', 'I', 'ACCIDENTES Y ENFERMEDADES(DURANTE EL TIEMPO LABORADO)', 'Accidentes y Enfermedades:(Durante el tiempo laborado)', 'A', '9999', NOW(), NOW()),
('0270', 'I', 'HABITOS(PASATIEMPOS)', 'HABITOS', 'A', '9999', NOW(), NOW()),
('0271', 'B', 'TABACO SI/NO', 'Tabaco', 'A', '9999', NOW(), NOW()),
('0272', 'B', 'ALCOHOL SI/NO', 'Alcohol', 'A', '9999', NOW(), NOW()),
('0273', 'B', 'DROGAS SI/NO', 'Drogas', 'A', '9999', NOW(), NOW()),
('0274', 'S', 'PRESENTACION(VESTIR)', 'Presentacion', 'A', '9999', NOW(), NOW()),
('0275', 'S', 'POSTURA', 'Postura', 'A', '9999', NOW(), NOW()),
('0276', 'S', 'DISCURSO(RITMO)', 'Ritmo', 'A', '9999', NOW(), NOW()),
('0277', 'S', 'DISCURSO(TONO)', 'Tono', 'A', '9999', NOW(), NOW()),
('0278', 'S', 'DISCURSO(ARTICULACION)', 'Articulacion', 'A', '9999', NOW(), NOW()),
('0279', 'S', 'ORIENTACION(TIEMPO)', 'Tiempo', 'A', '9999', NOW(), NOW()),
('0280', 'S', 'ORIENTACION(ESPACIO)', 'Espacio', 'A', '9999', NOW(), NOW()),
('0281', 'S', 'ORIENTACION(PERSONA)', 'Persona', 'A', '9999', NOW(), NOW()),
('0282', 'I', 'TEST DE PERSONALIDAD EYSENCK', 'Test EYSENCK', 'A', '9999', NOW(), NOW()),
('0283', 'I', 'ESCALA DE MOTIVADORES PSICOSOCIALES MPS', 'Escala de Motivadores psicosociales MPS', 'A', '9999', NOW(), NOW()),
('0284', 'I', 'DIAGNOSTICO NEUROPSICOLOGICO ADULTOS LURIA-DNA', 'Luria-DNA, Diagnostico neuropsicologico adultos', 'A', '9999', NOW(), NOW()),
('0285', 'I', 'ESCALA DE SOMNOLENCIA EPWORTH', 'Escala de somnolencia EPWORTH', 'A', '9999', NOW(), NOW()),
('0286', 'I', 'INVENTARIO DE BURNOUT', 'Inventario de Burnout', 'A', '9999', NOW(), NOW()),
('0287', 'I', 'TEST DE SADS', 'Test SADS', 'A', '9999', NOW(), NOW()),
('0288', 'I', 'BATERIA DE CONDUCTORES', 'Bateria de conductores', 'A', '9999', NOW(), NOW()),
('0289', 'I', 'WAIS', 'WAIS', 'A', '9999', NOW(), NOW()),
('0290', 'I', 'TEST BENTON', 'Test Benton', 'A', '9999', NOW(), NOW()),
('0291', 'I', 'TEST BENDER', 'Test Bender', 'A', '9999', NOW(), NOW()),
('0292', 'I', 'TEST DE ANSIEDAD DE ZUNG', 'Test de ansiedad Zung', 'A', '9999', NOW(), NOW()),
('0293', 'I', 'TEST DE DEPRESION ZUNG', 'Test de depresion Zung', 'A', '9999', NOW(), NOW()),
('0294', 'I', 'ESCALA DE ESTRES', 'Escala de estres', 'A', '9999', NOW(), NOW()),
('0295', 'I', 'TEST DE FIGURA BAJO LA LLUVIA', 'Test de figura bajo la lluvia', 'A', '9999', NOW(), NOW()),
('0296', 'I', 'TEST DE FATIGA', 'Test de fatiga', 'A', '9999', NOW(), NOW()),
('0297', 'I', 'TEST ISTAS', 'Test ISTAS', 'A', '9999', NOW(), NOW()),
('0298', 'I', 'LUCIDO ATENTO', 'Lucido/Atento', 'A', '9999', NOW(), NOW()),
('0299', 'I', 'PENSAMIENTO', 'Pensamiento', 'A', '9999', NOW(), NOW()),
('0300', 'I', 'PERCEPCION', 'Percepcion', 'A', '9999', NOW(), NOW()),
('0301', 'S', 'MEMORIA', 'Memoria', 'A', '9999', NOW(), NOW()),
('0302', 'S', 'INTELIGENCIA', 'Inteligencia', 'A', '9999', NOW(), NOW()),
('0303', 'I', 'APETITO', 'Apetito', 'A', '9999', NOW(), NOW()),
('0304', 'I', 'SUEÑO', 'Sueño', 'A', '9999', NOW(), NOW()),
('0305', 'I', 'PERSONALIDAD', 'Personalidad', 'A', '9999', NOW(), NOW()),
('0306', 'I', 'SEXUALIDAD', 'Sexualidad', 'A', '9999', NOW(), NOW()),
('0307', 'I', 'CONDUCTA SEXUAL', 'Conducta Sexual', 'A', '9999', NOW(), NOW());

INSERT INTO Medicina.Subtitulos VALUES
('600100', '3000', 'HABITOS', '9999', NOW()),
('600100', '4000', 'EXAMEN MENTAL', '9999', NOW()),
('600100', '4100', 'OBSERVACION DE CONDUCTAS', '9999', NOW()),
('600100', '4200', 'PRUEBAS PSICOLOGICAS', '9999', NOW()),
('600100', '4300', 'PROCESOS COGNITIVOS', '9999', NOW());

INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '1001', '600100', '0268','9999', NOW()),
(DEFAULT, '2001', '600100', '0269','9999', NOW()),
(DEFAULT, '3001', '600100', '0270','9999', NOW()),
(DEFAULT, '3002', '600100', '0271','9999', NOW()),
(DEFAULT, '3003', '600100', '0272','9999', NOW()),
(DEFAULT, '3004', '600100', '0273','9999', NOW()),
(DEFAULT, '4101', '600100', '0274','9999', NOW()),
(DEFAULT, '4102', '600100', '0275','9999', NOW()),
(DEFAULT, '4111', '600100', '0276','9999', NOW()),
(DEFAULT, '4112', '600100', '0277','9999', NOW()),
(DEFAULT, '4113', '600100', '0278','9999', NOW()),
(DEFAULT, '4121', '600100', '0279','9999', NOW()),
(DEFAULT, '4122', '600100', '0280','9999', NOW()),
(DEFAULT, '4123', '600100', '0281','9999', NOW()),
(DEFAULT, '4201', '600100', '0282','9999', NOW()),
(DEFAULT, '4202', '600100', '0283','9999', NOW()),
(DEFAULT, '4203', '600100', '0284','9999', NOW()),
(DEFAULT, '4204', '600100', '0285','9999', NOW()),
(DEFAULT, '4205', '600100', '0286','9999', NOW()),
(DEFAULT, '4206', '600100', '0287','9999', NOW()),
(DEFAULT, '4207', '600100', '0288','9999', NOW()),
(DEFAULT, '4208', '600100', '0289','9999', NOW()),
(DEFAULT, '4209', '600100', '0290','9999', NOW()),
(DEFAULT, '4210', '600100', '0291','9999', NOW()),
(DEFAULT, '4211', '600100', '0292','9999', NOW()),
(DEFAULT, '4212', '600100', '0293','9999', NOW()),
(DEFAULT, '4213', '600100', '0294','9999', NOW()),
(DEFAULT, '4214', '600100', '0295','9999', NOW()),
(DEFAULT, '4215', '600100', '0296','9999', NOW()),
(DEFAULT, '4216', '600100', '0297','9999', NOW()),
(DEFAULT, '4301', '600100', '0298','9999', NOW()),
(DEFAULT, '4302', '600100', '0299','9999', NOW()),
(DEFAULT, '4303', '600100', '0300','9999', NOW()),
(DEFAULT, '4304', '600100', '0301','9999', NOW()),
(DEFAULT, '4305', '600100', '0302','9999', NOW()),
(DEFAULT, '4306', '600100', '0303','9999', NOW()),
(DEFAULT, '4307', '600100', '0304','9999', NOW()),
(DEFAULT, '4308', '600100', '0305','9999', NOW()),
(DEFAULT, '4309', '600100', '0306','9999', NOW()),
(DEFAULT, '4310', '600100', '0307','9999', NOW());

--INFORME PSICOLOGICO
INSERT INTO clinica.Examen VALUES 
('600101', 'M', 'INFORME PSICOLOGICO OCUPACIONAL', 'A', '9999', NOW(), 'S', NULL, NULL, 'S');

INSERT INTO Medicina.Indicador VALUES 
('0308', 'I', 'NIVEL INTELECTUAL', 'Nivel Intelectual', 'A', '9999', NOW(), NOW()),
('0309', 'I', 'COORDINACION VISOMOTRIZ', 'Coordinación Visomotriz', 'A', '9999', NOW(), NOW()),
('0310', 'I', 'NIVEL DE MEMORIA', 'Nivel de memoria', 'A', '9999', NOW(), NOW()),
('0311', 'I', 'PERSONALIDAD', 'Personalidad', 'A', '9999', NOW(), NOW()),
('0312', 'I', 'AFECTIVIDAD', 'Afectividad', 'A', '9999', NOW(), NOW());

INSERT INTO Medicina.Subtitulos VALUES
('600101', '0100', 'MOTIVO DE LA EVALUACION', '9999', NOW()),
('600101', '0200', 'OBSERVACIONES DE CONDUCTAS', '9999', NOW()),
('600101', '0300', 'RESULTADOS DE EVALUACION', '9999', NOW());

INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '0301', '600101', '0308','9999', NOW()),
(DEFAULT, '0302', '600101', '0309','9999', NOW()),
(DEFAULT, '0303', '600101', '0310','9999', NOW()),
(DEFAULT, '0304', '600101', '0311','9999', NOW()),
(DEFAULT, '0305', '600101', '0312','9999', NOW());

--CUESTIONARIO ESPIROMETRIA
INSERT INTO clinica.Examen VALUES 
('600102', 'M', 'CUESTIONARIO ESPIROMETRIA', 'A', '9999', NOW(), 'S', NULL, NULL, 'S');

INSERT INTO Medicina.Indicador VALUES 
('0313', 'B', '¿TUVO DESPRENDIMIENTO DE LA RETINA O UNA OPERACION (CIRUGIA) DE LOS OJOS, TORAX O ABDOMEN, EN LOS ULTIMOS 3 MESES?', '¿Tuvo desprendimiento de la retina o una operación (cirugía) de los ojos, tórax o abdomen, en los últimos 3 meses?', 'A', '9999', NOW(), NOW()),
('0314', 'B', '¿HA TENIDO ALGUN ATAQUE CARDIACO O INFARTO AL CORAZON EN LOS ULTIMOS 3 MESES?', '¿Ha tenido algún ataque cardíaco o infarto al corazón en los últimos 3 meses?', 'A', '9999', NOW(), NOW()),
('0315', 'B', '¿HA ESTADO HOSPITALIZADO (A) POR CUALQUIER OTRO PROBLEMA DEL CORAZON EN LOS ULTIMOS 3 MESES?', '¿Ha estado hospitalizado (a) por cualquier otro problema del corazón en los últimos 3 meses?', 'A', '9999', NOW(), NOW()),
('0316', 'B', '¿ESTA USANDO MEDICAMENTOS PARA LA TUBERCULOSIS, EN ESTE MOMENTO?', '¿Está usando medicamentos para la tuberculosis, en este momento?', 'A', '9999', NOW(), NOW()),
('0317', 'B', 'EN CASO DE SER MUJER: ¿ESTA USTED EMBARAZADA ACTUALMENTE?', 'En caso de ser mujer: ¿Esta usted embarazada actualmente?', 'A', '9999', NOW(), NOW()),
('0318', 'B', 'HEMOPTISIS', 'HEMOPTISIS', 'A', '9999', NOW(), NOW()),
('0319', 'B', 'PNEUMOTORAX', 'PNEUMOTORAX', 'A', '9999', NOW(), NOW()),
('0320', 'B', 'TRAQUEOSTOMIA', 'TRAQUEOSTOMIA', 'A', '9999', NOW(), NOW()),
('0321', 'B', 'SONDA PLEURAL', 'SONDA PLEURAL', 'A', '9999', NOW(), NOW()),
('0322', 'B', 'ANEURISMAS CEREBRAL, ABDOMEN, TORAX', 'ANEURISMAS CEREBRAL, ABDOMEN, TORAX', 'A', '9999', NOW(), NOW()),
('0323', 'B', 'EMBOLIA PULMONAR', 'EMBOLIA PULMONAR', 'A', '9999', NOW(), NOW()),
('0324', 'B', 'INFARTO RECIENTE', 'INFARTO RECIENTE', 'A', '9999', NOW(), NOW()),
('0325', 'B', 'INESTABILIDAD CV', 'INESTABILIDAD CV', 'A', '9999', NOW(), NOW()),
('0326', 'B', 'FIEBRE,NAUSEA, VOMITO', 'FIEBRE,NAUSEA, VOMITO', 'A', '9999', NOW(), NOW()),
('0327', 'B', 'EMBARAZO AVANZADO', 'EMBARAZO AVANZADO', 'A', '9999', NOW(), NOW()),
('0328', 'B', 'EMBARAZO COMPLICADO', 'EMBARAZO COMPLICADO', 'A', '9999', NOW(), NOW()),
('0329', 'B', 'TUVO UNA INFECCION RESPIRATORIA (RESFRIADO), EN LAS ULTIMAS 3 SEMANAS?', 'Tuvo una infección respiratoria (resfriado), en las últimas 3 semanas?', 'A', '9999', NOW(), NOW()),
('0330', 'B', 'TUVO INFECCION EN EL OIDO EN LAS ULTIMAS 3 SEMANAS?', 'Tuvo infección en el oído en las ULTIMAS 3 SEMANAS?', 'A', '9999', NOW(), NOW()),
('0331', 'B', 'USO AEROSOLES (SPRAYS INHALADOS) O NEBULIZACIONES CON BRONCODILATADORES, EN LAS ULTIMAS 3 HORAS?', 'Uso aerosoles (sprays inhalados) o nebulizaciones con broncodilatadores, en las últimas 3 horas?', 'A', '9999', NOW(), NOW()),
('0332', 'B', '¿HA USADO ALGUN MEDICAMENTO BRONCODILATADOR TOMA EN LAS ULTIMAS 8 HORAS?', '¿Ha usado algún medicamento broncodilatador toma en las últimas 8 horas?', 'A', '9999', NOW(), NOW()),
('0333', 'B', '¿FUMO (CUALQUIER TIPO DE CIGARRO), EN LAS ULTIMAS DOS HORAS?', '¿Fumó (cualquier tipo de cigarro), en las últimas dos horas?', 'A', '9999', NOW(), NOW()),
('0334', 'I', 'CANTIDAD CIGARROS DOS HORAS', 'Cantidad cigarros dos horas', 'A', '9999', NOW(), NOW()),
('0335', 'B', '¿REALIZO ALGUN EJERCICIO FISICO FUERTE (COMO GIMNASIA, CAMINATA O TROTAR), EN LA ULTIMA HORA?', '¿Realizó algún ejercicio físico fuerte (como gimnasia, caminata o trotar), en la última hora?', 'A', '9999', NOW(), NOW()),
('0336', 'B', '¿COMIO EN LA ULTIMA HORA?', '¿Comió en la última hora?', 'A', '9999', NOW(), NOW());

INSERT INTO Medicina.Subtitulos VALUES
('600102', '0200', 'PARA SER LLENADO POR EL PROFESIONAL QUE REALIZA LA PRUEBA', '9999', NOW()),
('600102', '0300', 'PREGUNTAS PARA TODOS LOS ENTREVISTADOS QUE NO TIENEN LOS CRITERIOS DE EXCLUSION Y QUE POR LO TANTO DEBEN HACER LA ESPIROMETRIA.', '9999', NOW());

INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '0101', '600102', '0313','9999', NOW()),
(DEFAULT, '0102', '600102', '0314','9999', NOW()),
(DEFAULT, '0103', '600102', '0315','9999', NOW()),
(DEFAULT, '0104', '600102', '0316','9999', NOW()),
(DEFAULT, '0105', '600102', '0317','9999', NOW()),
(DEFAULT, '0201', '600102', '0318','9999', NOW()),
(DEFAULT, '0202', '600102', '0319','9999', NOW()),
(DEFAULT, '0203', '600102', '0320','9999', NOW()),
(DEFAULT, '0204', '600102', '0321','9999', NOW()),
(DEFAULT, '0205', '600102', '0322','9999', NOW()),
(DEFAULT, '0206', '600102', '0323','9999', NOW()),
(DEFAULT, '0207', '600102', '0324','9999', NOW()),
(DEFAULT, '0208', '600102', '0325','9999', NOW()),
(DEFAULT, '0209', '600102', '0326','9999', NOW()),
(DEFAULT, '0210', '600102', '0327','9999', NOW()),
(DEFAULT, '0211', '600102', '0328','9999', NOW()),
(DEFAULT, '0301', '600102', '0329','9999', NOW()),
(DEFAULT, '0302', '600102', '0330','9999', NOW()),
(DEFAULT, '0303', '600102', '0331','9999', NOW()),
(DEFAULT, '0304', '600102', '0332','9999', NOW()),
(DEFAULT, '0305', '600102', '0333','9999', NOW()),
(DEFAULT, '0306', '600102', '0334','9999', NOW()),
(DEFAULT, '0307', '600102', '0335','9999', NOW()),
(DEFAULT, '0308', '600102', '0336','9999', NOW());

-- ALTURA 1.8
INSERT INTO clinica.Examen VALUES 
('600202', 'M', 'ALTURA 1.8', 'A', '9999', NOW(), 'S', NULL, NULL, 'S');

INSERT INTO Medicina.Indicador VALUES
('0337', 'B', 'ACROFOBIA', 'Acrofobia', 'A', '0000', NOW(), NOW()),
('0338', 'B', 'AGORAFOBIA', 'Agorafobia', 'A', '0000', NOW(), NOW()),
('0339', 'B', 'CONSUMO DE ALCOHOL', 'Consumo de alcohol', 'A', '0000', NOW(), NOW()),
('0340', 'B', 'CONSUMO DE DROGAS', 'Consumo de drogas', 'A', '0000', NOW(), NOW()),
('0341', 'B', 'CONSUMO DE MEDICAMENTOS', 'Consumo de Medicamentos', 'A', '0000', NOW(), NOW()),
('0342', 'B', 'ENFERMEDAD PSIQUIATRICA', 'Enfermedad Psiquiatrica', 'A', '0000', NOW(), NOW()),
('0343', 'B', 'ANTECEDENTES DE TEC', 'Antecedentes TEC`', 'A', '0000', NOW(), NOW()),
('0344', 'B', 'CONVULCIONES Y EPILEPSIA', 'Convulciones y Epilepsia', 'A', '0000', NOW(), NOW()),
('0345', 'B', 'VERTIGOS', 'Vertigos', 'A', '0000', NOW(), NOW()),
('0346', 'B', 'MAREOS', 'Mareos', 'A', '0000', NOW(), NOW()),
('0347', 'B', 'SINCOPE', 'Sincope', 'A', '0000', NOW(), NOW()),
('0348', 'B', 'MIOCLONIAS', 'Mioclonias', 'A', '0000', NOW(), NOW()),
('0349', 'B', 'ACATISIA', 'Acatisia', 'A', '0000', NOW(), NOW()),
('0350', 'B', 'CEFALEAS / MIGRANA', 'Cefaleas / Migraña', 'A', '0000', NOW(), NOW()),
('0351', 'B', 'DIABETES NO CONTROLADA', 'Diabetes no controlada', 'A', '0000', NOW(), NOW()),
('0352', 'B', 'INSUFICIENCIA CARDIACA', 'Insuficiencia cardiaca', 'A', '0000', NOW(), NOW()),
('0353', 'B', 'HIPERTENSION ARTERIAL NO CONTROLADA', 'Hipertension arterial no controlada', 'A', '0000', NOW(), NOW()),
('0354', 'B', 'ARRITMIAS', 'Arritmias', 'A', '0000', NOW(), NOW()),
('0355', 'B', 'OTRAS ALTERACIONES CARDIOVASCULARES', 'Otras alteraciones cardiovasculares', 'A', '0000', NOW(), NOW()),
('0356', 'B', 'AMETROPIA DE LEJOS', 'Ametropia de lejos', 'A', '0000', NOW(), NOW()),
('0357', 'B', 'ESTEREOPSIA ALTERADA', 'Estereopsia alterada', 'A', '0000', NOW(), NOW()),
('0358', 'B', 'ASMA BRONQUIAL NO CONTROLADO', 'Asma bronquial no controlado', 'A', '0000', NOW(), NOW()),
('0359', 'B', 'PATRON  OBSTRUCTIVO MODERADO O SEVERO', 'Patron obstructivo moderado o severo', 'A', '0000', NOW(), NOW()),
('0360', 'B', 'HIPOACUSIA SEVERA', 'Hipoacusia severa', 'A', '0000', NOW(), NOW()),
('0361', 'B', 'RECIBIO ENTRENAMIENTO PARA TRABAJOS EN ALTURA', 'Recibio entrenamiento para trabajos en altura', 'A', '0000', NOW(), NOW()),
('0362', 'B', 'CLAUSTROFOBIA', 'Claustrofobia', 'A', '0000', NOW(), NOW()),
('0363', 'B', 'ANTECEDENTES DE ACCIDENTES DE TRABAJO', 'Antecedentes de accidentes de trabajo', 'A', '0000', NOW(), NOW()),
('0364', 'B', 'ALERGIAS', 'Alergias', 'A', '0000', NOW(), NOW()),
('0365', 'B', 'TIMPANOS', 'Timpanos', 'A', '0000', NOW(), NOW()),
('0366', 'B', 'AUDICION(2M)', 'Audicon (escucha a 2 metros)', 'A', '0000', NOW(), NOW()),
('0367', 'B', 'SUSTENTACION EN UN PIE POR 15', 'Sustentacion en un pie por 15', 'A', '0000', NOW(), NOW()),
('0368', 'B', 'CAMINAR LIBRE SOBRE RECTA (3M SIN DESVIO)', 'Caminar libre sobre recta (3m sin desvio)', 'A', '0000', NOW(), NOW()),
('0369', 'B', 'CAMINAR LIBRE OJOS VENDADOS (3M SIN DESVIO)', 'Caminar libre ojos vendados (3m sin desvio)', 'A', '0000', NOW(), NOW()),
('0370', 'B', 'CAMINAR LIBRE OJOS VENDADOS PUNTA TALON (3M SIN DESVIO)', 'Caminar libre ojos vendados punta talon (3m sin desvio)', 'A', '0000', NOW(), NOW()),
('0371', 'B', 'LIMITACION EN FUERZA O MOVILIDAD DE EXTREMIDADES', 'Limitacion en fuerza o movilidad de extremidades', 'A', '0000', NOW(), NOW()),
('0372', 'B', 'DIADOCOQUINESIA DIRECTA', 'Diadocoquinesia directa', 'A', '0000', NOW(), NOW()),
('0373', 'B', 'DIADOCOQUINESIA CRUZADA', 'Diadocoquinesia cruzada', 'A', '0000', NOW(), NOW()),
('0374', 'B', 'NISTAGMUS', 'Nistagmus', 'A', '0000', NOW(), NOW());

INSERT INTO Medicina.Subtitulos VALUES
('600202', '0100', 'ANTECEDENTES', '9999', NOW()),
('600202', '0200', 'EXAMEN MEDICO DIRIGIDO', '9999', NOW());

INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '0101', '600202', '0337', '0000', NOW()),
(DEFAULT, '0102', '600202', '0338', '0000', NOW()),
(DEFAULT, '0103', '600202', '0339', '0000', NOW()),
(DEFAULT, '0104', '600202', '0340', '0000', NOW()),
(DEFAULT, '0105', '600202', '0341', '0000', NOW()),
(DEFAULT, '0106', '600202', '0342', '0000', NOW()),
(DEFAULT, '0107', '600202', '0343', '0000', NOW()),
(DEFAULT, '0108', '600202', '0344', '0000', NOW()),
(DEFAULT, '0109', '600202', '0345', '0000', NOW()),
(DEFAULT, '0110', '600202', '0346', '0000', NOW()),
(DEFAULT, '0111', '600202', '0347', '0000', NOW()),
(DEFAULT, '0112', '600202', '0348', '0000', NOW()),
(DEFAULT, '0113', '600202', '0349', '0000', NOW()),
(DEFAULT, '0114', '600202', '0350', '0000', NOW()),
(DEFAULT, '0115', '600202', '0351', '0000', NOW()),
(DEFAULT, '0116', '600202', '0352', '0000', NOW()),
(DEFAULT, '0117', '600202', '0353', '0000', NOW()),
(DEFAULT, '0118', '600202', '0354', '0000', NOW()),
(DEFAULT, '0119', '600202', '0355', '0000', NOW()),
(DEFAULT, '0120', '600202', '0356', '0000', NOW()),
(DEFAULT, '0121', '600202', '0357', '0000', NOW()),
(DEFAULT, '0122', '600202', '0358', '0000', NOW()),
(DEFAULT, '0123', '600202', '0359', '0000', NOW()),
(DEFAULT, '0124', '600202', '0360', '0000', NOW()),
(DEFAULT, '0125', '600202', '0361', '0000', NOW()),
(DEFAULT, '0126', '600202', '0362', '0000', NOW()),
(DEFAULT, '0127', '600202', '0363', '0000', NOW()),
(DEFAULT, '0128', '600202', '0364', '0000', NOW()),
(DEFAULT, '0201', '600202', '0365', '0000', NOW()),
(DEFAULT, '0202', '600202', '0366', '0000', NOW()),
(DEFAULT, '0203', '600202', '0367', '0000', NOW()),
(DEFAULT, '0204', '600202', '0368', '0000', NOW()),
(DEFAULT, '0205', '600202', '0369', '0000', NOW()),
(DEFAULT, '0206', '600202', '0370', '0000', NOW()),
(DEFAULT, '0207', '600202', '0371', '0000', NOW()),
(DEFAULT, '0208', '600202', '0372', '0000', NOW()),
(DEFAULT, '0209', '600202', '0373', '0000', NOW()),
(DEFAULT, '0210', '600202', '0374', '0000', NOW());

--SCREENING DERMATOLOGICO
INSERT INTO clinica.Examen VALUES 
('600203', 'M', 'FICHA DE SCREENING DERMATOLOGICO', 'A', '9999', NOW(), 'S', NULL, NULL, 'S');

INSERT INTO Medicina.Indicador VALUES
('0375', 'I', 'CUERPO DE FRENTE', 'Cuerpo de frente', 'A', '0000', NOW(), NOW()),
('0376', 'I', 'CUERPO DETRÁS', 'Cuerpo detrás', 'A', '0000', NOW(), NOW()),
('0377', 'I', 'ROSTRO', 'Rostro', 'A', '0000', NOW(), NOW()),
('0378', 'I', 'MANOS', 'Manos', 'A', '0000', NOW(), NOW()),
('0379', 'I', 'PIES', 'Pies', 'A', '0000', NOW(), NOW()),
('0380', 'S', 'TIPO DE PIEL', 'Tipo de piel', 'A', '0000', NOW(), NOW()),
('0381', 'I', 'TAMAÑO', 'Tamaño', 'A', '0000', NOW(), NOW()),
('0382', 'I', 'ASPECTO', 'Aspecto', 'A', '0000', NOW(), NOW()),
('0383', 'I', 'PATRÓN DE DISTRIBUCIÓN', 'Patrón de distribución', 'A', '0000', NOW(), NOW()),
('0384', 'I', 'MORFOLOGÍA (LINEAL, PLANA, DIFUSA, OTRAS)', 'Morfología (lineal, plana, difusa, otras)', 'A', '0000', NOW(), NOW()),
('0385', 'B', 'EXISTEN SIGNOS DE RASCADO', 'Existen signos de rascado', 'A', '0000', NOW(), NOW()),
('0386', 'B', 'EXISTEN LESIONES EN AREA FOTOEXPUESTA', 'Existen lesiones en area fotoexpuesta', 'A', '0000', NOW(), NOW()),
('0387', 'B', 'EXISTEN LESIONES A DISTANCIA', 'Existen lesiones a distancia', 'A', '0000', NOW(), NOW()),
('0388', 'I', 'PALPACIÓN GANGLIONAR', 'Palpación ganglionar', 'A', '0000', NOW(), NOW()),
('0389', 'I', 'AUSCULTACIÓN PULMONAR', 'Auscultación pulmonar', 'A', '0000', NOW(), NOW()),
('0390', 'B', 'ALTERACIÓN DEL SNC', 'Alteración del SNC', 'A', '0000', NOW(), NOW()),
('0391', 'B', 'ALTERACIÓN GASTROINTESTINAL', 'Alteración gastrointestinal', 'A', '0000', NOW(), NOW());

INSERT INTO Medicina.Subtitulos VALUES
('600203', '0100', 'LOCALIZACION DE LESIONES', '9999', NOW()),
('600203', '0200', 'TIPOS DE PIEL', '9999', NOW()),
('600203', '0300', 'CARACTERISTICAS DE LAS LESIONES', '9999', NOW());

INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '0101', '600203', '0375', '0000', NOW()),
(DEFAULT, '0102', '600203', '0376', '0000', NOW()),
(DEFAULT, '0103', '600203', '0377', '0000', NOW()),
(DEFAULT, '0104', '600203', '0378', '0000', NOW()),
(DEFAULT, '0105', '600203', '0379', '0000', NOW()),
(DEFAULT, '0201', '600203', '0380', '0000', NOW()),
(DEFAULT, '0301', '600203', '0381', '0000', NOW()),
(DEFAULT, '0302', '600203', '0382', '0000', NOW()),
(DEFAULT, '0303', '600203', '0383', '0000', NOW()),
(DEFAULT, '0304', '600203', '0384', '0000', NOW()),
(DEFAULT, '0305', '600203', '0385', '0000', NOW()),
(DEFAULT, '0306', '600203', '0386', '0000', NOW()),
(DEFAULT, '0307', '600203', '0387', '0000', NOW()),
(DEFAULT, '0308', '600203', '0388', '0000', NOW()),
(DEFAULT, '0309', '600203', '0389', '0000', NOW()),
(DEFAULT, '0310', '600203', '0390', '0000', NOW()),
(DEFAULT, '0311', '600203', '0391', '0000', NOW());

--CUESTIONARIO DE SOMNOLENCIA
INSERT INTO clinica.Examen VALUES 
('600204', 'M', 'CUESTIONARIO DE SOMNOLENCIA DIURNA DE EPWORTH', 'A', '9999', NOW(), 'S', NULL, NULL, 'S');

INSERT INTO Medicina.Indicador VALUES
('0392', 'S', 'SENTADO Y LEYENDO', 'Sentado y leyendo', 'A', '0000', NOW(), NOW()),
('0393', 'S', 'VIENDO LA TV', 'Viendo la TV', 'A', '0000', NOW(), NOW()),
('0394', 'S', 'SENTADO, INACTIVO EN UN LUGAR PÚBLICO (EJ: CINE, TEATRO, CONFERENCIA, ETC.)', 'Sentado, inactivo en un lugar público (ej: cine, teatro, conferencia, etc.)', 'A', '0000', NOW(), NOW()),
('0395', 'S', 'COMO PASAJERO DE UN COCHE EN UN VIAJE DE 1 HORA SIN PARADAS', 'Como pasajero de un coche en un viaje de 1 hora sin paradas', 'A', '0000', NOW(), NOW()),
('0396', 'S', 'ESTIRADO PARA DESCANSAR AL MEDIODÍA CUANDO LAS CIRCUNSTANCIAS LO PERMITEN', 'Estirado para descansar al mediodía cuando las circunstancias lo permiten', 'A', '0000', NOW(), NOW()),
('0397', 'S', 'SENTADO Y HABLANDO CON OTRA PERSONA', 'Sentado y hablando con otra persona', 'A', '0000', NOW(), NOW()),
('0398', 'S', 'SENTADO TRANQUILAMENTE DESPUÉS DE UNA COMIDA SIN ALCOHOL', 'Sentado tranquilamente después de una comida sin alcohol', 'A', '0000', NOW(), NOW()),
('0399', 'S', 'EN UN COCHE, ESTANDO PARADO POR EL TRANSITO UNOS MINUTOS (EJ: SEMÁFORO, RETENCIÓN,..)', 'En un coche, estando parado por el transito unos minutos (ej: semáforo, retención,..)', 'A', '0000', NOW(), NOW());

--INSERT INTO Medicina.Subtitulos VALUES

INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '0101', '600204', '0392', '0000', NOW()),
(DEFAULT, '0102', '600204', '0393', '0000', NOW()),
(DEFAULT, '0103', '600204', '0394', '0000', NOW()),
(DEFAULT, '0104', '600204', '0395', '0000', NOW()),
(DEFAULT, '0105', '600204', '0396', '0000', NOW()),
(DEFAULT, '0106', '600204', '0397', '0000', NOW()),
(DEFAULT, '0107', '600204', '0398', '0000', NOW()),
(DEFAULT, '0108', '600204', '0399', '0000', NOW());

-- ANEXO A16A
INSERT INTO clinica.Examen VALUES 
('600200', 'M', 'ANEXO 16-A', 'A', '9999', NOW(), 'S', NULL, NULL, 'S');

INSERT INTO Medicina.Indicador VALUES
('0400', 'B', 'CIRUGIA MAYOR RECIENTE', 'Cirugia mayor reciente', 'A', '0000', NOW(), NOW()),
('0401', 'B', 'DESORDENES DE LA COAGULACION, TROMBOSIS, OTROS', 'Desordenes de la coagulacion, trombosis, otros', 'A', '0000', NOW(), NOW()),
('0402', 'B', 'DIABETES MELLITUS', 'Diabetes mellitus', 'A', '0000', NOW(), NOW()),
('0403', 'B', 'HIPERTENSION ARTERIAL', 'Hipertension arterial', 'A', '0000', NOW(), NOW()),
('0404', 'B', 'EMBARAZO', 'Embarazo', 'A', '0000', NOW(), NOW()),
('0405', 'B', 'PROBLEMAS NEUROLOGICOS', 'Problemas neurologicos: epilepsia, vertigos, otros', 'A', '0000', NOW(), NOW()),
('0406', 'B', 'INFECCIONES RECIENTES (DE MODERADAS A SEVERAS)', 'Infecciones recientes (de moderadas a severas)', 'A', '0000', NOW(), NOW()),
('0407', 'B', 'OBESIDAD', 'Obesidad', 'A', '0000', NOW(), NOW()),
('0408', 'B', 'PROBLEMAS CARDIACOS', 'Problemas cardiacos: marcapasos, coronariopatia, otros', 'A', '0000', NOW(), NOW()),
('0409', 'B', 'PROBLEMAS RESPIRATORIOS', 'Problemas respiratorios: asma, EPOC, otros', 'A', '0000', NOW(), NOW()),
('0410', 'B', 'PROBLEMAS OFTALMOLOGICOS', 'Problemas oftalmologicos: retinopatia, glaucoma, otros', 'A', '0000', NOW(), NOW()),
('0411', 'B', 'PROBLEMAS DIGESTIVOS', 'Problemas digestivos: sangrado digestivo, hepatitis, cirrosis hepatica, otros', 'A', '0000', NOW(), NOW()),
('0412', 'B', 'APNEA DEL SUEÑO', 'Apnea del sueño', 'A', '0000', NOW(), NOW()),
('0413', 'B', 'ALERGIAS', 'Alergias', 'A', '0000', NOW(), NOW()),
('0414', 'B', 'OTRA CONDICION MEDICA IMPORTANTE', 'Otra condicion medica importante', 'A', '0000', NOW(), NOW()),
('0415', 'I', 'USO DE MEDICACION ACTUAL', 'Uso de medicacion actual', 'A', '0000', NOW(), NOW());

INSERT INTO Medicina.Subtitulos VALUES
('600200', '0100', 'FUNCIONES VITALES', '9999', NOW()),
('600200', '0200', 'El/La señor(a)/(ita) ha presentado en los ultimos 6 meses:', '9999', NOW());

INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '0201', '600200', '0400', '0000', NOW()),
(DEFAULT, '0202', '600200', '0401', '0000', NOW()),
(DEFAULT, '0203', '600200', '0402', '0000', NOW()),
(DEFAULT, '0204', '600200', '0403', '0000', NOW()),
(DEFAULT, '0205', '600200', '0404', '0000', NOW()),
(DEFAULT, '0206', '600200', '0405', '0000', NOW()),
(DEFAULT, '0207', '600200', '0406', '0000', NOW()),
(DEFAULT, '0208', '600200', '0407', '0000', NOW()),
(DEFAULT, '0209', '600200', '0408', '0000', NOW()),
(DEFAULT, '0210', '600200', '0409', '0000', NOW()),
(DEFAULT, '0211', '600200', '0410', '0000', NOW()),
(DEFAULT, '0212', '600200', '0411', '0000', NOW()),
(DEFAULT, '0213', '600200', '0412', '0000', NOW()),
(DEFAULT, '0214', '600200', '0413', '0000', NOW()),
(DEFAULT, '0215', '600200', '0414', '0000', NOW()),
(DEFAULT, '0216', '600200', '0415', '0000', NOW());











-- ANEXO 16
INSERT INTO clinica.Examen VALUES 
('600201', 'M', 'ANEXO 16', 'A', '9999', NOW(), 'S', NULL, NULL, 'S')

INSERT INTO Medicina.Indicador VALUES
('0059', 'I', 'ANTECEDENTES', 'Antecedentes', 'A', '0000', NOW(), NOW()),
('0060', 'I', 'INMUNIZACIONES', 'Inmunizaciones', 'A', '0000', NOW(), NOW()),
('0061', 'I', 'HIJOS VIVOS', 'Vivos', 'A', '0000', NOW(), NOW()),
('0062', 'I', 'HIJOS MUERTOS', 'Muertos', 'A', '0000', NOW(), NOW()),
('0063', 'I', 'FVC', 'FVC', 'A', '0000', NOW(), NOW()),
('0064', 'I', 'FVE1', 'FVE1', 'A', '0000', NOW(), NOW()),
('0065', 'I', 'FVE1/FVC', 'FVE1/FVC', 'A', '0000', NOW(), NOW()),
('0066', 'I', 'FEF 25-75%', 'FEF 25-75%', 'A', '0000', NOW(), NOW()),
('0067', 'I', 'CONCLUSION DE FUNCIONES RESPIRATORIAS', 'Conclusion', 'A', '0000', NOW(), NOW()),
('0068', 'I', 'CABEZA', 'Cabeza', 'A', '0000', NOW(), NOW()),
('0069', 'I', 'CUELLO', 'Cuello', 'A', '0000', NOW(), NOW()),
('0070', 'I', 'NARIZ', 'Nariz', 'A', '0000', NOW(), NOW()),
('0071', 'I', 'BOCA, AMIGDALAS, FARINGE, LARINGE', 'Boca, Amigdalas, Faringe, Laringe', 'A', '0000', NOW(), NOW()),
('0072', 'I', 'BOCA PIEZAS EN MAL ESTADO', 'Piezas en mal estado', 'A', '0000', NOW(), NOW()),
('0073', 'I', 'BOCA PIEZAS QUE FALTAN', 'Piezas que faltan', 'A', '0000', NOW(), NOW()),
('0074', 'I', 'OJOS VISION DE LEJOS SIN CORREGIR OJO DERECHO', 'OD', 'A', '0000', NOW(), NOW()),
('0075', 'I', 'OJOS VISION DE LEJOS SIN CORREGIR OJO IZQUIERDO', 'OI', 'A', '0000', NOW(), NOW()),
('0076', 'I', 'OJOS VISION DE LEJOS CORREGIDA OJO DERECHO', 'OD', 'A', '0000', NOW(), NOW()),
('0077', 'I', 'OJOS VISION DE LEJOS CORREGIDA OJO DERECHO', 'OD', 'A', '0000', NOW(), NOW()),
('0078', 'I', 'OJOS VISION DE CERCA SIN CORREGIR OJO DERECHO', 'OD', 'A', '0000', NOW(), NOW()),
('0079', 'I', 'OJOS VISION DE CERCA SIN CORREGIR OJO IZQUIERDO', 'OI', 'A', '0000', NOW(), NOW()),
('0080', 'I', 'OJOS VISION DE CERCA CORREGIDA OJO DERECHO', 'OD', 'A', '0000', NOW(), NOW()),
('0081', 'I', 'OJOS VISION DE CERCA CORREGIDA OJO DERECHO', 'OD', 'A', '0000', NOW(), NOW()),
('0082', 'I', 'VISION DE COLORES', 'Vision de colores', 'A', '0000', NOW(), NOW()),
('0083', 'I', 'ENFERMEDADES OCULARES', 'Enfermedades Oculares', 'A', '0000', NOW(), NOW()),
('0084', 'I', 'REFLEJOS PUPILARES', 'Reflejos Pupilares', 'A', '0000', NOW(), NOW()),
('0085', 'I', 'OIDO DERECHO', 'Audicion derecho 500', 'A', '0000', NOW(), NOW()),
('0086', 'I', 'OIDO DERECHO', 'Audicion derecho 1000', 'A', '0000', NOW(), NOW()),
('0087', 'I', 'OIDO DERECHO', 'Audicion derecho 2000', 'A', '0000', NOW(), NOW()),
('0088', 'I', 'OIDO DERECHO', 'Audicion derecho 3000', 'A', '0000', NOW(), NOW()),
('0089', 'I', 'OIDO DERECHO', 'Audicion derecho 4000', 'A', '0000', NOW(), NOW()),
('0090', 'I', 'OIDO DERECHO', 'Audicion derecho 6000', 'A', '0000', NOW(), NOW()),
('0091', 'I', 'OIDO DERECHO', 'Audicion derecho 8000', 'A', '0000', NOW(), NOW()),
('0092', 'I', 'OIDO IZQUIERDO', 'Audicion izquierda 500', 'A', '0000', NOW(), NOW()),
('0093', 'I', 'OIDO IZQUIERDO', 'Audicion izquierda 1000', 'A', '0000', NOW(), NOW()),
('0094', 'I', 'OIDO IZQUIERDO', 'Audicion izquierda 2000', 'A', '0000', NOW(), NOW()),
('0095', 'I', 'OIDO IZQUIERDO', 'Audicion izquierda 3000', 'A', '0000', NOW(), NOW()),
('0096', 'I', 'OIDO IZQUIERDO', 'Audicion izquierda 4000', 'A', '0000', NOW(), NOW()),
('0097', 'I', 'OIDO IZQUIERDO', 'Audicion izquierda 6000', 'A', '0000', NOW(), NOW()),
('0098', 'I', 'OIDO IZQUIERDO', 'Audicion izquierda 8000', 'A', '0000', NOW(), NOW()),
('0099', 'I', 'OTOSCOPIA IZQUIERDO', 'OD', 'A', '0000', NOW(), NOW()),
('0100', 'I', 'OTOSCOPIA DERECHO', 'OI', 'A', '0000', NOW(), NOW()),
('0101', 'S', 'PULMONES', 'Pulmones', 'A', '0000', NOW(), NOW()),
('0102', 'I', 'PULMONES DESCRIPCION', 'Descripcion', 'A', '0000', NOW(), NOW()),
('0103', 'I', 'TORAX', 'Torax', 'A', '0000', NOW(), NOW()),
('0104', 'I', 'CORAZON', 'Corazon', 'A', '0000', NOW(), NOW()),
('0105', 'I', 'MIEMBROS SUPERIORES', 'Miembros Superiores', 'A', '0000', NOW(), NOW()),
('0106', 'I', 'MIEMBROS INFERIORES', 'Miembros Inferiores', 'A', '0000', NOW(), NOW()),
('0107', 'I', 'REFLEJOS OSTEO-TENDINOSOS', 'Reflejos Osteo-tendinosos', 'A', '0000', NOW(), NOW()),
('0108', 'I', 'MARCHA', 'Marcha', 'A', '0000', NOW(), NOW()),
('0109', 'I', 'COLUMNA VERTEBRAL', 'Columna Vertebral', 'A', '0000', NOW(), NOW()),
('0110', 'I', 'ABDOMEN', 'Abdomen', 'A', '0000', NOW(), NOW()),
('0111', 'S', 'TACTO RECTAL', 'Tacto Rectal', 'A', '0000', NOW(), NOW()),
('0112', 'I', 'TACTO RECTAL DESCRIPCION', 'Descripcion', 'A', '0000', NOW(), NOW()),
('0113', 'S', 'ANILLOS INGUINALES', 'Anillos Inguinales', 'A', '0000', NOW(), NOW()),
('0114', 'S', 'HERNIAS', 'Hernias', 'A', '0000', NOW(), NOW()),
('0115', 'S', 'ORGANOS GENITALES', 'Organos Genitales', 'A', '0000', NOW(), NOW()),
('0116', 'S', 'GANGLIOS', 'Ganglios', 'A', '0000', NOW(), NOW()),
('0117', 'S', 'LENGUAJE , ATENCION, MEMORIA, ORIENTACION, INTELIGENCIA, AFECTIVIDAD', 'Lenguaje, Atencion, Memoria, Orientacion, Inteligencia, Afectividad', 'A', '0000', NOW(), NOW()),--??
('0118', 'S', 'VARICES', 'Varices', 'A', '0000', NOW(), NOW()),


INSERT INTO Medicina.DetallePlantilla VALUES
(DEFAULT, '0101', '600201', '0056', '0000', NOW()),
(DEFAULT, '0102', '600201', '0059', '0000', NOW()),
(DEFAULT, '0103', '600201', '0060', '0000', NOW()),
(DEFAULT, '0201', '600201', '0061', '0000', NOW()),
(DEFAULT, '0202', '600201', '0062', '0000', NOW()),
(DEFAULT, '0301', '600201', '0063','9999', NOW()),
(DEFAULT, '0302', '600201', '0064','9999', NOW()),
(DEFAULT, '0303', '600201', '0065','9999', NOW()),
(DEFAULT, '0401', '600201', '0066','9999', NOW()),
(DEFAULT, '0402', '600201', '0067','9999', NOW()),
(DEFAULT, '0403', '600201', '0068','9999', NOW()),
(DEFAULT, '0404', '600201', '0069','9999', NOW()),
(DEFAULT, '0405', '600201', '0070','9999', NOW()),
(DEFAULT, '0501', '600201', '0071','9999', NOW()),
(DEFAULT, '0601', '600201', '0072','9999', NOW()),
(DEFAULT, '0701', '600201', '0073','9999', NOW()),
(DEFAULT, '0801', '600201', '0074','9999', NOW()),
(DEFAULT, '0802', '600201', '0075','9999', NOW()),
(DEFAULT, '0803', '600201', '0076','9999', NOW()),
(DEFAULT, '0901', '600201', '0077','9999', NOW()),
(DEFAULT, '0902', '600201', '0078','9999', NOW()),
(DEFAULT, '0903', '600201', '0079','9999', NOW()),
(DEFAULT, '0904', '600201', '0080','9999', NOW()),
(DEFAULT, '0905', '600201', '0081','9999', NOW()),
(DEFAULT, '0906', '600201', '0082','9999', NOW()),
(DEFAULT, '0907', '600201', '0083','9999', NOW()),
(DEFAULT, '0908', '600201', '0084','9999', NOW()),
(DEFAULT, '1008', '600201', '0085','9999', NOW()),
(DEFAULT, '1101', '600201', '0086','9999', NOW()),
(DEFAULT, '1201', '600201', '0087','9999', NOW()),
(DEFAULT, '1301', '600201', '0088','9999', NOW()),
(DEFAULT, '1302', '600201', '0089','9999', NOW()),
(DEFAULT, '1303', '600201', '0090','9999', NOW()),
(DEFAULT, '1304', '600201', '0091','9999', NOW()),
(DEFAULT, '1305', '600201', '0092','9999', NOW()),
(DEFAULT, '1306', '600201', '0093','9999', NOW()),
(DEFAULT, '1307', '600201', '0094','9999', NOW()),
(DEFAULT, '1308', '600201', '0095','9999', NOW()),
(DEFAULT, '1309', '600201', '0096','9999', NOW()),
(DEFAULT, '1310', '600201', '0097','9999', NOW()),
(DEFAULT, '1311', '600201', '0098','9999', NOW()),
(DEFAULT, '1312', '600201', '0099','9999', NOW()),
(DEFAULT, '1313', '600201', '0100','9999', NOW()),
(DEFAULT, '1314', '600201', '0101','9999', NOW()),
(DEFAULT, '1401', '600201', '0102','9999', NOW()),
(DEFAULT, '1402', '600201', '0103','9999', NOW()),
(DEFAULT, '1501', '600201', '0104','9999', NOW()),
(DEFAULT, '1502', '600201', '0105','9999', NOW()),
(DEFAULT, '1601', '600201', '0106','9999', NOW()),
(DEFAULT, '1701', '600201', '0107','9999', NOW()),
(DEFAULT, '1801', '600201', '0108','9999', NOW()),
(DEFAULT, '1901', '600201', '0109','9999', NOW()),
(DEFAULT, '2001', '600201', '0110','9999', NOW()),
(DEFAULT, '2101', '600201', '0111','9999', NOW()),
(DEFAULT, '2201', '600201', '0112','9999', NOW()),
(DEFAULT, '2301', '600201', '0113','9999', NOW()),
(DEFAULT, '2401', '600201', '0114','9999', NOW()),
(DEFAULT, '2402', '600201', '0115','9999', NOW()),
(DEFAULT, '2501', '600201', '0116','9999', NOW()),
(DEFAULT, '2601', '600201', '0117','9999', NOW()),
(DEFAULT, '2701', '600201', '0118','9999', NOW()),

INSERT INTO Medicina.Subtitulos VALUES
('600201', '0200', 'NUMERO DE HIJOS', '9999', NOW()),
('600201', '0300', 'HABITOS', '9999', NOW()),
('600201', '0400', 'FUNCION RESPIRATORIA', '9999', NOW()),
('600201', '0800', 'BOCA', '9999', NOW()),
('600201', '1300', 'OIDO', '9999', NOW()),
('600201', '1400', 'OTOSCOPIA', '9999', NOW()),
('600201', '1500', 'PULMONES', '9999', NOW()),
('600201', '1800', 'MIEMBROS', '9999', NOW()),
('600201', '2400', 'TACTO RECTAL', '9999', NOW()),



INSERT INTO Medicina.Indicador VALUES
('0156', 'B', 'TUBERCULOSIS TBC', 'TBC', 'A', '0000', NOW(), NOW()),
('0157', 'B', 'HEPATITIS B', 'Hepatitis B', 'A', '0000', NOW(), NOW()),
('0158', 'B', 'H COL', 'H. Col', 'A', '0000', NOW(), NOW()),
('0159', 'B', 'H COL', 'Pt. Columna', 'A', '0000', NOW(), NOW()),
('0160', 'B', 'QX', 'Qx', 'A', '0000', NOW(), NOW()),
('0161', 'B', 'ASMA', 'Asma', 'A', '0000', NOW(), NOW()),
('0162', 'B', 'HTA', 'HTA', 'A', '0000', NOW(), NOW()),
('0163', 'B', 'ITS', 'ITS', 'A', '0000', NOW(), NOW()),
('0164', 'B', 'TIFOIDEA', 'Tifoidea', 'A', '0000', NOW(), NOW()),
('0165', 'B', 'PROB CV', 'Prob CV', 'A', '0000', NOW(), NOW()),
('0166', 'B', 'HBP', 'HBP', 'A', '0000', NOW(), NOW()),
('0167', 'B', 'BRONQUITIS', 'Bronquitis', 'A', '0000', NOW(), NOW()),
('0168', 'B', 'NEOPLASIA', 'Neoplasia', 'A', '0000', NOW(), NOW()),
('0169', 'B', 'CONVULCIONES', 'Convulciones', 'A', '0000', NOW(), NOW()),
('0170', 'B', 'H. TG', 'H.tg', 'A', '0000', NOW(), NOW()),
('0171', 'B', 'ARTROPATIA', 'Artropatia', 'A', '0000', NOW(), NOW()),
('0172', 'B', 'MIGRAÑA', 'Migraña', 'A', '0000', NOW(), NOW()),
('0173', 'I', 'OTROS', 'Otros', 'A', '0000', NOW(), NOW()),
('0174', 'I', 'QUEMADURAS', 'Quemaduras', 'A', '0000', NOW(), NOW()),
('0175', 'I', 'CIRUGIAS', 'Cirugias', 'A', '0000', NOW(), NOW()),
('0176', 'I', 'INTOXICACIONES', 'Intoxicaciones', 'A', '0000', NOW(), NOW()),
('0177', 'I', 'ALCOHOL TIPO', 'Alcohol tipo', 'A', '0000', NOW(), NOW()),
('0178', 'I', 'ALCOHOL CANTIDAD', 'Alcohol cantidad', 'A', '0000', NOW(), NOW()),
('0179', 'I', 'ALCOHOL FRECUENCIA', 'Alcohol frecuencia', 'A', '0000', NOW(), NOW()),
('0180', 'I', 'TABACO TIPO', 'Tabaco tipo', 'A', '0000', NOW(), NOW()),
('0181', 'I', 'TABACO CANTIDAD', 'Tabaco cantidad', 'A', '0000', NOW(), NOW()),
('0182', 'I', 'TABACO FRECUENCIA', 'Tabaco frecuencia', 'A', '0000', NOW(), NOW()),
('0183', 'I', 'DROGAS TIPO', 'Drogas tipo', 'A', '0000', NOW(), NOW()),
('0184', 'I', 'DROGAS CANTIDAD', 'Drogas cantidad', 'A', '0000', NOW(), NOW()),
('0185', 'I', 'DROGAS FRECUENCIA', 'Drogas frecuencia', 'A', '0000', NOW(), NOW()),
('0186', 'I', 'MEDICAMENTOS TIPO', 'Medicamentos tipo', 'A', '0000', NOW(), NOW()),
('0187', 'I', 'MEDICAMENTOS CANTIDAD', 'Medicamentos cantidad', 'A', '0000', NOW(), NOW()),
('0188', 'I', 'MEDICAMENTOS FRECUENCIA', 'Medicamentos frecuencia', 'A', '0000', NOW(), NOW()),




CREATE TABLE rx.Indicador (
   cCodInd   CHARACTER(4)    NOT NULL PRIMARY KEY,
   c_TipReg  CHARACTER(1)    NOT NULL, 
   cDescri   VARCHAR(300)    NOT NULL,
   cImprim   VARCHAR(300)    NOT NULL,
   c_Estado  CHARACTER(1)    NOT NULL,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tGenera   TIMESTAMP       NOT NULL DEFAULT NOW(),
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);
CREATE TABLE rx.DetallePlantilla(
   nSerial    SERIAL         NOT NULL UNIQUE,
   cLisEnl   VARCHAR(6)      NOT NULL,
   _cCodExa   CHARACTER(6)   NOT NULL REFERENCES Clinica.Examen (cCodExa) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cCodInd  CHARACTER(4)    NOT NULL REFERENCES rx.Indicador (cCodInd) ON DELETE RESTRICT ON UPDATE CASCADE,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);

CREATE TABLE rx.Subtitulos(
   _cCodExa   CHARACTER(6)   NOT NULL REFERENCES Clinica.Examen (cCodExa) ON DELETE RESTRICT ON UPDATE CASCADE,
   cLisEnl   VARCHAR(6)      NOT NULL,
   cDescri  VARCHAR(200) NOT NULL,
   _cUsuCod  CHARACTER(4)    NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi   TIMESTAMP       NOT NULL DEFAULT NOW()
);

INSERT INTO rx.Indicador VALUES 
('0000', 'I', 'SIN INDICADOR', 'SIN INDICADOR', 'A', '9999', NOW(), NOW()),
('0001', 'S', 'CALIDAD DE LA RADIOGRAFIA', 'Calidad Radiografica', 'A', '9999', NOW(), NOW()),
('0002', 'S', 'CAUSA', 'Causa', 'A', '9999', NOW(), NOW()),
('0003', 'I', 'COMENTARIOS SOBRE DEFECTOS TECNICOS', 'Comentarios defectos tecnicos', 'A', '9999', NOW(), NOW()),
('0004', 'B', 'ZONAS AFECTADAS SUPERIOR DERECHA', 'Zonas afectadas Superior derecha', 'A', '9999', NOW(), NOW()),
('0005', 'B', 'ZONAS AFECTADAS SUPERIOR IZQUIERDA', 'Zonas afectadas Superior izquierda', 'A', '9999', NOW(), NOW()),
('0006', 'B', 'ZONAS AFECTADAS MEDIA DERECHA', 'Zonas afectadas Media derecha', 'A', '9999', NOW(), NOW()),
('0007', 'B', 'ZONAS AFECTADAS MEDIA IZQUIERDA', 'Zonas afectadas Media izquierda', 'A', '9999', NOW(), NOW()),
('0008', 'B', 'ZONAS AFECTADAS INFERIOR DERECHA', 'Zonas afectadas Inferior derecha', 'A', '9999', NOW(), NOW()),
('0009', 'B', 'ZONAS AFECTADAS INFERIOR IZQUIERDA', 'Zonas afectadas Inferior izquierda', 'A', '9999', NOW(), NOW()),
('0010', 'S', 'PROFUSION OPASIDADES PEQUEÑAS, ESCALA DE 12 PUNTOS', ' Profusión (opacidades pequeñas ) (escala de 12 puntos) (consulte las riográfias estandar - marque la subcategoria de profusión', 'A', '9999', NOW(), NOW()),
('0011', 'S', 'FORMA Y TAMAÑO PRIMARIA', 'Primaria', 'A', '9999', NOW(), NOW()),
('0012', 'S', 'FORMA Y TAMAÑO SECUNDARIA', 'Secundaria', 'A', '9999', NOW(), NOW()),
('0013', 'S', 'OPACIDADES GRANDES', 'Opacidades Grandes', 'A', '9999', NOW(), NOW()),
('0014', 'B', 'ANORMALIDADES PLEURALES', 'Anormalidades pleurales', 'A', '9999', NOW(), NOW()),
('0015', 'S', 'PARED TORACICA DE PERFIL', 'Pared toracica de perfil', 'A', '9999', NOW(), NOW()),
('0016', 'S', 'DE FRENTE', 'De frente', 'A', '9999', NOW(), NOW()),
('0017', 'S', 'DIAFRAGMA', 'Diafragma', 'A', '9999', NOW(), NOW()),
('0018', 'S', 'OTROS SITIOS', 'Otro(s) sitio(s)', 'A', '9999', NOW(), NOW()),
('0019', 'S', 'CALCIFICACION PARED TORACICA DE PERFIL', 'PAred toracica de perfil', 'A', '9999', NOW(), NOW()),
('0020', 'S', 'CALCIFICACION DE FRENTE', 'De frente', 'A', '9999', NOW(), NOW()),
('0021', 'S', 'CALCIFICACION DIAFRAGMA', 'Diafragma', 'A', '9999', NOW(), NOW()),
('0022', 'S', 'CALCIFICACION OTROS SITIOS', 'Otro(s) sitio(s)', 'A', '9999', NOW(), NOW()),
('0023', 'S', 'EXTENSION PARED TORACICA COMBINADA PARA LAS PLACAS DE PERFIL Y DE FRENTE DERECHO', 'Derecho', 'A', '9999', NOW(), NOW()),
('0024', 'S', 'EXTENSION PARED TORACICA COMBINADA PARA LAS PLACAS DE PERFIL Y DE FRENTE IZQUIERDO', 'Izquierdo', 'A', '9999', NOW(), NOW()),
('0025', 'S', 'ANCHO 3MM DERECHO', 'Derecho', 'A', '9999', NOW(), NOW()),
('0026', 'S', 'ANCHO 3MM IZQUIERDO', 'Izquierdo', 'A', '9999', NOW(), NOW()),
('0027', 'S', 'OBLITERACION DEL ANGULO COSTOFRENICO', 'Obliteracion del angulo costofrenico', 'A', '9999', NOW(), NOW()),
('0028', 'S', 'PARED TORACICA DE PERFIL', 'De perfil', 'A', '9999', NOW(), NOW()),
('0029', 'S', 'PARED TORACICA DE FRENTE', 'De frente', 'A', '9999', NOW(), NOW()),
('0030', 'S', 'CALCIFICACION DE PERFIL', 'De perfil', 'A', '9999', NOW(), NOW()),
('0031', 'S', 'CALCIFICACION DE FRENTE', 'De frente', 'A', '9999', NOW(), NOW()),
('0032', 'S', 'EXTENSION DERECHO', 'Derecho', 'A', '9999', NOW(), NOW()),
('0033', 'S', 'EXTENSION IZQUIERDO', 'Izquierdo', 'A', '9999', NOW(), NOW()),
('0034', 'S', 'ANCHO DERECHO', 'Derecho', 'A', '9999', NOW(), NOW()),
('0035', 'S', 'ANCHO IZQUIERDO', 'Izquierdo', 'A', '9999', NOW(), NOW()),
('0036', 'B', 'SIMBOLOS', 'Simbolos', 'A', '9999', NOW(), NOW()),
('0037', 'B', 'SIMBOLOS AA', 'aa', 'A', '9999', NOW(), NOW()),
('0038', 'B', 'SIMBOLOS AT', 'at', 'A', '9999', NOW(), NOW()),
('0039', 'B', 'SIMBOLOS AX', 'ax', 'A', '9999', NOW(), NOW()),
('0040', 'B', 'SIMBOLOS BU', 'bu', 'A', '9999', NOW(), NOW()),
('0041', 'B', 'SIMBOLOS CA', 'ca', 'A', '9999', NOW(), NOW()),
('0042', 'B', 'SIMBOLOS CG', 'cg', 'A', '9999', NOW(), NOW()),
('0043', 'B', 'SIMBOLOS CN', 'cn', 'A', '9999', NOW(), NOW()),
('0044', 'B', 'SIMBOLOS CO', 'co', 'A', '9999', NOW(), NOW()),
('0045', 'B', 'SIMBOLOS CP', 'cp', 'A', '9999', NOW(), NOW()),
('0046', 'B', 'SIMBOLOS CV', 'cv', 'A', '9999', NOW(), NOW()),
('0047', 'B', 'SIMBOLOS DI', 'di', 'A', '9999', NOW(), NOW()),
('0048', 'B', 'SIMBOLOS EF', 'ef', 'A', '9999', NOW(), NOW()),
('0049', 'B', 'SIMBOLOS EM', 'em', 'A', '9999', NOW(), NOW()),
('0050', 'B', 'SIMBOLOS ES', 'es', 'A', '9999', NOW(), NOW()),
('0051', 'B', 'SIMBOLOS FR', 'fr', 'A', '9999', NOW(), NOW()),
('0052', 'B', 'SIMBOLOS HI', 'hi', 'A', '9999', NOW(), NOW()),
('0053', 'B', 'SIMBOLOS HO', 'ho', 'A', '9999', NOW(), NOW()),
('0054', 'B', 'SIMBOLOS ID', 'id', 'A', '9999', NOW(), NOW()),
('0055', 'B', 'SIMBOLOS IH', 'ih', 'A', '9999', NOW(), NOW()),
('0056', 'B', 'SIMBOLOS KL', 'kl', 'A', '9999', NOW(), NOW()),
('0057', 'B', 'SIMBOLOS ME', 'me', 'A', '9999', NOW(), NOW()),
('0058', 'B', 'SIMBOLOS PA', 'pa', 'A', '9999', NOW(), NOW()),
('0059', 'B', 'SIMBOLOS PB', 'pb', 'A', '9999', NOW(), NOW()),
('0060', 'B', 'SIMBOLOS PI', 'pi', 'A', '9999', NOW(), NOW()),
('0061', 'B', 'SIMBOLOS PX', 'px', 'A', '9999', NOW(), NOW()),
('0062', 'B', 'SIMBOLOS RA', 'ra', 'A', '9999', NOW(), NOW()),
('0063', 'B', 'SIMBOLOS RP', 'rp', 'A', '9999', NOW(), NOW()),
('0064', 'B', 'SIMBOLOS TB', 'tb', 'A', '9999', NOW(), NOW()),
('0065', 'B', 'SIMBOLOS OD', 'od', 'A', '9999', NOW(), NOW()),

INSERT INTO rx.Subtitulos VALUES
('900200', '10000', 'DETALLE RADIOGRAFIA', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '10001', '900200', '0001', '0000', NOW()),
(DEFAULT, '10002', '900200', '0002', '0000', NOW()),
(DEFAULT, '10003', '900200', '0003', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '20000', 'ANORMALIDADES PARENQUIMATOSAS', '9999', NOW()),
('900200', '21000', 'ZONAS AFECTADAS', '9999', NOW()),
('900200', '21100', 'SUPERIOR', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '21101', '900200', '0004', '0000', NOW()),
(DEFAULT, '21102', '900200', '0005', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '21200', 'MEDIA', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '21201', '900200', '0006', '0000', NOW()),
(DEFAULT, '21202', '900200', '0007', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '21300', 'INFERIOR', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '21301', '900200', '0008', '0000', NOW()),
(DEFAULT, '21302', '900200', '0009', '0000', NOW()),
(DEFAULT, '22001', '900200', '0010', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '23000', 'FORMA Y TAMAÑO', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '23001', '900200', '0011', '0000', NOW()),
(DEFAULT, '23002', '900200', '0012', '0000', NOW()),
(DEFAULT, '24001', '900200', '0013', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '30000', 'ANORMALIDADES PLEURALES', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '30001', '900200', '0014', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '31000', 'SITIO', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '31001', '900200', '0015', '0000', NOW()),
(DEFAULT, '31002', '900200', '0016', '0000', NOW()),
(DEFAULT, '31003', '900200', '0017', '0000', NOW()),
(DEFAULT, '31004', '900200', '0018', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '32000', 'CALCIFICACION', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '32001', '900200', '0019', '0000', NOW()),
(DEFAULT, '32002', '900200', '0020', '0000', NOW()),
(DEFAULT, '32003', '900200', '0021', '0000', NOW()),
(DEFAULT, '32004', '900200', '0022', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '33000', 'EXTENSION', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '33001', '900200', '0023', '0000', NOW()),
(DEFAULT, '33002', '900200', '0024', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '34000', 'ANCHO', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '34001', '900200', '0025', '0000', NOW()),
(DEFAULT, '34002', '900200', '0026', '0000', NOW()),
(DEFAULT, '35001', '900200', '0027', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '40000', 'ENGROSAMIENTO DIFUSO DE PLEURA', '9999', NOW()),
('900200', '41000', 'PARED TORACICA', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '41001', '900200', '0028', '0000', NOW()),
(DEFAULT, '41002', '900200', '0029', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '42000', 'CALCIFICACION', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '42001', '900200', '0030', '0000', NOW()),
(DEFAULT, '42002', '900200', '0031', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '43000', 'EXTENSION', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '43001', '900200', '0032', '0000', NOW()),
(DEFAULT, '43002', '900200', '0033', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '44000', 'ANCHO', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '44001', '900200', '0034', '0000', NOW()),
(DEFAULT, '44002', '900200', '0035', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '50000', 'SIMBOLOS', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '50001', '900200', '0036', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '51000', 'RODEE CON UN CIRCULO', '9999', NOW());
INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '51001', '900200', '0037', '0000', NOW()),
(DEFAULT, '51001', '900200', '0038', '0000', NOW()),
(DEFAULT, '51001', '900200', '0039', '0000', NOW()),
(DEFAULT, '51001', '900200', '0040', '0000', NOW()),
(DEFAULT, '51001', '900200', '0041', '0000', NOW()),
(DEFAULT, '51001', '900200', '0042', '0000', NOW()),
(DEFAULT, '51001', '900200', '0043', '0000', NOW()),
(DEFAULT, '51001', '900200', '0044', '0000', NOW()),
(DEFAULT, '51001', '900200', '0045', '0000', NOW()),
(DEFAULT, '51001', '900200', '0046', '0000', NOW()),
(DEFAULT, '51001', '900200', '0047', '0000', NOW()),
(DEFAULT, '51001', '900200', '0048', '0000', NOW()),
(DEFAULT, '51001', '900200', '0049', '0000', NOW()),
(DEFAULT, '51001', '900200', '0050', '0000', NOW()),
(DEFAULT, '51001', '900200', '0051', '0000', NOW()),
(DEFAULT, '51001', '900200', '0052', '0000', NOW()),
(DEFAULT, '51001', '900200', '0053', '0000', NOW()),
(DEFAULT, '51001', '900200', '0054', '0000', NOW()),
(DEFAULT, '51001', '900200', '0055', '0000', NOW()),
(DEFAULT, '51001', '900200', '0056', '0000', NOW()),
(DEFAULT, '51001', '900200', '0057', '0000', NOW()),
(DEFAULT, '51001', '900200', '0058', '0000', NOW()),
(DEFAULT, '51001', '900200', '0059', '0000', NOW()),
(DEFAULT, '51001', '900200', '0060', '0000', NOW()),
(DEFAULT, '51001', '900200', '0061', '0000', NOW()),
(DEFAULT, '51001', '900200', '0062', '0000', NOW()),
(DEFAULT, '51001', '900200', '0063', '0000', NOW()),
(DEFAULT, '51001', '900200', '0064', '0000', NOW()),
(DEFAULT, '51001', '900200', '0065', '0000', NOW());
INSERT INTO rx.Subtitulos VALUES
('900200', '60000', 'COMENTARIOS', '9999', NOW());


INSERT INTO rx.DetallePlantilla VALUES
(DEFAULT, '22002', '900200', '0012', '0000', NOW()),
(DEFAULT, '22101', '900200', '0013', '0000', NOW()),
(DEFAULT, '30001', '900200', '0014', '0000', NOW()),
(DEFAULT, '31001', '900200', '0015', '0000', NOW()),
(DEFAULT, '31002', '900200', '0016', '0000', NOW()),
(DEFAULT, '31003', '900200', '0017', '0000', NOW()),
(DEFAULT, '31004', '900200', '0018', '0000', NOW()),


(DEFAULT, '0302', '900200', '0015', '0000', NOW()),
(DEFAULT, '0303', '900200', '0016', '0000', NOW()),
(DEFAULT, '0304', '900200', '0017', '0000', NOW()),
(DEFAULT, '0305', '900200', '0018', '0000', NOW()),
(DEFAULT, '0305', '900200', '0019', '0000', NOW()),
(DEFAULT, '0306', '900200', '0020', '0000', NOW()),
(DEFAULT, '0307', '900200', '0021', '0000', NOW()),
(DEFAULT, '0308', '900200', '0022', '0000', NOW()),
(DEFAULT, '0309', '900200', '0023', '0000', NOW()),
(DEFAULT, '0401', '900200', '0024', '0000', NOW()),
(DEFAULT, '0402', '900200', '0025', '0000', NOW()),
(DEFAULT, '0403', '900200', '0026', '0000', NOW()),
(DEFAULT, '0404', '900200', '0027', '0000', NOW()),
(DEFAULT, '0405', '900200', '0028', '0000', NOW()),
(DEFAULT, '0406', '900200', '0029', '0000', NOW()),
(DEFAULT, '0407', '900200', '0030', '0000', NOW()),
(DEFAULT, '0408', '900200', '0031', '0000', NOW()),
(DEFAULT, '0501', '900200', '0032', '0000', NOW()),
(DEFAULT, '0502', '900200', '0033', '0000', NOW()),
(DEFAULT, '0503', '900200', '0034', '0000', NOW()),
(DEFAULT, '0504', '900200', '0035', '0000', NOW()),
(DEFAULT, '0505', '900200', '0036', '0000', NOW()),
(DEFAULT, '0506', '900200', '0037', '0000', NOW()),
(DEFAULT, '0507', '900200', '0038', '0000', NOW()),
(DEFAULT, '0508', '900200', '0039', '0000', NOW()),
(DEFAULT, '0509', '900200', '0040', '0000', NOW()),
(DEFAULT, '0510', '900200', '0041', '0000', NOW()),
(DEFAULT, '0511', '900200', '0042', '0000', NOW()),
(DEFAULT, '0512', '900200', '0043', '0000', NOW()),
(DEFAULT, '0513', '900200', '0044', '0000', NOW()),
(DEFAULT, '0514', '900200', '0045', '0000', NOW()),
(DEFAULT, '0515', '900200', '0046', '0000', NOW()),
(DEFAULT, '0516', '900200', '0047', '0000', NOW()),
(DEFAULT, '0517', '900200', '0048', '0000', NOW()),
(DEFAULT, '0518', '900200', '0049', '0000', NOW()),
(DEFAULT, '0519', '900200', '0050', '0000', NOW()),
(DEFAULT, '0520', '900200', '0051', '0000', NOW()),
(DEFAULT, '0521', '900200', '0052', '0000', NOW()),
(DEFAULT, '0522', '900200', '0053', '0000', NOW()),
(DEFAULT, '0523', '900200', '0054', '0000', NOW()),
(DEFAULT, '0524', '900200', '0055', '0000', NOW()),
(DEFAULT, '0525', '900200', '0056', '0000', NOW()),
(DEFAULT, '0526', '900200', '0057', '0000', NOW()),
(DEFAULT, '0527', '900200', '0058', '0000', NOW()),
(DEFAULT, '0528', '900200', '0059', '0000', NOW()),
(DEFAULT, '0529', '900200', '0060', '0000', NOW()),
(DEFAULT, '0530', '900200', '0061', '0000', NOW());



-- ANTECEDENTES OCUPACIONALES
CREATE TABLE Clinica.AntecedentesOcupacionales (
   _cCodPer   CHARACTER(3) NOT NULL REFERENCES Clinica.Perfil (cCodPer) ON DELETE RESTRICT ON UPDATE CASCADE,
   cFecIni    DATE NOT NULL,
   cFecFin    DATE,
   cAltitu    SMALLINT,
   _cCodEmp   CHARACTER(X) NOT NULL REFERENCES Clinica.Empresa (cCodEmp) ON DELETE RESTRICT ON UPDATE CASCADE,
   cArea      VARCHAR(X),
   cOcupa     VARCHAR(X) NOT NULL,
   cSubTie    SMALLINT O NUMERIC(X, 2) NOT NULL,
   cSupTie    SMALLINT O NUMERIC(X, 2) NOT NULL,
   cRetiro    VARCHAR(X) NOT NULL,
   cEPP       VARCHAR(X),
   cRuidoH    NUMERIC(8, 2),
   cRuidoE    NUMERIC(5, 2),
   cPolvoH    NUMERIC(8, 2),
   cPolvoE    NUMERIC(5, 2),
   cErgoH     NUMERIC(8, 2),
   cErgoE     NUMERIC(5, 2),
   cVibraH    NUMERIC(8, 2),
   cVibraE    NUMERIC(5, 2),
   cElectH    NUMERIC(8, 2),
   cElectE    NUMERIC(5, 2),
   cQuimiH    NUMERIC(8, 2),
   cQuimiE    NUMERIC(5, 2),
   cOtrosH    NUMERIC(8, 2),
   cOtrosE    NUMERIC(5, 2),
   _cUsuCod   CHARACTER(4)    NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi    TIMESTAMP NOT NULL DEFAULT NOW()   
);

CREATE TABLE Clinica.Empresa (
   cCodEmp    CHARACTER(X) NOT NULL PRIMARY KEY,
   cDescri    VARCHAR(X) NOT NULL,
   cActivi    VARCHAR(X) NOT NULL,
   cDpto      VARCHAR(X) NOT NULL,
   cProvin    VARCHAR(X) NOT NULL,
   cDistri    VARCHAR(X) NOT NULL,
   _cUsuCod   CHARACTER(4) NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi    TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE Clinica.Absentismo (
   _cCodPer   CHARACTER(3) NOT NULL REFERENCES Clinica.Perfil (cCodPer) ON DELETE RESTRICT ON UPDATE CASCADE,
   cEnfAcc    VARCHAR(X) NOT NULL,
   cAsocia    CHARACTER(1) NOT NULL,
   cAnio      CHARACTER(4) NOT NULL,
   cDiasDe    SMALLINT NOT NULL DEFAULT 0,
   _cUsuCod   CHARACTER(4)    NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi    TIMESTAMP NOT NULL DEFAULT NOW()
);