import traceback

from app.CBase import CBase
from app.CSql import CSql
from app.decorators import exception_handler_request, user_required
from flask import Blueprint, jsonify, request

loSql = CSql()
loBase = CBase()

Empresa = Blueprint("empresa", __name__)


@Empresa.route("/empresas", methods=["GET"])
@user_required
@exception_handler_request
def planes():
    R1 = {"OK": 1, "DATA": "OK"}
    lcSql = """
    SELECT A.cNroRuc, A.cDescri, A._cCodDis, A.cDirecc,
        A.c_Estado, B.cDescri AS cDesEst,
        A.cConSul
    FROM Empresa A
    LEFT OUTER JOIN V_TABLATABLAS_1 B ON B.cCodTab = '001' AND TRIM(B.cCodigo) = A.c_Estado
    """
    loSql.ExecRS(lcSql)
    if loSql.data is None or len(loSql.data) == 0:
        raise AttributeError("RESPUESTA VACIA")
    L1 = [
        "CNRORUC",
        "CDESCRI",
        "CCODDIS",
        "CDIRECC",
        "CESTADO",
        "CDESEST",
        "CCONSUL",
    ]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200


@Empresa.route("/empresa", methods=["GET"])
@user_required
@exception_handler_request
def plan():
    R1 = {"OK": 1, "DATA": "OK"}
    if not (request.args["CNRORUC"]):
        raise ValueError("RUC NO DEFINIDO")
    lcSql = f"""
    SELECT A.cNroRuc, A.cDescri, A._cCodDis, A.cDirecc,
            A.c_Estado, B.cDescri AS cDesEst,
            A.cConSul
    FROM Empresa A
    LEFT OUTER JOIN V_TABLATABLAS_1 B ON B.cCodTab = '001' AND TRIM(B.cCodigo) = A.c_Estado
    WHERE A.cNroRuc = '{request.args['CNRORUC']}'
    """
    loSql.ExecRS(lcSql)
    if loSql.data is None or len(loSql.data) == 0:
        raise AttributeError("RESPUESTA VACIA")
    L1 = [
        "CNRORUC",
        "CDESCRI",
        "CCODDIS",
        "CDIRECC",
        "CESTADO",
        "CDESEST",
        "CCONSUL",
    ]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2][0]
    return jsonify(R1), 200
