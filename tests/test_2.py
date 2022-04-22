#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import os
import sys

import pytest

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, os.path.split(basedir)[0])
from app.config import Config
from app.PDF.CActividad import CActividad

"""
{"CCODIGO": "000000", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "T"},
      {"CCODIGO": "S00001", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "T"},
      {"CCODIGO": "210201", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "C"},
      {"CCODIGO": "200213", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "O"},
      {"CCODIGO": "200214", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "O"},
      {"CCODIGO": "210301", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "A"},
      {"CCODIGO": "200302", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "P"},
      {"CCODIGO": "900000", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "D"},
      {"CCODIGO": "XXXX01", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "M"},
      {"CCODIGO": "XXXX03", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "M"},
      {"CCODIGO": "XXXX04", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "M"},
      {"CCODIGO": "XXXX09", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "M"},
      {"CCODIGO": "XXXX10", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "M"},
"""


@pytest.mark.parametrize(
    "input_a",
    [
        {"CCODIGO": "XXXX11", "CDESCRI": "PRUEBA ACTIVIDADES", "CTIPSER": "M"},
    ],
)
def test_factory_print(input_a):
    lcCodigo = input_a["CCODIGO"]
    location = Config.PROJECT_DIR + "/tests"
    loActividad = CActividad(location + "/Docs", lcCodigo)
    f = open(location + "/Json/" + lcCodigo + ".json", encoding="utf8")
    laDatos = json.load(f)
    f.close()
    loActividad.setDatos(laDatos["DATA"])

    f1 = open(location + "/Json/data.json", encoding="utf8")
    laData = json.load(f1)
    f1.close()
    loActividad.setData(laData["DATA"])
    loActividad.setExamen([input_a])
    assert loActividad.print_actividad() == True


# def test_monkey(monkeypatch):
# monkeypatch.setattr(Clase, funcion, lambda x:3)
# c=Clase
# assert  c.funcion() == 4
