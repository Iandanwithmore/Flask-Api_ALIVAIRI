import json

from app.CBase import CBase
from app.CSql import CSql
from app.decorators import exception_handler_request, user_required
from flask import Blueprint, jsonify, request

loSql = CSql()
loBase = CBase()

Login = Blueprint("Login", __name__)

@Login.post("/login")
@exception_handler_request
def login():
    R1 = {"OK": 1, "DATA": "OK"}
    laData = request.get_json()
    lcSql = "SELECT Login('{}')".format(laData)
    loSql.ExecRS(lcSql)
    assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    laFila = loSql.data
    assert not loBase.json_to_str(laFila[0][0]),"ERROR AL TRANSFORMAR A JSON"
    R1 = json.loads(laFila[0][0])
    return jsonify(R1), 200

@Login.get("/main")
@user_required
@exception_handler_request
def main():
    R1 = {"OK": 1, "DATA": "OK"}
    assert not request.args["CCODUSU"], "CREDENCIALES NO ENCONTRADAS"
    lcCodUsu = request.args["CCODUSU"]
    lcSql = f"""SELECT cCodOpc, cDescri, COALESCE(cSvgPat, 'null')  
            FROM Opcion WHERE _nIdApp = 3 AND 
            cCodOpc IN (
                SELECT DISTINCT(B._cCodOpc) 
                FROM usuario_rol A 
                INNER JOIN rol_opcion B ON B._cCodRol = A._cCodRol
                WHERE A._cCodUsu = '{lcCodUsu}'
            )"""
    loSql.ExecRS(lcSql)
    assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    L1 = ["CCODOPC", "CDESCRI", "CSVGPAT"]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200
