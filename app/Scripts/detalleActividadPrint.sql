-- FUNCTION: Clinica.f_r110(character, character, integer)

-- DROP FUNCTION Clinica.f_r110(character, character, integer);

CREATE OR REPLACE FUNCTION Clinica.DetalleActividadPrint(p_ccodact character)
    RETURNS text
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
DECLARE
   R0              RECORD;
   R1              RECORD;
   R2              RECORD;
   i                 INTEGER := 0;
   j                 INTEGER := 0;
   k                INTEGER := 0;
   lnorden        INTEGER := -1;
   lFlag          BOOLEAN :=True;
   lcCodExa     CHARACTER(6)    := '';
   lfHTML     CHARACTER(1)    := '';
   lcCodInd    CHARACTER(4)    := '';
   lcImprim    VARCHAR(200)    := '';
   lcValPre      CHARACTER(1)  := '';
   lcDesUni    VARCHAR(100)    :='';
   lcResult      VARCHAR(800)    := '';
   lnOpcion      SMALLINT    := 0;
   lcCodTab    CHARACTER(4)    := '';
   lcDesTab    VARCHAR(200)    := '';
   ltmp     TEXT      :=''; 
   lmData     TEXT      :=''; 
   lmDatos     TEXT      :=''; 
   lmTabla      TEXT;
BEGIN
   FOR R0 IN
        SELECT _cCodExa FROM Clinica.PlantillaActividad WHERE _cCodAct = p_cCodAct LOOP
        lcCodExa := R0._cCodExa;
        FOR R1 IN
            (SELECT 'AAAA' AS cCodInd, cDescri AS cImprim, '' AS cValPre, '' AS cDesUni,'' AS fHTML, cLisEnl FROM Clinica.Subtitulos WHERE _cCodExa = lcCodExa)
            UNION ALL
            (SELECT B.cCodInd, B.cImprim, B.cValPre, C.cDescri AS cDesUni, B.c_TipReg AS fHTML,  A.cLisEnl  FROM Clinica.DetallePlantilla A
                INNER JOIN Clinica.Indicador B ON B.cCodInd = A._cCodInd 
                INNER JOIN Clinica.Unidad C ON C.cCodUni = B._cCodUni
            WHERE A._cCodExa = lcCodExa)
        ORDER BY cLisEnl LOOP
            lcCodInd := R1.cCodInd;
            IF lcCodInd = 'AAAA' THEN
                IF lFlag THEN
                    lnorden := lnorden+1;
                    lFlag :=False;
                END IF;
            ELSE
                lFlag :=True;
                lcImprim := R1.cImprim;
                lcValPre := R1.cValPre;
                lcDesUni := R1.cDesUni;
                lfHTML  := R1.fHTML;
                SELECT cResult, n_Opcion INTO lcResult, lnOpcion FROM Clinica.DetalleActividad WHERE _cCodAct = p_cCodAct AND _cCodInd = lcCodInd;
                IF NOT FOUND THEN
                    lcResult := lcValPre; 
                    lnOpcion := 0;
                END IF;
                IF lfHTML = 'S' THEN
                    k:= 0;
                    lmTabla :='';
                    FOR R2 IN SELECT nOrden, cDescri FROM Clinica.TablaTablas WHERE _cCodInd = lcCodInd AND c_Estado = 'A' ORDER BY nOrden LOOP
                        lcCodTab := R2.nOrden;
                        lcDesTab  := R2.cDescri;
                        IF k = 0 THEN
                            lmTabla := '[{"CCODIGO":"'||lcCodTab||'", "CDESCRI":"'||lcDesTab||'"}';
                        ELSE
                            lmTabla := lmTabla || ',{"CCODIGO":"'||lcCodTab||'", "CDESCRI":"'||lcDesTab||'"}';
                        END IF;
                        k := k+1;
                    END LOOP;
                    IF TRIM(lmTabla) = '' THEN
                        lmTabla := '[{"CCODIGO":0, "CDESCRI":"ALGO SALIO MAL"}';
                    END IF;
                    lmTabla := lmTabla || ']';
                ELSE
                    lmTabla := 'null';
                END IF;
                IF i = 0 THEN
                    lmDatos := '[{"NORDEN":'||lnorden||',"CCODIND":"'||lcCodInd||'","CIMPRIM":"'||lcImprim||'","CVALPRE":"'||lcValPre||'","CDESUNI":"'||lcDesUni||'","FHTML":"'||lfHTML||'","CRESULT":"'||lcResult||'","NOPCION":'||lnOpcion||',"MTABLA":'||lmTabla||'}';
                    i := i+1;
                ELSE
                    lmDatos := lmDatos || ',{"NORDEN":'||lnorden||',"CCODIND":"'||lcCodInd||'","CIMPRIM":"'||lcImprim||'","CVALPRE":"'||lcValPre||'","CDESUNI":"'||lcDesUni||'","FHTML":"'||lfHTML||'","CRESULT":"'||lcResult||'","NOPCION":'||lnOpcion||',"MTABLA":'||lmTabla||'}';
                END IF;
            END IF;
            RAISE NOTICE '%',lmDatos;
        END LOOP;
        IF j=0 THEN 
            lmData := '['||lmDatos||']';
            j:=1;
        ELSE
            lmData := lmData||','||lmDatos||']';
        END IF;
    END LOOP;
   RETURN '{"OK":1,"DATA":'|| lmData ||']}';
EXCEPTION WHEN OTHERS THEN
    RAISE INFO 'ERROR NAME: %', SQLERRM;
    RAISE INFO 'ERROR STATE: %', SQLSTATE;
    RETURN '{"OK":0,"DATA":"null"}';
END
$BODY$;