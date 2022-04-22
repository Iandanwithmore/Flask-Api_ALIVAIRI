CREATE TABLE Medicina.TablaTablas (
   nSerial SERIAL         NOT NULL UNIQUE,
   _cCodInd CHARACTER(4)   NOT NULL REFERENCES Medicina.Indicador (cCodInd) ON DELETE RESTRICT ON UPDATE CASCADE,
   nOrden  SMALLINT       NOT NULL,
   cDescri  VARCHAR(100)  NOT NULL,
   c_Estado CHARACTER(1) NOT NULL DEFAULT 'A',
   _cUsuCod CHARACTER(4)  NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi TIMESTAMP      NOT NULL DEFAULT NOW()
);

-- AUDIOMETRIA
INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0010', 0, 'TAPONES', '0000', NOW()),
(DEFAULT, '0010', 1, 'OREJERAS', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0011', 0, 'DISMINUCION DE LA AUDICION', '0000', NOW()),
(DEFAULT, '0011', 1, 'ACUFENOS', '0000', NOW()),
(DEFAULT, '0011', 2, 'DOLOR DE OIDOS', '0000', NOW()),
(DEFAULT, '0011', 3, 'MAREOS', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0013', 0, 'NORMAL', '0000', NOW()),
(DEFAULT, '0013', 1, 'ALTERADO', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0015', 0, 'NORMAL', '0000', NOW()),
(DEFAULT, '0015', 1, 'ALTERADO', '0000', NOW());

--CUESTIONARIO DE SINTOMAS MUSCULO TENDINOSOS
INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0143', 0, 'I', '0000', NOW()),
(DEFAULT, '0143', 1, 'D', '0000', NOW()),
(DEFAULT, '0143', 2, 'AMBOS', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0147', 0, 'I', '0000', NOW()),
(DEFAULT, '0147', 1, 'D', '0000', NOW()),
(DEFAULT, '0147', 2, 'AMBOS', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0149', 0, 'I', '0000', NOW()),
(DEFAULT, '0149', 1, 'D', '0000', NOW()),
(DEFAULT, '0149', 2, 'AMBOS', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0151', 0, 'I', '0000', NOW()),
(DEFAULT, '0151', 1, 'D', '0000', NOW()),
(DEFAULT, '0151', 2, 'AMBOS', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0153', 0, 'I', '0000', NOW()),
(DEFAULT, '0153', 1, 'D', '0000', NOW()),
(DEFAULT, '0153', 2, 'AMBOS', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0155', 0, 'I', '0000', NOW()),
(DEFAULT, '0155', 1, 'D', '0000', NOW()),
(DEFAULT, '0155', 2, 'AMBOS', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0156', 0, '< a 1 año', '0000', NOW()),
(DEFAULT, '0156', 1, '1 - 5 años', '0000', NOW()),
(DEFAULT, '0156', 2, '6 - 10 años', '0000', NOW()),
(DEFAULT, '0156', 3, '> a 11 años', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0157', 0, '< a 1 año', '0000', NOW()),
(DEFAULT, '0157', 1, '1 - 5 años', '0000', NOW()),
(DEFAULT, '0157', 2, '6 - 10 años', '0000', NOW()),
(DEFAULT, '0157', 3, '> a 11 años', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0158', 0, '< a 1 año', '0000', NOW()),
(DEFAULT, '0158', 1, '1 - 5 años', '0000', NOW()),
(DEFAULT, '0158', 2, '6 - 10 años', '0000', NOW()),
(DEFAULT, '0158', 3, '> a 11 años', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0159', 0, '< a 1 año', '0000', NOW()),
(DEFAULT, '0159', 1, '1 - 5 años', '0000', NOW()),
(DEFAULT, '0159', 2, '6 - 10 años', '0000', NOW()),
(DEFAULT, '0159', 3, '> a 11 años', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0160', 0, '< a 1 año', '0000', NOW()),
(DEFAULT, '0160', 1, '1 - 5 años', '0000', NOW()),
(DEFAULT, '0160', 2, '6 - 10 años', '0000', NOW()),
(DEFAULT, '0160', 3, '> a 11 años', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0161', 0, '< a 1 año', '0000', NOW()),
(DEFAULT, '0161', 1, '1 - 5 años', '0000', NOW()),
(DEFAULT, '0161', 2, '6 - 10 años', '0000', NOW()),
(DEFAULT, '0161', 3, '> a 11 años', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0162', 0, '< a 1 año', '0000', NOW()),
(DEFAULT, '0162', 1, '1 - 5 años', '0000', NOW()),
(DEFAULT, '0162', 2, '6 - 10 años', '0000', NOW()),
(DEFAULT, '0162', 3, '> a 11 años', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0163', 0, '< a 1 año', '0000', NOW()),
(DEFAULT, '0163', 1, '1 - 5 años', '0000', NOW()),
(DEFAULT, '0163', 2, '6 - 10 años', '0000', NOW()),
(DEFAULT, '0163', 3, '> a 11 años', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0164', 0, '< a 1 año', '0000', NOW()),
(DEFAULT, '0164', 1, '1 - 5 años', '0000', NOW()),
(DEFAULT, '0164', 2, '6 - 10 años', '0000', NOW()),
(DEFAULT, '0164', 3, '> a 11 años', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0183', 0, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0183', 1, '8 - 30 días', '0000', NOW()),
(DEFAULT, '0183', 2, '> 30 días no seguidos', '0000', NOW()),
(DEFAULT, '0183', 3, 'siempre', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0184', 0, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0184', 1, '8 - 30 días', '0000', NOW()),
(DEFAULT, '0184', 2, '> 30 días no seguidos', '0000', NOW()),
(DEFAULT, '0184', 3, 'siempre', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0185', 0, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0185', 1, '8 - 30 días', '0000', NOW()),
(DEFAULT, '0185', 2, '> 30 días no seguidos', '0000', NOW()),
(DEFAULT, '0185', 3, 'siempre', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0186', 0, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0186', 1, '8 - 30 días', '0000', NOW()),
(DEFAULT, '0186', 2, '> 30 días no seguidos', '0000', NOW()),
(DEFAULT, '0186', 3, 'siempre', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0187', 0, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0187', 1, '8 - 30 días', '0000', NOW()),
(DEFAULT, '0187', 2, '> 30 días no seguidos', '0000', NOW()),
(DEFAULT, '0187', 3, 'siempre', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0188', 0, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0188', 1, '8 - 30 días', '0000', NOW()),
(DEFAULT, '0188', 2, '> 30 días no seguidos', '0000', NOW()),
(DEFAULT, '0188', 3, 'siempre', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0189', 0, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0189', 1, '8 - 30 días', '0000', NOW()),
(DEFAULT, '0189', 2, '> 30 días no seguidos', '0000', NOW()),
(DEFAULT, '0189', 3, 'siempre', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0190', 0, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0190', 1, '8 - 30 días', '0000', NOW()),
(DEFAULT, '0190', 2, '> 30 días no seguidos', '0000', NOW()),
(DEFAULT, '0190', 3, 'siempre', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0191', 0, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0191', 1, '8 - 30 días', '0000', NOW()),
(DEFAULT, '0191', 2, '> 30 días no seguidos', '0000', NOW()),
(DEFAULT, '0191', 3, 'siempre', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0192', 0, '< 1 hora', '0000', NOW()),
(DEFAULT, '0192', 1, '1 - 24 horas', '0000', NOW()),
(DEFAULT, '0192', 2, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0192', 3, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0192', 4, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0193', 0, '< 1 hora', '0000', NOW()),
(DEFAULT, '0193', 1, '1 - 24 horas', '0000', NOW()),
(DEFAULT, '0193', 2, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0193', 3, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0193', 4, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0194', 0, '< 1 hora', '0000', NOW()),
(DEFAULT, '0194', 1, '1 - 24 horas', '0000', NOW()),
(DEFAULT, '0194', 2, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0194', 3, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0194', 4, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0195', 0, '< 1 hora', '0000', NOW()),
(DEFAULT, '0195', 1, '1 - 24 horas', '0000', NOW()),
(DEFAULT, '0195', 2, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0195', 3, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0195', 4, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0196', 0, '< 1 hora', '0000', NOW()),
(DEFAULT, '0196', 1, '1 - 24 horas', '0000', NOW()),
(DEFAULT, '0196', 2, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0196', 3, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0196', 4, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0197', 0, '< 1 hora', '0000', NOW()),
(DEFAULT, '0197', 1, '1 - 24 horas', '0000', NOW()),
(DEFAULT, '0197', 2, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0197', 3, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0197', 4, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0198', 0, '< 1 hora', '0000', NOW()),
(DEFAULT, '0198', 1, '1 - 24 horas', '0000', NOW()),
(DEFAULT, '0198', 2, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0198', 3, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0198', 4, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0199', 0, '< 1 hora', '0000', NOW()),
(DEFAULT, '0199', 1, '1 - 24 horas', '0000', NOW()),
(DEFAULT, '0199', 2, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0199', 3, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0199', 4, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0200', 0, '< 1 hora', '0000', NOW()),
(DEFAULT, '0200', 1, '1 - 24 horas', '0000', NOW()),
(DEFAULT, '0200', 2, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0200', 3, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0200', 4, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0201', 0, '0 días', '0000', NOW()),
(DEFAULT, '0201', 1, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0201', 2, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0201', 3, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0202', 0, '0 días', '0000', NOW()),
(DEFAULT, '0202', 1, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0202', 2, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0202', 3, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0203', 0, '0 días', '0000', NOW()),
(DEFAULT, '0203', 1, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0203', 2, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0203', 3, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0204', 0, '0 días', '0000', NOW()),
(DEFAULT, '0204', 1, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0204', 2, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0204', 3, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0205', 0, '0 días', '0000', NOW()),
(DEFAULT, '0205', 1, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0205', 2, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0205', 3, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0206', 0, '0 días', '0000', NOW()),
(DEFAULT, '0206', 1, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0206', 2, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0206', 3, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0207', 0, '0 días', '0000', NOW()),
(DEFAULT, '0207', 1, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0207', 2, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0207', 3, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0208', 0, '0 días', '0000', NOW()),
(DEFAULT, '0208', 1, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0208', 2, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0208', 3, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0209', 0, '0 días', '0000', NOW()),
(DEFAULT, '0209', 1, '1 - 7 días', '0000', NOW()),
(DEFAULT, '0209', 2, '1 - 4 semanas', '0000', NOW()),
(DEFAULT, '0209', 3, '> 1 mes', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0228', 0, '1', '0000', NOW()),
(DEFAULT, '0228', 1, '2', '0000', NOW()),
(DEFAULT, '0228', 2, '3', '0000', NOW()),
(DEFAULT, '0228', 3, '4', '0000', NOW()),
(DEFAULT, '0228', 4, '5', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0229', 0, '1', '0000', NOW()),
(DEFAULT, '0229', 1, '2', '0000', NOW()),
(DEFAULT, '0229', 2, '3', '0000', NOW()),
(DEFAULT, '0229', 3, '4', '0000', NOW()),
(DEFAULT, '0229', 4, '5', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0230', 0, '1', '0000', NOW()),
(DEFAULT, '0230', 1, '2', '0000', NOW()),
(DEFAULT, '0230', 2, '3', '0000', NOW()),
(DEFAULT, '0230', 3, '4', '0000', NOW()),
(DEFAULT, '0230', 4, '5', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0231', 0, '1', '0000', NOW()),
(DEFAULT, '0231', 1, '2', '0000', NOW()),
(DEFAULT, '0231', 2, '3', '0000', NOW()),
(DEFAULT, '0231', 3, '4', '0000', NOW()),
(DEFAULT, '0231', 4, '5', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0232', 0, '1', '0000', NOW()),
(DEFAULT, '0232', 1, '2', '0000', NOW()),
(DEFAULT, '0232', 2, '3', '0000', NOW()),
(DEFAULT, '0232', 3, '4', '0000', NOW()),
(DEFAULT, '0232', 4, '5', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0233', 0, '1', '0000', NOW()),
(DEFAULT, '0233', 1, '2', '0000', NOW()),
(DEFAULT, '0233', 2, '3', '0000', NOW()),
(DEFAULT, '0233', 3, '4', '0000', NOW()),
(DEFAULT, '0233', 4, '5', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0234', 0, '1', '0000', NOW()),
(DEFAULT, '0234', 1, '2', '0000', NOW()),
(DEFAULT, '0234', 2, '3', '0000', NOW()),
(DEFAULT, '0234', 3, '4', '0000', NOW()),
(DEFAULT, '0234', 4, '5', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0235', 0, '1', '0000', NOW()),
(DEFAULT, '0235', 1, '2', '0000', NOW()),
(DEFAULT, '0235', 2, '3', '0000', NOW()),
(DEFAULT, '0235', 3, '4', '0000', NOW()),
(DEFAULT, '0235', 4, '5', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0236', 0, '1', '0000', NOW()),
(DEFAULT, '0236', 1, '2', '0000', NOW()),
(DEFAULT, '0236', 2, '3', '0000', NOW()),
(DEFAULT, '0236', 3, '4', '0000', NOW()),
(DEFAULT, '0236', 4, '5', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0237', 0, 'Trabajo', '0000', NOW()),
(DEFAULT, '0237', 1, 'Deportes', '0000', NOW()),
(DEFAULT, '0237', 2, 'Otros', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0239', 0, 'Trabajo', '0000', NOW()),
(DEFAULT, '0239', 1, 'Deportes', '0000', NOW()),
(DEFAULT, '0239', 2, 'Otros', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0241', 0, 'Trabajo', '0000', NOW()),
(DEFAULT, '0241', 1, 'Deportes', '0000', NOW()),
(DEFAULT, '0241', 2, 'Otros', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0243', 0, 'Trabajo', '0000', NOW()),
(DEFAULT, '0243', 1, 'Deportes', '0000', NOW()),
(DEFAULT, '0243', 2, 'Otros', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0245', 0, 'Trabajo', '0000', NOW()),
(DEFAULT, '0245', 1, 'Deportes', '0000', NOW()),
(DEFAULT, '0245', 2, 'Otros', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0247', 0, 'Trabajo', '0000', NOW()),
(DEFAULT, '0247', 1, 'Deportes', '0000', NOW()),
(DEFAULT, '0247', 2, 'Otros', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0249', 0, 'Trabajo', '0000', NOW()),
(DEFAULT, '0249', 1, 'Deportes', '0000', NOW()),
(DEFAULT, '0249', 2, 'Otros', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0251', 0, 'Trabajo', '0000', NOW()),
(DEFAULT, '0251', 1, 'Deportes', '0000', NOW()),
(DEFAULT, '0251', 2, 'Otros', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0253', 0, 'Trabajo', '0000', NOW()),
(DEFAULT, '0253', 1, 'Deportes', '0000', NOW()),
(DEFAULT, '0253', 2, 'Otros', '0000', NOW());

--PSICOLOGIA
--DELETE FROM Medicina.TablaTablas;
INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0274', 0, 'Adecuada', '0000', NOW()),
(DEFAULT, '0274', 1, 'Inadecuada', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0275', 0, 'Erguida', '0000', NOW()),
(DEFAULT, '0275', 1, 'Encorvada', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0276', 0, 'Lento', '0000', NOW()),
(DEFAULT, '0276', 1, 'Rapido', '0000', NOW()),
(DEFAULT, '0276', 2, 'Fluido', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0277', 0, 'Bajo', '0000', NOW()),
(DEFAULT, '0277', 1, 'Moderado', '0000', NOW()),
(DEFAULT, '0277', 2, 'Alto', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0278', 0, 'Con Dificultad', '0000', NOW()),
(DEFAULT, '0278', 1, 'Sin Dificultad', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0279', 0, 'Orientado', '0000', NOW()),
(DEFAULT, '0279', 1, 'Desorientado', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0280', 0, 'Orientado', '0000', NOW()),
(DEFAULT, '0280', 1, 'Desorientado', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0281', 0, 'Orientado', '0000', NOW()),
(DEFAULT, '0281', 1, 'Desorientado', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0301', 0, 'Corto', '0000', NOW()),
(DEFAULT, '0301', 1, 'Mediano', '0000', NOW()),
(DEFAULT, '0301', 2, 'Largo', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0302', 0, 'Muy superior', '0000', NOW()),
(DEFAULT, '0302', 1, 'Superior', '0000', NOW()),
(DEFAULT, '0302', 2, 'N. brillante', '0000', NOW()),
(DEFAULT, '0302', 3, 'N. promedio', '0000', NOW()),
(DEFAULT, '0302', 4, 'N. torpe', '0000', NOW()),
(DEFAULT, '0302', 5, 'Fronterizo', '0000', NOW()),
(DEFAULT, '0302', 6, 'RM. leve', '0000', NOW()),
(DEFAULT, '0302', 7, 'RM. moderado', '0000', NOW()),
(DEFAULT, '0302', 8, 'RM. severo', '0000', NOW()),
(DEFAULT, '0302', 9, 'RM. profundo', '0000', NOW());

--SCREENING DERMATOLOGICO
INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0380', 0, 'Siempre enrojece, nunca broncea', '0000', NOW()),
(DEFAULT, '0380', 1, 'Siempre enrojece, broncea poco', '0000', NOW()),
(DEFAULT, '0380', 2, 'Enrojece a veces, se pigmenta bien', '0000', NOW()),
(DEFAULT, '0380', 3, 'No enrojece, siempre se broncea', '0000', NOW()),
(DEFAULT, '0380', 4, 'Muy pigmentada', '0000', NOW()),
(DEFAULT, '0380', 5, 'Negro', '0000', NOW());

--CUESTIONARIO DE SOMNOLENCIA
INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0392', 0, 'Nunca tengo sueño', '0000', NOW()),
(DEFAULT, '0392', 1, 'Ligera probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0392', 2, 'Moderada probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0392', 3, 'Alta probabilidad de tener sueño', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0393', 0, 'Nunca tengo sueño', '0000', NOW()),
(DEFAULT, '0393', 1, 'Ligera probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0393', 2, 'Moderada probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0393', 3, 'Alta probabilidad de tener sueño', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0394', 0, 'Nunca tengo sueño', '0000', NOW()),
(DEFAULT, '0394', 1, 'Ligera probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0394', 2, 'Moderada probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0394', 3, 'Alta probabilidad de tener sueño', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0395', 0, 'Nunca tengo sueño', '0000', NOW()),
(DEFAULT, '0395', 1, 'Ligera probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0395', 2, 'Moderada probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0395', 3, 'Alta probabilidad de tener sueño', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0396', 0, 'Nunca tengo sueño', '0000', NOW()),
(DEFAULT, '0396', 1, 'Ligera probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0396', 2, 'Moderada probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0396', 3, 'Alta probabilidad de tener sueño', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0397', 0, 'Nunca tengo sueño', '0000', NOW()),
(DEFAULT, '0397', 1, 'Ligera probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0397', 2, 'Moderada probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0397', 3, 'Alta probabilidad de tener sueño', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0398', 0, 'Nunca tengo sueño', '0000', NOW()),
(DEFAULT, '0398', 1, 'Ligera probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0398', 2, 'Moderada probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0398', 3, 'Alta probabilidad de tener sueño', '0000', NOW());

INSERT INTO Medicina.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0399', 0, 'Nunca tengo sueño', '0000', NOW()),
(DEFAULT, '0399', 1, 'Ligera probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0399', 2, 'Moderada probabilidad de tener sueño', '0000', NOW()),
(DEFAULT, '0399', 3, 'Alta probabilidad de tener sueño', '0000', NOW());





CREATE TABLE rx.TablaTablas (
   nSerial SERIAL         NOT NULL UNIQUE,
   _cCodInd CHARACTER(4)   NOT NULL REFERENCES rx.Indicador (cCodInd) ON DELETE RESTRICT ON UPDATE CASCADE,
   nOrden  SMALLINT       NOT NULL,
   cDescri  VARCHAR(100)  NOT NULL,
   _cUsuCod CHARACTER(4)  NOT NULL REFERENCES Core.Usuario (cCodUsu) ON DELETE RESTRICT ON UPDATE CASCADE,
   tModifi TIMESTAMP      NOT NULL DEFAULT NOW(),
   c_Estado CHARACTER(1) NOT NULL DEFAULT 'A'
);

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0001', 0, 'BUENA', '0000', NOW()),
(DEFAULT, '0001', 1, 'ACEPTABLE', '0000', NOW()),
(DEFAULT, '0001', 2, 'BAJA CALIDAD', '0000', NOW()),
(DEFAULT, '0001', 3, 'INACEPTABLE', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0002', 0, 'SOBREEXPOSICION', '0000', NOW()),
(DEFAULT, '0002', 1, 'SUBEXPOSICION', '0000', NOW()),
(DEFAULT, '0002', 2, 'POSICION CENTRADO', '0000', NOW()),
(DEFAULT, '0002', 3, 'INSPIRACION INSUFICIENTE', '0000', NOW()),
(DEFAULT, '0002', 4, 'ESCAPULA', '0000', NOW()),
(DEFAULT, '0002', 5, 'ARTEFACTO', '0000', NOW()),
(DEFAULT, '0002', 6, 'OTROS', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0010', 0, '0/-', '0000', NOW()),
(DEFAULT, '0010', 1, '0/0', '0000', NOW()),
(DEFAULT, '0010', 2, '0/1', '0000', NOW()),
(DEFAULT, '0010', 3, '1/0', '0000', NOW()),
(DEFAULT, '0010', 4, '1/1', '0000', NOW()),
(DEFAULT, '0010', 5, '1/2', '0000', NOW()),
(DEFAULT, '0010', 6, '2/1', '0000', NOW()),
(DEFAULT, '0010', 7, '2/2', '0000', NOW()),
(DEFAULT, '0010', 8, '2/3', '0000', NOW()),
(DEFAULT, '0010',9, '3/2', '0000', NOW()),
(DEFAULT, '0010', 10, '3/3', '0000', NOW()),
(DEFAULT, '0010', 11, '3/+', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0011', 0, 'p', '0000', NOW()),
(DEFAULT, '0011', 1, 's', '0000', NOW()),
(DEFAULT, '0011', 2, 'q', '0000', NOW()),
(DEFAULT, '0011', 3, 't', '0000', NOW()),
(DEFAULT, '0011', 4, 'r', '0000', NOW()),
(DEFAULT, '0011', 5, 'u', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0002', 0, 'SOBREEXPOSICION', '0000', NOW()),
(DEFAULT, '0002', 1, 'SUBEXPOSICION', '0000', NOW()),
(DEFAULT, '0002', 2, 'POSICION CENTRADO', '0000', NOW()),
(DEFAULT, '0002', 3, 'INSPIRACION INSUFICIENTE', '0000', NOW()),
(DEFAULT, '0002', 4, 'ESCAPULA', '0000', NOW()),
(DEFAULT, '0002', 5, 'ARTEFACTO', '0000', NOW()),
(DEFAULT, '0002', 6, 'OTROS', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0010', 0, '0/-', '0000', NOW()),
(DEFAULT, '0010', 1, '0/0', '0000', NOW()),
(DEFAULT, '0010', 2, '0/1', '0000', NOW()),
(DEFAULT, '0010', 3, '1/0', '0000', NOW()),
(DEFAULT, '0010', 4, '1/1', '0000', NOW()),
(DEFAULT, '0010', 5, '1/2', '0000', NOW()),
(DEFAULT, '0010', 6, '2/1', '0000', NOW()),
(DEFAULT, '0010', 7, '2/2', '0000', NOW()),
(DEFAULT, '0010', 8, '2/3', '0000', NOW()),
(DEFAULT, '0010',9, '3/2', '0000', NOW()),
(DEFAULT, '0010', 10, '3/3', '0000', NOW()),
(DEFAULT, '0010', 11, '3/+', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0011', 0, 'p', '0000', NOW()),
(DEFAULT, '0011', 1, 's', '0000', NOW()),
(DEFAULT, '0011', 2, 'q', '0000', NOW()),
(DEFAULT, '0011', 3, 't', '0000', NOW()),
(DEFAULT, '0011', 4, 'r', '0000', NOW()),
(DEFAULT, '0011', 5, 'u', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0012',0, 'p', '0000', NOW()),
(DEFAULT, '0012',1, 's', '0000', NOW()),
(DEFAULT, '0012',2, 'q', '0000', NOW()),
(DEFAULT, '0012',3, 't', '0000', NOW()),
(DEFAULT, '0012',4, 'r', '0000', NOW()),
(DEFAULT, '0012',5, 'u', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0013',0, '0', '0000', NOW()),
(DEFAULT, '0013',1, 'A', '0000', NOW()),
(DEFAULT, '0013',2, 'B', '0000', NOW()),
(DEFAULT, '0013',3, 'C', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0015',0, '0', '0000', NOW()),
(DEFAULT, '0015',1, 'D', '0000', NOW()),
(DEFAULT, '0015',2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0016',0, '0', '0000', NOW()),
(DEFAULT, '0016',1, 'D', '0000', NOW()),
(DEFAULT, '0016',2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0017',0, '0', '0000', NOW()),
(DEFAULT, '0017',1, 'D', '0000', NOW()),
(DEFAULT, '0017',2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0018', 0, '0', '0000', NOW()),
(DEFAULT, '0018', 1, 'D', '0000', NOW()),
(DEFAULT, '0018', 2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0019',0, '0', '0000', NOW()),
(DEFAULT, '0019',1, 'D', '0000', NOW()),
(DEFAULT, '0019',2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0020',0, '0', '0000', NOW()),
(DEFAULT, '0020',1, 'D', '0000', NOW()),
(DEFAULT, '0020',2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0021',0, '0', '0000', NOW()),
(DEFAULT, '0021',1, 'D', '0000', NOW()),
(DEFAULT, '0021',2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0022',0, '0', '0000', NOW()),
(DEFAULT, '0022',1, 'D', '0000', NOW()),
(DEFAULT, '0022',2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0023',0, '0', '0000', NOW()),
(DEFAULT, '0023',1, '1', '0000', NOW()),
(DEFAULT, '0023',2, '2', '0000', NOW()),
(DEFAULT, '0023',3, '3', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0024',0, '0', '0000', NOW()),
(DEFAULT, '0024',1, '1', '0000', NOW()),
(DEFAULT, '0024',2, '2', '0000', NOW()),
(DEFAULT, '0024',3, '3', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0025',0, 'a', '0000', NOW()),
(DEFAULT, '0025',1, 'b', '0000', NOW()),
(DEFAULT, '0025',2, 'c', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0026',0, 'a', '0000', NOW()),
(DEFAULT, '0026',1, 'b', '0000', NOW()),
(DEFAULT, '0026',2, 'c', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0027',0, '0', '0000', NOW()),
(DEFAULT, '0027',1, 'D', '0000', NOW()),
(DEFAULT, '0027',2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0028',0, '0', '0000', NOW()),
(DEFAULT, '0028',1, 'D', '0000', NOW()),
(DEFAULT, '0028',2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0029',0, '0', '0000', NOW()),
(DEFAULT, '0029',1, 'D', '0000', NOW()),
(DEFAULT, '0029',2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0030',0, '0', '0000', NOW()),
(DEFAULT, '0030',1, 'D', '0000', NOW()),
(DEFAULT, '0030',2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0031',0, '0', '0000', NOW()),
(DEFAULT, '0031',1, 'D', '0000', NOW()),
(DEFAULT, '0031',2, 'I', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0032',0, '0', '0000', NOW()),
(DEFAULT, '0032',1, '1', '0000', NOW()),
(DEFAULT, '0032',2, '2', '0000', NOW()),
(DEFAULT, '0032',3, '3', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0033', 0, '0', '0000', NOW()),
(DEFAULT, '0033', 1, '1', '0000', NOW()),
(DEFAULT, '0033', 2, '2', '0000', NOW()),
(DEFAULT, '0033', 3, '3', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0034',0, 'a', '0000', NOW()),
(DEFAULT, '0034',1, 'b', '0000', NOW()),
(DEFAULT, '0034',2, 'c', '0000', NOW());

INSERT INTO rx.TablaTablas
(nSerial, _cCodInd, nOrden, cDescri, _cUsuCod, tModifi) VALUES
(DEFAULT, '0035',0, 'a', '0000', NOW()),
(DEFAULT, '0035',1, 'b', '0000', NOW()),
(DEFAULT, '0035',2, 'c', '0000', NOW());

