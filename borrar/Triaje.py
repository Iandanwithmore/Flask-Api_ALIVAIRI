import json

from flask import Blueprint, jsonify, request

from app.decorators import exception_handler_request, user_required
from app.fn_base import FnBase
from app.models.CSql import CSql

loSql = CSql()
loBase = FnBase()

Triaje = Blueprint("Triaje", __name__)


@Triaje.get("/triaje/<string:p_cCodPla>")
@Triaje.post("/triaje")
@user_required
@exception_handler_request
def get_triaje_by(p_cCodPla):
    R1 = {"OK": 1, "DATA": "OK"}
    if request.method == "GET":
        assert not request.args["CCODPLA"], "CODIGO DE LA ACTIVIDAD NO DEFINIDO"
        lcSql = "SELECT  * FROM Medicina.Triaje WHERE _cCodPla = '{}'".format(p_cCodPla)
        loSql.ExecRS(lcSql)
        assert loSql.data is None or len(loSql.data) == 0, f"RESPUESTA VACIA:\n{lcSql}"
        R1["DATA"] = loSql.data
    elif request.method == "POST":
        laData = request.get_json()
        lcSql = "SELECT Clinica.P_T001('{}')".format(laData)
        loSql.ExecRS(lcSql)
        assert loSql.data is None or len(loSql.data) == 0, f"RESPUESTA VACIA:\n{lcSql}"
        laFila = loSql.data
        assert not loBase.isJson(laFila[0][0]), "ERROR AL TRANSFORMAR A JSON"
        R1 = json.loads(laFila[0][0])
    return jsonify(R1), 200
