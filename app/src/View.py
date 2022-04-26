import datetime
import os

from app.CBase import CBase
from app.CSql import CSql
from app.decorators import exception_handler_request, user_required
from flask import Blueprint, current_app, jsonify, request

loSql = CSql()
loBase = CBase()

View = Blueprint("view", __name__)

@View.get("/view/actividades")
# @user_required
@exception_handler_request
def view_actividades():
    R1 = {"OK": 1, "DATA": "OK"}
    if request.args["CTIPSER"] != "X":
        lcSearch = f"WHERE c_TipSer = '{request.args['CTIPSER']}' "
    else:
        lcSearch = f"WHERE "
    if "CESTADO" not in request.args:
        lcSearch = lcSearch + "AND c_Estado != 'F'"
    else:
        lcSearch = lcSearch + f"AND A.c_Estado = {request.args['CESTADO']}"
    if request.args.get("DINIACT") and request.args.get("DFINACT"):
        format = "%Y-%m-d"
        ltInico = request.args["DINIACT"]
        ltFin = request.args["DFINACT"]
        datetime.datetime.strptime(ltInico, format)
        datetime.datetime.strptime(ltFin, format)
        lcSearch = lcSearch + f" AND tActCit::DATE BETWEEN '{ltInico}' AND '{ltFin}'"
    lcSql = (
        """
    SELECT cCodAct, tActCit, tActAte, tActFin, cCodPla, cUsuCod,
        c_TipSer, cDesSer,
        cDesDoc, cNroDni, cNroDoc, cNombres, tNacimi, nEdad, cDesSex,
        cDesTip, cDesPue, 
        cNroRuc, cDesEmp, cDesSed,
        c_Aptitu, cDesApt,
        c_Estado, cDesEst,
        cDesPer,
        c_TipPla, tPlaIni, tPlaFin, cVauche
    FROM Clinica.V_ACTIVIDAD_1
    """
        + lcSearch
    )
    loSql.ExecRS(lcSql)
    assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    L1 = [
        "CCODACT",
        "TCITA",
        "TATENCI",
        "TFIN",
        "CCODPLA",
        "CUSUCOD",
        "CTIPSER",
        "CDESSER",
        "CDESDOC",
        "CNRODNI",
        "CNRODOC",
        "CNOMBRE",
        "TNACIMI",
        "NEDAD",
        "CDESSEX",
        "CDESTIP",
        "CDESPUE",
        "CNRORUC",
        "CDESEMP",
        "CDESSED",
        "CAPTITU",
        "CDESAPT",
        "CESTADO",
        "CDESEST",
        "CDESPER",
        "CTIPPLA",
        "TINICIO",
        "TFINPLA",
        "CVAUCHE",
    ]
    for idx in range(0, len(loSql.data)):
        laFila = loSql.data[idx]
        if os.path.isfile(
            current_app.config["PATH_FILE"]
            + "/"
            + laFila[11]
            + "/"
            + laFila[1]
            + ".pdf"
        ):
            lcArchiv = "S"
        else:
            lcArchiv = "N"
        loSql.data[idx] = loSql.data[idx] + (lcArchiv,)
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200

@View.get("/view/actividad")
# @user_required
@exception_handler_request
def view_actividad():
    R1 = {"OK": 1, "DATA": "OK"}
    assert not request.args["CCODACT"], "CODIGO DE LA ACTIVIDAD NO DEFINIDO"
    lcSql = f"""
    SELECT cCodAct, tActCit, tActAte, tActFin, cCodPla, cUsuCod,
        c_TipSer, cDesSer,
        cDesDoc, cNroDni, cNroDoc, cNombres, tNacimi, nEdad, cDesSex,
        cDesTip, cDesPue, 
        cNroRuc, cDesEmp, cDesSed,
        c_Aptitu, cDesApt,
        c_Estado, cDesEst,
        cDesPer,
        c_TipPla, tPlaIni, tPlaFin, cVauche
    FROM Clinica.V_ACTIVIDAD_1 WHERE cCodact = '{request.args["CCODACT"]}'
    LIMIT 1
    """
    loSql.ExecRS(lcSql)
    assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    L1 = [
        "CCODACT",
        "TCITA",
        "TATENCI",
        "TFIN",
        "CCODPLA",
        "CUSUCOD",
        "CTIPSER",
        "CDESSER",
        "CDESDOC",
        "CNRODNI",
        "CNRODOC",
        "CNOMBRE",
        "TNACIMI",
        "NEDAD",
        "CDESSEX",
        "CDESTIP",
        "CDESPUE",
        "CNRORUC",
        "CDESEMP",
        "CDESSED",
        "CAPTITU",
        "CDESAPT",
        "CESTADO",
        "CDESEST",
        "CDESPER",
        "CTIPPLA",
        "TINICIO",
        "TFINPLA",
        "CVAUCHE",
        "CARCHIV",
    ]
    for idx in range(0, len(loSql.data)):
        laFila = loSql.data[idx]
        if os.path.isfile(
            current_app.config["PATH_FILE"]
            + "/"
            + laFila[11]
            + "/"
            + laFila[1]
            + ".pdf"
        ):
            lcArchiv = "S"
        else:
            lcArchiv = "N"
        loSql.data[idx] = loSql.data[idx] + (lcArchiv,)
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2][0]
    return jsonify(R1), 200

@View.get("/view/plan")
# @user_required
@exception_handler_request
def view_plan():
    R1 = {"OK": 1, "DATA": "OK"}
    assert not request.args["CCODPLA"], "CODIGO DE LA ACTIVIDAD NO DEFINIDO"
    lcSql = f"""
    SELECT cCodPla, tGenera, tFinAdm, tFinPla, cUsuCod,
        cDesDoc, cNroDni, cNroDoc, cNombres, tNacimi, nEdad, cDesSex,
        cDesTip, cDesPue, 
        cNroRuc, cDesEmp, cDesSed,
        c_Aptitu, cDesApt,
        c_Estado, cDesEst,
        cDesPer,
        c_TipPla, cVauche
    FROM Clinica.V_PLAN_1 WHERE cCodPla = '{request.args["CCODPLA"]}'
    LIMIT 1
    """
    loSql.ExecRS(lcSql)
    assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    L1 = [
        "CCODPLA",
        "TGENERA",
        "TFINADM",
        "TFINPLA",
        "CUSUCOD",
        "CDESDOC",
        "CNRODNI",
        "CNRODOC",
        "CNOMBRE",
        "TNACIMI",
        "NEDAD",
        "CDESSEX",
        "CDESTIP",
        "CDESPUE",
        "CNRORUC",
        "CDESEMP",
        "CDESSED",
        "CAPTITU",
        "CDESAPT",
        "CESTADO",
        "CDESEST",
        "CDESPER",
        "CTIPPLA",
        "CVAUCHE",
    ]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2][0]
    return jsonify(R1), 200
