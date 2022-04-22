CREATE OR REPLACE FUNCTION Medicina.F_R111(p_cCodInd CHARACTER(4), nFlagSe SMALLINT)
    RETURNS TEXT AS
$BODY$
DECLARE
   R0              RECORD;
   i                  INTEGER := 0;
   lnOrden      SMALLINT    := 0;
   lnFlagSe      SMALLINT    := 0;
   lcDesTab    VARCHAR(200)    := '';
   lmDatos      TEXT; 
BEGIN
   -- OBTIENE PARAMETROS DEL OBJETO JSON
   i := 0;
    FOR R0 IN SELECT nOrden, cDescri FROM Medicina.TablaTablas WHERE _cCodInd = p_cCodInd ORDER BY nOrden LOOP
        lnOrden := R0.nOrden;
        lcDesTab  := R0.cDescri;
        IF i = nFlagSe THEN
            lnFlagSe := 1;
        ELSE
            lnFlagSe := 0;
        END IF; 
        IF i = 0 THEN
            lmDatos := '[{"NORDEN":"'||lnOrden||'", "CDESCRI":"'||lcDesTab||'", "CFLAGSE":'||lnFlagSe||'}';
        ELSE
            lmDatos := lmDatos || ',{"NORDEN":"'||lnOrden||'", "CDESCRI":"'||lcDesTab||'", "CFLAGSE":'||lnFlagSe||'}';
        END IF;
        i := i+1;
    END LOOP;
   lmDatos := lmDatos || ']';
   RETURN lmDatos;
END
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;