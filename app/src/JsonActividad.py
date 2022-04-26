import json

import pandas
from app.CBase import CBase
from app.CSql import CSql
from app.decorators import exception_handler_request
from app.PDF.CActividad import CActividad
from flask import Blueprint, current_app, jsonify
from openpyxl import load_workbook

loSql = CSql()
loBase = CBase()

JsonActividad = Blueprint("Jsonactividad", __name__)

@JsonActividad.get("/jsonactividad/PDF")
@exception_handler_request
def PDF_JsonActividad():
    R1 = {"OK": 1, "DATA": "OK"}
    excel = current_app.config["PROJECT_DIR"] + "/tests/Json/data.xlsx"
    data_df = pandas.read_excel(excel, sheet_name="DATOS")
    data_df.columns = [
        "CCODACT",
        "CAPTITU",
        "CDESPUE",
        "CDESSEX",
        "CNOMBRE",
        "CNRODNI",
        "CNRODOC",
        "CTIPPLA",
        "CUSUFIR",
        "NEDAD",
        "TATENCI",
        "TCITA",
        "TFIN",
        "TNACIMI",
        "OCIE10",
        "MCONCLU",
        "MRECOME",
        "MOBSERV",
        "CDESSER",
        "CDESEMP",
        "CDESSED",
        "T001",
        "T002",
        "T003",
        "T004",
        "T005",
        "M001",
        "M002",
        "M003",
        "M004",
        "M005",
        "M006",
        "M007",
        "M008",
        "M009",
        "M010",
        "M011",
        "M012",
        "M013",
        "M014",
        "M015",
        "M016",
        "M017",
    ]
    data_df = data_df.fillna(0)
    json_string = data_df.to_json(orient="records")
    data = loBase.fix_json(json_string)
    for laFila in data:
        print("------------------------ITEM")
        print(laFila)
        f = open(current_app.config["PROJECT_DIR"] + "/tests/Json/data.json")
        laData = json.load(f)
        f.close()
        laData["DATA"]["CCODACT"] = str(laFila["CCODACT"])
        if laFila["CAPTITU"] == "APTO":
            laData["DATA"]["CAPTITU"] = 0
        elif laFila["CAPTITU"] == "APTO CON RESTRICCIONES":
            laData["DATA"]["CAPTITU"] = 1
        else:
            print("------------------ERROR")
        laData["DATA"]["CDESPUE"] = str(laFila["CDESPUE"])
        laData["DATA"]["CDESSEX"] = str(laFila["CDESSEX"])
        laData["DATA"]["CNOMBRE"] = str(laFila["CNOMBRE"])
        laData["DATA"]["CNRODNI"] = str(laFila["CNRODNI"])
        laData["DATA"]["CNRODOC"] = str(laFila["CNRODOC"])
        laData["DATA"]["CTIPPLA"] = str(laFila["CTIPPLA"])
        laData["DATA"]["CUSUFIR"] = str(laFila["CUSUFIR"])
        laData["DATA"]["NEDAD"] = str(laFila["NEDAD"])
        laData["DATA"]["TATENCI"] = str(laFila["TATENCI"])
        laData["DATA"]["TCITA"] = str(laFila["TCITA"])
        laData["DATA"]["TFIN"] = str(laFila["TFIN"])
        laData["DATA"]["TNACIMI"] = str(laFila["TNACIMI"])
        laData["DATA"]["CDESSER"] = str(laFila["CDESSER"])
        laData["DATA"]["CDESSED"] = str(laFila["CDESSED"])
        lmCie10 = dict()
        lmCie10["OCIE10"] = " " if laFila["OCIE10"] == 0 else laFila["OCIE10"].replace(",", "\n")

        lmExtra = dict()
        lmExtra["MCONCLU"] = " " if laFila["MCONCLU"] == 0 else laFila["MCONCLU"].replace(",", "\n")
        lmExtra["MRECOME"] = " " if laFila["MRECOME"] == 0 else laFila["MRECOME"].replace(",", "\n")
        lmExtra["MOBSERV"] = " " if laFila["MOBSERV"] == 0 else laFila["MOBSERV"].replace(",", "\n")

        f = open(current_app.config["PROJECT_DIR"] + "/tests/Json/TTTTT1.json")
        laDatos = json.load(f)
        f.close()
        laDatos["DATA"][0]["CRESULT"] = str(laFila["T001"])
        laDatos["DATA"][1]["CRESULT"] = str(laFila["T002"])
        laDatos["DATA"][2]["CRESULT"] = str(laFila["T003"])
        laDatos["DATA"][3]["CRESULT"] = str(laFila["T004"])
        laDatos["DATA"][4]["CRESULT"] = str(laFila["T005"])
        laDatos["DATA"][5]["NOPCION"] = 1 if laFila["M001"] == "NORMAL" else 2
        laDatos["DATA"][6]["CRESULT"] = str(laFila["M002"])
        laDatos["DATA"][7]["NOPCION"] = 1 if laFila["M003"] == "NORMAL" else 2
        laDatos["DATA"][8]["CRESULT"] = str(laFila["M004"])
        laDatos["DATA"][9]["CRESULT"] = str(laFila["M005"])
        laDatos["DATA"][10]["CRESULT"] = str(laFila["M006"])
        laDatos["DATA"][11]["CRESULT"] = str(laFila["M007"])
        laDatos["DATA"][12]["CRESULT"] = str(laFila["M008"])
        laDatos["DATA"][13]["CRESULT"] = str(laFila["M009"])
        laDatos["DATA"][14]["CRESULT"] = str(laFila["M010"])
        laDatos["DATA"][15]["CRESULT"] = str(laFila["M011"])
        laDatos["DATA"][16]["CRESULT"] = str(laFila["M012"])
        laDatos["DATA"][17]["CRESULT"] = str(laFila["M013"])
        laDatos["DATA"][18]["CRESULT"] = str(laFila["M014"])
        laDatos["DATA"][19]["CRESULT"] = str(laFila["M015"])
        laDatos["DATA"][20]["CRESULT"] = str(laFila["M016"])
        laDatos["DATA"][21]["CRESULT"] = str(laFila["M017"])
        location = current_app.config["PROJECT_DIR"]
        loActividad = CActividad(location, laFila["CNOMBRE"])
        loActividad.setExamen([{"CTIPSER": "X", "CCODIGO": "XXXXXX", "CDESCRI": ""}])
        # print("DATA-------------------")
        # print(json.dumps(laData, indent=3, sort_keys=True))
        # print("DATOS-------------------")
        # print(json.dumps(laDatos, indent=3, sort_keys=True))
        # print("EXTRA-------------------")
        # print(lmExtra)
        # print("CIE-------------------")
        # print(lmCie10)
        loActividad.setDatos(laDatos["DATA"])
        loActividad.setData(laData["DATA"])
        loActividad.setExtras(lmExtra)
        loActividad.setCie10(lmCie10)
        llOK = loActividad.print_actividad()
        if not llOK:
            print("Algo fallo")
            raise ValueError(loActividad.error)
    return jsonify(R1), 200

