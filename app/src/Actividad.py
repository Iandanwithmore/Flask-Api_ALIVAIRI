import json

import requests
from app.CBase import CBase
from app.CSql import CSql
from app.decorators import exception_handler_request, user_required
from app.PDF.CActividad import CActividad
from flask import Blueprint, current_app, jsonify, request

loSql = CSql()
loBase = CBase()

Actividad = Blueprint("actividad", __name__)

@Actividad.get("/actividad/examenes")
@user_required
@exception_handler_request
def examenes():
    R1 = {"OK": 1, "DATA": "OK"}
    assert "CCODACT" not in request.args,"CODIGO DE LA ACTIVIDAD NO DEFINIDO"
    lcSql = f"""SELECT B.cCodExa, B.c_TipSer, B.cDescri FROM Clinica.PlantillaActividad A
        INNER JOIN clinica.Examen B ON B.cCodExa = A._cCodExa
        WHERE A._cCodAct = '{request.args['CCODACT']}'"""
    loSql.ExecRS(lcSql)
    assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    L1 = ["CCODIGO", "CTIPSER", "CDESCRI"]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    R1["OK"] = 1
    return jsonify(R1), 200

@Actividad.get("/actividad/extra")
@user_required
@exception_handler_request
def extras():
    R1 = {"OK": 1, "DATA": "OK"}
    assert "CCODACT" not in request.args, "CODIGO DEL ACTIVIDAD NO DEFINIDO"
    lcCodAct = request.args["CCODACT"]
    lcSql = f"""
        SELECT COALESCE(
            (SELECT cDescri
            FROM Clinica.ExtraActividad
            WHERE _cCodAct = '{lcCodAct}' AND c_Tipo = 'O'), NULL)
        UNION ALL
        SELECT COALESCE(
            (SELECT cDescri
            FROM Clinica.ExtraActividad
            WHERE _cCodAct = '{lcCodAct}' AND c_Tipo = 'R'), NULL)
        UNION ALL
        SELECT COALESCE(
            (SELECT cDescri
            FROM Clinica.ExtraActividad
            WHERE _cCodAct = '{lcCodAct}' AND c_Tipo = 'C'), NULL)
    """
    loSql.ExecRS(lcSql)
    assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    R1["DATA"] = {
        "COBSERV": None if loSql.data[0][0] is None else loSql.data[0][0],
        "CRECOME": None if loSql.data[1][0] is None else loSql.data[1][0],
        "CCONCLU": None if loSql.data[2][0] is None else loSql.data[2][0],
    }
    return jsonify(R1), 200

@Actividad.get("/actividad/detalle")
@Actividad.post("/actividad/detalle")
@user_required
@exception_handler_request
def detalleActividad():
    R1 = {"OK": 1, "DATA": "OK"}
    if request.method == "GET":
        assert "CCODACT" not in request.args, "CODIGO DE LA ACTIVIDAD NO DEFINIDO"
        lcSql = f"SELECT Clinica.detalleActividad('{request.args['CCODACT']}')"
        loSql.ExecRS(lcSql)
        assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
        laFila = loSql.data
        assert not loBase.json_to_str(laFila[0][0]),"ERROR AL TRANSFORMAR A JSON"
        R1 = json.loads(laFila[0][0])
    elif request.method == "POST":
        laData = json.loads(request.get_json())
        ploads = [
            "CCODACT",
            "CTIPSER",
            "CCODPLA",
            "CNRODNI",
            "CNRORUC",
            "MDATOS",
            "CCODUSU",
        ]
        dict_data = {}
        for item in ploads:
            assert item not in laData, f"VARIABLE NO DEFINIDA : '{item}'"
            dict_data[item] = laData[item]
        lcSql = f"SELECT Clinica.grabarDetalleActividad('{json.dumps(laData)}')"
        loSql.ExecRS(lcSql)
        assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
        laFila = loSql.data
        assert not loBase.json_to_str(laFila[0][0]),"ERROR AL TRANSFORMAR A JSON"
        R1 = json.loads(laFila[0][0])
        if R1["OK"]:
            PDF_Actividad(json.dumps(laData))
    return jsonify(R1), 200

@Actividad.get("/actividad/print/detalle")
@user_required
@exception_handler_request
def print_detalleActividad():
    R1 = {"OK": 1, "DATA": "OK"}
    assert "CCODACT" not in request.args, "CODIGO DEL ACTIVIDAD NO DEFINIDO"
    lcSql = f"SELECT Clinica.detalleActividadPrint('{request.args['CCODACT']}')"
    loSql.ExecRS(lcSql)
    assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    laFila = loSql.data
    assert not loBase.json_to_str(laFila[0][0]),"ERROR AL TRANSFORMAR A JSON"
    R1 = json.loads(laFila[0][0])
    return jsonify(R1), 200


