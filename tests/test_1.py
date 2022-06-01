#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import os
import sys

import pytest

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, os.path.split(basedir)[0])
from app.adapters.ConsentPDF import CConsentimiento
from app.config import Config

# @pytest.fixture(autouse=True)
# def change_test_dir(request, monkeypatch):
#     monkeypatch.chdir(request.fspath.dirname)


def test_print():
    laconsentimiento = [
        {"CCODIGO": "1", "CDESCRI": "PRUEBA FORMATOS ESPECIALES"},
        {"CCODIGO": "2", "CDESCRI": "PRUEBA FORMATOS ESPECIALES"},
        {"CCODIGO": "3", "CDESCRI": "PRUEBA FORMATOS ESPECIALES"},
        {"CCODIGO": "4", "CDESCRI": "PRUEBA FORMATOS ESPECIALES"},
        {"CCODIGO": "5", "CDESCRI": "PRUEBA FORMATOS ESPECIALES"},
        {"CCODIGO": "6", "CDESCRI": "PRUEBA FORMATOS ESPECIALES"},
        {"CCODIGO": "7", "CDESCRI": "PRUEBA FORMATOS ESPECIALES"},
        {"CCODIGO": "8", "CDESCRI": "PRUEBA FORMATOS ESPECIALES"},
        {"CCODIGO": "9", "CDESCRI": "PRUEBA FORMATOS ESPECIALES"},
        {"CCODIGO": "A", "CDESCRI": "PRUEBA FORMATOS ESPECIALES"},
        {"CCODIGO": "B", "CDESCRI": "PRUEBA FORMATOS ESPECIALES"},
        {"CCODIGO": "C", "CDESCRI": "PRUEBA FORMATOS ESPECIALES"},
    ]
    laexamenes = [
        {
            "ADESEXA": "CUESTIONARIO ESPRIOMETRIA,AUDIOMETRIA",
            "CARCHIV": "S",
            "CCODACT": "00017185",
            "CDESSER": "AUDIOMETRIA",
            "CESTADO": "E",
            "CNRODNI": "72539751",
            "CTIPSER": "A",
        },
        {
            "ADESEXA": "RIESGO CARDIOVASCULAR,EKG",
            "CARCHIV": "S",
            "CCODACT": "00017186",
            "CDESSER": "CARDIOLOGIA",
            "CESTADO": "E",
            "CNRODNI": "72539751",
            "CTIPSER": "C",
        },
        {
            "ADESEXA": "ODONTOLOGIA",
            "CARCHIV": "N",
            "CCODACT": "00017187",
            "CDESSER": "ODONOTOLOGIA",
            "CESTADO": "E",
            "CNRODNI": "72539751",
            "CTIPSER": "D",
        },
        {
            "ADESEXA": "RM 312",
            "CARCHIV": "N",
            "CCODACT": "00017188",
            "CDESSER": "MEDICINA",
            "CESTADO": "E",
            "CNRODNI": "72539751",
            "CTIPSER": "M",
        },
        {
            "ADESEXA": "OFTALMOLOGIA,OFTALMOLOGIA ESPECIALIZADA",
            "CARCHIV": "S",
            "CCODACT": "00017189",
            "CDESSER": "OFTALMOLOGIA",
            "CESTADO": "E",
            "CNRODNI": "72539751",
            "CTIPSER": "O",
        },
        {
            "ADESEXA": "FICHA PSICOLOGICA",
            "CARCHIV": "S",
            "CCODACT": "00017190",
            "CDESSER": "PSICOLOGIA",
            "CESTADO": "E",
            "CNRODNI": "72539751",
            "CTIPSER": "P",
        },
        {
            "ADESEXA": "RAYOS X",
            "CARCHIV": "N",
            "CCODACT": "00017191",
            "CDESSER": "RAYOS X",
            "CESTADO": "A",
            "CNRODNI": "72539751",
            "CTIPSER": "R",
        },
        {
            "ADESEXA": "TRIAJE",
            "CARCHIV": "S",
            "CCODACT": "00017192",
            "CDESSER": "TRIAJE",
            "CESTADO": "A",
            "CNRODNI": "72539751",
            "CTIPSER": "T",
        },
    ]
    lcCodigo = "Consentimientos"
    location = Config.PROJECT_DIR + "/tests"
    loConsentimiento = CConsentimiento(location + "/Docs", lcCodigo)

    f1 = open(location + "/Json/data.json", encoding="utf8")
    laData = json.load(f1)
    f1.close()
    loConsentimiento.setData(laData["DATA"])
    loConsentimiento.setConsentimiento(laconsentimiento)
    loConsentimiento.setExamenes(laexamenes)
    assert loConsentimiento.print_consentimiento() is True