@JsonActividad.get("/hemograma/subir")
@exception_handler_request
def Hemograma_Actividad():
    R1 = {"OK": 1, "DATA": "OK"}
    excel = current_app.config["PROJECT_DIR"] + "/tests/Docs/data.xlsx"
    data_df = pandas.read_excel(excel, sheet_name="DATOS")
    data_df.columns = [
        "CCODACT",
        "CNOMBRE",
        "CAPELLI",
        "CMODOOP",
        "TFECATE",
        "CHORATE",
        "CESTMUE",
        "L001",  # WBC (10^3/uL)
        "L019",  # Neu# (10^3/uL)
        "L015",  # Lym# (10^3/uL)
        "L016",  # Mon# (10^3/uL)
        "L024",  # Eos# (10^3/uL)
        "L018",  # Bas# (10^3/uL)
        "L012",  # Neu% (%)
        "L015",  # Lym% (%)
        "L016",  # Mon% (%)
        "L017",  # Eos% (%)
        "L018",  # Bas% (%)
        "L002",  # RBC (10^6/uL)
        "L006",  # HGB (g/dL)
        "",  # HCT (%)
        "",  # HCT (%)
        "",  # MCV (fL)
        "",  # MCH (pg)
        "",  # MCHC (g/dL)
        "",  # RDW-CV (%)
        "",  # RDW-SD (fL)
        "",  # PLT (10^3/uL)
        "",  # MPV (fL)
        "",  # PDW ( )
        "",  # PCT (mL/L)
        "",  # P-LCC (10^9/L)
        "",  # P-LCR (%)
        "NIDPACI",  # ID pac
        "CGENERO",  # Sexo
        "",  # Tipo pac
        "",  # Grupo de ref.
        "TNACIMI",  # Fecha nac
        "NEDAD",  # Edad
        "CDESDEP",  # Dpto
        "NROCAM",  # N? cama
        "TPROCES",  # Fecha de trazado
        "HPROCES",  # Hora de trazado
        "TENTREG",  # Fecha entrega
        "HENTREG",  # Hor entr
        "CUSUCOD",  # MEDICO
        "COPERAR",  # Operador
        "CUSUVAL",  # Validado por
        "CCOMENT",  # Comentarios
        "CCOMWBC",  # Mensaje WBC
        "CCOMRBC",  # Mensaje RBC
        "CCOMPLT",  # Mensaje PLT
        "L027",  # Grupo SANGUINEO
        "",  # ESR
        "L208",  # PARASITOS
    ]
    data_df = data_df.fillna(0)
    json_string = data_df.to_json(orient="records")
    data = loBase.fix_json(json_string)
    for laFila in data:
        f = open(current_app.config["PROJECT_DIR"] + "/tests/Json/actividad.json")
        laData = json.load(f)
        f.close()
        idx = 0
        idx_2 = 0
        print("------------------------ITEM")
        print(laFila)
        for k, v in laFila.items():
            print(f"{k}, {v}  {idx}")
            if v is not None:
                str_item = str(v)
            else:
                str_item = None
            if idx == 1:
                if str_item == "APTO":
                    laData["DATA"][k] = 0
                else:
                    laData["DATA"][k] = 1
            elif idx < 14:
                laData["DATA"][k] = str_item
            elif idx == 14:
                laData["DATA"][k] = str_item.replace(")", ") \n")
            elif idx in (15, 16):
                if str_item.strip() == "0.0" or str_item.strip() == "0":
                    laData["DATA"]["OEXTRA"][k] = " "
                else:
                    laData["DATA"]["OEXTRA"][k] = str_item.replace(",", "\n")
            else:
                if idx_2 in (5, 7):
                    if str_item == "NORMAL":
                        laData["DATA"]["MDATOS"][idx_2]["NOPCION"] = 1
                    else:
                        laData["DATA"]["MDATOS"][idx_2]["NOPCION"] = 2
                laData["DATA"]["MDATOS"][idx_2]["CRESULT"] = str_item
                idx_2 = idx_2 + 1
            idx = idx + 1
        location = current_app.config["PROJECT_DIR"]
        loActividad = CActividad(location, laData["DATA"]["CNOMBRE"])
        loActividad.setDatos(laData["DATA"]["MDATOS"])
        laData["DATA"].pop("MDATOS")
        loActividad.setData(laData["DATA"])
        llOK = loActividad.print_jsonactividad()
        if not llOK:
            print("Algo fallo")
            raise ValueError(loActividad.error)
    return jsonify(R1), 200
