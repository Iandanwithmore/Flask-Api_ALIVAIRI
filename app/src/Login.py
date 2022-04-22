import json

from app.CBase import CBase
from app.CSql import CSql
from app.decorators import exception_handler_request, user_required
from flask import Blueprint, jsonify, request

loSql = CSql()
loBase = CBase()

Login = Blueprint("Login", __name__)


@Login.route("/login", methods=["POST"])
@exception_handler_request
def login():
    R1 = {"OK": 1, "DATA": "OK"}
    laData = request.get_json()
    lcSql = "SELECT Login('{}')".format(laData)
    loSql.ExecRS(lcSql)
    if loSql.data is None or len(loSql.data) == 0:
        raise AttributeError("RESPUESTA VACIA")
    laFila = loSql.data
    if not loBase.json_to_str(laFila[0][0]):
        raise ValueError("ERROR EN DECODIFICACION")
    R1 = json.loads(laFila[0][0])
    return jsonify(R1), 200


@Login.route("/main", methods=["GET"])
@user_required
@exception_handler_request
def main():
    R1 = {"OK": 1, "DATA": "OK"}
    if not (request.args["CCODUSU"]):
        raise ValueError("CREDENCIALES NO ENCONTRADAS")
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
    if loSql.data is None or len(loSql.data) == 0:
        raise AttributeError("RESPUESTA VACIA")
    L1 = ["CCODOPC", "CDESCRI", "CSVGPAT"]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200
