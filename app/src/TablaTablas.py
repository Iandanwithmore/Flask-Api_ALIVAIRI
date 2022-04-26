import json

from app.CBase import CBase
from app.CSql import CSql
from app.decorators import exception_handler_request, user_required
from flask import Blueprint, jsonify, request

loSql = CSql()
loBase = CBase()

TablaTablas = Blueprint("TablaTablas", __name__)

@TablaTablas.get("/tablatablas/<string:p_cCodigo>")
@TablaTablas.post("/tablatablas")
@user_required
@exception_handler_request
def get_triaje_by(p_cCodigo):
    R1 = {"OK": 1, "DATA": "OK"}
    if request.method == "GET":
        if len(p_cCodigo) != 3:
            raise ValueError("CODIGO DE TABLAS NO VALIDO")
        lcSql = (
            "SELECT cCodigo, cDescri FROM V_TABLATABLAS_1 WHERE cCodTab = '{}'".format(
                p_cCodigo
            )
        )
        loSql.ExecRS(lcSql)
        assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
        L1 = ["CCODIGO", "CDESCRI"]
        L2 = loSql.data
        R1["DATA"] = [dict(zip(L1, item)) for item in L2]
        R1["OK"] = 1
    elif request.method == "POST":
        laData = request.get_json()
        lcSql = "SELECT Clinica.P_T001('{}')".format(laData)
        loSql.ExecRS(lcSql)
        assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
        laFila = loSql.data
        assert not loBase.json_to_str(laFila[0][0]),"ERROR AL TRANSFORMAR A JSON"
        R1 = json.loads(laFila[0][0])
    return jsonify(R1), 200
