CREATE OR REPLACE FUNCTION Medicina.F_R110(p_cCodAct CHARACTER(8), p_cCodExa CHARACTER(6), p_nOrden INTEGER)
    RETURNS TEXT AS
$BODY$
DECLARE
   R0              RECORD;
   i                 INTEGER := 0;
   lfHTML     CHARACTER(1)    := '';
   lcCodInd    CHARACTER(4)    := '';
   lcImprim    VARCHAR(200)    := '';
   lcResult      VARCHAR(800)    := '';
   lnOpcion      SMALLINT    := 0;
   lmDatos     TEXT; 
   lmTabla      TEXT;
BEGIN
   --INDICADOR            AIndica    :={"CCODIND","CIMPRIM","FHTML","CRESULT","CUNIDAD", "CRANGO","MTABLA"};
   i := 0;
   FOR R0 IN 
         (SELECT '0000' AS cCodInd, cDescri AS cImprim, '' AS fHTML, cLisEnl FROM Medicina.Subtitulos WHERE _cCodExa = p_cCodExa)
         UNION ALL
         (SELECT B.cCodInd, B.cImprim, B.c_TipReg AS fHTML,  A.cLisEnl  FROM Medicina.DetallePlantilla A
               INNER JOIN Medicina.Indicador B ON B.cCodInd = A._cCodInd 
         WHERE A._cCodExa = p_cCodExa) 
         ORDER BY cLisEnl LOOP
      lcCodInd := R0.cCodInd;
      lcImprim := R0.cImprim;
      lfHTML  := R0.fHTML;
      SELECT '"'||cResult||'"', nOpcion INTO lcResult, lnOpcion FROM Medicina.DetalleActividad WHERE _cCodAct = p_cCodAct AND _cCodInd = lcCodInd;
      IF NOT FOUND THEN
         lcResult := 'null';
         lnOpcion := -1;
      END IF;
      IF i = 0 THEN
         lmDatos := '[{"CCODIND":"'||lcCodInd||'","NORDEN":"'||p_nOrden||'","CIMPRIM":"'||lcImprim||'","FHTML":"'||lfHTML||'","CRESULT":'||lcResult||',"NOPCION":'||lnOpcion||'';
      ELSE
         lmDatos := lmDatos || ',{"CCODIND":"'||lcCodInd||'","NORDEN":"'||p_nOrden||'","CIMPRIM":"'||lcImprim||'","FHTML":"'||lfHTML||'","CRESULT":'||lcResult||',"NOPCION":'||lnOpcion||'';
      END IF;
      SELECT COALESCE(Medicina.F_R111(lcCodInd, lnOpcion), 'null') INTO lmTabla;
      IF TRIM(lmTabla) != '' THEN
         lmDatos := lmDatos || ', "MTABLA":'||lmTabla||'}';
      END IF;
      i := i+1;
   END LOOP;
   lmDatos := lmDatos || ']';
   RETURN lmDatos;
END
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;