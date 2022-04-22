import asyncio
import json
import os
import traceback

import requests
from app.CBase import CBase
from app.CSql import CSql
from app.decorators import exception_handler_request, user_required
from flask import Blueprint, current_app, jsonify, request

loSql = CSql()
loBase = CBase()

PlanActividad = Blueprint("plan", __name__)


def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()


def fetch_async(urls):
    """Fetch list of web pages asynchronously."""
    loop = get_or_create_eventloop()  # event loop
    future = asyncio.ensure_future(fetch_all(urls, loop))  # tasks to do
    done = loop.run_until_complete(future)  # loop until done
    return done


async def fetch_all(urls, loop):
    tasks = []  # dictionary of start times for each url
    for url in urls:
        task = loop.run_in_executor(None, requests.get, url)
        tasks.append(task)  # create list of tasks
    done = await asyncio.gather(*tasks)  # gather task responses
    return done


@PlanActividad.route("/planes", methods=["GET"])
@user_required
@exception_handler_request
def planes():
    R1 = {"OK": 1, "DATA": "OK"}
    lcSql = """
        SELECT A.cCodPla, COALESCE(A._cVauche,'-'),
        A.c_TipPla, B.cDescri AS cDesTip,
        A.c_CodPue, D.cDescri AS cDescri,
        A.tGenera, A.tFin, A._cNroRuc,
        A.c_Estado, E.cDescri AS cDesEst,
        A._cCenDis, F.cDescri AS cDesDis
    FROM Clinica.PlanActividad A
    LEFT OUTER JOIN V_TABLATABLAS_1 B ON B.cCodTab = '007' AND TRIM(B.cCodigo) = A.c_TipPla
    LEFT OUTER JOIN V_TABLATABLAS_1 D ON D.cCodTab = '013' AND TRIM(D.cCodigo) = A.c_CodPue
    LEFT OUTER JOIN V_TABLATABLAS_1 E ON E.cCodTab = '011' AND TRIM(E.cCodigo) = A.c_Estado
    LEFT OUTER JOIN Empresa_CentroDistribucion F ON F.cCenDis = A._cCenDis AND F._cNroRuc = A._cNroRuc 
    """
    loSql.ExecRS(lcSql)
    if loSql.data is None or len(loSql.data) == 0:
        raise AttributeError("RESPUESTA VACIA")
    L1 = [
        "CCODPLA",
        "CBAUCHE",
        "CTIPPLA",
        "CDESTIP",
        "CCODARE",
        "CDESARE",
        "CCODPUE",
        "CDESPUE",
        "TGENERA",
        "TFIN",
        "CNRORUC",
        "CESTADO",
        "CDESEST",
        "CCENDIS",
        "CDESDIS",
        "CCODPER",
        "CDESPER",
    ]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200


@PlanActividad.route("/plan", methods=["GET"])
@user_required
@exception_handler_request
def plan():
    R1 = {"OK": 1, "DATA": "OK"}
    if not (request.args["CCODPLA"]):
        raise ValueError("CODIGO DE PLAN NO DEFINIDO")
    lcSql = f"""
    SELECT A.cCodPla, COALESCE(A._cVauche,'-'),
        A.c_TipPla, B.cDescri AS cDesTip,
        A.c_CodPue, D.cDescri AS cDescri,
        A.tGenera, A.tFin, A._cNroRuc,
        A.c_Estado, E.cDescri AS cDesEst,
        A._cCenDis, F.cDescri AS cDesDis,
        G.cCodPer, G.cDescri
    FROM Clinica.PlanActividad A
    INNER JOIN Clinica.Perfil G ON G.cCodPer = A._cCodPer
    LEFT OUTER JOIN V_TABLATABLAS_1 B ON B.cCodTab = '007' AND TRIM(B.cCodigo) = A.c_TipPla
    LEFT OUTER JOIN V_TABLATABLAS_1 D ON D.cCodTab = '013' AND TRIM(D.cCodigo) = A.c_CodPue
    LEFT OUTER JOIN V_TABLATABLAS_1 E ON E.cCodTab = '011' AND TRIM(E.cCodigo) = A.c_Estado
    LEFT OUTER JOIN Empresa_CentroDistribucion F ON F.cCenDis = A._cCenDis AND F._cNroRuc = A._cNroRuc 
    WHERE A.cCodPla = '{request.args['CCODPLA']}'
    LIMIT 1
    """
    loSql.ExecRS(lcSql)
    if loSql.data is None or len(loSql.data) == 0:
        raise AttributeError("RESPUESTA VACIA")
    L1 = [
        "CCODPLA",
        "CBAUCHE",
        "CTIPPLA",
        "CDESTIP",
        "CCODPUE",
        "CDESPUE",
        "TGENERA",
        "TFIN",
        "CNRORUC",
        "CESTADO",
        "CDESEST",
        "CCENDIS",
        "CDESDIS",
        "CCODPER",
        "CDESPER",
    ]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2][0]
    return jsonify(R1), 200