@Actividad.route("/actividad/PDF/<string:data>", methods=["GET"])
@Actividad.route("/actividad/PDF", methods=["GET"])
@user_required
@exception_handler_request
def PDF_Actividad(data=None):
    R1 = {"OK": 1, "DATA": "OK"}
    if data is None:
        laData = request.args.to_dict()
    else:
        laData = json.loads(data)
    ploads = ["CCODACT", "CNRODNI", "CCODUSU"]
    for item in ploads:
        assert item not in laData, f"VARIABLE NO DEFINIDA : '{item}'"
    lcCodAct = laData["CCODACT"]
    lcCodUsu = laData["CCODUSU"]
    lcNroDni = laData["CNRODNI"]
    urls = [
        current_app.config["API_URL"]
        + f"/actividad/print/detalle?CCODACT={lcCodAct}&CCODUSU={lcCodUsu}",
        current_app.config["API_URL"]
        + f"/view/actividad?CCODACT={lcCodAct}&CCODUSU={lcCodUsu}",
        current_app.config["API_URL"]
        + f"/actividad/examenes?CCODACT={lcCodAct}&CCODUSU={lcCodUsu}",
    ]
    s = requests.Session()
    R0 = []
    for url in urls:
        r = s.get(url)
        R0.append(r.json())
    location = current_app.config["PATH_FILE"] + "/" + lcNroDni
    loActividad = CActividad(location, lcCodAct)
    print("-----------------DATOS")
    print(json.dumps(R0[0], indent=3, sort_keys=True))
    # print("-----------------DATA")
    # print(json.dumps(R0[1], indent=3, sort_keys=True))
    print("-----------------EXAMEN")
    print(json.dumps(R0[2], indent=3, sort_keys=True))
    loActividad.setDatos(R0[0]["DATA"])
    loActividad.setData(R0[1]["DATA"])
    loActividad.setExamen(R0[2]["DATA"])
    llOK = loActividad.print_actividad()
    if not llOK:
        err = "ALGO SALIO MAL AL IMPRIMIR"
        if loActividad.error is not None and loActividad.error != "":
            err = loActividad.error
        raise ValueError(err)
    return jsonify(R1), 200

@Actividad.get('/cie10')
@user_required
@exception_handler_request
def buscar_cie10():
    R1 = {"OK": 1, "DATA": "OK"}
    if not (request.args["CPARAME"]):
        raise ValueError("PARAMETRO DE BUSQUEDA NO DEFINIDO")
    lcSql = f"SELECT cCodCie, cDescri FROM Clinica.Cie10 WHERE TRIM(cCodCie) = '{request.args['CPARAME']}' OR cDescri LIKE '%{request.args['CPARAME']}%'"
    loSql.ExecRS(lcSql)
    assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    L1 = ["CCODIGO", "CDESCRI"]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200

@Actividad.get('/actividad/cie10')
@user_required
@exception_handler_request
def cie10_actividad():
    R1 = {"OK": 1, "DATA": "OK"}
    if request.method == "GET":
        assert not request.args["CCODACT"], "CODIGO ACTIVIDAD NO DEFINIDO"
        lcSql = f"SELECT B.cCodCie, B.cDescri FROM Clinica.Cie10Actividad A INNER JOIN Clinica.Cie10 B ON B.cCodCie = A._cCodCie WHERE A._cCodAct = '{request.args['CCODACT']}'"
        loSql.ExecRS(lcSql)
        assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
        L1 = ["CCODIGO", "CDESCRI"]
        L2 = loSql.data
        R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    elif request.method == "POST":
        laData = request.get_json()
        ploads = ["CCODACT", "CCODIGO", "CCODPLA"]
        for item in ploads:
            assert item not in laData, f"VARIABLE NO DEFINIDA : '{item}'"
        lcSql = f"INSERT INTO Clinica.Cie10Actividad (_cCodCie, _cCodAct. _cCodPla, _cUsuCod) VALUES ('{request.args['CCODIGO']}','{request.args['CCODACT']}''{request.args['CCODPLA']}','{request.args['CUSUCOD']}') ON CONFLICT DO NOTHING"
        loSql.ExecRS(lcSql)
        assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    return jsonify(R1), 200

@Actividad.get('/actividad/cmp')
@user_required
@exception_handler_request
def cmp_actividad():
    R1 = {"OK": 1, "DATA": "OK"}
    if request.method == "GET":
        assert not (request.args["CCODACT"]), "CODIGO ACTIVIDAD NO DEFINIDO"
        lcSql = f"SELECT B.cCodCMP, B.cDescri FROM Clinica.CMPActividad A INNER JOIN Clinica.CMP B ON B.cCodCmp = A._cCodCmp WHERE A._cCodAct = '{request.args['CCODACT']}'"
        loSql.ExecRS(lcSql)
        assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
        L1 = ["CCODIGO", "CDESCRI"]
        L2 = loSql.data
        R1["DATA"] = [dict(zip(L1, item)) for item in L2][0]
    elif request.method == "POST":
        laData = request.get_json()
        ploads = ["CCODACT", "CCODIGO", "CCODPLA"]
        for item in ploads:
            assert item not in laData, f"VARIABLE NO DEFINIDA : '{item}'"
        lcSql = f"INSERT INTO Clinica.Cie10Actividad (_cCodCie, _cCodAct. _cCodPla, _cUsuCod) VALUES ('{request.args['CCODIGO']}','{request.args['CCODACT']}''{request.args['CCODPLA']}','{request.args['CUSUCOD']}')"
        loSql.ExecRS(lcSql)
        assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    return jsonify(R1), 200

@Actividad.get('/cmp')
@user_required
@exception_handler_request
def buscar_cmp():
    R1 = {"OK": 1, "DATA": "OK"}
    assert not request.args["CPARAME"], "PARAMETRO DE BUSQUEDA NO DEFINIDO"
    lcSql = f"SELECT cCodCMP, cDescri FROM Clinica.cmp WHERE TRIM(ccodcmp) = '{request.args['CPARAME']}' OR cDescri LIKE '%{request.args['CPARAME']}%'"
    loSql.ExecRS(lcSql)
    assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    L1 = ["CCODIGO", "CDESCRI"]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2]
    return jsonify(R1), 200
