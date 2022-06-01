import json
import os

import requests
from flask import Blueprint, current_app, jsonify, request

from app.decorators import exception_handler_request, user_required
from app.fn_base import FnBase
from app.models.CSql import CSql

loSql = CSql()
loBase = FnBase()

PlanActividad = Blueprint("plan", __name__)


@PlanActividad.get("/planes")
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
    assert loSql.data is None or len(loSql.data) == 0, f"RESPUESTA VACIA:\n{lcSql}"
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


@PlanActividad.get("/plan")
@user_required
@exception_handler_request
def plan():
    R1 = {"OK": 1, "DATA": "OK"}
    assert not request.args["CCODPLA"], "CODIGO DE PLAN NO DEFINIDO"
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
    assert loSql.data is None or len(loSql.data) == 0, f"RESPUESTA VACIA:\n{lcSql}"
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


@PlanActividad.get("/plan/experiencia_laboral")
@user_required
@exception_handler_request
def planotrasactividades():
    R1 = {"OK": 1, "DATA": "OK"}
    assert "CCODPLA" not in request.args, "CODIGO DE PLAN NO DEFINIDO"
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
    assert loSql.data is None or len(loSql.data) == 0, f"RESPUESTA VACIA:\n{lcSql}"
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


@PlanActividad.get("/plan/hoja_ruta")
@user_required
@exception_handler_request
def plan_hoja_ruta():
    R1 = {"OK": 1, "DATA": "OK"}
    assert "CCODPLA" not in request.args, "CODIGO DE PLAN NO DEFINIDO"
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
    assert loSql.data is None or len(loSql.data) == 0, f"RESPUESTA VACIA:\n{lcSql}"
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


@PlanActividad.get("/plan/examenes")
@user_required
@exception_handler_request
def plan_examenes():
    R1 = {"OK": 1, "DATA": "OK"}
    assert "CCODPLA" not in request.args, "CODIGO DE PLAN NO DEFINIDO"
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
    assert loSql.data is None or len(loSql.data) == 0, f"RESPUESTA VACIA:\n{lcSql}"
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


@PlanActividad.get("/plan/cie10")
@user_required
@exception_handler_request
def plancie10():
    R1 = {"OK": 1, "DATA": "OK"}
    assert not request.args["CCODPLA"], "CODIGO DE PLAN NO DEFINIDO"
    lcSql = f"""
    SELECT B.cCodCie, B.cDescri FROM Clinica.Cie10Actividad A
    INNER JOIN Clinica.Cie10 B ON B.cCodCie = A._cCodCie
    WHERE A._cCodPla ='{request.args['CCODPLA']}'
    """
    loSql.ExecRS(lcSql)
    assert loSql.data is None or len(loSql.data) == 0, f"RESPUESTA VACIA:\n{lcSql}"
    L1 = ["CCODIGO", "CDESCRI"]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200


@PlanActividad.get("/plan/extras")
@user_required
@exception_handler_request
def planextras():
    R1 = {"OK": 1, "DATA": "OK"}
    assert not request.args["CCODPLA"], "CODIGO DE PLAN NO DEFINIDO"
    lcSql = f"""
    SELECT A.c_Tipo, B.cDescri||': '||A.cDescri FROM Clinica.ExtraActividad A 
    LEFT OUTER JOIN V_TABLATABLAS_1 B ON B.cCodTab = '017' AND TRIM(B.cCodigo) = A.c_Tipo
    WHERE A._cCodPla ='{request.args['CCODPLA']}'
    """
    loSql.ExecRS(lcSql)
    assert loSql.data is None or len(loSql.data) == 0, f"RESPUESTA VACIA:\n{lcSql}"
    L1 = ["CTIPO", "CDESCRI"]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200


@PlanActividad.get("/plan/consentientos")
@user_required
@exception_handler_request
def planconsentientos():
    R1 = {"OK": 1, "DATA": "OK"}
    assert not request.args["CCODPLA"], "CODIGO DE PLAN NO DEFINIDO"
    lcSql = f"""
    SELECT B.cCodigo, B.cDescri
    FROM Clinica.ConsentimientoPlan A
    INNER JOIN Clinica.Consentimiento B ON B.cCodigo = A._cCodigo
    WHERE A._cCodPla ='{request.args['CCODPLA']}'
    """
    loSql.ExecRS(lcSql)
    assert loSql.data is None or len(loSql.data) == 0, f"RESPUESTA VACIA:\n{lcSql}"
    L1 = ["CCODIGO", "CDESCRI"]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200


@PlanActividad.get("/plan/PDF")
@user_required
@exception_handler_request
def PDF_plan_actividad(data=None):
    R1 = {"OK": 1, "DATA": "OK"}
    from app.adapters.ConsentPDF import CConsentimiento

    if data is None:
        laData = request.args.to_dict()
    else:
        laData = json.loads(data)
    ploads = ["CCODPLA", "CCODUSU"]
    for item in ploads:
        assert item not in laData, f"VARIABLE NO DEFINIDA : '{item}'"
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
    assert not llOK, loConsentimiento.error
    return jsonify(R1), 200
