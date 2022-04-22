-- FUNCTION: medicina.f_r110(character, character, integer)

-- DROP FUNCTION medicina.f_r110(character, character, integer);

CREATE OR REPLACE FUNCTION Clinica.grabarDetalleActividad(p_cparam text)
    RETURNS text
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
DECLARE
   p_cFlagGrabar CHARACTER(1) NOT NULL := '';
   p_cCodAct CHARACTER(8) NOT NULL := '';
   p_cObserv  VARCHAR(1000) NOT NULL := '';
   p_cConclu VARCHAR(1000) NOT NULL := '';
   p_cRecom VARCHAR(1000) NOT NULL := '';
   p_cUsuCod CHARACTER(4) NOT NULL := '';
   p_cCodInd CHARACTER(4) NOT NULL := '';
   p_fHtml CHARACTER(1) NOT NULL := '';
   p_cResult  VARCHAR(800) NOT NULL := '';
   p_cCodCie VARCHAR(8) NOT NULL :='';
   lcCodpla CHARACTER(11) := '';
   lnOpcion  INTEGER                      :=0;
   loData     JSON;
   loDatos   JSON;
   loCie       JSON;
   loJson     JSON;
   p_mDatos    TEXT;
   p_mCie    TEXT;
   i         INTEGER                      :=1;
BEGIN
    BEGIN
        loData    := p_cParam::JSON;
    EXCEPTION WHEN OTHERS THEN
        RETURN '{"OK": 0,"DATA":"PARAMETRO DE ENTRADA NO ES JSON"}';
   END;
    BEGIN
        p_cFlagGrabar := TRIM(loData->>'CGRABAR')::CHARACTER(1);
        i := i+1;
        p_cCodAct := TRIM(loData->>'CCODACT');
        i := i+1;
        p_cObserv := TRIM(loData->>'COBSERV');
        i := i+1;
        p_cConclu := TRIM(loData->>'CCONCLU');
        i := i+1;
        p_cRecom := TRIM(loData->>'CRECOME');
        i := i+1;
        p_cUsuCod := TRIM(loData->>'CCODUSU');
        i := i+1;
        p_mDatos  := loData->>'MDATOS';
        i := i+1;
        loDatos   := p_mDatos::JSON;
        i := i+1;
        p_mCie  := loData->>'MCODCIE';
        i := i+1;
        loCie   := p_mCie::JSON;
    EXCEPTION WHEN OTHERS THEN
        RETURN '{"OK": 0,"DATA":"'||i||'-VARIABLES DE CABECERA ERRONEAS"}';
    END;
    IF NOT EXISTS (SELECT cCodAct FROM Clinica.Actividad WHERE cCodAct = p_cCodAct) THEN
      RETURN '{"OK": 0, "DATA":"ACTIVIDAD NO EXISTE"}';
    END IF;
    SELECT _cCodPla INTO lcCodPla FROM Clinica.Actividad WHERE cCodAct = p_cCodAct;
    IF p_cObserv != '' THEN
        UPDATE CLINICA.ExtraActividad SET c_Estado = 'I' WHERE _cCodAct = p_cCodAct AND c_Tipo = 'O';
        INSERT INTO CLINICA.ExtraActividad (_cCodAct, _cCodPla, cExtra, c_Tipo, _cUsuCod) VALUES
        (p_cCodAct, lcCodpla, p_cObserv, 'O', p_cUsuCod);
    END IF;
    IF p_cConclu != '' THEN
        UPDATE CLINICA.ExtraActividad SET c_Estado = 'I' WHERE _cCodAct = p_cCodAct AND c_Tipo = 'C';
        INSERT INTO CLINICA.ExtraActividad (_cCodAct, _cCodPla, cExtra, c_Tipo, _cUsuCod) VALUES
        (p_cCodAct, lcCodpla, p_cConclu, 'C', p_cUsuCod);
    END IF;
    IF p_cRecom != '' THEN
        UPDATE CLINICA.ExtraActividad SET c_Estado = 'I' WHERE _cCodAct = p_cCodAct AND c_Tipo = 'R';
        INSERT INTO CLINICA.ExtraActividad (_cCodAct, _cCodPla, cExtra, c_Tipo, _cUsuCod) VALUES
        (p_cCodAct, lcCodpla, p_cRecom, 'R', p_cUsuCod);
    END IF;
    FOR loJson IN SELECT json_array_elements(loDatos) LOOP
        BEGIN
            i := 1;
            p_cCodInd := loJson->>'CCODIND';
            i := i+1;
            p_fHtml := (loJson->>'FHTML')::CHARACTER(1);
            i := i+1;
            p_cResult := loJson->>'CRESULT';   
        EXCEPTION WHEN OTHERS THEN
            RETURN '{"OK": 0,"DATA":"'||i||'-VARIABLES DE DETALLE ERRONEAS"}';
        END;
        IF NOT EXISTS (SELECT cCodInd FROM Clinica.Indicador WHERE cCodInd = p_cCodInd) THEN
            RETURN '{"OK": 0, "DATA":"INDICADOR NO EXISTE"}';
        END IF;
        IF p_fHtml = 'S' THEN
            lnOpcion := p_cResult::INT;
            SELECT cDescri INTO p_cResult FROM Clinica.TablaTablas WHERE _cCodInd = p_cCodInd;
        ELSIF p_fHtml = 'B' AND p_cResult IN ('0','1') THEN
            lnOpcion := p_cResult::INT;
        ELSE
            lnOpcion := 0;
        END IF;
        IF EXISTS(SELECT cResult FROM Clinica.DetalleActividad WHERE _cCodInd = p_cCodInd AND _cCodAct = p_cCodAct) THEN
            UPDATE Clinica.DetalleActividad SET cResult = p_cResult, n_Opcion = lnOpcion, _cUsuCod = p_cUsuCod, tModifi = NOW() WHERE  _cCodInd = p_cCodInd AND _cCodAct = p_cCodAct;
        ELSE
            INSERT INTO Clinica.DetalleActividad(_cCodInd, n_Opcion, _cCodPla, _cCodAct, cResult, c_Estado, _cUsuCod, tModifi) VALUES
                                       (p_cCodInd, lnOpcion, lcCodPla, p_cCodAct, p_cResult, 'A', p_cUsuCod, NOW());
        END IF;
    END LOOP;
    DELETE FROM Clinica.Cie10Actividad WHERE _cCodAct = p_cCodAct;
    FOR loJson IN SELECT json_array_elements(loCie) LOOP
        BEGIN
            p_cCodCie := loJson->>'CCODIGO';   
        EXCEPTION WHEN OTHERS THEN
            RETURN '{"OK": 0,"DATA":"VARIABLES DE DETALLE CIE ERRONEAS"}';
        END;
        IF NOT EXISTS (SELECT cCodCie FROM Clinica.Cie10 WHERE cCodCie = p_cCodCie) THEN
            RETURN '{"OK": 0, "DATA":"CODIGO CIE NO EXISTE"}';
        END IF;
        INSERT INTO Clinica.Cie10Actividad(_cCodCie, _cCodPla, _cCodAct, _cUsuCod, tModifi) VALUES
                                    (p_cCodCie, lcCodPla, p_cCodAct, p_cUsuCod, NOW()); 
    END LOOP;
    RETURN '{"OK":1, "DATA":"OK"}';
EXCEPTION WHEN OTHERS THEN
    RAISE INFO 'ERROR NAME: %', SQLERRM;
    RAISE INFO 'ERROR STATE: %', SQLSTATE;
    RETURN '{"OK":0, "DATA":"FALLO EN EL PROCEDIMIENTO"}';
END
$BODY$;