@PlanActividad.route("/plan/experiencia_laboral", methods=["GET"])
@user_required
@exception_handler_request
def planotrasactividades():
    R1 = {"OK": 1, "DATA": "OK"}
    if "CCODPLA" not in request.args:
        raise ValueError("CODIGO DE PLAN NO DEFINIDO")
    lcSql = f"""
    SELECT tIniAct,
        tFinAct,
        cDescri,
        cDesAct,
        nHorTra,
        cDesAre,
        cDesPue,
        cCauRet,
        nSUBSUE,
        nSUPERF,
        nRRuido,
        nRPolvo,
        nRErgon,
        nRVinRa,
        nRElect,
        nRQuimi,
        nROtros
    WHERE _cCodPla = '{request.args['CCODPLA']}'
    AND c_Estado = 'A'
    """
    loSql.ExecRS(lcSql)
    if loSql.data is None or len(loSql.data) == 0:
        raise AttributeError("RESPUESTA VACIA")

    L1 = [
        "TINIACT",
        "TFINACT",
        "CDESCRI",
        "CEMPACT",
        "NHORTRA" "CDESARE",
        "CDESPUE",
        "CCAURET",
        "TSUBSUE",
        "TSUPERF",
        "BRRUIDO",
        "BRPOLVO",
        "BRERGON",
        "BRVIBRA",
        "BRELECT",
        "BRQUIMI",
        "BROTROS",
    ]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200


@PlanActividad.route("/plan/hoja_ruta", methods=["GET"])
@user_required
@exception_handler_request
def plan_hoja_ruta():
    R1 = {"OK": 1, "DATA": "OK"}
    if "CCODPLA" not in request.args:
        raise ValueError("CODIGO DE PLAN NO DEFINIDO")
    lcSql = f"""
    SELECT A.c_TipSer, D.cDescri, A.cCodAct, A._cNroDni, A.c_Estado, STRING_AGG(C.cDescri, ',')
        FROM Clinica.Actividad A
        INNER JOIN Clinica.PlantillaActividad B ON B._cCodACt = A.cCodAct
        INNER JOIN Clinica.Examen C ON C.cCodExa = B._cCodExa
        LEFT OUTER JOIN V_TABLATABLAS_1 D ON D.cCodTab = '014' AND TRIM(D.cCodigo) = A.c_TipSer
    WHERE A._cCodPla = '{request.args['CCODPLA']}'
    GROUP BY A.c_TipSer, D.cDescri, A.cCodAct, A._cNroDni, A.c_Estado
    ORDER BY A.c_TipSer
    """
    loSql.ExecRS(lcSql)
    if loSql.data is None or len(loSql.data) == 0:
        raise AttributeError("RESPUESTA VACIA")

    L1 = [
        "CTIPSER",
        "CDESSER",
        "CCODACT",
        "CNRODNI",
        "CESTADO",
        "ADESEXA",
        "CARCHIV",
    ]
    for idx in range(0, len(loSql.data)):
        laFila = loSql.data[idx]
        if os.path.isfile(
            current_app.config["PATH_FILE"] + "/" + laFila[3] + "/" + laFila[2] + ".pdf"
        ):
            lcArchiv = "S"
        else:
            lcArchiv = "N"
        loSql.data[idx] = loSql.data[idx] + (lcArchiv,)
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200


@PlanActividad.route("/plan/examenes", methods=["GET"])
@user_required
@exception_handler_request
def plan_examenes():
    R1 = {"OK": 1, "DATA": "OK"}
    if "CCODPLA" not in request.args:
        raise ValueError("CODIGO DE PLAN NO DEFINIDO")
    lcSql = f"""
    SELECT A.c_TipSer, D.cDescri, A.cCodAct, B._cCodExa, C.cDescri AS  cDesExa, A._cNroDni, A.c_Estado
        FROM Clinica.Actividad A
        INNER JOIN Clinica.PlantillaActividad B ON B._cCodACt = A.cCodAct
        INNER JOIN Clinica.Examen C ON C.cCodExa = B._cCodExa
        LEFT OUTER JOIN V_TABLATABLAS_1 D ON D.cCodTab = '014' AND TRIM(D.cCodigo) = A.c_TipSer
    WHERE A._cCodPla = '{request.args['CCODPLA']}'
    ORDER BY A.c_TipSer
    """
    loSql.ExecRS(lcSql)
    if loSql.data is None or len(loSql.data) == 0:
        raise AttributeError("RESPUESTA VACIA")

    L1 = [
        "CTIPSER",
        "CDESSER",
        "CCODACT",
        "CCODEXA",
        "CDESEXA",
        "CNRODNI",
        "CESTADO",
    ]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200


