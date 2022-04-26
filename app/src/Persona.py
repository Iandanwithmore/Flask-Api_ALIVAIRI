from app.decorators import exception_handler_request, user_required
from flask import Blueprint, jsonify, request

from ..CBase import CBase
from ..CSql import CSql

loSql = CSql()
loBase = CBase()

Persona = Blueprint("persona", __name__)

@Persona.get("/persona")
@user_required
@exception_handler_request
def persona():
    R1 = {"OK": 1, "DATA": "OK"}
    assert not ("CNRODNI" in request.args or "CNRODOC" in request.args), "NUMERO DE DOCUMENTO NO DEFINIDO"
    if "CNRODNI" not in request.args:
        lcSearch = f"cnrodoc = '{request.args['CNRODOC']}' LIMIT 1"
    else:
        lcSearch = f"cnrodoc = '{request.args['CNRODNI']}' LIMIT 1"
    lcSql = (
        """
    SELECT c_tipdoc, cdesdoc,
        cnrodoc, cnrodni, 
        cnombres, capepat, capemat, cnombre,
        c_sexo, cdessex,
        c_tipseg, cdesseg,
        TO_CHAR(tnacimi,'YYYY-MM-DD'), nedad,
        cdirecc, ccoddep, cdesdep, ccodpro, cdespro, ccoddis, cdesdis,
        cemail, cnrocel,
        c_estado, cdesest
    FROM 
        V_PERSONA_1
    WHERE 
    """
        + lcSearch
    )
    loSql.ExecRS(lcSql)
    assert(loSql.data is None or len(loSql.data) == 0), f"RESPUESTA VACIA:\n{lcSql}"
    L1 = [
        "CTIPDOC",
        "CDESDOC",
        "CNRODOC",
        "CNRODNI",
        "CNOMBRES",
        "CAPEPAT",
        "CAPEMAT",
        "CNOMBRE",
        "CSEXO",
        "CDESSEX",
        "CTIPSEG",
        "CDESSEG",
        "TNACIMI",
        "NEDAD",
        "CDIRECC",
        "CCODDEP",
        "CDESDEP",
        "CCODPRO",
        "CDESPRO",
        "CCODDIS",
        "CDESDIS",
        "CEMAIL",
        "CNROCEL",
        "CESTADO",
        "CDESEST",
    ]
    L2 = loSql.data
    R1["DATA"] = [dict(zip(L1, item)) for item in L2][0]
    return jsonify(R1), 200

@Persona.get("/persona/huella/<string:p_cNroDni>")
@Persona.post("/persona/huella/<string:p_cNroDni>")
@user_required
@exception_handler_request
def download_huella(p_cNroDni):
    if "/" in p_cNroDni:
        raise ValueError("SUBRUTAS NO PERMITIDAS")
    if request.method == "GET":
        lcFile = loBase.download(p_cNroDni, "HUELLA.jpg")
        assert not lcFile, "ERROR AL DESCARGAR EL ARCHIVO"
        return lcFile
    elif request.method == "POST":
        if "p_cFile" not in request.files:
            return jsonify({"OK": 0, "DATA": "NO FILE"})
        file = request.files["p_cFile"]
        lcFile = loBase.upload(file, p_cNroDni, "HUELLA.jpg")
        assert not lcFile, loBase.error
        return jsonify({"OK": 1, "DATA": "ARCHIVO SUBIDO EXITOSAMENTE"})

@Persona.get("/persona/firma/<string:p_cNroDni>")
@Persona.post("/persona/firma/<string:p_cNroDni>")
@user_required
def updaload_huella(p_cNroDni):
    if "/" in p_cNroDni:
        raise ValueError("SUBRUTAS NO PERMITIDAS")
    if request.method == "GET":
        lcFile = loBase.download(p_cNroDni, "HUELLA.jpg")
        assert not lcFile, "ERROR AL DESCARGAR EL ARCHIVO"
        return lcFile
    elif request.method == "POST":
        if "p_cFile" not in request.files:
            return jsonify({"OK": 0, "DATA": "NO FILE"})
        file = request.files["p_cFile"]
        lcFile = loBase.upload(file, p_cNroDni, "HUELLA.jpg")
        assert not lcFile, loBase.error
        return jsonify({"OK": 1, "DATA": "ARCHIVO SUBIDO EXITOSAMENTE"})