@PlanActividad.route("/plan/cie10", methods=["GET"])
@user_required
@exception_handler_request
def plancie10():
    R1 = {"OK": 1, "DATA": "OK"}
    if not (request.args["CCODPLA"]):
        raise ValueError("CODIGO DE PLAN NO DEFINIDO")
    lcSql = f"""
    SELECT B.cCodCie, B.cDescri FROM Clinica.Cie10Actividad A
    INNER JOIN Clinica.Cie10 B ON B.cCodCie = A._cCodCie
    WHERE A._cCodPla ='{request.args['CCODPLA']}'
    """
    loSql.ExecRS(lcSql)
    if loSql.data is None or len(loSql.data) == 0:
        raise AttributeError("RESPUESTA VACIA")
    L1 = ["CCODIGO", "CDESCRI"]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200


@PlanActividad.route("/plan/extras", methods=["GET"])
@user_required
@exception_handler_request
def planextras():
    R1 = {"OK": 1, "DATA": "OK"}
    if not (request.args["CCODPLA"]):
        raise ValueError("CODIGO DE PLAN NO DEFINIDO")
    lcSql = f"""
    SELECT A.c_Tipo, B.cDescri||': '||A.cDescri FROM Clinica.ExtraActividad A 
    LEFT OUTER JOIN V_TABLATABLAS_1 B ON B.cCodTab = '017' AND TRIM(B.cCodigo) = A.c_Tipo
    WHERE A._cCodPla ='{request.args['CCODPLA']}'
    """
    loSql.ExecRS(lcSql)
    if loSql.data is None or len(loSql.data) == 0:
        raise AttributeError("RESPUESTA VACIA")
    L1 = ["CTIPO", "CDESCRI"]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200


@PlanActividad.route("/plan/consentientos", methods=["GET"])
@user_required
@exception_handler_request
def planconsentientos():
    R1 = {"OK": 1, "DATA": "OK"}
    if not (request.args["CCODPLA"]):
        raise ValueError("CODIGO DE PLAN NO DEFINIDO")
    lcSql = f"""
    SELECT B.cCodigo, B.cDescri
    FROM Clinica.ConsentimientoPlan A
    INNER JOIN Clinica.Consentimiento B ON B.cCodigo = A._cCodigo
    WHERE A._cCodPla ='{request.args['CCODPLA']}'
    """
    loSql.ExecRS(lcSql)
    if loSql.data is None or len(loSql.data) == 0:
        raise AttributeError("RESPUESTA VACIA")
    L1 = ["CCODIGO", "CDESCRI"]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200


@PlanActividad.route("/plan/PDF", methods=["GET"])
@user_required
@exception_handler_request
def PDF_plan_actividad(data=None):
    R1 = {"OK": 1, "DATA": "OK"}
    from app.PDF.CConsentimiento import CConsentimiento

    if data is None:
        laData = request.args.to_dict()
    else:
        laData = json.loads(data)
    ploads = ["CCODPLA", "CCODUSU"]
    for item in ploads:
        if item not in laData:
            raise ValueError(f"VARIABLE NO DEFINIDA : '{item}'")
    lcCodPla = laData["CCODPLA"]
    lcCodUsu = laData["CCODUSU"]
    urls = [
        current_app.config["API_URL"]
        + f"/view/plan?CCODPLA={lcCodPla}&CCODUSU={lcCodUsu}",
        current_app.config["API_URL"]
        + f"/plan/consentientos?CCODPLA={lcCodPla}&CCODUSU={lcCodUsu}",
        current_app.config["API_URL"]
        + f"/plan/hoja_ruta?CCODPLA={lcCodPla}&CCODUSU={lcCodUsu}",
    ]
    s = requests.Session()
    R0 = []
    for url in urls:
        r = s.get(url)
        R0.append(r.json())
    lcNroDni = R0[0]["DATA"]["CNRODNI"]
    location = current_app.config["PATH_FILE"] + "/" + lcNroDni
    loConsentimiento = CConsentimiento(location, lcCodPla)
    loConsentimiento.setData(R0[0]["DATA"])
    loConsentimiento.setConsentimiento(R0[1]["DATA"])
    loConsentimiento.setExamenes(R0[2]["DATA"])
    llOK = loConsentimiento.print_consentimiento()
    if not llOK:
        err = "ALGO SALIO MAL AL IMPRIMIR"
        if loConsentimiento.error is not None and loConsentimiento.error != "":
            err = loConsentimiento.error
        raise ValueError(err)
    return jsonify(R1), 200
