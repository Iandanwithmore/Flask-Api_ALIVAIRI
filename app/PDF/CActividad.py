#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from itertools import groupby
from pathlib import Path
from typing import List, Tuple, Union

import requests
from app.CBase import CBase
from app.config import Config
from app.decorators import exception_handler
from app.PDF.PYFPDF import PYFPDF


class CActividad(CBase):
    loBase = CBase()

    def __init__(self, p_cPath, p_cCodigo):
        self.lcPath = p_cPath
        Path(p_cPath).mkdir(parents=True, exist_ok=True)
        self.lcCodigo = p_cCodigo
        self.paData = None
        self.paExamen = None
        self.paDatos = None
        self.cie10 = None
        self.cmp = None
        self.extras = None
        self.tmp = None
        self.error = None
        self.l_w = None
        self.l_h = None

    def setData(self, data: dict):
        self.paData = data

    def setExamen(self, examen: list):
        self.paExamen = examen

    def setDatos(self, datos: list):
        self.paDatos = datos

    def setExtras(self, extras: list):
        self.extras = extras

    def setCMP(self, cmp: list):
        self.cmp = cmp

    def setCie10(self, cie10: list):
        self.cie10 = cie10

    def setWidth(self, w):
        self.l_w = w

    def setHeigth(self, h):
        self.l_h = h

    # FUNCTIONS #
    @exception_handler(None)
    def str_si_no_x(self, item: dict) -> List[Union[str, str]]:
        if "NOPCION" not in item:
            raise KeyError(item)
        if int(item["NOPCION"]) != 0:
            return ["SI   (X)", "NO"]
        else:
            return ["SI", "NO   (X)"]

    @exception_handler([" ", "X"])
    def arr_si_no_x(self, item: dict) -> List[Union[str, str]]:
        if "NOPCION" not in item:
            raise KeyError(item)
        if int(item["NOPCION"]) != 0:
            return ["X", " "]
        else:
            return [" ", "X"]

    @exception_handler(None)
    def str_check_si(self, item: dict) -> str:
        if "NOPCION" not in item:
            raise KeyError(item)
        if int(item["NOPCION"]) != 0:
            return "X"
        else:
            return " "

    @exception_handler(None)
    def arr_str_select_x(self, item: dict) -> List[str]:
        res = [""]
        ploads = ["NOPCION", "MTABLA"]
        for key in ploads:
            if key not in item:
                raise KeyError(key)
        if (
            item["MTABLA"] is None
            or len(item["MTABLA"]) < 1
            or not isinstance(item["MTABLA"], list)
        ):
            raise AssertionError(item)
        else:
            i = item["NOPCION"]
            for lafila in item["MTABLA"]:
                if "CCODIGO" not in lafila:
                    raise KeyError(lafila)
                if "CDESCRI" not in lafila:
                    raise KeyError(lafila)
                if lafila["CCODIGO"] == i:
                    res += [lafila["CDESCRI"] + "   (X)"]
                else:
                    res += [lafila["CDESCRI"] + " "]
        return res

    @exception_handler(None)
    def list_select_x(self, item: dict) -> List[str]:
        res = []
        ploads = ["NOPCION", "MTABLA"]
        for key in ploads:
            if key not in item:
                raise KeyError(key)
        if (
            item["MTABLA"] is None
            or len(item["MTABLA"]) < 1
            or not isinstance(item["MTABLA"], list)
        ):
            raise AssertionError(item)
        else:
            i = item["NOPCION"]
            for lafila in item["MTABLA"]:
                if "CCODIGO" not in lafila:
                    raise KeyError(item)
                if lafila["CCODIGO"] == i:
                    res.append("X")
                else:
                    res.append("")
        return res

    @exception_handler(None)
    def tuple_select_x(self, item: dict) -> List[str]:
        res = []
        ploads = ["NOPCION", "MTABLA"]
        for key in ploads:
            if key not in item:
                raise KeyError(key)
        if (
            item["MTABLA"] is None
            or len(item["MTABLA"]) < 1
            or not isinstance(item["MTABLA"], list)
        ):
            raise AssertionError(item)
        else:
            i = item["NOPCION"]
            res = []
            for lafila in item["MTABLA"]:
                if "CCODIGO" not in lafila:
                    raise KeyError(lafila)
                if "CDESCRI" not in lafila:
                    raise KeyError(lafila)
                if lafila["CCODIGO"] == i:
                    res += [lafila["CDESCRI"], "(X)"]
                else:
                    res += [lafila["CDESCRI"], " "]
        return res

    @exception_handler(None)
    def arr_select_x_per_item(self, option, selection) -> List[Union[str, str]]:
        res = []
        ploads = ["CCODIGO", "CDESCRI"]
        for key in ploads:
            if key not in option:
                raise KeyError(key)
        if int(option["CCODIGO"]) == int(selection):
            res = [option["CDESCRI"], "X"]
        else:
            res = [option["CDESCRI"], " "]
        return res

    @exception_handler(False)
    def check_sino_square_h(
        self, p_oPdf, w, h, item: dict, border_1: int = 0, border_2: int = 0
    ) -> bool:
        ploads = ["NOPCION"]
        for key in ploads:
            if key not in item:
                raise KeyError(key)
        w5 = w / 2
        h5 = h / 2
        xboolean = self.arr_si_no_x(item)
        x = p_oPdf.get_x()
        y = p_oPdf.get_y()
        p_oPdf.cell(w5, h5, "SI", border_1, 0, "C")
        p_oPdf.cell(w5, h5, "NO", border_1, 0, "C")
        p_oPdf.set_xy(x, y + h5)
        p_oPdf.cell(w5, h5, xboolean[0], border_2, 0, "C")
        p_oPdf.cell(w5, h5, xboolean[1], border_2, 0, "C")
        p_oPdf.set_xy(x + w5 + w5, y + h5 + h5)
        return True

    @exception_handler(False)
    def check_sino_square_v(
        self, p_oPdf, w, h, item: dict, border_1: int = 0, border_2: int = 0
    ) -> bool:
        ploads = ["NOPCION"]
        for key in ploads:
            if key not in item:
                raise KeyError(key)
        w5 = w / 2
        h5 = h / 2
        xboolean = self.arr_si_no_x(item)
        x = p_oPdf.get_x()
        y = p_oPdf.get_y()
        p_oPdf.cell(w5, h5, "SI", border_1, 0, "C")
        p_oPdf.cell(w5, h5, xboolean[0], border_2, 0, "C")
        p_oPdf.set_xy(x, y + h5)
        p_oPdf.cell(w5, h5, "NO", border_1, 0, "C")
        p_oPdf.cell(w5, h5, xboolean[1], border_2, 0, "C")
        p_oPdf.set_xy(x + w5 + w5, y + h5 + h5)
        return True

    @exception_handler(False)
    def check_v(
        self,
        p_oPdf,
        w,
        h,
        item: dict,
        border_1: int = 0,
        border_2: int = 0,
        align_1: str = "L",
    ) -> bool:
        ploads = ["NOPCION", "MTABLA"]
        for key in ploads:
            if key not in item:
                raise KeyError(key)
        if (
            item["MTABLA"] is None
            or len(item["MTABLA"]) < 1
            or not isinstance(item["MTABLA"], list)
        ):
            raise AssertionError(item)
        x = p_oPdf.get_x()
        y = p_oPdf.get_y()
        arr = item["MTABLA"]
        if arr is not None:
            h = h / len(arr)
            w2 = w * 0.2
            w8 = w * 0.8
            for lafila in arr:
                if "CCODIGO" not in lafila:
                    raise KeyError(lafila)
                if "CDESCRI" not in lafila:
                    raise KeyError(lafila)
                lcheck = " "
                p_oPdf.cell(w8, h, lafila["CDESCRI"], border_1, 0, align_1)
                if lafila["CCODIGO"] == str(item["NOPCION"]):
                    lcheck = "X"
                p_oPdf.cell(w2, h, lcheck, border_2, 0, "C")
                y = y + h
                p_oPdf.set_xy(x, y)
            return True

    @exception_handler(False)
    def check_h(self, p_oPdf, w, h, item: dict) -> bool:
        ploads = ["NOPCION", "MTABLA"]
        for key in ploads:
            if key not in item:
                raise KeyError(key)
        if (
            item["MTABLA"] is None
            or len(item["MTABLA"]) < 1
            or not isinstance(item["MTABLA"], list)
        ):
            raise AssertionError(f"ERROR MTABLA:{item}")
        x = p_oPdf.get_x()
        arr = item["MTABLA"]
        if arr is not None:
            wt = w / len(arr)
            w8 = wt * 0.8
            w2 = wt * 0.2
            for lafila in arr:
                if "CCODIGO" not in lafila:
                    raise KeyError(lafila)
                if "CDESCRI" not in lafila:
                    raise KeyError(lafila)
                lcheck = " "
                p_oPdf.cell(w8, self.l_h, lafila["CDESCRI"], 1, 0, "C")
                if lafila["CCODIGO"] == str(item["NOPCION"]):
                    lcheck = "X"
                p_oPdf.cell(w2, self.l_h, lcheck, 1, 0, "C")
            p_oPdf.set_x(x + w)
            return True

    @exception_handler(False)
    def opt_h(self, p_oPdf, w, h, item: dict) -> bool:
        ploads = ["NOPCION", "MTABLA"]
        for key in ploads:
            if key not in item:
                raise KeyError(key)
        if (
            item["MTABLA"] is None
            or len(item["MTABLA"]) < 1
            or not isinstance(item["MTABLA"], list)
        ):
            raise AssertionError(item)
        x = p_oPdf.get_x()
        arr = item["MTABLA"]
        if arr is not None:
            wt = w / len(arr)
            for lafila in arr:
                if "CCODIGO" not in lafila:
                    raise KeyError(lafila)
                if "CDESCRI" not in lafila:
                    raise KeyError(lafila)
                lcheck = " "
                if lafila["CCODIGO"] == str(item["NOPCION"]):
                    lcheck = "X"
                p_oPdf.cell(wt, h, lcheck, 1, 0, "C")
                x += wt
                p_oPdf.set_x(x)
            return True

    @exception_handler(False)
    def opt_v(self, p_oPdf, w, h, item: dict) -> bool:
        ploads = ["NOPCION", "MTABLA"]
        for key in ploads:
            if key not in item:
                raise KeyError(key)
        l_tabla = len(item["MTABLA"])
        if (
            item["MTABLA"] is None
            or l_tabla < 1
            or not isinstance(item["MTABLA"], list)
        ):
            raise AssertionError(item)
        x = p_oPdf.get_x()
        arr = item["MTABLA"]
        if arr is not None:
            wt = w / len(arr)
            w85 = wt * 0.85
            w15 = wt * 0.15
            for lafila in arr:
                if "CCODIGO" not in lafila:
                    raise KeyError(lafila)
                if "CDESCRI" not in lafila:
                    raise KeyError(lafila)
                lcheck = " "
                p_oPdf.cell(w85, self.l_h, lafila["CDESCRI"], 0, 0, "C")
                if lafila["CCODIGO"] == str(item["NOPCION"]):
                    lcheck = "X"
                p_oPdf.cell(w15, h * 0.8, lcheck, 1, 0, "C")
            p_oPdf.set_x(x + w)
            return True

    @exception_handler(False)
    def opt_v_coment(self, p_oPdf, w, h, item, coment) -> bool:
        ploads = ["NOPCION", "MTABLA"]
        for key in ploads:
            if key not in item:
                raise KeyError(key)
        if (
            item["MTABLA"] is None
            or len(item["MTABLA"]) < 1
            or not isinstance(item["MTABLA"], list)
        ):
            raise AssertionError(item)
        x = p_oPdf.get_x()
        arr = item["MTABLA"]
        if arr is not None:
            wt = w / len(arr)
            for lafila in arr:
                if "CCODIGO" not in lafila:
                    raise KeyError(lafila)
                if "CDESCRI" not in lafila:
                    raise KeyError(lafila)
                lcheck = " "
                p_oPdf.cell(wt * 0.2, self.l_h, lafila["CDESCRI"], 0, 0, "C")
                if lafila["CCODIGO"] == str(item["NOPCION"]):
                    lcheck = "X"
                p_oPdf.cell(wt * 0.15, h * 0.8, lcheck, 1, 0, "C")
                x = x + wt * 0.35
            p_oPdf.set_x(x + 0.2)
            p_oPdf.cell(w * 0.637, self.l_h, coment, 1, 0, "L")
            p_oPdf.ln(self.l_h)
            return True

    def print_title(self, p_oPdf, p_cTitle):
        font_size = 17
        p_oPdf.set_font("Arial", "B", font_size)
        while p_oPdf.get_string_width(p_cTitle) > self.l_w:
            font_size -= 1
            p_oPdf.set_font("Arial", "B", font_size)
        p_oPdf.cell(0, 1, p_cTitle, 0, 1, "C")
        p_oPdf.set_font("Arial", "", 6)

    # END FUNCTIONS #

    # PRINT WITH REQUESTS #
    def om_cmp(self, p_oPdf) -> bool:
        if not self.mx_data_cmp():
            return False
        if not self.print_cmp(p_oPdf):
            return False
        return True

    @exception_handler(False)
    def mx_data_cmp(self) -> bool:
        self.cmp = []
        ploads = {"CCODPLA": self.paData["CCODACT"], "CCODUSU": "0000"}
        llOk = requests.get(Config.API_URL + "/actividad/cmp", params=ploads).json()
        if llOk["OK"]:
            self.cmp = llOk["DATA"]
        return True

    @exception_handler(False)
    def mx_print_cmp(self, p_oPdf) -> bool:
        if self.cmp is not None:
            p_oPdf.cell(0, 1, "CMP", 1, 0, "L")
            p_oPdf.set_border(1)
            w1 = self.l_w * 0.1
            w9 = self.l_w * 0.9
            for item in self.cmp:
                if ["CCODIGO", "CDESCRI"] in item:
                    p_oPdf.set_bolds(["B", " "])
                    p_oPdf.row([item["CCODIGO"], item["CDESCRI"]], [w1, w9])
            return True

    def om_cie10(self, p_oPdf) -> bool:
        if not self.mx_data_cie10():
            return False
        if not self.print_cmp(p_oPdf):
            return False
        return True

    @exception_handler(False)
    def mx_data_cie10(self) -> bool:
        self.cie10 = []
        ploads = {"CCODPLA": self.paData["CCODACT"], "CCODUSU": "0000"}
        llOk = requests.get(Config.API_URL + "/actividad/cie10", params=ploads).json()
        if llOk["OK"]:
            self.cie10 = llOk["DATA"]
        return True

    @exception_handler(False)
    def mx__print_cie10(self, p_oPdf) -> bool:
        if self.cie10 is not None:
            p_oPdf.cell(self.l_w, self.l_h, "CIE10", 1, 0, "L")
            p_oPdf.set_border(1)
            w1 = self.l_w * 0.1
            w9 = self.l_w * 0.9
            for item in self.cie10:
                if ["CCODIGO", "CDESCRI"] in item:
                    p_oPdf.set_bolds(["B", " "])
                    p_oPdf.row([item["CCODIGO"], item["CDESCRI"]], [w1, w9])
            p_oPdf.ln(self.l_h)
            return True

    @exception_handler(False)
    def mx__print_cie10_for_json_actividad(self, p_oPdf) -> bool:
        if self.cie10 is not None:
            p_oPdf.cell(self.l_w, self.l_h, "CIE10", 1, 1, "L")
            w1 = self.l_w * 0.1
            w9 = self.l_w * 0.9
            for item in self.cie10:
                p_oPdf.cell(self.l_w, self.l_h, item, 1, 1, "L")
            p_oPdf.ln(self.l_h)
            return True

    def om_extras(self, p_oPdf) -> bool:
        if not self.mx_data_extras():
            return False
        if not self.print_extras(p_oPdf):
            return False
        return True

    @exception_handler(False)
    def mx_data_extras(self) -> bool:
        self.extras = []
        ploads = {"CCODACT": self.paData["CCODACT"], "CCODUSU": "0000"}
        llOk = requests.get(Config.API_URL + "/actividad/extra", params=ploads).json()
        if not llOk["OK"]:
            self.extras["MOBSERV"] = ""
            self.extras["MRECOME"] = ""
            self.extras["MRECOME"] = ""
        self.extras = llOk["DATA"]
        return True

    @exception_handler(False)
    def mx_print_extras(self, p_oPdf) -> bool:
        p_oPdf.set_font("Arial", "B", 6)
        p_oPdf.cell(self.l_w, self.l_h, "Observacion", 1, 1, "L")
        p_oPdf.set_font("Arial", "", 6)
        p_oPdf.multi_cell(self.l_w, self.l_h, self.extras["MOBSERV"], 1, "L")
        p_oPdf.set_font("Arial", "B", 6)
        p_oPdf.cell(self.l_w, self.l_h, "Recomendacion", 1, 1, "L")
        p_oPdf.set_font("Arial", "", 6)
        p_oPdf.multi_cell(self.l_w, self.l_h, self.extras["MRECOME"], 1, "L")
        p_oPdf.set_font("Arial", "B", 6)
        p_oPdf.cell(self.l_w, self.l_h, "Conclusion", 1, 1, "L")
        p_oPdf.set_font("Arial", "", 6)
        p_oPdf.multi_cell(self.l_w, self.l_h, self.extras["MCONCLU"], 1, "L")
        return True

    def om_conclusiones(self, p_oPdf) -> bool:
        if not self.mx_data_conclusiones():
            return False
        if not self.mx_print_conclusiones(p_oPdf):
            return False
        return True

    @exception_handler(False)
    def mx_data_conclusiones(self) -> bool:
        self.tmp = []
        ploads = {"CCODPLA": self.paData["CCODPLA"], "CCODUSU": "0000"}
        llOk = requests.get(Config.API_URL + "/plan/conclusiones", params=ploads).json()
        if llOk["OK"]:
            raise ValueError(llOk["DATA"])
        self.tmp = llOk["DATA"]
        return True

    @exception_handler(False)
    def mx_print_conclusiones(self, p_oPdf) -> bool:
        for item in self.tmp:
            p_oPdf.set_font("Arial", "B", 6)
            p_oPdf.cell(self.l_w, self.l_h, item["CDESCRI"], 1, 0, "C")
            p_oPdf.set_font("Arial", "", 6)
            p_oPdf.multi_cell(self.l_w, self.l_h, item["CDESCRI"], 1, "L")
        return True

    def om_diagnosticos(self, p_oPdf) -> bool:
        if not self.mx_data_diagnosticos():
            return False
        if not self.mx_print_diagnosticos(p_oPdf):
            return False
        return True

    @exception_handler(False)
    def mx_data_diagnosticos(self) -> bool:
        ploads = {"CCODPLA": self.paData["CCODPLA"], "CCODUSU": "0000"}
        llOk = requests.get(Config.API_URL + "/plan/cie10", params=ploads).json()
        if llOk["OK"]:
            raise ValueError(llOk["DATA"])
        self.tmp = llOk["DATA"]
        return True

    @exception_handler(False)
    def mx_print_diagnosticos(self, p_oPdf) -> bool:
        p_oPdf.set_font("Arial", "", 6)
        for item in self.tmp:
            p_oPdf.cell(self.l_w, self.l_h, item["CDESCRI"], 0, 1, "C")
        return True

    def om_experiencia_laboral(self, p_oPdf) -> bool:
        if not self.mx_data_experiencia_laboral():
            return False
        if not self.mx_print_experiencia_laboral_1(p_oPdf):
            return False
        return True

    @exception_handler(False)
    def mx_data_experiencia_laboral(self) -> bool:
        ploads = {"CCODPLA": self.paData["CCODPLA"], "CCODUSU": "0000"}
        llOk = requests.get(
            Config.API_URL + "/plan/experiencia_laboral",
            params=ploads,
        ).json()
        if llOk["OK"]:
            raise ValueError(llOk["DATA"])
        self.tmp = llOk["DATA"]
        return True

    @exception_handler(False)
    def mx_print_experiencia_laboral_1(self, p_oPdf) -> bool:
        if self.tmp is not None:
            w6 = self.l_w * 0.6
            p_oPdf.set_font("Arial", "B", 6)
            p_oPdf.set_border(1)
            p_oPdf.row(
                [
                    "FECHA",
                    "EMPRESA",
                    "ACTIVIDAD",
                    "PUESTO",
                    "TIEMPO SUB",
                    "CAUSA DE RETIRO",
                ],
                [w6, w6, w6, w6, w6, w6],
            )
            p_oPdf.set_font("Arial", "", 6)
            for item in self.tmp:
                p_oPdf.row(
                    [
                        item["TINIACT"],
                        item["CDESCRI"],
                        item["CEMPACT"],
                        item["CPUESTO"],
                        item["NSUBSUE"],
                        item["CCAURET"],
                    ],
                    [w6, w6, w6, w6, w6, w6],
                )
            p_oPdf.set_border(0)
            return True

    @exception_handler(False)
    def mx_print_experiencia_laboral_2(self, p_oPdf) -> bool:
        if self.tmp is not None:
            w6 = self.l_w * 0.6
            w2 = self.l_w * 0.2
            w7 = self.l_w * 0.7
            p_oPdf.set_font("Arial", "B", 6)
            p_oPdf.set_border(1)
            p_oPdf.row(
                [
                    "FECHA INICIO",
                    "FECHA FIN",
                    "EMPRESA",
                    "ALTITUD",
                    "AREA",
                    "OCUPACION",
                    "TIEMPO DE TRABAJO" "TIPO EPP",
                ],
                [w6, w6, w6, w6, w6, w6],
            )
            p_oPdf.row(
                [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "TIEMPO SUBSUELO",
                    "TIEMPO SUPERFICIE",
                    "RUIDO",
                    "POLVO",
                    "ERGO",
                    "VIBRA",
                    "ELECT",
                    "QUIMI",
                    "OTROS",
                ],
                [w6, w6, w6, w6, w6, w6, w6, w2, w2, w7, w7, w7, w7],
            )
            p_oPdf.set_font("Arial", "", 6)
            for item in self.tmp:
                cal1 = ("\n" + str(item["NHORTRA"] or 1) / (item["BRRUIDO"] or 1)) + "%"
                cal2 = ("\n" + str(item["NHORTRA"] or 1) / (item["BRPOLVO"] or 1)) + "%"
                cal3 = ("\n" + str(item["NHORTRA"] or 1) / (item["BRERGON"] or 1)) + "%"
                cal4 = ("\n" + str(item["NHORTRA"] or 1) / (item["BRVIBRA"] or 1)) + "%"
                cal5 = ("\n" + str(item["NHORTRA"] or 1) / (item["BRELECT"] or 1)) + "%"
                cal6 = ("\n" + str(item["NHORTRA"] or 1) / (item["BRQUIMI"] or 1)) + "%"
                cal7 = ("\n" + str(item["NHORTRA"] or 1) / (item["BROTROS"] or 1)) + "%"
                p_oPdf.row(
                    [
                        item["TINIACT"],
                        item["TFINACT"],
                        item["CDESCRI"],
                        item["CDESARE"],
                        item["CPUESTO"],
                        item["NSUBSUE"],
                        item["NSUPERF"],
                        item["BRRUIDO"] + cal1,
                        item["BRPOLVO"] + cal2,
                        item["BRERGON"] + cal3,
                        item["BRVIBRA"] + cal4,
                        item["BRELECT"] + cal5,
                        item["BRQUIMI"] + cal6,
                        item["BROTROS"] + cal7,
                    ],
                    [w6, w6, w6, w6, w6, w6],
                )
            p_oPdf.set_border(0)
            return True

    # END PRINT WITH REQUESTS #

    # PRINT FUNCTION #
    @exception_handler(False)
    def mx_print_aptitud(self, p_oPdf):
        arr = [
            {"CCODIGO": "0", "CDESCRI": "APTO"},
            {"CCODIGO": "1", "CDESCRI": "APTO CON RESTRICCION"},
            {"CCODIGO": "2", "CDESCRI": "NO APTO TEMPORAL"},
            {"CCODIGO": "4", "CDESCRI": "NO APTO"},
        ]
        item = {"NOPCION": self.paData["CAPTITU"], "MTABLA": arr}
        xo = p_oPdf.get_x()
        yo = p_oPdf.get_y()
        w4 = self.l_w * 0.4
        w6 = self.l_w * 0.6
        self.check_v(p_oPdf, w4, 1.8, item, 1, 1)
        p_oPdf.set_xy(xo + w4, yo)
        p_oPdf.multi_cell(w6, 1.8, (self.extras["MOBSERV"] or " "), 0, "L")
        p_oPdf.rect(xo + +w4, yo, w6, 1.8)
        p_oPdf.ln(self.l_h)
        return True

    @exception_handler(False)
    def print_signature_by_ccodusu(self, p_oPdf) -> bool:
        y = p_oPdf.gety_end_page()
        loFirma = Config.PATH_PDF_SRC + "/" + self.paData["CUSUCOD"] + ".jpg"
        if Path(loFirma).is_file():
            p_oPdf.image(loFirma, 1, y, 3.5, 2.5)
        return True

    @exception_handler(False)
    def print_signature_by_cnrodni(self, p_oPdf) -> bool:
        y = p_oPdf.gety_end_page()
        loFirma = Config.PATH_FILE + "/" + self.paData["CNRODNI"] + "/" + "FIRMA.jpg"
        if Path(loFirma).is_file():
            p_oPdf.image(loFirma, 17, y, 3.5, 2.5)
        return True

    @exception_handler(False)
    def print_signatures(self, p_oPdf) -> bool:
        y = p_oPdf.gety_end_page()
        loFirma = Config.PATH_PDF_SRC + "/" + self.paData["CUSUCOD"] + ".jpg"
        if Path(loFirma).is_file():
            p_oPdf.image(loFirma, 1, y, 3.5, 2.5)
        loHuella = Config.PATH_FILE + "/" + self.paData["CNRODNI"] + "/" + "HUELLA.jpg"
        if Path(loHuella).is_file():
            p_oPdf.image(loHuella, 15, y, 1.5, 2)
        loFirma = Config.PATH_FILE + "/" + self.paData["CNRODNI"] + "/" + "FIRMA.jpg"
        if Path(loFirma).is_file():
            p_oPdf.image(loFirma, 17, y, 3.5, 2.5)
        return True

    # END PRINT FUNCTION #

    # SUB FUNCTIONS #
    @exception_handler(False)
    def sub_header(self, loPdf) -> bool:
        loPdf.set_border(1)
        loPdf.setHeader(self.paData["CDESSER"])
        loPdf.set_font("Arial", "", 6)
        loPdf.set_bolds(["B", " ", "B", " "])
        w1 = self.l_w * 0.1
        w15 = self.l_w * 0.15
        w2 = self.l_w * 0.2
        w25 = self.l_w * 0.25
        w4 = self.l_w * 0.4
        w8 = self.l_w * 0.8
        loPdf.row(
            [
                "COD.ATENCION :",
                self.paData["CCODACT"],
                "FECHA ATENCIÓN",
                self.paData["TCITA"],
            ],
            [w2, w25, w15, w4],
        )
        loPdf.set_bolds(["B", " ", "B", " ", "B", " "])
        loPdf.row(
            [
                "DOC.IDENTIDAD :",
                self.paData["CNRODOC"],
                "F.NACIMIENTO",
                self.paData["TNACIMI"],
                " EDAD :",
                self.paData["NEDAD"],
            ],
            [w2, w25, w15, w1, w2, w1],
        )
        loPdf.set_bolds(["B", " "])
        loPdf.row(
            [
                "APELLIDOS Y NOMBRES:",
                self.paData["CNOMBRE"] + "   (SEXO :" + self.paData["CDESSEX"] + ")",
            ],
            [w2, w8],
        )
        if self.paData["CTIPPLA"] != "E":
            loPdf.set_bolds(["B", " "])
            loPdf.row(
                [
                    "EMPRESA :",
                    self.paData["CDESEMP"][0:20] + "(" + self.paData["CDESSED"] + ")",
                ],
                [w2, w8],
            )
            loPdf.set_bolds(["B", " ", "B", " "])
            loPdf.row(
                [
                    "TIPO EXAMEN :",
                    self.paData["CDESTIP"],
                    "PERFIL",
                    self.paData["CDESPER"],
                ],
                [w2, w25, w15, w4],
            )
            loPdf.set_bolds(["B", " "])
            loPdf.row(
                ["PUESTO LABORAL :", self.paData["CDESPUE"]],
                [w2, w8],
            )
        loPdf.set_border(0)
        loPdf.ln(0.2)
        return True

    @exception_handler(False)
    def sub_antecedentes(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "M409",
            "M493",
            "M636",
            "M637",
            "M638",
            "M639",
            "M640",
            "M641",
            "M642",
            "M643",
            "M644",
            "M645",
            "M646",
            "M647",
            "M648",
            "M649",
            "M650",
            "M651",
            "M652",
            "M653",
            "M654",
            "M655",
            "M656",
            "M657",
            "M658",
            "M659",
            "M660",
            "M661",
            "M662",
            "M663",
            "M664",
            "M665",
            "M666",
            "M667",
            "M668",
            "M669",
            "M575",
            "M576",
            "M577",
            "M578",
            "M579",
            "M580",
            "M581",
            "M582",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)
        # INIT EXEC #
        w02 = self.l_w * 0.02
        w12 = self.l_w * 0.12
        w13 = self.l_w * 0.13
        w15 = self.l_w * 0.15
        w25 = self.l_w * 0.25
        w35 = self.l_w * 0.35
        w85 = self.l_w * 0.85
        self.print_title(
            loPdf,
            "ANTECEDENTES OCUPACIONALES",
        )
        loPdf.cell(self.l_w, self.l_h, "ANTECEDENTES PATOLOGICOS PERSONALES", 1, 1, "C")
        loPdf.set_font("Arial", "", 6)
        loPdf.ln(0.2)
        loPdf.set_border(1)
        idx = 0
        xboolean1 = self.str_check_si(LADATOS[idx])
        xboolean2 = self.str_check_si(LADATOS[idx + 1])
        xboolean3 = self.str_check_si(LADATOS[idx + 2])
        xboolean4 = self.str_check_si(LADATOS[idx + 3])
        xboolean5 = self.str_check_si(LADATOS[idx + 4])
        xboolean6 = self.str_check_si(LADATOS[idx + 5])
        xboolean7 = self.str_check_si(LADATOS[idx + 6])
        loPdf.row(
            [
                "Alergias",
                xboolean1,
                "Diabetes",
                xboolean2,
                "TBC",
                xboolean3,
                "Hepatitis B",
                xboolean4,
                "H.Col",
                xboolean5,
                "Pt. Columna",
                xboolean6,
                "Qx.",
                xboolean7,
            ],
            [
                w12,
                w02,
                w12,
                w02,
                w13,
                w02,
                w12,
                w02,
                w12,
                w02,
                w13,
                w02,
                w12,
                w02,
            ],
        )
        idx += 7
        xboolean1 = self.str_check_si(LADATOS[idx])
        xboolean2 = self.str_check_si(LADATOS[idx + 1])
        xboolean3 = self.str_check_si(LADATOS[idx + 2])
        xboolean4 = self.str_check_si(LADATOS[idx + 3])
        xboolean5 = self.str_check_si(LADATOS[idx + 4])
        xboolean6 = self.str_check_si(LADATOS[idx + 5])
        xboolean7 = self.str_check_si(LADATOS[idx + 6])
        loPdf.row(
            [
                "Asma",
                xboolean1,
                "HTA",
                xboolean2,
                "ITS",
                xboolean3,
                "Tifoidea",
                xboolean4,
                "Prob CV",
                xboolean5,
                "HBP",
                xboolean6,
                "Otros",
                xboolean7,
            ],
            [
                w12,
                w02,
                w12,
                w02,
                w13,
                w02,
                w12,
                w02,
                w12,
                w02,
                w13,
                w02,
                w12,
                w02,
            ],
        )
        idx += 7
        xboolean1 = self.str_check_si(LADATOS[idx])
        xboolean2 = self.str_check_si(LADATOS[idx + 1])
        xboolean3 = self.str_check_si(LADATOS[idx + 2])
        xboolean4 = self.str_check_si(LADATOS[idx + 3])
        xboolean5 = self.str_check_si(LADATOS[idx + 4])
        xboolean6 = self.str_check_si(LADATOS[idx + 5])
        loPdf.row(
            [
                "Bronquitis",
                xboolean1,
                "Neoplasia",
                xboolean2,
                "Convulsione",
                xboolean3,
                "H.tg",
                xboolean4,
                "Atropatía",
                xboolean5,
                "Migraña",
                xboolean6,
            ],
            [
                w12,
                w02,
                w12,
                w02,
                w13,
                w02,
                w12,
                w02,
                w12,
                w02,
                w13,
                w02,
            ],
        )
        loPdf.ln(0.2)
        idx += 6
        loPdf.row(["Otros:", LADATOS[idx]["CRESULT"]], [w15, w85])
        idx += 1
        loPdf.row(
            ["Quemaduras:", LADATOS[idx]["CRESULT"]],
            [w15, w85],
        )
        idx += 1
        loPdf.row(
            [
                "Cirugías:",
                LADATOS[idx]["CRESULT"],
                "Intoxicaciones:",
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w15, w35, w15, w35],
        )
        loPdf.ln(0.2)
        loPdf.set_aligns(["C", "C", "C", "C"])
        loPdf.row(
            ["Hábitos nocivos", "TIPO", "CANTIDAD", "FRECUENCIA"],
            [w25, w25, w25, w25],
        )
        idx += 2
        loPdf.row(
            [
                "Alcohol",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
                LADATOS[idx + 2]["CRESULT"],
            ],
            [w25, w25, w25, w25],
        )
        idx += 3
        loPdf.row(
            [
                "Tabaco",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
                LADATOS[idx + 2]["CRESULT"],
            ],
            [w25, w25, w25, w25],
        )
        idx += 3
        loPdf.row(
            [
                "Drogas",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
                LADATOS[idx + 2]["CRESULT"],
            ],
            [w25, w25, w25, w25],
        )
        idx += 3
        loPdf.row(
            [
                "Medicamentos",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
                LADATOS[idx + 2]["CRESULT"],
            ],
            [w25, w25, w25, w25],
        )

        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "ANTECEDENTES PATOLOGICOS FAMILIARES", 1, 1, "C")
        loPdf.set_font("Arial", "", 6)
        idx += 3
        loPdf.row(
            [
                "Padre:",
                LADATOS[idx]["CRESULT"],
                "Madre:",
                LADATOS[idx + 1]["CRESULT"],
                "Hermanos:",
                LADATOS[idx + 2]["CRESULT"],
                "N°",
                LADATOS[idx + 3]["CRESULT"],
            ],
            [
                w12,
                w13,
                w12,
                w13,
                w12,
                w13,
                w12,
                w13,
            ],
        )
        idx += 4
        loPdf.row(
            [
                "Esposo(a):",
                LADATOS[idx]["CRESULT"],
                "N°",
                LADATOS[idx + 1]["CRESULT"],
                "Hijos vivos:",
                LADATOS[idx + 2]["CRESULT"],
                "Hijos Fallecidos:",
                LADATOS[idx + 3]["CRESULT"],
            ],
            [
                w12,
                w13,
                w12,
                w13,
                w12,
                w13,
                w12,
                w13,
            ],
        )
        return True

    @exception_handler(False)
    def sub_audiologico_cuadro(
        self, loPdf, p_l_nx: float, p_r_nx: float, p_ny: float
    ) -> bool:
        # VAL #
        arr_ind = [
            "M034",
            "M035",
            "M036",
            "M037",
            "M038",
            "M039",
            "M040",
            "M041",
            "M042",
            "M043",
            "M044",
            "M045",
            "M046",
            "M047",
            "M048",
            "M049",
            "M050",
            "M051",
            "M052",
            "M053",
            "M054",
            "M055",
            "M056",
            "M057",
            "M058",
            "M059",
            "M060",
            "M061",
            "M062",
            "M063",
            "M064",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(int(find["CRESULT"]))
            arr_ind.remove(item)
        v_aerea_d = LADATOS[0:7]
        v_aerea_i = LADATOS[8:15]
        v_osea_d = LADATOS[16:23]
        v_osea_i = LADATOS[24:32]
        xo = p_l_nx
        yo = p_ny
        len_x = 0.75  # ancho de la celda
        len_y = 0.45  # alto de la celda
        self.sub_plano_cartesiano(loPdf, p_l_nx, yo, len_x, len_y)
        self.sub_plano_cartesiano(loPdf, p_r_nx, yo, len_x, len_y)
        # izquierdo
        # aerea
        x = p_l_nx
        y = yo + (v_aerea_d[0] + 10) / 10 * len_y
        loPdf.image(
            Config.PATH_PDF_SRC + "/circle-red.png",
            x - 0.1,
            y - 0.1,
            0.2,
            0.2,
        )
        loPdf.set_draw_color(255, 0, 0)
        for item_d in v_aerea_d:
            x2 = x + len_x
            y2 = yo + (item_d + 10) / 10 * len_y
            loPdf.line(x, y, x2, y2)
            loPdf.image(
                Config.PATH_PDF_SRC + "/circle-red.png",
                x2 - 0.1,
                y2 - 0.1,
                0.2,
                0.2,
            )
            x = x2
            y = y2
        # osea
        x = xo
        y = yo + (v_osea_d[0] + 10) / 10 * len_y
        loPdf.image(
            Config.PATH_PDF_SRC + "/less_red.png",
            x - 0.1,
            y - 0.1,
            0.2,
            0.2,
        )
        for item_o_d in v_osea_d:
            x2 = x + len_x
            y2 = yo + (item_o_d + 10) / 10 * len_y
            loPdf.image(
                Config.PATH_PDF_SRC + "/less_red.png",
                x2 - 0.1,
                y2 - 0.1,
                0.2,
                0.2,
            )
            x = x2
            y = y2
        # derecho
        # aerea
        x = p_r_nx
        y = yo + (v_aerea_i[0] + 10) / 10 * len_y
        loPdf.image(
            Config.PATH_PDF_SRC + "/x-blue.png",
            x - 0.1,
            y - 0.1,
            0.2,
            0.2,
        )
        loPdf.set_draw_color(0, 0, 255)
        for item_i in v_aerea_i:
            x2 = x + len_x
            y2 = yo + (item_i + 10) / 10 * len_y
            loPdf.line(x, y, x2, y2)
            loPdf.image(
                Config.PATH_PDF_SRC + "/x-blue.png",
                x2 - 0.1,
                y2 - 0.1,
                0.2,
                0.2,
            )
            x = x2
            y = y2
        # osea
        x = xo
        y = yo + (v_osea_i[0] + 10) / 10 * len_y
        loPdf.image(
            Config.PATH_PDF_SRC + "/more_blue.png",
            x - 0.1,
            y - 0.1,
            0.2,
            0.2,
        )
        for item_o_i in v_osea_i:
            x2 = x + len_x
            y2 = yo + (item_o_i + 10) / 10 * len_y
            loPdf.image(
                Config.PATH_PDF_SRC + "/more_blue.png",
                x2 - 0.1,
                y2 - 0.1,
                0.2,
                0.2,
            )
            x = x2
            y = y2
        loPdf.set_draw_color(0)
        return True

    @exception_handler(False)
    def sub_plano_cartesiano(
        self, loPdf, p_x: float, p_y: float, w_x: float, w_y: float
    ) -> bool:
        valores_eje_x = [
            "250",
            "500",
            "1000",
            "2000",
            "3000",
            "4000",
            "6000",
            "8000",
        ]
        valores_eje_y = [
            "-10",
            "0",
            "10",
            "20",
            "30",
            "40",
            "50",
            "60",
            "70",
            "80",
            "90",
            "100",
            "110",
        ]
        cant_lineas_ver = len(valores_eje_x)
        cant_lineas_hor = len(valores_eje_y)
        # dibujar lineas del plano cartesiano
        loPdf.set_line_width(0.01)
        loPdf.set_draw_color(200)
        # dibujar lineas del plano cartesiano horizontales
        x = p_x
        y = p_y + w_y
        for i in range(1, cant_lineas_hor):
            loPdf.line(x - 0.1, y, x + (cant_lineas_ver - 1) * w_x + 0.1, y)
            y += w_y
        yf = y + w_y  # yf para saber donde acaba el gráfico
        # dibujar lineas del plano cartesiano verticales
        x = p_x + w_x
        y = p_y
        for i in range(1, cant_lineas_ver - 1):
            loPdf.line(x, y - 0.1, (y + (cant_lineas_hor - 1) * w_y) + 0.1, y)
            x += w_x

        # dibujar eje x del plano cartesiano
        x = p_x
        y = p_y
        loPdf.set_line_width(0.08)
        loPdf.line(x - 0.1, y, (x + (cant_lineas_ver - 1) * w_x) + 0.1, y)
        x = p_x - 0.22
        y = p_y - 0.2
        loPdf.set_line_width(0.02)
        for i in range(cant_lineas_ver):
            loPdf.text(x, y, valores_eje_x[i])
            x += w_x
        # dibujar ejes y del plano cartesiano
        x = p_x
        y = p_y
        loPdf.set_line_width(0.08)
        loPdf.line(x, y - 0.1, x, (y + (cant_lineas_hor - 1) * w_y) + 0.1)
        x = p_x + w_x * (cant_lineas_ver - 1)
        loPdf.line(x, y - 0.1, x, (y + (cant_lineas_hor - 1) * w_y) + 0.1)
        x = p_x - 0.48
        y = p_y + 0.06
        x1 = p_x + w_x * (cant_lineas_ver - 1) + 0.16
        loPdf.set_line_width(0.02)
        for i in range(cant_lineas_hor):
            loPdf.text(x, y, valores_eje_y[i])
            loPdf.text(x1, y, valores_eje_y[i])
            y += w_y
        # dibujar lineas intermedia
        x = p_x + w_x * (cant_lineas_ver - 1)
        y = p_y + (25 + 10) / 10 * w_y
        loPdf.line(p_x, y, x, y)

        loPdf.set_line_width(0.02)  # reverts to default
        loPdf.set_xy(p_x, yf)
        return True

    @exception_handler(False)
    def sub_agudeza_visual(self, loPdf) -> bool:
        # VAL #
        arr_ind = ["M501", "M502", "M503", "M504", "M505", "M727", "M506", "M728"]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)

        # DO EXEC #
        # AGUDEZA VISUAL
        w3 = self.l_w * 0.3
        w4 = self.l_w * 0.4
        w15 = self.l_w * 0.15
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w4, self.l_h * 2, "AGUDEZA VISUAL", 1, 0, "C")
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(w3, self.l_h, "SIN CORRECTORES", 1, 0, "C")
        loPdf.cell(w3, self.l_h, "CON CORRECTORES", 1, 1, "C")
        loPdf.cell(w4)
        loPdf.cell(w15, self.l_h, "OJO DERECHO", 1, 0, "C")
        loPdf.cell(w15, self.l_h, "OJO IZQUIERDO", 1, 0, "C")
        loPdf.cell(w15, self.l_h, "OJO DERECHO", 1, 0, "C")
        loPdf.cell(w15, self.l_h, "OJO IZQUIERDO", 1, 1, "C")

        loPdf.set_border(1)
        loPdf.set_align("C")
        idx = 0
        loPdf.row(
            [
                "VISION DE LEJOS",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
                LADATOS[idx + 2]["CRESULT"],
                LADATOS[idx + 3]["CRESULT"],
            ],
            [w4, w15, w15, w15, w15],
        )
        idx += 4
        loPdf.row(
            [
                "VISION DE CERCA",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
                LADATOS[idx + 2]["CRESULT"],
                LADATOS[idx + 3]["CRESULT"],
            ],
            [w4, w15, w15, w15, w15],
        )
        loPdf.set_border(0)
        loPdf.ln()
        return True

    @exception_handler(False)
    def sub_profundidad(self, loPdf) -> bool:
        # VAL #
        arr_ind = ["M527", "M528", "M529", "M530", "M531"]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)

        idx = 0
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w * 0.4, self.l_h, "OJO SECO (BUT):10 SEGUNDOS", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[idx]["CRESULT"], 0, "L")
        idx += 1
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w * 0.4, self.l_h, "OJO SECO (BUT):10 SEGUNDOS", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        w1 = self.l_w * 0.1
        w9 = self.l_w * 0.9
        loPdf.row(["PIO OD:", LADATOS[idx]["CRESULT"]], [w1, w9])
        idx += 1
        loPdf.row(["PIO OI:", LADATOS[idx]["CRESULT"]], [w1, w9])
        idx += 1
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w * 0.4, self.l_h, "FONDO DE OJO (POLO POSTERIOR)", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.row(["OD:", LADATOS[idx]["CRESULT"]], [w1, w9])
        idx += 1
        loPdf.row(["OI:", LADATOS[idx]["CRESULT"]], [w1, w9])
        return True

    # END SUB FUNCTIONS #

    # PRINT ACTIVITIES #
    @exception_handler(False)
    def print_lab(self, loPdf) -> bool:
        # VAL idxES ?
        # tmp = [d for d in self.paDatos if d.get("CCODIND")[0] == "L"]
        LADATOS = [list(v) for k, v in groupby(self.paDatos, key=lambda x: x["NORDEN"])]

        self.print_title(
            loPdf,
            "LABORATORIO",
        )
        loPdf.set_border(1)
        loPdf.row(["ANALISIS", "RESULTADO", "UNIDAD", "RANGO"], [7, 4, 2.4, 5])
        loPdf.set_border(0)
        i = 0
        w2 = self.l_w * 0.2
        for laData in self.paExamen:
            loPdf.set_font("Arial", "B", 6)
            loPdf.cell(w2, self.l_h, laData["CDESCRI"], 1, 0, "C")
            loPdf.set_font("Arial", "", 6)
            if LADATOS[i]:
                for lafila in LADATOS[i]:
                    loPdf.row(
                        [
                            lafila["CIMPRIM"],
                            lafila["CRESULT"],
                            lafila["CDESUNI"],
                            lafila["CRANGO"],
                        ],
                        [7, 4, 2.4, 5],
                    )
            if laData["CEXTRA"]:
                loPdf.set_font("Arial", "", 6)
                loPdf.cell(w2, self.l_h, laData["CEXTRA"], 1, 0, "C")
            loPdf.cell(
                w2,
                self.l_h,
                "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                1,
                0,
                "C",
            )
            i += 1
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_triaje(self, loPdf) -> bool:
        # VAL #
        LADATOS = [d for d in self.paDatos if d.get("CCODIND")[0] == "T"]

        # INIT EXEC #
        self.print_title(
            loPdf,
            "TRIAJE",
        )
        # DO EXEC
        lnidx = len(LADATOS)
        w1 = self.l_w * 0.1
        w2 = self.l_w * 0.2
        ln = 0
        for idx in range(0, lnidx):
            if ln > 18:
                loPdf.ln()
                ln = 0
            loPdf.cell(w1, self.l_h, LADATOS[idx]["CIMPRIM"], 0, 0, "L")
            loPdf.cell(
                w1,
                self.l_h,
                LADATOS[idx]["CRESULT"] + "   " + LADATOS[idx]["CDESUNI"],
                1,
                0,
                "L",
            )
            ln += w2
        return True

    @exception_handler(False)
    def print_rx(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "R001",
            "R002",
            "R003",
            "R004",
            "R005",
            "R006",
            "R007",
            "R008",
            "R009",
            "R010",
            "R011",
            "R012",
            "R013",
            "R014",
            "R015",
            "R016",
            "R017",
            "R018",
            "R019",
            "R020",
            "R021",
            "R022",
            "R023",
            "R024",
            "R025",
            "R026",
            "R027",
            "R028",
            "R029",
            "R030",
            "R031",
            "R032",
            "R033",
            "R034",
            "R035",
            "R036",
            "R037",
            "R038",
            "R039",
            "R040",
            "R041",
            "R042",
            "R043",
            "R044",
            "R045",
            "R046",
            "R047",
            "R048",
            "R049",
            "R050",
            "R051",
            "R052",
            "R053",
            "R054",
            "R055",
            "R056",
            "R057",
            "R058",
            "R059",
            "R060",
            "R061",
            "R062",
            "R063",
            "R064",
            "R065",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)

        # INIT EXEC #
        self.print_title(loPdf, "INFORME RADIOGRAFICO CON METODOLOGIA OIT")
        # DO EXEC #
        w03 = self.l_w * 0.03
        w04 = self.l_w * 0.04
        w06 = self.l_w * 0.06
        w045 = self.l_w * 0.045
        w048 = self.l_w * 0.048
        w05 = self.l_w * 0.05
        w06 = self.l_w * 0.06
        w1 = self.l_w * 0.1
        w12 = self.l_w * 0.12
        w15 = self.l_w * 0.15
        w17 = self.l_w * 0.17
        w2 = self.l_w * 0.2
        w25 = self.l_w * 0.25
        w27 = self.l_w * 0.27
        w3 = self.l_w * 0.3
        w75 = self.l_w * 0.75
        w8 = self.l_w * 0.8
        w85 = self.l_w * 0.85
        # CALIDAD RADIOGRAFICA
        # DO EXEC #
        loPdf.set_border(1)
        # CALIDAD RADIOGRAFICA
        y = loPdf.get_y()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w2, self.l_h, LADATOS[0]["CIMPRIM"], 1, 0, "C")
        loPdf.set_font("Arial", "", 6)
        x = loPdf.get_x()
        cont = 1
        selection = LADATOS[0]["NOPCION"]
        for i in LADATOS[0]["MTABLA"]:
            loPdf.cell(w03, self.l_h, str(cont), 1, 0, "C")
            xselect = self.arr_select_x_per_item(i, selection)
            loPdf.cell(w12, self.l_h, xselect[0], 1, 0, "L")
            loPdf.cell(w05, self.l_h, xselect[1], 1, 1, "C")
            loPdf.set_x(x)
            cont += 1
        # CAUSA
        loPdf.set_xy(x + w2 + w05, y)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w1, self.l_h, LADATOS[1]["CIMPRIM"], 1, 0, "C")
        loPdf.set_font("Arial", "", 6)
        x = loPdf.get_x()
        y = loPdf.get_y()
        cont = 1
        ancho = w17
        selection = LADATOS[0]["NOPCION"]
        for i in LADATOS[1]["MTABLA"]:
            loPdf.cell(w03, self.l_h, str(cont), 1, 0, "C")
            xselect = self.arr_select_x_per_item(i, selection)
            loPdf.cell(ancho, self.l_h, xselect[0], 1, 0, "L")
            loPdf.cell(w05, self.l_h, xselect[1], 1, 1, "C")
            loPdf.set_x(x)
            if cont == 4:
                ancho = w12
                x = x + w25
                loPdf.set_xy(x, y)
            cont += 1
        # COMENTARIO SOBRE DEFECTOS TECNICOS
        loPdf.ln(self.l_h, +0.2)
        loPdf.row(
            [LADATOS[2]["CIMPRIM"], LADATOS[2]["CRESULT"]],
            [w15, w85],
        )
        # ANORMALIDADES PARENQUIMATOSAS
        loPdf.ln(0.2)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(
            self.l_w,
            self.l_h,
            "ANORMALIDADES PARENQUIMATOSAS (SI no hay anormalidades parenquimatosas pase a A. pleurales)",
            1,
            1,
            "L",
        )
        loPdf.set_font("Arial", "", 6)
        # 2.1
        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.multi_cell(
            w25,
            self.l_h,
            "2.1 Zonas afectadas (Marque Todas las zonas afectadas).",
            0,
            "L",
        )
        loPdf.set_xy(x, y)
        loPdf.cell(w25, self.l_h * 4, "", 1, 2, "C")

        loPdf.set_bolds(["B", "B", "B"])
        loPdf.set_borders([0])
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            ["", "Derecha", "Izquierda"],
            [w75, w75, w75],
        )
        loPdf.set_bolds(["B"])
        xbool1 = self.str_check_si(LADATOS[3])
        xbool2 = self.str_check_si(LADATOS[4])
        loPdf.set_aligns(["L", "C", "C"])
        loPdf.row(
            ["Superior", xbool1[0], xbool2[0]],
            [w75, w75, w75],
        )
        loPdf.set_bolds(["B"])
        xbool1 = self.str_check_si(LADATOS[5])
        xbool2 = self.str_check_si(LADATOS[6])
        loPdf.set_aligns(["L", "C", "C"])
        loPdf.row(
            ["Medio", xbool1[0], xbool2[0]],
            [w75, w75, w75],
        )
        loPdf.set_bolds(["B"])
        xbool1 = self.str_check_si(LADATOS[7])
        xbool2 = self.str_check_si(LADATOS[8])
        loPdf.set_aligns(["L", "C", "C"])
        loPdf.row(
            ["Inferior", xbool1[0], xbool2[0]],
            [w75, w75, w75],
        )
        # 2.2
        x = x + w25
        loPdf.set_xy(x, y)
        loPdf.multi_cell(w25, self.l_h, "2.2" + LADATOS[9]["CIMPRIM"] + ".", 0, "L")
        loPdf.set_xy(x, y)
        loPdf.cell(w25, self.l_h * 4, "", 1, 2, "C")

        xselect = self.list_select_x(LADATOS[9])
        cont = 0
        for i in xselect:
            loPdf.cell(w75, self.l_h, i, 1, 0, "C")
            if cont in [2, 5, 8]:
                loPdf.ln()
                loPdf.set_x(x)
            cont += 1

        # 2.3
        x = x + w25
        loPdf.set_xy(x, y)
        loPdf.multi_cell(
            w25,
            self.l_h,
            "2.3 Forma y tamaño (Consúltelas radiografías estándar, se requiere dos símbolos:marque un primario y un secundario)",
            0,
            "L",
        )
        loPdf.set_xy(x, y)
        loPdf.cell(w25, self.l_h * 4, "", 1, 2, "C")
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w25 / 2, self.l_h, "Primaria", 1, 0, "C")
        x1 = loPdf.get_x()
        loPdf.cell(w25 / 2, self.l_h, "Secundaria", 1, 0, "C")
        loPdf.set_font("Arial", "", 6)
        loPdf.ln()
        y1 = loPdf.get_y()
        loPdf.set_x(x)

        xselect = self.list_select_x(LADATOS[10])
        cont = 0
        for i in xselect:
            loPdf.cell(w1, self.l_h, i, 1, 0, "C")
            if cont in [1, 3]:
                loPdf.ln()
                loPdf.set_x(x)
            cont += 1
        loPdf.set_xy(x1, y1)
        xselect = self.list_select_x(LADATOS[11])
        cont = 0
        for i in xselect:
            loPdf.cell(w1, self.l_h, i, 1, 0, "C")
            if cont in [1, 3]:
                loPdf.ln()
                loPdf.set_x(x1)
            cont += 1

        # 2.4
        x = x + w25
        loPdf.set_xy(x, y)
        loPdf.multi_cell(
            w25,
            self.l_h,
            "2.4 Opacidades grandes (Marque 0 si no hay ninguna o marque A, B o C)",
            0,
            "L",
        )
        loPdf.set_xy(x, y)
        loPdf.cell(w25, self.l_h * 4, "", 1, 2, "C")

        loPdf.cell(w75)
        xselect = self.list_select_x(LADATOS[12])
        for i in xselect:
            loPdf.cell(w75, self.l_h, i, 1, 2, "C")

        # ANOMALIDADES PLEURALES
        loPdf.ln(0.2)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(
            w8,
            self.l_h,
            "ANORMALIDADES PLEURALES (sI no hay anormalidades pase a simbolos)",
            1,
            0,
            "L",
        )
        xboolean = self.arr_si_no_x(LADATOS[13])
        loPdf.cell(w06, self.l_h, "Si", 0, 0, "R")
        loPdf.cell(w04, self.l_h, xboolean[0], 1, 0, "C")
        loPdf.cell(w06, self.l_h, "No", 0, 0, "R")
        loPdf.cell(w04, self.l_h, xboolean[1], 1, 1, "C")
        loPdf.set_font("Arial", "", 6)

        loPdf.cell(
            self.l_w,
            self.l_h,
            "3.1 Placas pleurales (0=Ninguna, D=Hemitorax derecho, I=Hemitorax izquierdo)",
            1,
            1,
            "L",
        )

        # SITIO
        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.multi_cell(
            (self.l_w, -0.3) * 0.25,
            self.l_h,
            "Sitio\n(marque las casillas adecuadas)",
            0,
            "C",
        )
        loPdf.set_xy(x, y)
        loPdf.cell((self.l_w, -0.3) * 0.25, self.l_h * 8, "", 1, 2, "C")

        for i in range(14, 18):
            xselect = self.list_select_x(LADATOS[i])
            loPdf.set_aligns(["L", "C", "C", "C"])
            loPdf.row(
                [LADATOS[i]["CIMPRIM"], xselect[0], xselect[1], xselect[2]],
                [
                    (self.l_w, -0.3) * w1,
                    (self.l_w, -0.3) * w05,
                    (self.l_w, -0.3) * w05,
                    (self.l_w, -0.3) * w05,
                ],
            )
        yf = loPdf.get_y()
        # CALIFICACIONES
        x = x + (self.l_w, -0.3) * 0.25 + 0.1
        loPdf.set_xy(x, y)
        loPdf.multi_cell(
            (self.l_w, -0.3) * 0.15, self.l_h, "Calificaciones\n(marque)", 0, "C"
        )
        loPdf.set_xy(x, y)
        loPdf.cell((self.l_w, -0.3) * 0.15, self.l_h * 8, "", 1, 2, "C")

        for i in range(18, 22):
            xselect = self.list_select_x(LADATOS[i])
            if i == 18:
                xselect[0] += "\n "
                xselect[1] += "\n "
                xselect[2] += "\n "
            loPdf.set_aligns(["C", "C", "C"])
            loPdf.row(
                [xselect[0], xselect[1], xselect[2]],
                [
                    (self.l_w, -0.3) * 0.15 * 0.33,
                    (self.l_w, -0.3) * 0.15 * 0.34,
                    (self.l_w, -0.3) * 0.15 * 0.33,
                ],
            )
            loPdf.set_x(x)
        # EXTENSION
        x = x + (self.l_w, -0.3) * 0.15 + 0.1
        loPdf.set_xy(x, y)
        loPdf.multi_cell(
            (self.l_w, -0.3) * 0.30,
            self.l_h,
            "Extension (pared Torácica combinada para placas de perfil y de frente)",
            0,
            "C",
        )
        loPdf.set_xy(x, y)
        loPdf.cell((self.l_w, -0.3) * 0.30, self.l_h * 2, "", 1, 2, "C")

        loPdf.cell((self.l_w, -0.3) * w3, self.l_h * 2, "1", 1, 0, "C")
        y1 = loPdf.get_y()
        loPdf.multi_cell(
            (self.l_w, -0.3) * w27,
            self.l_h,
            "< 1/4 de la pared lateral de tórax",
            0,
            "C",
        )
        loPdf.set_xy(x + (self.l_w, -0.3) * w3, y1)
        loPdf.cell((self.l_w, -0.3) * w27, self.l_h * 2, "", 1, 1, "C")
        loPdf.set_x(x)

        loPdf.cell((self.l_w, -0.3) * w3, self.l_h * 2, "2", 1, 0, "C")
        y1 = loPdf.get_y()
        loPdf.multi_cell(
            (self.l_w, -0.3) * w27,
            self.l_h,
            "Entre 1/4 y 1/2 de la pared lateral de tórax",
            0,
            "C",
        )
        loPdf.set_xy(x + (self.l_w, -0.3) * w3, y1)
        loPdf.cell((self.l_w, -0.3) * w27, self.l_h * 2, "", 1, 1, "C")
        loPdf.set_x(x)

        loPdf.cell((self.l_w, -0.3) * w3, self.l_h * 2, "3", 1, 0, "C")
        y1 = loPdf.get_y()
        loPdf.multi_cell(
            (self.l_w, -0.3) * w27,
            self.l_h,
            "> 1/2 de la pared lateral de tórax",
            0,
            "C",
        )
        loPdf.set_xy(x + (self.l_w, -0.3) * w3, y1)
        loPdf.cell((self.l_w, -0.3) * w27, self.l_h * 2, "", 1, 1, "C")
        loPdf.set_x(x)

        y1 = loPdf.get_y()
        xselect = self.list_select_x(LADATOS[22])
        loPdf.set_aligns(["C", "C"])
        loPdf.row(
            [xselect[0], "D"],
            [(self.l_w, -0.3) * 0.30 * 0.25, (self.l_w, -0.3) * 0.30 * 0.25],
        )
        loPdf.set_x(x)
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            [xselect[1], xselect[2], xselect[3]],
            [
                (self.l_w, -0.3) * w048,
                (self.l_w, -0.3) * w05,
                (self.l_w, -0.3) * w05,
            ],
        )

        x = x + (self.l_w, -0.3) * w15
        loPdf.set_xy(x, y1)
        xselect = self.list_select_x(LADATOS[23])
        loPdf.set_aligns(["C", "C"])
        loPdf.row(
            [xselect[0], "I"],
            [(self.l_w, -0.3) * 0.30 * 0.25, (self.l_w, -0.3) * 0.30 * 0.25],
        )
        loPdf.set_x(x)
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            [xselect[1], xselect[2], xselect[3]],
            [
                (self.l_w, -0.3) * w048,
                (self.l_w, -0.3) * w05,
                (self.l_w, -0.3) * w05,
            ],
        )

        # #ANCHO
        x = x + (self.l_w, -0.3) * 0.15 + 0.1
        loPdf.set_xy(x, y)
        loPdf.multi_cell(
            (self.l_w, -0.3) * 0.30,
            self.l_h,
            "Ancho (opcional) ancho mínimo exigido 3 mm",
            0,
            "C",
        )
        loPdf.set_xy(x, y)
        loPdf.cell((self.l_w, -0.3) * 0.30, self.l_h * 2, "", 1, 2, "C")

        loPdf.cell((self.l_w, -0.3) * w3, self.l_h * 2, "a", 1, 0, "C")
        y1 = loPdf.get_y()
        loPdf.multi_cell((self.l_w, -0.3) * w27, self.l_h, "De 3 a 5 mm", 0, "C")
        loPdf.set_xy(x + (self.l_w, -0.3) * w3, y1)
        loPdf.cell((self.l_w, -0.3) * w27, self.l_h * 2, "", 1, 1, "C")
        loPdf.set_x(x)

        loPdf.cell((self.l_w, -0.3) * w3, self.l_h * 2, "b", 1, 0, "C")
        y1 = loPdf.get_y()
        loPdf.multi_cell((self.l_w, -0.3) * w27, self.l_h, "De 5 a 10 mm", 0, "C")
        loPdf.set_xy(x + (self.l_w, -0.3) * w3, y1)
        loPdf.cell((self.l_w, -0.3) * w27, self.l_h * 2, "", 1, 1, "C")
        loPdf.set_x(x)

        loPdf.cell((self.l_w, -0.3) * w3, self.l_h * 2, "c", 1, 0, "C")
        y1 = loPdf.get_y()
        loPdf.multi_cell((self.l_w, -0.3) * w27, self.l_h, "Mayor a 10 mm", 0, "C")
        loPdf.set_xy(x + (self.l_w, -0.3) * w3, y1)
        loPdf.cell((self.l_w, -0.3) * w27, self.l_h * 2, "", 1, 1, "C")
        loPdf.set_x(x)

        y1 = loPdf.get_y()
        xselect = self.list_select_x(LADATOS[24])
        loPdf.set_aligns(["C"])
        loPdf.row(["D"], [(self.l_w, -0.3) * w15])
        loPdf.set_x(x)
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            [xselect[0], xselect[1], xselect[2]],
            [
                (self.l_w, -0.3) * w048,
                (self.l_w, -0.3) * w05,
                (self.l_w, -0.3) * w05,
            ],
        )

        x = x + (self.l_w, -0.3) * w15
        loPdf.set_xy(x, y1)
        xselect = self.list_select_x(LADATOS[25])
        loPdf.set_aligns(["C"])
        loPdf.row(["I"], [(self.l_w, -0.3) * w15])
        loPdf.set_x(x)
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            [xselect[0], xselect[1], xselect[2]],
            [
                (self.l_w, -0.3) * w048,
                (self.l_w, -0.3) * w05,
                (self.l_w, -0.3) * w05,
            ],
        )

        # OBLITERACION ANGULO COSTOFRENICO
        loPdf.set_y(yf)
        xselect = self.list_select_x(LADATOS[26])
        loPdf.set_aligns(["L", "C", "C", "C"])
        loPdf.row(
            [LADATOS[26]["CIMPRIM"], xselect[0], xselect[1], xselect[2]],
            [(self.l_w, -0.3) * 0.4 + 0.1, w05, w05, w05],
        )

        # ENGROSAMIENTO DIFUSO DE LA PLEURA
        loPdf.ln(0.2)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(
            self.l_w,
            self.l_h,
            "ENGROSAMIENTO DIFUSO DE LA PLEURA (0=Ninguna, D=Hemitorax derecho, I=Hemitorax izquierdo)",
            1,
            1,
            "L",
        )
        loPdf.set_font("Arial", "", 6)

        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w06, self.l_h, "De perfil", 1, 1, "L")
        loPdf.cell(w06, self.l_h, "", 1, 1, "L")
        loPdf.cell(w06, self.l_h, "De frente", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        # Pared toracica
        x = x + w06
        loPdf.set_xy(x, y)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w15, self.l_h, "Pared Torácica", 1, 2, "C")
        loPdf.set_font("Arial", "", 6)
        xselect = self.list_select_x(LADATOS[27])
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            [xselect[0], xselect[1], xselect[2]],
            [w045, w045, w045],
        )
        loPdf.set_x(x)
        loPdf.row(["", "", ""], [w045, w045, w045])
        loPdf.set_x(x)
        xselect = self.list_select_x(LADATOS[28])
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            [xselect[0], xselect[1], xselect[2]],
            [w045, w045, w045],
        )
        # Calcificacion
        x = x + w15
        loPdf.set_xy(x, y)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w15, self.l_h, "Calcificación", 1, 2, "C")
        loPdf.set_font("Arial", "", 6)
        xselect = self.list_select_x(LADATOS[29])
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            [xselect[0], xselect[1], xselect[2]],
            [w045, w045, w045],
        )
        loPdf.set_x(x)
        loPdf.row(["", "", ""], [w045, w045, w045])
        loPdf.set_x(x)
        xselect = self.list_select_x(LADATOS[30])
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            [xselect[0], xselect[1], xselect[2]],
            [w045, w045, w045],
        )
        yf = loPdf.get_y()
        # Extension
        x = x + w25
        loPdf.set_xy(x, y)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w3, self.l_h, "Extensión", 1, 2, "C")
        loPdf.set_font("Arial", "", 6)
        y1 = loPdf.get_y()
        xselect = self.list_select_x(LADATOS[31])
        loPdf.set_aligns(["C", "C"])
        loPdf.row([xselect[0], "D"], [w03, w03])
        loPdf.set_x(x)
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            [xselect[1], xselect[2], xselect[3]],
            [w045, w045, w045],
        )

        x = x + w15
        loPdf.set_xy(x, y1)
        xselect = self.list_select_x(LADATOS[32])
        loPdf.set_aligns(["C", "C"])
        loPdf.row([xselect[0], "I"], [w03, w03])
        loPdf.set_x(x)
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            [xselect[1], xselect[2], xselect[3]],
            [w045, w045, w045],
        )

        # Ancho
        x = x + w25
        loPdf.set_xy(x, y)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w3, self.l_h, "Ancho", 1, 2, "C")
        loPdf.set_font("Arial", "", 6)
        y1 = loPdf.get_y()
        xselect = self.list_select_x(LADATOS[33])
        loPdf.set_aligns(["C"])
        loPdf.row(["D"], [w15])
        loPdf.set_x(x)
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            [xselect[0], xselect[1], xselect[2]],
            [w045, w045, w045],
        )

        x = x + w15
        loPdf.set_xy(x, y1)
        xselect = self.list_select_x(LADATOS[34])
        loPdf.set_aligns(["C"])
        loPdf.row(["I"], [w15])
        loPdf.set_x(x)
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            [xselect[0], xselect[1], xselect[2]],
            [w045, w045, w045],
        )

        # SIMBOLOS
        loPdf.set_y(yf)
        loPdf.ln(0.2)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w8, self.l_h, "SIMBOLOS", 1, 0, "L")
        xboolean = self.arr_si_no_x(LADATOS[35])
        loPdf.cell(w06, self.l_h, "Si", 0, 0, "R")
        loPdf.cell(w04, self.l_h, xboolean[0], 1, 0, "C")
        loPdf.cell(w06, self.l_h, "No", 0, 0, "R")
        loPdf.cell(w04, self.l_h, xboolean[1], 1, 1, "C")
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(
            self.l_w,
            self.l_h,
            "(Rodee con un círculo la respuesta adecuada, si rodea od, escriba a continuación un COMENTARIO)",
            1,
            1,
            "L",
        )
        y = loPdf.get_y()
        for i in range(36, 64):
            xboolean = self.str_check_si(LADATOS[i])
            loPdf.cell(
                w15,
                self.l_h,
                LADATOS[i]["CIMPRIM"]
                + ("   (" + xboolean + ")" if xboolean[0] == "X" else ""),
                1,
                0,
                "C",
            )
            if i == 49:
                loPdf.ln()
        loPdf.set_xy(loPdf.get_x(), y)
        xboolean = self.str_check_si(LADATOS[64])
        loPdf.cell(
            w15,
            self.l_h,
            *2,
            LADATOS[64]["CIMPRIM"]
            + ("   (" + xboolean + ")" if xboolean[0] == "X" else ""),
            1,
            1,
            "C",
        )
        # FIRMA TECNOLOGO
        loFirma = Config.PATH_PDF_SRC + "/" + "9999" + ".jpg"
        if Path(loFirma).is_file():
            loPdf.image(loFirma, 9, 26, 3.5, 2.5)
        return True

    @exception_handler(False)
    def print_audiologico(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "M017",
            "M018",
            "M015",
            "M019",
            "M020",
            "M021",
            "M022",
            "M023",
            "M024",
            "M025",
            "M026",
            "M027",
            "M028",
            "M029",
            "M030",
            "M031",
            "M032",
            "M033",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)

        # INIT EXEC #
        self.print_title(
            loPdf,
            "EXAMEN AUDIOLÓGICO",
        )
        w04 = self.l_w * 0.04
        w07 = self.l_w * 0.07
        w15 = self.l_w * 0.15
        w2 = self.l_w * 0.2
        w21 = self.l_w * 0.21
        w22 = self.l_w * 0.22
        w3 = self.l_w * 0.3
        w4 = self.l_w * 0.4
        w05 = self.l_w * 0.05
        w08 = self.l_w * 0.08
        w5 = self.l_w * 0.5
        w55 = self.l_w * 0.55
        # DO EXEC #
        loPdf.set_border(1)
        loPdf.set_bolds(["B", "B", "B", "B"])
        loPdf.set_aligns(["L", "C", "C", "L"])
        loPdf.row(
            ["ANTECEDENTES", "SI", "NO", "DETALLAR"],
            [w4, w05, w05, w5],
        )
        loPdf.set_aligns(["L", "C", "C"])
        boolean = self.arr_si_no_x(LADATOS[0])
        loPdf.row(
            [LADATOS[0]["CIMPRIM"]]
            + boolean
            + [LADATOS[8]["CIMPRIM"], LADATOS[8]["CRESULT"]],
            [w4, w05, w05, w2, w3],
        )
        loPdf.set_aligns(["L", "C", "C"])
        boolean = self.arr_si_no_x(LADATOS[1])
        xselect = self.arr_si_no_x(LADATOS[1])
        loPdf.row(
            [LADATOS[1]["CIMPRIM"]]
            + boolean
            + [LADATOS[10]["CIMPRIM"]]
            + [xselect[0]]
            + [xselect[1]],
            [w4, w05, w05, w2, w15, w15],
        )
        loPdf.set_aligns(["L", "C", "C"])
        boolean = self.arr_si_no_x(LADATOS[2])
        loPdf.row(
            [LADATOS[2]["CIMPRIM"]] + boolean + ["", "AUDIÓMETRO"],
            [w4, w05, w05, w2, w3],
        )
        loPdf.set_aligns(["L", "C", "C"])
        boolean = self.arr_si_no_x(LADATOS[3])
        loPdf.row(
            [LADATOS[3]["CIMPRIM"]] + boolean + ["", "Marca:"],
            [w4, w05, w05, w2, w3],
        )
        loPdf.set_aligns(["L", "C", "C"])
        boolean = self.arr_si_no_x(LADATOS[4])
        loPdf.row(
            [LADATOS[4]["CIMPRIM"]] + boolean + ["", "Modelo:"],
            [w4, w05, w05, w2, w3],
        )
        loPdf.set_aligns(["L", "C", "C"])
        boolean = self.arr_si_no_x(LADATOS[5])
        loPdf.row(
            [LADATOS[5]["CIMPRIM"]] + boolean + ["", "Serie:"],
            [w4, w05, w05, w2, w3],
        )
        loPdf.set_aligns(["L", "C", "C"])
        boolean = self.arr_si_no_x(LADATOS[6])
        loPdf.row(
            [LADATOS[6]["CIMPRIM"]] + boolean + ["", "Fecha calibración:"],
            [w4, w05, w05, w2, w3],
        )
        loPdf.set_aligns(["L", "C", "C"])
        boolean = self.arr_si_no_x(LADATOS[7])
        loPdf.row(
            [LADATOS[7]["CIMPRIM"]] + boolean + ["", ""],
            [w4, w05, w05, w2, w3],
        )
        # SINTOMAS ACTUALES
        loPdf.ln()
        loPdf.set_bolds(["B"])
        xselect = self.list_select_x(LADATOS[11])
        loPdf.row(
            [
                LADATOS[11]["CIMPRIM"],
                xselect[0],
                xselect[1],
                xselect[2],
                xselect[3],
            ],
            [w15, w22, w21, w21, w21],
        )
        loPdf.row(
            [LADATOS[12]["CIMPRIM"]],
            [
                self.l_w,
            ],
        )
        loPdf.row(
            [LADATOS[12]["CRESULT"]],
            [
                self.l_w,
            ],
        )
        # EXAMEN CLINICO OTOSCOPIA
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "OTOSCOPIA", 0, 1, "L")
        loPdf.set_font("Arial", "", 6)
        xselect1 = self.list_select_x(LADATOS[13])
        xselect2 = self.list_select_x(LADATOS[15])
        loPdf.row(
            [
                LADATOS[13]["CIMPRIM"],
                xselect1[0],
                xselect1[1],
                LADATOS[14]["CRESULT"],
            ],
            [w15, w15, w15, w55],
        )
        loPdf.row(
            [
                LADATOS[15]["CIMPRIM"],
                xselect2[0],
                xselect2[1],
                LADATOS[16]["CRESULT"],
            ],
            [w15, w15, w15, w55],
        )
        # AUDIOGRAMAS
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(10.3, self.l_h, "AUDIOGRAMA OD", 0, 0, "C")
        loPdf.cell(5.8, self.l_h, "AUDIOGRAMA OI", 0, 1, "C")
        loPdf.set_font("Arial", "", 6)
        loPdf.ln()
        xo = loPdf.get_x()
        yo = loPdf.get_y()
        self.sub_audiologico_cuadro(loPdf, xo + 2.5, xo + 10.6, yo)
        loPdf.set_x(xo)
        # CUADRO SIMBOLOGIA
        xo = loPdf.get_x()
        yo = loPdf.get_y()
        esp = 14  # espacio a la derecha para dibujar el cuadro leyenda
        loPdf.set_x(xo + esp + 1.3)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(1, self.l_h, "SIMBOLOGIA", 0, 1, "L")
        loPdf.set_font("Arial", "", 4)
        loPdf.set_x(xo + esp + 2.73)
        loPdf.row(["enmascaramiento"], [w08])
        loPdf.set_font("Arial", "", 6)
        loPdf.set_x(xo + esp)
        loPdf.row(
            ["", "OD", "OI", "OD", "OI"],
            [w07, w04, w04, w04, w04],
        )
        loPdf.set_x(xo + esp)
        loPdf.row(
            ["Via aérea", "", "", "", ""],
            [w07, w04, w04, w04, w04],
        )
        loPdf.image(
            Config.PATH_PDF_SRC + "/circle-red.png",
            xo + esp + 2.55,
            yo + self.l_h * 3 + 0.1,
            0.2,
            0.2,
        )
        loPdf.image(
            Config.PATH_PDF_SRC + "/x-blue.png",
            xo + esp + 2.27,
            yo + self.l_h * 3 + 0.1,
            0.2,
            0.2,
        )
        loPdf.image(
            Config.PATH_PDF_SRC + "/triangle-red.png",
            xo + esp + 2.99,
            yo + self.l_h * 3 + 0.1,
            0.2,
            0.2,
        )
        loPdf.image(
            Config.PATH_PDF_SRC + "/triangle-red.png",
            xo + esp + 3.71,
            yo + self.l_h * 3 + 0.1,
            0.2,
            0.2,
        )
        loPdf.set_x(xo + esp)
        loPdf.row(
            ["Via ósea", "", "", "", ""],
            [w07, w04, w04, w04, w04],
        )
        loPdf.image(
            Config.PATH_PDF_SRC + "/less_red.png",
            xo + esp + 2.55,
            yo + self.l_h * 4 + 0.1,
            0.2,
            0.2,
        )
        loPdf.image(
            Config.PATH_PDF_SRC + "/more_blue.png",
            xo + esp + 2.27,
            yo + self.l_h * 4 + 0.1,
            0.2,
            0.2,
        )
        loPdf.image(
            Config.PATH_PDF_SRC + "/bracket-left-red.png",
            xo + esp + 2.99,
            yo + self.l_h * 4 + 0.1,
            0.2,
            0.2,
        )
        loPdf.image(
            Config.PATH_PDF_SRC + "/bracket-right-blue.png",
            xo + esp + 3.71,
            yo + self.l_h * 4 + 0.1,
            0.2,
            0.2,
        )
        loPdf.set_x(xo + esp)
        loPdf.row(
            ["Color", "Rojo", "Azul", "Rojo", "Azul"],
            [w07, w04, w04, w04, w04],
        )
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_espirometria(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "M342",
            "M343",
            "M344",
            "M345",
            "M346",
            "M347",
            "M348",
            "M349",
            "M350",
            "M351",
            "M352",
            "M353",
            "M354",
            "M355",
            "M356",
            "M357",
            "M358",
            "M359",
            "M360",
            "M361",
            "M362",
            "M363",
            "M364",
            "M365",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)

        # INIT EXEC #
        self.print_title(
            loPdf,
            "CUESTIONARIO ESPIROMETRIA",
        )
        w1 = self.l_w * 0.1
        w7 = self.l_w * 0.7
        w25 = self.l_w * 0.25
        # DO EXEC #
        loPdf.set_border(1)
        # ESPIROMETRO CALIBRACION
        loPdf.row(
            [
                "ESPIROMETRO",
                "MARCA",
                "SIBELMED",
                "MODELO",
                "DATOSPIR",
                "CALIBRACION",
                "16/08/2019",
            ],
            [w7, w7, w7, w7, w7, w7, w7],
        )
        loPdf.set_border(0)
        loPdf.ln()
        loPdf.set_borders([0, 0, 1, 1])
        loPdf.set_aligns(["C", "L", "C", "C"])
        loPdf.row(["", "", "SI", "NO"], [w1, w7, w1, w1])
        # CUESTIONARIO
        i = 1
        loPdf.set_border(1)
        for item in LADATOS[0:4]:
            xbool = self.arr_si_no_x(item)
            loPdf.set_aligns(["C", "L", "C", "C"])
            loPdf.row([str(i), item["CIMPRIM"], xbool[0], xbool[1]], [w1, w7, w1, w1])
            i += 1
        loPdf.set_border(0)
        loPdf.ln()
        i = 1
        loPdf.cell(
            self.l_w,
            self.l_h,
            "PARA SER LLENADO POR EL PROFESIONAL QUE REALIZA LA PRUEBA",
            1,
            1,
            "L",
        )
        yo = loPdf.get_y()
        for item in LADATOS[5:11]:
            loPdf.set_aligns(["C", "L", "L", "L"])
            xbool = self.str_si_no_x(item)
            loPdf.row([str(i), item["CIMPRIM"], xbool[0], xbool[1]], [w1, w25, w1, w1])
            i += 1
        loPdf.ln()
        yf = loPdf.get_y()
        xo = w1 + w25 + w1 + w1
        plus = yo
        for item in LADATOS[11:15]:
            loPdf.set_xy(xo, plus)
            loPdf.set_aligns(["C", "L", "L", "L"])
            loPdf.row([str(i), item["CIMPRIM"], xbool[0], xbool[1]], [w1, w25, w1, w1])
            i += 1
            plus += self.l_h
        loPdf.set_y(yf)
        loPdf.cell(
            self.l_w,
            self.l_h,
            "PREGUNTAS PARA TODOS LOS ENTREVISTADOS QUE NO TIENEN LOS CRITERIOS DE EXCLUSION Y QUE POR LO TANTO DEBEN HACER LA ESPIROMETRIA",
            1,
            1,
            "L",
        )
        i = 1
        loPdf.set_borders([0, 0, 1, 1])
        loPdf.set_aligns(["C", "L", "C", "C"])
        loPdf.row(["", "", "SI", "NO"], [w1, w7, w1, w1])
        loPdf.set_border(1)
        for item in LADATOS[15:21]:
            xbool = self.arr_si_no_x(item)
            loPdf.set_aligns(["C", "L", "C", "C"])
            loPdf.row([str(i), item["CIMPRIM"], xbool[0], xbool[1]], [w1, w7, w1, w1])
            i += 1
        loPdf.set_border(0)
        loPdf.ln()
        y = loPdf.get_y()
        if "CNRODNI" in self.paData:
            loHuella = (
                Config.PATH_FILE + "/" + self.paData["CNRODNI"] + "/" + "HUELLA.jpg"
            )
            if Path(loHuella).is_file():
                loPdf.image(loHuella, 9.2, y, 1.5, 2)
                loPdf.rect(8, y - 0.5, 4, 3)
                loPdf.text(9, y + 2, "HUELLA PACIENTE")
            loFirma = (
                Config.PATH_FILE + "/" + self.paData["CNRODNI"] + "/" + "FIRMA.jpg"
            )
            if Path(loFirma).is_file():
                loPdf.image(loFirma, 12.1, y, 3.5, 2.5)
                loPdf.rect(12, y - 0.5, 4, 3)
                loPdf.text(13, y + 2, "FIRMA PACIENTE")
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_electrocardiograma(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "T012",
            "T003",
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
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)

        # INIT EXEC #
        self.print_title(
            loPdf,
            "FORMATO EKG",
        )
        # DO EXEC #
        w14 = self.l_w * 0.14
        w36 = self.l_w * 0.36
        wt = (w14 + w36) / 4
        loPdf.set_border(1)
        loPdf.row(
            [
                LADATOS[0]["CIMPRIM"],
                LADATOS[0]["CRESULT"],
                LADATOS[1]["CIMPRIM"],
                LADATOS[1]["CRESULT"],
                LADATOS[2]["CIMPRIM"],
                LADATOS[2]["CRESULT"],
            ],
            [wt, wt, wt, wt, w14, w36],
        )
        for i in range(3, 13, 2):
            loPdf.row(
                [
                    LADATOS[i]["CIMPRIM"],
                    LADATOS[i]["CRESULT"],
                    LADATOS[i + 1]["CIMPRIM"],
                    LADATOS[i + 1]["CRESULT"],
                ],
                [w14, w36, w14, w36],
            )
        loPdf.set_border(0)
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_electrocardiograma_riesgo(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "T012",
            "T003",
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
            "L051",
            "L052",
            "T013",
            "T014",
            "M013",
            "M014",
            "M015",
            "M016",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)

        # INIT EXEC #
        self.print_title(
            loPdf,
            "FORMATO EKG",
        )
        # DO EXEC #
        w14 = self.l_w * 0.14
        w36 = self.l_w * 0.36
        wt = (w14 + w36) / 4
        loPdf.set_border(1)
        loPdf.row(
            [
                LADATOS[0]["CIMPRIM"],
                LADATOS[0]["CRESULT"],
                LADATOS[1]["CIMPRIM"],
                LADATOS[1]["CRESULT"],
                LADATOS[2]["CIMPRIM"],
                LADATOS[2]["CRESULT"],
            ],
            [wt, wt, wt, wt, w14, w36],
        )
        for i in range(3, 13, 2):
            loPdf.row(
                [
                    LADATOS[i]["CIMPRIM"],
                    LADATOS[i]["CRESULT"],
                    LADATOS[i + 1]["CIMPRIM"],
                    LADATOS[i + 1]["CRESULT"],
                ],
                [w14, w36, w14, w36],
            )
        loPdf.set_border(0)
        loPdf.ln()
        self.print_title(
            loPdf,
            "RIESGO CARDIOVASCULA",
        )
        idx = 13
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(
            self.l_w,
            self.l_h,
            "2013 ACC/AHA Guideline on the Assessment of Cardiovascular Risk",
            0,
            1,
            "L",
        )
        loPdf.ln(0.2)
        loPdf.cell(2.5, self.l_h, "RAZA", 0, 0, "L")
        self.check_h(loPdf, self.l_w, -2.5, self.l_h, LADATOS[idx])
        loPdf.ln()
        idx += 1
        loPdf.cell(2.5, self.l_h, "COLESTEROL TOTAL", 0, 0, "L")
        loPdf.cell(0.3, self.l_h, ":", 0, 0, "C")
        loPdf.cell(1.1, self.l_h, LADATOS[idx]["CRESULT"], 0, 0, "L")
        loPdf.cell(0, self.l_h, LADATOS[idx]["CDESUNI"], 0, 1, "L")
        idx += 1
        loPdf.cell(2.5, self.l_h, "HDL", 0, 0, "L")
        loPdf.cell(0.3, self.l_h, ":", 0, 0, "C")
        loPdf.cell(1.1, self.l_h, LADATOS[idx]["CRESULT"], 0, 0, "L")
        loPdf.cell(0, self.l_h, LADATOS[idx]["CDESUNI"], 0, 1, "L")
        loPdf.ln(0.2)
        idx += 1
        loPdf.cell(3.6, self.l_h, "PRESION ARTERIAL SISTOLICA", 0, 0, "L")
        loPdf.cell(0.3, self.l_h, ":", 0, 0, "C")
        loPdf.cell(1.1, self.l_h, LADATOS[idx]["CRESULT"], 0, 0, "L")
        loPdf.cell(0, self.l_h, LADATOS[idx]["CDESUNI"], 0, 1, "L")
        idx += 1
        loPdf.cell(3.6, self.l_h, "PRESION ARTERIAL DIASTOLICA", 0, 0, "L")
        loPdf.cell(0.3, self.l_h, ":", 0, 0, "C")
        loPdf.cell(1.1, self.l_h, LADATOS[idx]["CRESULT"], 0, 0, "L")
        loPdf.cell(0, self.l_h, LADATOS[idx]["CDESUNI"], 0, 1, "L")
        loPdf.ln(0.2)
        idx += 1
        xboolean = self.arr_si_no_x(LADATOS[idx])
        loPdf.cell(3.6, self.l_h, "TRATAMIENTO PARA HTA", 0, 0, "L")
        loPdf.cell(0.3, self.l_h, ":", 0, 0, "C")
        loPdf.cell(0.5, self.l_h, "SI", 0, 0, "L")
        loPdf.cell(0.5, self.l_h, xboolean[0], 1, 0, "C")
        loPdf.cell(0.5)
        loPdf.cell(0.5, self.l_h, "NO", 0, 0, "L")
        loPdf.cell(0.5, self.l_h, xboolean[1], 1, 1, "C")
        idx += 1
        xboolean = self.arr_si_no_x(LADATOS[idx])
        loPdf.cell(3.6, self.l_h, "DIABETES MELLITUS", 0, 0, "L")
        loPdf.cell(0.3, self.l_h, ":", 0, 0, "C")
        loPdf.cell(0.5, self.l_h, "SI", 0, 0, "L")
        loPdf.cell(0.5, self.l_h, xboolean[0], 1, 0, "C")
        loPdf.cell(0.5)
        loPdf.cell(0.5, self.l_h, "NO", 0, 0, "L")
        loPdf.cell(0.5, self.l_h, xboolean[1], 1, 1, "C")
        idx += 1
        xboolean = self.arr_si_no_x(LADATOS[idx])
        loPdf.cell(3.6, self.l_h, "TABACO", 0, 0, "L")
        loPdf.cell(0.3, self.l_h, ":", 0, 0, "C")
        loPdf.cell(0.5, self.l_h, "SI", 0, 0, "L")
        loPdf.cell(0.5, self.l_h, xboolean[0], 1, 0, "C")
        loPdf.cell(0.5)
        loPdf.cell(0.5, self.l_h, "NO", 0, 0, "L")
        loPdf.cell(0.5, self.l_h, xboolean[1], 1, 1, "C")
        loPdf.ln(0.2)
        idx += 1
        loPdf.cell(
            0,
            self.l_h,
            "RIESGO DE ENFERMEDAD CARDÍACA O STROKE A 10 AÑOS :"
            + LADATOS[idx]["CRESULT"],
            0,
            1,
            "L",
        )
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_psicologica(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "M445",
            "M462",
            "M463",
            "M464",
            "M465",
            "M466",
            "M015",
            "M384",
            "M385",
            "M446",
            "M447",
            "M448",
            "M449",
            "M450",
            "M451",
            "M452",
            "M453",
            "M467",
            "M468",
            "M469",
            "M470",
            "M471",
            "M472",
            "M473",
            "M474",
            "M475",
            "M476",
            "M477",
            "M478",
            "M479",
            "M480",
            "M481",
            "M482",
            "M483",
            "M484",
            "M485",
            "M486",
            "M487",
            "M488",
            "M489",
            "M490",
            "M491",
            "M492",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)

        # INIT EXEC #
        self.print_title(
            loPdf,
            "FICHA PSICOLOGICA",
        )
        w1 = self.l_w * 0.1
        w18 = self.l_w * 0.18
        w2 = self.l_w * 0.2
        w28 = self.l_w * 0.28
        w3 = self.l_w * 0.3
        w4 = self.l_w * 0.4
        w6 = self.l_w * 0.6
        # DO EXEC #
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "I. MOTIVO DE LA EVALUACION", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[0]["CRESULT"], 1, "L")
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "II. DATOS OCUPACIONALES", 1, 1, "L")
        loPdf.cell(self.l_w, self.l_h, "PRINCIPALES RIESGOS", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[1]["CRESULT"], 1, "L")
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "MEDIDAS DE SEGURIDAD", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[2]["CRESULT"], 1, "L")
        if self.om_experiencia_laboral(loPdf):
            self.mx_experiencia_laboral_1(
                loPdf,
                self.l_w,
                self.l_h,
            )
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "III.  Historia Familia", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[3]["CRESULT"], 1, "L")
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(
            self.l_w,
            self.l_h,
            "IV. Accidentes y Enfermedades:(Durante el tiempo laborado)",
            1,
            1,
            "L",
        )
        loPdf.set_font("Arial", "", 6)
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[4]["CRESULT"], 1, "L")
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "V. HABITOS", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[5]["CRESULT"], 1, "L")
        loPdf.row(
            [
                LADATOS[6]["CIMPRIM"],
                self.str_check_si(LADATOS[6]),
                LADATOS[7]["CIMPRIM"],
                self.str_check_si(LADATOS[7]),
                LADATOS[8]["CIMPRIM"],
                self.str_check_si(LADATOS[8]),
            ],
            [w6, w6, w6, w6, w6, w6],
        )
        loPdf.setHeader("HISTORIA 2")
        loPdf.add_page()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "VI. EXAMEN MENTAL", 1, 1, "L")
        loPdf.set_border(1)
        loPdf.row(
            ["OBSERVACION DE CONDUCTAS", "PTJ", "PRUEBAS PSICOLOGICAS"],
            [w6, w1, w3],
        )
        loPdf.set_border(0)
        yo = loPdf.get_y()
        loPdf.set_font("Arial", "", 6)
        loPdf.ln(0.2)
        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w18, self.l_h, "Presentacion", 0, 1, "L")
        loPdf.set_xy(x + w18, y)
        loPdf.set_font("Arial", "B", 6)
        self.opt_v(loPdf, w4, self.l_h, LADATOS[9])

        loPdf.ln(self.l_h)
        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w18, self.l_h, "Postura", 0, 1, "L")
        loPdf.set_xy(x + w18, y)
        loPdf.set_font("Arial", "B", 6)
        self.opt_v(loPdf, w4, self.l_h, LADATOS[10])

        loPdf.ln(self.l_h)
        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w18, self.l_h, "Discurso", 0, 1, "L")
        loPdf.set_xy(x + w18, y)
        loPdf.cell(w1, self.l_h, "Ritmo", 0, 1, "L")
        loPdf.set_xy(x + w28, y)
        loPdf.set_font("Arial", "B", 6)
        self.opt_v(loPdf, w3, self.l_h, LADATOS[11])
        loPdf.ln(self.l_h)
        loPdf.set_x(x + self.l_w * 0.18)
        y = loPdf.get_y()
        loPdf.cell(w3, self.l_h, "Tono", 0, 1, "L")
        loPdf.set_xy(x + w28, y)
        self.opt_v(loPdf, w3, self.l_h, LADATOS[12])
        loPdf.ln(self.l_h)
        loPdf.set_x(x + self.l_w * 0.18)
        y = loPdf.get_y()
        loPdf.cell(w3, self.l_h, "Articulacion", 0, 1, "L")
        loPdf.set_xy(x + w28, y)
        self.opt_v(loPdf, w3, self.l_h, LADATOS[13])

        loPdf.ln(self.l_h)
        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w18, self.l_h, "Orientación", 0, 1, "L")
        loPdf.set_xy(x + w18, y)
        loPdf.cell(w1, self.l_h, "Tiempo", 0, 1, "L")
        loPdf.set_xy(x + w28, y)
        loPdf.set_font("Arial", "B", 6)
        self.opt_v(loPdf, w3, self.l_h, LADATOS[14])
        loPdf.ln(self.l_h)
        loPdf.set_x(x + self.l_w * 0.18)
        y = loPdf.get_y()
        loPdf.cell(w3, self.l_h, "Espacio", 0, 1, "L")
        loPdf.set_xy(x + w28, y)
        self.opt_v(loPdf, w3, self.l_h, LADATOS[15])
        loPdf.ln(self.l_h)
        loPdf.set_x(x + self.l_w * 0.18)
        y = loPdf.get_y()
        loPdf.cell(w3, self.l_h, "Persona", 0, 1, "L")
        loPdf.set_xy(x + w28, y)
        self.opt_v(loPdf, w3, self.l_h, LADATOS[16])
        loPdf.ln(self.l_h)
        loPdf.cell(w6, self.l_h, "PROCESOS COGNITIVOS", 1, 1, "L")
        loPdf.cell(w2, self.l_h, "Lucido/Atento", 0, 0, "L")
        loPdf.cell(w4, self.l_h, LADATOS[17]["CRESULT"], 0, 1, "L")
        loPdf.cell(w2, self.l_h, "Pensamiento", 0, 0, "L")
        loPdf.cell(w4, self.l_h, LADATOS[18]["CRESULT"], 0, 1, "L")
        loPdf.cell(w2, self.l_h, "Percepcion", 0, 0, "L")
        loPdf.cell(w4, self.l_h, LADATOS[19]["CRESULT"], 0, 1, "L")
        y = loPdf.get_y()
        loPdf.cell(w2, self.l_h, "Memoria", 0, 0, "L")
        loPdf.set_xy(x + self.l_w * 0.18, y)
        self.opt_v(loPdf, w4, self.l_h, LADATOS[20])

        loPdf.ln(self.l_h)
        y = loPdf.get_y()
        loPdf.cell(w2, self.l_h, "Inteligencia", 0, 0, "L")
        loPdf.set_xy(x + self.l_w * 0.18, y)
        tmp_arr1 = LADATOS[idx].copy()
        tmp_arr2 = tmp_arr1.copy()
        tmp_arr3 = tmp_arr1.copy()
        tmp_arr4 = tmp_arr1.copy()
        tmp_arr1["MTABLA"] = LADATOS[idx]["MTABLA"][0:3]
        tmp_arr2["MTABLA"] = LADATOS[idx]["MTABLA"][3:6]
        tmp_arr3["MTABLA"] = LADATOS[idx]["MTABLA"][6:8]
        tmp_arr4["MTABLA"] = LADATOS[idx]["MTABLA"][8:10]

        self.opt_v(loPdf, w4, self.l_h, tmp_arr1)
        loPdf.ln(self.l_h)
        y = loPdf.get_y()
        loPdf.set_xy(x + self.l_w * 0.18, y)
        self.opt_v(loPdf, w4, self.l_h, tmp_arr2)
        loPdf.ln(self.l_h)
        y = loPdf.get_y()
        loPdf.set_xy(x + self.l_w * 0.18, y)
        self.opt_v(loPdf, w4, self.l_h, tmp_arr3)
        loPdf.ln(self.l_h)
        y = loPdf.get_y()
        loPdf.set_xy(x + self.l_w * 0.18, y)
        self.opt_v(loPdf, w4, self.l_h, tmp_arr4)

        loPdf.ln(self.l_h)
        loPdf.cell(w2, self.l_h, "Apetito", 0, 0, "L")
        loPdf.cell(w4, self.l_h, LADATOS[22]["CRESULT"], 0, 1, "L")
        loPdf.cell(w2, self.l_h, "Sueño", 0, 0, "L")
        loPdf.cell(w4, self.l_h, LADATOS[23]["CRESULT"], 0, 1, "L")
        loPdf.cell(w2, self.l_h, "Personalidad", 0, 0, "L")
        loPdf.cell(w4, self.l_h, LADATOS[24]["CRESULT"], 0, 1, "L")
        loPdf.cell(w2, self.l_h, "Sexualidad", 0, 0, "L")
        loPdf.cell(w4, self.l_h, LADATOS[25]["CRESULT"], 0, 1, "L")
        loPdf.cell(w2, self.l_h, "Conducta Sexual", 0, 0, "L")
        loPdf.cell(w4, self.l_h, LADATOS[26]["CRESULT"], 0, 1, "L")
        xo = loPdf.get_x() + w6
        y = yo
        loPdf.set_border(1)
        # loPdf.set_row_square(0.8)
        loPdf.set_xy(xo, y)
        # 47
        for i in range(27, 42):
            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.set_row_square(1)
            loPdf.row(
                [LADATOS[i]["CRESULT"], LADATOS[i]["CIMPRIM"]],
                [w1, w3],
            )
            y = y + 1
            loPdf.set_xy(xo, y)
        loPdf.set_border(0)
        y = loPdf.get_y()
        loPdf.ln()
        x = loPdf.get_x()
        loPdf.rect(x, yo, w6, y - yo, "")
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_ferreyros(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
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
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)

        # INIT EXEC #
        self.print_title(
            loPdf,
            "INFORME MEDICO",
        )
        w2 = self.l_w * 0.2
        w3 = self.l_w * 0.3
        w4 = self.l_w * 0.4
        w5 = self.l_w * 0.5
        w6 = self.l_w * 0.6
        w7 = self.l_w * 0.7
        w8 = self.l_w * 0.8
        # DO EXEC #
        loPdf.cell(self.l_w, self.l_h, "DATOS", 1, 1, "L")
        loPdf.row(
            [
                "PESO:" + LADATOS[0]["CRESULT"],
                "TALLA:" + LADATOS[1]["CRESULT"],
                "IMC:" + LADATOS[2]["CRESULT"],
            ],
            [w3, w3, w3],
        )
        loPdf.row(["PRESION ARTERIAL:", LADATOS[3]["CRESULT"]], [w3, w6])
        loPdf.row(
            ["FRECUENCIA CARDIACA:", LADATOS[4]["CRESULT"]],
            [w3, w6],
        )
        loPdf.ln(self.l_h)
        loPdf.cell(self.l_w, self.l_h, "LABORATORIO", 1, 1, "L")
        loPdf.ln(self.l_h)
        loPdf.cell(w2, self.l_h, "HEMOGRAMA", 0, 0, "L")
        self.opt_v_coment(
            loPdf,
            w8,
            self.l_h,
            LADATOS[5],
            LADATOS[6]["CRESULT"],
        )
        loPdf.cell(w2, self.l_h, "EXAMEN DE ORINA", 0, 0, "L")
        self.opt_v_coment(
            loPdf,
            w8,
            self.l_h,
            LADATOS[7],
            LADATOS[8]["CRESULT"],
        )
        loPdf.row(
            ["Hemoglobina", LADATOS[9]["CRESULT"], LADATOS[9]["CRANGO"]],
            [w4, w3, w3],
        )
        loPdf.row(
            ["Glucosa", LADATOS[10]["CRESULT"], LADATOS[10]["CRANGO"]],
            [w4, w3, w3],
        )
        loPdf.row(
            [
                "Colesterol Total",
                LADATOS[11]["CRESULT"],
                LADATOS[11]["CRANGO"],
            ],
            [w4, w3, w3],
        )
        loPdf.row(
            [
                "Trigliceridos",
                LADATOS[12]["CRESULT"],
                LADATOS[12]["CRANGO"],
            ],
            [w4, w3, w3],
        )
        loPdf.row(
            ["Creatinina", LADATOS[13]["CRESULT"], LADATOS[13]["CRANGO"]],
            [w4, w3, w3],
        )
        loPdf.ln(self.l_h)
        loPdf.cell(self.l_w, self.l_h, "MEDICOS AUXILIARES", 1, 1, "L")
        for item in LADATOS[14:22]:
            loPdf.row([item["CIMPRIM"], item["CRESULT"]], [w3, w7])
        loPdf.ln()
        # EXTRA #
        # FOOTER
        loPdf.cell(0, 0.4, "DIAGNOSTICO", 1, 1, "L")
        if self.paData["OCIE10"] is not None:
            loPdf.multi_cell(0, 0.4, self.paData["OCIE10"], 1, "L")
        loPdf.ln(0.2)
        loPdf.cell(0, 0.4, "RECOMENDACIONES", 1, 1, "L")
        if self.paData["OEXTRA"]["MRECOME"] is not None:
            loPdf.multi_cell(0, 0.4, self.paData["OEXTRA"]["MRECOME"], 1, "L")
        loPdf.ln(0.2)
        self.mx_print_aptitud(loPdf)
        loPdf.ln(self.l_h)
        loPdf.set_bold("B")
        loPdf.set_align("C")
        loPdf.set_border(1)
        loPdf.row(
            ["Nombre del Medico calificador", "Nombre del Medico auditor"],
            [w5, w5],
        )
        loPdf.set_border(0)
        loPdf.ln(0.1)
        y = loPdf.get_y()
        loPdf.cell(w5, 0.4, "Dra Lizbeth Zegarra Quiroz", 0, 1, "C")
        x = loPdf.get_x()
        loPdf.cell(w5, 0.4, "Medico Evaluador", 0, 1, "C")
        loPdf.cell(w5, 0.4, "C.M.P 094678", 0, 1, "C")
        loPdf.set_xy(x + w5, y)
        loPdf.cell(w5, 0.4, "Dra Nadieshda Flores Barriga", 0, 1, "C")
        loPdf.set_xy(x + w5, y + 0.4)
        loPdf.cell(w5, 0.4, "Director Medico Ocupacional", 0, 1, "C")
        loPdf.set_xy(x + w5, y + 0.8)
        loPdf.cell(w5, 0.4, "C.M.P 054801", 0, 1, "C")
        loFirma = Config.PATH_PDF_SRC + "/" + self.paData["CUSUFIR"] + ".jpg"
        if Path(loFirma).is_file():
            loPdf.image(loFirma, 13, 26, 3.5, 2.5)
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_ferreyros_evaluacion(self, loPdf) -> bool:
        # VAL #
        arr_ind = ["M654", "M724", "M725", "M549", "M726"]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)

        # INIT EXEC #
        self.print_title(
            loPdf,
            "CONSTANCIA DE EVALUACION DE LA CONDICION DE SALUD",
        )

        # DO EXEC #
        for item in LADATOS:
            loPdf.set_font("Arial", "B", 6)
            loPdf.cell(self.l_w, self.l_h, item["CIMPRIM"], 1, 1, "L")
            loPdf.set_font("Arial", "", 6)
            loPdf.multi_cell(self.l_w, self.l_h, item["CRESULT"], 1, "L")
        loPdf.ln()
        self.print_triaje(loPdf)
        loPdf.ln()
        y = loPdf.get_y()
        # loFirma = (
        #    Config.PATH_PDF_SRC
        #    + "/9999.jpg"
        # )
        loPdf.rect(0.6, y - 0.2, 4.2, 2.9)
        loPdf.text(1.3, y + 3, "FIRMA MEDICOEVALUADOR")
        loPdf.ln()
        loPdf.add_page()
        loPdf.ln(1)
        loPdf.set_border(1)
        loPdf.row(["ANALISIS", "RESULTADO", "UNIDAD", "RANGO"], [7, 4, 2.4, 5])
        loPdf.set_border(0)
        loPdf.ln()
        find_lab = next((d for d in self.paDatos if d.get("CCODIND") == "L278"), None)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(18.4, self.l_h, "MOLECULAR PCR-SARS COV-2(COVID-19)", 1, 2, "C")
        loPdf.ln()
        loPdf.set_font("Arial", "", 6)
        loPdf.row(
            [
                find_lab["CIMPRIM"],
                find_lab["CRESULT"],
                find_lab["CDESUNI"],
                find_lab["CRANGO"],
            ],
            [7, 4, 2.4, 5],
        )
        loPdf.ln()
        loPdf.set_font("Arial", "", 6)
        loPdf.multi_cell(
            self.l_w,
            self.l_h,
            "El estudio molecular del virus respiratorio SARS-COV-2, se realizo por transcripcion reversa seguido de detección por PCR en tiempo real. Se utilizo el sistema ISOTHERMAL AMPLIFICACION - REAL TIME FLUORESCENTE ASSAY, el cual detecta el Gen ORFab y el Gen N del SARS-COV-2 y utiliza como control interno el sistema CPA que detecta en forma especifica el GAPDHnRNA humano que garantiza la extracción, purificación y amplificación de la prueba, lo cual valida el ensayo molecular.El resultado se puede expresar como POSITIVO, NEGATIVO o INVALIDO, indicandose si hubiese observaciones relacionadas a la calidad y cantidad de muestra tomada en cada paciente, el adecuado transporte en cadena de frio y calidad de materiales que aseguran una muestra con RNA viable y con la carga virica que depende del estado de la enfermedad.",
            0,
            "L",
        )
        loPdf.cell(
            self.l_w,
            self.l_h,
            "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
            0,
            1,
            "C",
        )
        loPdf.set_font("Arial", "B", 7)
        x = loPdf.get_x()
        y = loPdf.get_y()
        loFirma = Config.PATH_PDF_SRC + "/firma_Meylyn_Palomino.png"
        if Path(loFirma).is_file():
            loPdf.image(loFirma, x + 13, y + 1, 2.9, 3)
        loPdf.SetY(y + 4)
        loPdf.cell(29, self.l_h, "----------------------------------------", 0, 2, "C")
        loPdf.cell(29, self.l_h, "Blgo. Meylyn Palomino Villafuerte", 0, 2, "C    ")
        loPdf.cell(29, self.l_h, "LABORATORIO ANALISIS CLINICOS", 0, 2, "C")
        loPdf.cell(29, self.l_h, "C.B.P.7722", 0, 2, "C")
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_oftalmologico(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "M493",
            "M494",
            "M495",
            "M496",
            "M497",
            "M498",
            "M499",
            "M500",
            "M507",
            "M508",
            "M509",
            "M510",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)
        # print("------------------DATOS")
        # print(json.dumps(LADATOS, indent=3, sort_keys=True))
        # INIT EXEC #
        self.print_title(
            loPdf,
            "EXAMEN OFTALMOLÓGICO",
        )
        w1 = self.l_w * 0.1
        w4 = self.l_w * 0.4
        w9 = self.l_w * 0.9
        # DO EXEC #
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "ANTECEDENTES", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.ln(0.2)
        labels = [
            "Diabetes",
            "Cirugía ocular",
            "Exp. Sustancia química",
            "Hipertensión",
            "Trauma ocular",
            "Glaucoma",
        ]
        idx = 0
        for i in range(0, 6):
            loPdf.cell(2.5, self.l_h, labels[i], 0, 0, "L")
            xboolean = self.str_check_si(LADATOS[i])
            loPdf.cell(0.4, self.l_h, xboolean, 1, 0, "C")
        loPdf.ln()
        idx += 6
        loPdf.ln(0.2)
        xboolean = self.arr_si_no_x(LADATOS[idx])
        loPdf.cell(2.9, self.l_h, "Correctores oculares", 0, 0, "L")
        loPdf.cell(0.5, self.l_h, "SI", 0, 0, "L")
        loPdf.cell(0.4, self.l_h, xboolean[0], 1, 0, "C")
        loPdf.cell(0.5)
        loPdf.cell(0.6, self.l_h, "NO", 0, 0, "L")
        loPdf.cell(0.4, self.l_h, xboolean[1], 1, 1, "C")
        loPdf.ln(0.2)
        loPdf.cell(2.9, self.l_h, "Última refracción", 0, 0, "L")
        idx += 1
        loPdf.cell(6, self.l_h, LADATOS[idx]["CRESULT"], 0, 1, "L")
        loPdf.ln(self.l_h)
        self.sub_agudeza_visual(loPdf)
        # PATOLOGIA
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "PATOLOGIA", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.ln(0.2)
        idx += 1
        self.check_v(loPdf, self.l_w, self.l_h * 5, LADATOS[idx], 1, 1)
        loPdf.ln()
        idx += 1
        loPdf.set_aligns(["L", "C"])
        loPdf.row(["OTRO", LADATOS[idx]["CRESULT"]], [w1, w9])
        # VISION DE COLORES (TEST DE ISHIHARA)
        loPdf.set_border(1)
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w4, self.l_h, "VISION DE COLORES (TEST DE ISHIHARA)", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        idx += 1
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[idx]["CRESULT"], 1, "L")
        # VISION ESTEREOSCOPICA
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w4, self.l_h, "VISION ESTEREOSCOPICA", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        idx += 1
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[idx]["CRESULT"], 1, "L")
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_oftalmologico_especializado(self, loPdf) -> bool:
        # VAL #
        arr_ind = ["M528", "M529", "M530", "M531"]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)

        w4 = self.l_w * 0.4
        # INIT EXEC #
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w4, self.l_h, "TONOMETRIA", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        idx = 0
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[idx]["CRESULT"], 0, "L")
        idx += 1
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[idx]["CRESULT"], 0, "L")
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w4, self.l_h, "FONDO DE OJO (POLO POSTERIOR)", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        idx += 1
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[idx]["CRESULT"], 0, "L")
        idx += 1
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[idx]["CRESULT"], 0, "L")
        # DO EXEC #
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_osteomioarticular(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "M065",
            "M066",
            "M067",
            "M068",
            "M069",
            "M070",
            "M071",
            "M072",
            "M073",
            "M074",
            "M075",
            "M076",
            "M077",
            "M078",
            "M079",
            "M080",
            "M081",
            "M082",
            "M083",
            "M084",
            "M085",
            "M086",
            "M087",
            "M088",
            "M089",
            "M090",
            "M091",
            "M092",
            "M093",
            "M094",
            "M095",
            "M096",
            "M097",
            "M098",
            "M099",
            "M100",
            "M101",
            "M102",
            "M103",
            "M104",
            "M105",
            "M106",
            "M107",
            "M108",
            "M109",
            "M110",
            "M111",
            "M112",
            "M113",
            "M114",
            "M115",
            "M116",
            "M117",
            "M118",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)
        # INIT EXEC #
        self.print_title(
            loPdf,
            "EVALUACION OSTEOMIOARTICULAR ARTICULACIONES",
        )
        w1 = self.l_w * 0.1
        w15 = self.l_w * 0.15
        w2 = self.l_w * 0.2
        w3 = self.l_w * 0.3
        w4 = self.l_w * 0.4
        w6 = self.l_w * 0.6
        # DO EXEC #
        loPdf.set_border(1)
        loPdf.set_align("C")
        loPdf.row(
            [
                "RESPONDA EN TODOS LOS CASOS",
                "RESPONDA SOLAMENTE SI HA TENIDO PROBLEMAS",
            ],
            [w4, w6],
        )
        loPdf.row(
            [
                "Usted ha tenido en los últimos 12 meses problemas (dolor, curvaturas, etc) a nivel de:",
                "Durante los últimos doce meses ha estado incapacitado/a para su trabajo (en casa o fuera) por causa del problema",
                "¿Ha tenido problemas en los últimos siete días?",
            ],
            [w4, w3, w3],
        )
        loPdf.row(
            ["", "SI", "NO", "SI", "NO", "SI", "NO"], [w2, w1, w1, w15, w15, w15, w15]
        )
        idx = 0
        xbollean1 = self.arr_si_no_x(LADATOS[idx])
        idx += 1
        xbollean2 = self.arr_si_no_x(LADATOS[idx])
        idx += 1
        xbollean3 = self.arr_si_no_x(LADATOS[idx])
        loPdf.set_aligns(["L", "C", "C", "C", "C", "C", "C"])
        loPdf.row(
            [
                "NUNCA",
                xbollean1[0],
                xbollean1[1],
                xbollean2[0],
                xbollean2[1],
                xbollean3[0],
                xbollean3[1],
            ],
            [w2, w1, w1, w15, w15, w15, w15],
        )
        label = "HOMBROS\n   Derecha\n   Izquierda\n   Ambos"
        idx += 1
        xbollean1 = list(
            map(
                lambda x, y, z: ("\n" + str(x) + "\n" + str(y) + "\n" + str(z)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
                self.arr_si_no_x(LADATOS[idx + 2]),
            )
        )
        idx += 1
        xbollean2 = list(
            map(
                lambda x, y, z: ("\n" + str(x) + "\n" + str(y) + "\n" + str(z)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
                self.arr_si_no_x(LADATOS[idx + 2]),
            )
        )
        idx += 1
        xbollean3 = list(
            map(
                lambda x, y, z: ("\n" + str(x) + "\n" + str(y) + "\n" + str(z)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
                self.arr_si_no_x(LADATOS[idx + 2]),
            )
        )
        loPdf.set_aligns(["L", "C", "C", "C", "C", "C", "C"])
        loPdf.row(
            [
                label,
                xbollean1[0],
                xbollean1[1],
                xbollean2[0],
                xbollean2[1],
                xbollean3[0],
                xbollean3[1],
            ],
            [w2, w1, w1, w15, w15, w15, w15],
        )
        label = "CODOS\n   Derecha\n   Izquierda\n   Ambos"
        idx += 1
        xbollean1 = list(
            map(
                lambda x, y, z: ("\n" + str(x) + "\n" + str(y) + "\n" + str(z)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
                self.arr_si_no_x(LADATOS[idx + 2]),
            )
        )
        idx += 1
        xbollean2 = list(
            map(
                lambda x, y, z: ("\n" + str(x) + "\n" + str(y) + "\n" + str(z)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
                self.arr_si_no_x(LADATOS[idx + 2]),
            )
        )
        idx += 1
        xbollean3 = list(
            map(
                lambda x, y, z: ("\n" + str(x) + "\n" + str(y) + "\n" + str(z)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
                self.arr_si_no_x(LADATOS[idx + 2]),
            )
        )
        loPdf.set_aligns(["L", "C", "C", "C", "C", "C", "C"])
        loPdf.row(
            [
                label,
                xbollean1[0],
                xbollean1[1],
                xbollean2[0],
                xbollean2[1],
                xbollean3[0],
                xbollean3[1],
            ],
            [w2, w1, w1, w15, w15, w15, w15],
        )
        label = "PUÑOS/MANOS\n   Derecha\n   Izquierda\n   Ambos"
        idx += 1
        xbollean1 = list(
            map(
                lambda x, y, z: ("\n" + str(x) + "\n" + str(y) + "\n" + str(z)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
                self.arr_si_no_x(LADATOS[idx + 2]),
            )
        )
        idx += 1
        xbollean2 = list(
            map(
                lambda x, y, z: ("\n" + str(x) + "\n" + str(y) + "\n" + str(z)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
                self.arr_si_no_x(LADATOS[idx + 2]),
            )
        )
        idx += 1
        xbollean3 = list(
            map(
                lambda x, y, z: ("\n" + str(x) + "\n" + str(y) + "\n" + str(z)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
                self.arr_si_no_x(LADATOS[idx + 2]),
            )
        )
        loPdf.set_aligns(["L", "C", "C", "C", "C", "C", "C"])
        loPdf.row(
            [
                label,
                xbollean1[0],
                xbollean1[1],
                xbollean2[0],
                xbollean2[1],
                xbollean3[0],
                xbollean3[1],
            ],
            [w2, w1, w1, w15, w15, w15, w15],
        )
        label = "   Columna alta(Dorso)\n   Columna baja(Lumbares)"
        idx += 1
        xbollean1 = list(
            map(
                lambda x, y: (str(x) + "\n" + str(y)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
            )
        )
        idx += 1
        xbollean2 = list(
            map(
                lambda x, y: (str(x) + "\n" + str(y)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
            )
        )
        idx += 1
        xbollean3 = list(
            map(
                lambda x, y: (str(x) + "\n" + str(y)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
            )
        )
        loPdf.set_aligns(["L", "C", "C", "C", "C", "C", "C"])
        loPdf.row(
            [
                label,
                xbollean1[0],
                xbollean1[1],
                xbollean2[0],
                xbollean2[1],
                xbollean3[0],
                xbollean3[1],
            ],
            [w2, w1, w1, w15, w15, w15, w15],
        )
        label = "CADERAS\n   Derecha\n   Izquierda"
        idx += 1
        xbollean1 = list(
            map(
                lambda x, y: ("\n" + str(x) + "\n" + str(y)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
            )
        )
        idx += 1
        xbollean2 = list(
            map(
                lambda x, y: ("\n" + str(x) + "\n" + str(y)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
            )
        )
        idx += 1
        xbollean3 = list(
            map(
                lambda x, y: ("\n" + str(x) + "\n" + str(y)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
            )
        )
        loPdf.set_aligns(["L", "C", "C", "C", "C", "C", "C"])
        loPdf.row(
            [
                label,
                xbollean1[0],
                xbollean1[1],
                xbollean2[0],
                xbollean2[1],
                xbollean3[0],
                xbollean3[1],
            ],
            [w2, w1, w1, w15, w15, w15, w15],
        )
        label = "RODILLA\n   Derecha\n   Izquierda"
        idx += 1
        xbollean1 = list(
            map(
                lambda x, y: ("\n" + str(x) + "\n" + str(y)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
            )
        )
        idx += 1
        xbollean2 = list(
            map(
                lambda x, y: ("\n" + str(x) + "\n" + str(y)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
            )
        )
        idx += 1
        xbollean3 = list(
            map(
                lambda x, y: ("\n" + str(x) + "\n" + str(y)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
            )
        )
        loPdf.set_aligns(["L", "C", "C", "C", "C", "C", "C"])
        loPdf.row(
            [
                label,
                xbollean1[0],
                xbollean1[1],
                xbollean2[0],
                xbollean2[1],
                xbollean3[0],
                xbollean3[1],
            ],
            [w2, w1, w1, w15, w15, w15, w15],
        )
        label = "TOBILLO/PIES\n   Derecha\n   Izquierda"
        idx += 1
        xbollean1 = list(
            map(
                lambda x, y: ("\n" + str(x) + "\n" + str(y)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
            )
        )
        idx += 1
        xbollean2 = list(
            map(
                lambda x, y: ("\n" + str(x) + "\n" + str(y)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
            )
        )
        idx += 1
        xbollean3 = list(
            map(
                lambda x, y: ("\n" + str(x) + "\n" + str(y)),
                self.arr_si_no_x(LADATOS[idx]),
                self.arr_si_no_x(LADATOS[idx + 1]),
            )
        )
        loPdf.set_aligns(["L", "C", "C", "C", "C", "C", "C"])
        loPdf.row(
            [
                label,
                xbollean1[0],
                xbollean1[1],
                xbollean2[0],
                xbollean2[1],
                xbollean3[0],
                xbollean3[1],
            ],
            [w2, w1, w1, w15, w15, w15, w15],
        )
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_sintomas_musculo_tendinoso(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "M228",
            "M229",
            "M230",
            "M231",
            "M232",
            "M233",
            "M234",
            "M235",
            "M236",
            "M237",
            "M238",
            "M239",
            "M240",
            "M241",
            "M242",
            "M243",
            "M244",
            "M245",
            "M246",
            "M247",
            "M248",
            "M249",
            "M250",
            "M251",
            "M252",
            "M253",
            "M254",
            "M255",
            "M256",
            "M257",
            "M258",
            "M259",
            "M260",
            "M261",
            "M262",
            "M263",
            "M264",
            "M265",
            "M266",
            "M267",
            "M268",
            "M269",
            "M270",
            "M271",
            "M272",
            "M273",
            "M274",
            "M275",
            "M276",
            "M277",
            "M278",
            "M279",
            "M280",
            "M281",
            "M282",
            "M283",
            "M284",
            "M285",
            "M286",
            "M287",
            "M288",
            "M289",
            "M290",
            "M291",
            "M292",
            "M293",
            "M294",
            "M295",
            "M296",
            "M297",
            "M298",
            "M299",
            "M300",
            "M301",
            "M302",
            "M303",
            "M304",
            "M305",
            "M306",
            "M307",
            "M308",
            "M309",
            "M310",
            "M311",
            "M312",
            "M313",
            "M314",
            "M315",
            "M316",
            "M317",
            "M318",
            "M319",
            "M320",
            "M321",
            "M322",
            "M323",
            "M324",
            "M325",
            "M326",
            "M327",
            "M328",
            "M329",
            "M330",
            "M331",
            "M332",
            "M333",
            "M334",
            "M335",
            "M336",
            "M337",
            "M338",
            "M339",
            "M340",
            "M341",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)
        print(json.dumps(self.paDatos, indent=3, sort_keys=True))
        # INIT EXEC #
        self.print_title(
            loPdf,
            "CUESTIONARIO DE SINTOMAS MUSCULO TENDINOSOS",
        )
        w01 = self.l_w * 0.01
        w04 = self.l_w * 0.04
        w08 = self.l_w * 0.08
        w09 = self.l_w * 0.09
        w1 = self.l_w * 0.1
        w19 = self.l_w * 0.19
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "RESPONDA TODOS LOS CASOS", 1, 0, "L")
        loPdf.ln()
        x = loPdf.get_x() + w1
        y = loPdf.get_y()
        loPdf.set_border(1)
        loPdf.set_align("C")
        loPdf.row(
            [
                "PREGUNTAS",
                "HOMBRO",
                "CUELLO",
                "COLUMNA DORSAL",
                "COLUMNA LUMBAR",
                "CODO O ANTEBRAZO",
                "MUÑECA O MANO",
                "CADERA O MUSLO",
                "RODILLA",
                "TOBILLO O PIE",
            ],
            [w19] + [w09] * 9,
        )
        loPdf.set_border(0)
        questions = [
            "1.¿Ha tenido \nmolestias en?",
            "2.¿Desde hace cuánto tiempo?",
            "3.¿Ha necesitado cambiar depuesto de trabajo?",
            "4.¿Ha tenido molestias en los ultimos 12 meses?",
            "5.¿Cuánto tiempo ha tenido molestias en los últimos 12 meses?",
            "6.¿Cuánto dura cada episodio? ",
            "7.¿Cuánto tiempo estas molestias le han impedido hacer su trabajo en los últimos",
            "8.¿Ha recibido tratamiento por estas molestias en los últimos 12 meses",
            "9.¿Ha tenido molestias en los últimos 7 días?",
            "10.Pongale nota sus molestias entre o 0(sinmolestias) y 5(molestias muy fuertes)",
            "11.¿A qué atribuye estas molestias?",
        ]
        xo = loPdf.get_x()
        y = loPdf.get_y()
        h = 1.8
        h1 = 1
        idx = 0
        for i in range(11):
            loPdf.set_xy(xo, y)
            loPdf.set_font("Arial", "", 6)
            loPdf.multi_cell(w19, 0.4, questions[i], 0, "L")
            loPdf.rect(xo, y, w19, h, "")
            x = xo + w19
            for j in range(9):
                loPdf.set_xy(x, y)
                if i == 0:
                    if j in [0, 2, 3]:
                        self.check_sino_square_h(loPdf, w09, h, LADATOS[idx], 1, 1)
                    else:
                        self.check_sino_square_v(loPdf, w04, h1, LADATOS[idx], 0, 1)
                        idx += 1
                        loPdf.set_xy(x + w01, y)
                        self.check_v(loPdf, w08, h, LADATOS[idx], 0, 1, "R")
                        loPdf.rect(x, y, w09, h, "")
                elif i in [1, 4, 5, 6, 9]:
                    self.check_v(loPdf, w09, h, LADATOS[idx], 0, 1, "R")
                    loPdf.rect(x, y, w09, h, "")
                elif i in [2, 3, 7, 8]:
                    self.check_sino_square_h(loPdf, w09, h, LADATOS[idx], 1, 1)
                elif i == 10:
                    self.check_v(loPdf, w09, h1, LADATOS[idx], 1, 1)
                    idx += 1
                    loPdf.set_xy(x, y + h1)
                    loPdf.multi_cell(w09, 0.8, LADATOS[idx]["CRESULT"], 1, "L")
                idx += 1
                x += w09
            y += h
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_rm_312(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "M583",
            "M712",
            "M713",
            "M714",
            "M715",
            "M716",
            "M717",
            "M718",
            "M719",
            "M720",
            "M721",
            "M722",
            "M723",
            "M533",
            "T001",
            "T002",
            "T003",
            "T004",
            "T005",
            "T006",
            "T007",
            "T008",
            "T009",
            "T010",
            "T011",
            "T017",
            "M671",
            "M672",
            "M673",
            "M674",
            "M675",
            "M676",
            "M501",
            "M502",
            "M503",
            "M504",
            "M530",
            "M531",
            "M711",
            "M678",
            "M677",
            "M679",
            "M680",
            "M681",
            "M682",
            "M683",
            "M684",
            "M685",
            "M686",
            "M687",
            "M688",
            "M689",
            "M690",
            "M691",
            "M692",
            "M693",
            "M694",
            "M695",
            "M696",
            "M697",
            "M698",
            "M699",
            "M700",
            "M701",
            "M702",
            "M703",
            "M704",
            "M705",
            "M706",
            "M707",
            "M708",
            "M709",
            "M710",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)
        # INIT EXEC #
        self.print_title(
            loPdf,
            "FICHA MEDICA RM-312",
        )
        h2 = self.l_h * 2
        h4 = self.l_h * 4
        h6 = self.l_h * 6
        w03 = self.l_w * 0.03
        w06 = self.l_w * 0.06
        w078 = self.l_w * 0.078
        w1 = self.l_w * 0.1
        w12 = self.l_w * 0.12
        w15 = self.l_w * 0.15
        w18 = self.l_w * 0.18
        w105 = self.l_w * 0.105
        w2 = self.l_w * 0.2
        w4 = self.l_w * 0.4
        w48 = self.l_w * 0.48
        w6 = self.l_w * 0.6
        w85 = self.l_w * 0.85
        self.sub_antecedentes(loPdf)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(
            self.l_w,
            self.l_h,
            "ABSENTISMO: Enfermedades y Accidentes (asociado a trabajo o no)",
            1,
            1,
            "C",
        )
        # ESTOS DATOS SALEN DE LA TABLA PROPIA DE ABSENTISMO, PARECIDO A ANTECEDENTES EN EL FORMATO DE PSICOLOGIA
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(w4, h2, "Enfermedad, Accidente", 1, 0, "C")
        x = loPdf.get_x()
        y = loPdf.get_y() + self.l_h
        loPdf.cell(w2, self.l_h, "Asociado al Trabajo", 1, 0, "C")
        loPdf.cell(w2, h2, "Año", 1, 0, "C")
        loPdf.cell(w2, h2, "Días de descanso", 1, 0, "C")
        loPdf.set_xy(x, y)
        loPdf.cell(w1, self.l_h, "SI", 1, 0, "C")
        loPdf.cell(w1, self.l_h, "NO", 1, 1, "C")
        idx = 0
        loPdf.set_aligns(["L", "C", "C", "C", "C"])
        lcheck = self.arr_si_no_x(LADATOS[idx + 2])
        loPdf.row(
            [
                LADATOS[idx]["CRESULT"],
                lcheck[0],
                lcheck[1],
                LADATOS[idx + 3]["CRESULT"],
                LADATOS[idx + 4]["CRESULT"],
            ],
            [w4, w1, w1, w2, w2],
        )
        idx += 4
        loPdf.set_aligns(["L", "C", "C", "C", "C"])
        lcheck = self.arr_si_no_x(LADATOS[idx + 2])
        loPdf.row(
            [
                LADATOS[idx]["CRESULT"],
                lcheck[0],
                lcheck[1],
                LADATOS[idx + 3]["CRESULT"],
                LADATOS[idx + 4]["CRESULT"],
            ],
            [w4, w1, w1, w2, w2],
        )
        idx += 4
        loPdf.set_aligns(["L", "C", "C", "C", "C"])
        lcheck = self.arr_si_no_x(LADATOS[idx + 2])
        loPdf.row(
            [
                LADATOS[idx]["CRESULT"],
                lcheck[0],
                lcheck[1],
                LADATOS[idx + 3]["CRESULT"],
                LADATOS[idx + 4]["CRESULT"],
            ],
            [w4, w1, w1, w2, w2],
        )
        idx += 4

        loPdf.add_page()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "EVALUACION MEDICA", 1, 1, "C")
        loPdf.set_font("Arial", "", 6)

        loPdf.ln(0.2)
        loPdf.row(["Anamnesis", LADATOS[idx]["CRESULT"]], [w15, w85])

        loPdf.ln(0.2)
        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.multi_cell(w1, self.l_h, "Examen Clínico", 0, "C")
        loPdf.set_font("Arial", "", 6)
        loPdf.set_xy(x, y)
        loPdf.cell(w1, h4, "", 1, 0, "C")
        x = loPdf.get_x()

        loPdf.set_bolds(["B", "", "B", "", "B", "", "B", ""])
        loPdf.row(
            [
                "PA (mmHg.)",
                "",
                "Temp. (°C)",
                "",
                "Sat. O2 (%)",
                "",
                "Cadera (cm.)",
                "",
            ],
            [
                w12,
                w105,
                w12,
                w105,
                w12,
                w105,
                w12,
                w105,
            ],
        )
        loPdf.set_x(x)
        loPdf.set_bolds(["B", "", "B", "", "B", "", "B", ""])
        loPdf.row(
            ["F. Resp (x min.)", "", "Peso Kg.", "", "IMC (Kg/m2)", "", "ICC", ""],
            [
                w12,
                w105,
                w12,
                w105,
                w12,
                w105,
                w12,
                w105,
            ],
        )
        loPdf.set_x(x)
        loPdf.set_bolds(["B", "", "B", "", "B", ""])
        loPdf.row(
            ["F.Card (x min.)", "", "Talla (m.)", "", "Cintura (cm.)", ""],
            [w12, w105, w12, w105, w12, w105],
        )
        loPdf.set_x(x)
        idx += 1
        loPdf.row(["Otros :", LADATOS[idx]["CRESULT"]], [w12, w078])

        loPdf.ln()
        idx += 1
        loPdf.row(
            ["Ectoscopia :", LADATOS[idx]["CRESULT"]],
            [w15, w85],
        )
        idx += 1
        loPdf.row(
            ["Estado Mental :", LADATOS[idx]["CRESULT"]],
            [w15, w85],
        )

        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "EXAMEN FISICO", 1, 1, "C")
        loPdf.set_font("Arial", "", 6)
        loPdf.ln(0.2)
        loPdf.set_bolds(["B", "B", "B"])
        loPdf.set_aligns(["C", "C", "C"])
        loPdf.row(
            ["Órgano o Sistema", "Sin Hallazgos", "Hallazgos"],
            [w2, w2, w6],
        )
        idx += 1
        loPdf.row(
            [
                "Piel",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Cabello",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        loPdf.cell(w2, h6, "Ojos y Anexos", 1, 0, "L")
        xtemp = loPdf.get_x()
        ytemp = loPdf.get_y()
        idx += 2
        loPdf.multi_cell(w2, 0.23, LADATOS[idx]["CRESULT"], 0, "L")
        loPdf.set_xy(xtemp, ytemp)
        loPdf.cell(w2, h6, "", 1, 0, "L")
        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.cell(w12, h2, "Agudeza visual", 1, 0, "C")
        loPdf.cell(w03, self.l_h, "OD", 1, 0, "C")
        idx += 1
        loPdf.cell(w06, self.l_h, LADATOS[idx]["CRESULT"], 1, 0, "L")
        loPdf.cell(w03, self.l_h, "OI", 1, 0, "C")
        idx += 1
        loPdf.cell(w06, self.l_h, LADATOS[idx]["CRESULT"], 1, 0, "L")
        loPdf.cell(w12, h2, "Con Correctores", 1, 0, "C")
        loPdf.cell(w03, self.l_h, "OD", 1, 0, "C")
        idx += 1
        loPdf.cell(w06, self.l_h, LADATOS[idx]["CRESULT"], 1, 0, "L")
        loPdf.cell(w03, self.l_h, "OI", 1, 0, "C")
        idx += 1
        loPdf.cell(w06, self.l_h, LADATOS[idx]["CRESULT"], 1, 1, "L")
        loPdf.set_x(x)
        loPdf.cell(w12)
        idx += 1
        loPdf.cell(w18, self.l_h, LADATOS[idx]["CRESULT"], 1, 0, "L")
        loPdf.cell(w12)
        idx += 1
        loPdf.cell(w18, self.l_h, LADATOS[idx]["CRESULT"], 1, 1, "L")
        loPdf.set_x(x)
        loPdf.cell(w12, h2, "Fondo de Ojo", 1, 0, "C")
        idx += 1
        loPdf.cell(w18, h2, LADATOS[idx]["CRESULT"], 1, 0, "L")
        loPdf.cell(w12, h2, "Visión de Colores", 1, 0, "C")
        idx += 1
        loPdf.cell(w18, h2, LADATOS[idx]["CRESULT"], 1, 1, "L")
        loPdf.set_x(x)
        loPdf.cell(w12, h2, "Visión de Profundidad", 1, 0, "C")
        idx += 1
        loPdf.cell(w48, h2, LADATOS[idx]["CRESULT"], 1, 1, "L")

        idx += 1
        loPdf.row(
            [
                "Oídos",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Nariz",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Boca",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Faringe",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Cuello",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Aparato Respiratorio",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Aparato Cardiovascular",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Aparato Digestivo",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Aparato Genitourinario",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Aparato Locomotor",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Marcha",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Columna",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Miembros Superiores",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Miembros Inferiores",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Sistema Linfático",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        idx += 2
        loPdf.row(
            [
                "Sistema Nervioso",
                LADATOS[idx]["CRESULT"],
                LADATOS[idx + 1]["CRESULT"],
            ],
            [w2, w2, w6],
        )
        self.om_conclusiones(loPdf)
        self.om_diagnosticos(loPdf)
        # DO EXEC #
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_anexo_16_a(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "T001",
            "T002",
            "T003",
            "T007",
            "T008",
            "M534",
            "M535",
            "M536",
            "M537",
            "M538",
            "M539",
            "M540",
            "M541",
            "M539",
            "M542",
            "M543",
            "M544",
            "M545",
            "M546",
            "M547",
            "M548",
            "M549",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)
        # INIT EXEC #
        self.print_title(
            loPdf,
            "ANEXO 16 A",
        )
        w0902 = self.l_w * 0.902
        w04 = self.l_w * 0.04
        w06 = self.l_w * 0.06
        w14 = self.l_w * 0.14
        w2 = self.l_w * 0.2
        w8 = self.l_w * 0.8
        # DO EXEC #
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, LADATOS[0]["CIMPRIM"], 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        for i in range(5):
            loPdf.set_font("Arial", "B", 6)
            loPdf.cell(w06, self.l_h, LADATOS[i]["CIMPRIM"], 1, 0, "C")
            loPdf.set_font("Arial", "", 6)
            loPdf.cell(w14, self.l_h, LADATOS[i]["CRESULT"], 1, 0, "L")
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(
            self.l_w,
            self.l_h,
            "El/La señor(a)/(ita) ha presentado en los ultimos 6 meses:",
            1,
            1,
            "C",
        )
        loPdf.set_font("Arial", "", 6)
        loPdf.ln(0.2)
        loPdf.set_border(1)
        loPdf.set_borders([0])
        loPdf.set_bolds(["", "B", "B"])
        loPdf.set_aligns(["L", "C", "C"])
        loPdf.row(["", "SI", "NO"], [w0902, w04, w04])
        for i in range(5, 21):
            xboolean = self.arr_si_no_x(LADATOS[i])
            loPdf.set_aligns(["L", "C", "C"])
            loPdf.row(
                ["- " + LADATOS[i]["CIMPRIM"], xboolean[0], xboolean[1]],
                [w0902, w04, w04],
            )
        loPdf.set_border(0)
        loPdf.row(
            ["- " + LADATOS[21]["CIMPRIM"], LADATOS[21]["CRESULT"]],
            [w2, w8],
        )
        loPdf.multi_cell(
            self.l_w,
            self.l_h,
            "Declaro que las respuestas dadas en el presente documento son verdaderas y estoy consciente que el ocultar o falsear información me puede causar daño por lo que asumo total responsabilidad de ello.",
            0,
            "J",
        )
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_anexo_16(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "M552",
            "M553",
            "M554",
            "M555",
            "M556",
            "M557",
            "M558",
            "M559",
            "M560",
            "M561",
            "M562",
            "M563",
            "M564",
            "M565",
            "M566",
            "M567",
            "M568",
            "M569",
            "M570",
            "M571",
            "M573",
            "M574",
            "M584",
            "M585",
            "M586",
            "T013",
            "T014",
            "T002",
            "T003",
            "T007",
            "T004",
            "T006",
            "T005",
            "T008",
            "T009",
            "T010",
            "T011",
            "M587",
            "M588",
            "M589",
            "M590",
            "M591",
            "M592",
            "M593",
            "M594",
            "M595",
            "M596",
            "M597",
            "M598",
            "M599",
            "M600",
            "O054",
            "M501",
            "M502",
            "M503",
            "M504",
            "M505",
            "M506",
            "M711",
            "M601",
            "M602",
            "M034",
            "M035",
            "M036",
            "M037",
            "M038",
            "M039",
            "M040",
            "M042",
            "M043",
            "M044",
            "M045",
            "M046",
            "M047",
            "M048",
            "M030",
            "M032",
            "M605",
            "M606",
            "M607",
            "M608",
            "M609",
            "M610",
            "M611",
            "M612",
            "M613",
            "M615",
            "M614",
            "M616",
            "M617",
            "M618",
            "M619",
            "M620",
            "M621",
            "R001",
            "R036",
            "M623",
            "M625",
            "M627",
            "M624",
            "M626",
            "M628",
            "R010",
            "R010",
            "R013",
            "M631",
            "M629",
            "L027",
            "L028",
            "L007",
            "L006",
            "L050",
            "L051",
            "L055",
            "L052",
            "L053",
            "L080",
            "M630",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)
        # INIT EXEC #
        self.print_title(
            loPdf,
            "ANEXO 16",
        )
        h2 = self.l_h * 2
        h3 = self.l_h * 3
        w02 = self.l_w * 0.02
        w05 = self.l_w * 0.05
        w06 = self.l_w * 0.06
        w07 = self.l_w * 0.07
        w08 = self.l_w * 0.08
        w1 = self.l_w * 0.1
        w12 = self.l_w * 0.12
        w125 = self.l_w * 0.125
        w14 = self.l_w * 0.14
        w15 = self.l_w * 0.15
        w16 = self.l_w * 0.16
        w2 = self.l_w * 0.2
        w26 = self.l_w * 0.26
        w25 = self.l_w * 0.25
        w28 = self.l_w * 0.28
        w35 = self.l_w * 0.35
        w36 = self.l_w * 0.36
        w3 = self.l_w * 0.3
        w32 = self.l_w * 0.32
        w4 = self.l_w * 0.4
        w42 = self.l_w * 0.42
        w45 = self.l_w * 0.45
        w48 = self.l_w * 0.48
        w5 = self.l_w * 0.5
        w52 = self.l_w * 0.52
        w6 = self.l_w * 0.6
        w65 = self.l_w * 0.65
        w74 = self.l_w * 0.74
        w75 = self.l_w * 0.75
        w79 = self.l_w * 0.79
        w8 = self.l_w * 0.8
        w94 = self.l_w * 0.94
        # MINERALES EXPLOTADOS O PROCESADOS
        loPdf.set_align("C")
        loPdf.set_border(1)
        loPdf.row(
            [
                "MINERALES EXPLOTADOS O PROCESADOS",
                "ALTITUD DE LA LABOR",
                "EXPUESTO A",
            ],
            [w2, w32, w48],
        )
        loPdf.ln()
        x = loPdf.get_x()
        y = loPdf.get_y()
        self.check_v(loPdf, w2, h3, LADATOS[0], 0, 1)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w06, self.l_h, "TIPO", 1, 0, "C")
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(w14, self.l_h, LADATOS[1]["CRESULT"], 1, 1, "C")
        loPdf.set_xy(x + w2, y)
        tmp_arr1 = LADATOS[2].copy()
        tmp_arr2 = tmp_arr1.copy()
        tmp_arr1["MTABLA"] = LADATOS[2]["MTABLA"][0:3]
        tmp_arr2["MTABLA"] = LADATOS[2]["MTABLA"][3:6]
        self.check_v(loPdf, w16, h3, tmp_arr1, 0, 1)
        loPdf.set_xy(x + w36, y)
        self.check_v(loPdf, w16, h3, tmp_arr2, 0, 1)
        xo = x + w52
        loPdf.set_xy(xo, y)
        for idx_2 in range(3, 7):
            xboolean = self.str_check_si(LADATOS[idx_2])
            loPdf.set_borders([0, 1])
            loPdf.row([LADATOS[idx_2]["CIMPRIM"], xboolean], [w06, w02])
            loPdf.set_x(xo)
        xo += w08
        loPdf.set_xy(xo, y)
        for idx_2 in range(7, 11):
            xboolean = self.str_check_si(LADATOS[idx_2])
            loPdf.set_borders([0, 1])
            loPdf.row([LADATOS[idx_2]["CIMPRIM"], xboolean], [w12, w02])
            loPdf.set_x(xo)
        xo += w14
        loPdf.set_xy(xo, y)
        for idx_2 in range(11, 15):
            xboolean = self.str_check_si(LADATOS[idx_2])
            loPdf.set_borders([0, 1])
            loPdf.row([LADATOS[idx_2]["CIMPRIM"], xboolean], [w08, w02])
            loPdf.set_x(xo)
        xo += w1
        loPdf.set_xy(xo, y)
        for idx in range(15, 19):
            xboolean = self.str_check_si(LADATOS[idx])
            loPdf.set_borders([0, 1])
            loPdf.row([LADATOS[idx]["CIMPRIM"], xboolean], [w14, w02])
            loPdf.set_x(xo)
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w06, self.l_h, "OTRO", 1, 0, "C")
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(w94, self.l_h, LADATOS[19]["CRESULT"], 1, 1, "L")
        loPdf.ln(self.l_h)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(
            self.l_w,
            self.l_h,
            "ANTECEDENTES OCUPACIONALES (Ver adjunto Historia Ocupacional)",
            1,
            1,
            "C",
        )
        loPdf.cell(
            self.l_w,
            self.l_h,
            "ANTECEDENTES PERSONALES (Enfermedades y accidetes en el trabajo y fuera del mismo)",
            1,
            1,
            "C",
        )
        loPdf.set_font("Arial", "", 6)
        loPdf.set_border(1)
        loPdf.row(["ALERGIAS", LADATOS[20]["CRESULT"]], [w2, w8])
        loPdf.row(["INMUNIZACIONES", LADATOS[21]["CRESULT"]], [w2, w8])
        loPdf.ln(self.l_h)
        loPdf.set_border(0)

        # HABITOS
        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w25, self.l_h, "HABITOS", 1, 2, "C")
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(w05, self.l_h, "", 0, 0, "C")
        loPdf.cell(w05, self.l_h, "Nada", 0, 0, "C")
        loPdf.cell(w05, self.l_h, "Poco", 0, 0, "C")
        loPdf.cell(w05, self.l_h, "Habitual", 0, 0, "C")
        loPdf.cell(w05, self.l_h, "Excesivo", 0, 0, "C")
        loPdf.ln()
        loPdf.cell(w05, self.l_h, "Tabaco", 1, 0, "L")
        loPdf.set_x(x + w05)
        self.opt_h(
            loPdf,
            w2,
            self.l_h,
            LADATOS[22],
        )
        loPdf.ln()
        loPdf.cell(w05, self.l_h, "Alcohol", 1, 0, "L")
        loPdf.set_x(x + w05)
        self.opt_h(
            loPdf,
            w2,
            self.l_h,
            LADATOS[23],
        )
        loPdf.ln()
        loPdf.cell(w05, self.l_h, "Drogas", 1, 0, "L")
        loPdf.set_x(x + w05)
        self.opt_h(
            loPdf,
            w2,
            self.l_h,
            LADATOS[24],
        )
        # FUNCIONES VITALES
        loPdf.set_xy(x + w25, y)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w2, self.l_h, "FUNCIONES VITALES", 1, 2, "C")
        loPdf.set_font("Arial", "", 6)
        for idx in range(25, 31):
            loPdf.set_x(x + w25)
            loPdf.set_borders([0, 1])
            loPdf.row(
                [
                    LADATOS[idx]["CIMPRIM"],
                    LADATOS[idx]["CRESULT"] + LADATOS[idx]["CDESUNI"],
                ],
                [w1, w1],
            )
        # BIOMETRIA
        loPdf.set_xy(x + w45, y)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w2, self.l_h, "BIOMETRIA", 1, 2, "C")
        loPdf.set_font("Arial", "", 6)
        for idx in range(31, 37):
            loPdf.set_x(x + w45)
            loPdf.set_borders([0, 1])
            loPdf.row(
                [
                    LADATOS[idx]["CIMPRIM"],
                    LADATOS[idx]["CRESULT"] + "  " + LADATOS[idx]["CDESUNI"],
                ],
                [w1, w1],
            )
        # FUNCION RESPIRATORIA
        loPdf.set_xy(x + w65, y)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w35, self.l_h, "FUNCION RESPIRATORIA", 1, 1, "C")
        loPdf.set_x(x + w65)
        loPdf.row(["", "Ref.", "Abs %"], [w1, w1, w1])
        loPdf.set_font("Arial", "", 6)
        loPdf.set_x(x + w65)
        loPdf.cell(w1, self.l_h, "FVC", 0, 1, "L")
        loPdf.set_x(x + w65)
        loPdf.cell(w1, self.l_h, "FEV1", 0, 1, "L")
        loPdf.set_x(x + w65)
        loPdf.cell(w1, self.l_h, "FEV1/FVC", 0, 1, "L")
        loPdf.set_x(x + w65)
        loPdf.cell(w1, self.l_h, "FEF 25-75%", 0, 1, "L")
        loPdf.set_xy(x + w75, y + 0.4)
        idx = 37
        for i in range(5):
            loPdf.set_x(x + w75)
            loPdf.cell(w1, self.l_h, LADATOS[idx]["CRESULT"], 1, 0, "C")
            idx += 1
            loPdf.cell(w1, self.l_h, LADATOS[idx]["CRESULT"], 1, 1, "C")
            idx += 1
        loPdf.ln(self.l_h)
        loPdf.set_x(x + w65)
        loPdf.set_borders([0, 1])
        loPdf.row(["Conclusion", LADATOS[45]["CRESULT"]], [w1, w2])

        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "CABEZA", 0, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(self.l_w, self.l_h, LADATOS[46]["CRESULT"], 1, 1, "L")
        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w5 - 0.2, self.l_h, "CUELLO", 0, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(w5 - 0.2, self.l_h, LADATOS[47]["CRESULT"], 1, 1, "L")
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w5 - 0.2, self.l_h, "BOCA, AMIGDALAS, FARINGE, LARINGE", 0, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(w5 - 0.2, self.l_h, LADATOS[48]["CRESULT"], 1, 1, "L")
        x = x + w5 + 0.2
        loPdf.set_xy(x, y)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w5 - 0.2, self.l_h, "NARIZ", 0, 2, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(w5 - 0.2, self.l_h, LADATOS[49]["CRESULT"], 1, 2, "L")
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(2.5, self.l_h, "Piezas en mal estado:", 1, 0, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(w35, self.l_h, LADATOS[50]["CRESULT"], 1, 2, "L")
        loPdf.set_x(x)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(2.5, self.l_h, "Piezas que faltan:", 1, 0, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.cell(w35, self.l_h, LADATOS[51]["CRESULT"], 1, 1, "L")
        loPdf.ln(0.2)
        y = loPdf.get_y()
        ancho = (w5 - 0.2) / 3
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(ancho, h2, "OJOS", 1, 0, "C")
        loPdf.cell(ancho, self.l_h, "SIN CORREGIR", 1, 0, "C")
        loPdf.cell(ancho, self.l_h, "CORREGIDA", 1, 1, "C")
        loPdf.cell(ancho)
        loPdf.cell(ancho / 2, self.l_h, "O.D.", 1, 0, "C")
        loPdf.cell(ancho / 2, self.l_h, "O.I.", 1, 0, "C")
        loPdf.cell(ancho / 2, self.l_h, "O.D.", 1, 0, "C")
        loPdf.cell(ancho / 2, self.l_h, "O.I.", 1, 1, "C")
        loPdf.set_font("Arial", "", 6)

        loPdf.cell(ancho, self.l_h, "VISIÓN DE LEJOS", 1, 0, "L")
        loPdf.cell(ancho / 2, self.l_h, LADATOS[52]["CRESULT"], 1, 0, "C")
        loPdf.cell(ancho / 2, self.l_h, LADATOS[53]["CRESULT"], 1, 0, "C")
        loPdf.cell(ancho / 2, self.l_h, LADATOS[54]["CRESULT"], 1, 0, "C")
        loPdf.cell(ancho / 2, self.l_h, LADATOS[55]["CRESULT"], 1, 1, "C")

        loPdf.cell(ancho, self.l_h, "VISIÓN DE CERCA", 1, 0, "L")
        loPdf.cell(ancho, self.l_h, LADATOS[56]["CRESULT"], 1, 0, "C")
        loPdf.cell(ancho, self.l_h, LADATOS[57]["CRESULT"], 1, 1, "C")

        loPdf.cell(ancho, self.l_h, "VISIÓN DE COLORES", 1, 0, "L")
        loPdf.cell(ancho * 2, self.l_h, LADATOS[58]["CRESULT"], 1, 0, "C")

        loPdf.set_xy(x, y)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w5 - 0.2, self.l_h, "ENFERMEDADES OCULARES:", 0, 2, "L")
        loPdf.set_font("Arial", "", 6)
        xtemp = loPdf.get_x()
        ytemp = loPdf.get_y()
        loPdf.multi_cell(w5 - 0.2, 0.23, LADATOS[59]["CRESULT"], 0, "L")
        loPdf.set_xy(xtemp, ytemp)
        loPdf.cell(w5 - 0.2, 0.6, "", 1, 2, "L")
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(w5 - 0.2, self.l_h, "REFLEJOS PUPILARES:", 0, 2, "L")
        loPdf.set_font("Arial", "", 6)
        xtemp = loPdf.get_x()
        ytemp = loPdf.get_y()
        loPdf.multi_cell(w5 - 0.2, 0.23, LADATOS[60]["CRESULT"], 0, "L")
        loPdf.set_xy(xtemp, ytemp)
        loPdf.cell(w5 - 0.2, 0.6, "", 1, 2, "L")
        # OIDOS
        loPdf.ln(0.2)
        ancho = (w5 - 0.2) * 0.125
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(4, self.l_h, "OIDOS", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        y = loPdf.get_y()
        loPdf.set_borders([0, 0, 0])
        loPdf.set_bolds(["", "B", "B"])
        loPdf.row(
            ["", "Audición derecha", "      500  1000 2000 3000 4000 6000 8000"],
            [ancho, (w5 - ancho) * 0.35, (w5 - ancho) * 0.65],
        )
        loPdf.set_borders([0])
        loPdf.set_aligns(["R", "C", "C", "C", "C", "C", "C", "C"])
        loPdf.set_bolds(["", "B", "B", "B", "B", "B", "B", "B"])
        loPdf.row(
            ["Hz", "500", "1000", "2000", "3000", "4000", "6000", "8000"],
            [ancho, ancho, ancho, ancho, ancho, ancho, ancho, ancho],
        )
        loPdf.set_borders([0])
        loPdf.set_aligns(["R", "C", "C", "C", "C", "C", "C", "C"])
        loPdf.row(
            [
                "dB (A)",
                LADATOS[61]["CRESULT"],
                LADATOS[62]["CRESULT"],
                LADATOS[63]["CRESULT"],
                LADATOS[64]["CRESULT"],
                LADATOS[65]["CRESULT"],
                LADATOS[66]["CRESULT"],
                LADATOS[67]["CRESULT"],
            ],
            [ancho, ancho, ancho, ancho, ancho, ancho, ancho, ancho],
        )

        loPdf.set_xy(x, y)
        loPdf.set_borders([0, 0, 0])
        loPdf.set_bolds(["", "B", "B"])
        loPdf.row(
            ["", "Audición izquierda", "      500  1000 2000 3000 4000 6000 8000"],
            [ancho, (w5 - ancho) * 0.35, (w5 - ancho) * 0.65],
        )
        loPdf.set_x(x)
        loPdf.set_borders([0])
        loPdf.set_aligns(["R", "C", "C", "C", "C", "C", "C", "C"])
        loPdf.set_bolds(["", "B", "B", "B", "B", "B", "B", "B"])
        loPdf.row(
            ["Hz", "500", "1000", "2000", "3000", "4000", "6000", "8000"],
            [ancho, ancho, ancho, ancho, ancho, ancho, ancho, ancho],
        )
        loPdf.set_x(x)
        loPdf.set_borders([0])
        loPdf.set_aligns(["R", "C", "C", "C", "C", "C", "C", "C"])
        loPdf.row(
            [
                "dB (A)",
                LADATOS[68]["CRESULT"],
                LADATOS[69]["CRESULT"],
                LADATOS[70]["CRESULT"],
                LADATOS[71]["CRESULT"],
                LADATOS[72]["CRESULT"],
                LADATOS[73]["CRESULT"],
                LADATOS[74]["CRESULT"],
            ],
            [ancho, ancho, ancho, ancho, ancho, ancho, ancho, ancho],
        )

        loPdf.ln(0.2)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(4, self.l_h, "OTOSCOPIA", 1, 1, "L")
        loPdf.set_font("Arial", "", 6)
        loPdf.ln(0.2)
        loPdf.set_borders([0, 1, 0, 0, 1])
        loPdf.set_aligns(["R", "L", "", "R", "L"])
        loPdf.row(
            ["OD", LADATOS[75]["CRESULT"], "", "OI", LADATOS[76]["CRESULT"]],
            [0.6, w5 - 0.2 - 0.6, 0.4, 0.6, w5 - 0.2 - 0.6],
        )

        loPdf.add_page()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(4, self.l_h, "PULMONES", 1, 0, "L")
        loPdf.set_font("Arial", "", 6)
        self.check_h(loPdf, 6, 0.4, LADATOS[77])
        loPdf.ln()

        loPdf.cell(2)
        loPdf.cell(2, self.l_h, "Descripción :", 0, 0, "R")
        loPdf.cell(6, self.l_h, LADATOS[78]["CRESULT"], 1, 1, "L")

        loPdf.set_border(1)
        loPdf.ln(0.1)
        loPdf.row(
            ["TORAX :", LADATOS[79]["CRESULT"], "CORAZÓN :", LADATOS[80]["CRESULT"]],
            [1.4, w5 - 1.4, 1.4, w5 - 1.4],
        )
        loPdf.ln(0.1)
        loPdf.set_border(0)
        loPdf.row(["Miembros superiores :", LADATOS[81]["CRESULT"]], [4, self.l_w - 4])
        loPdf.row(["Miembros inferiores :", LADATOS[82]["CRESULT"]], [4, self.l_w - 4])
        loPdf.set_borders([1, 1, 0, 1])
        loPdf.row(
            [
                "Reflejos Osteo-tendinos",
                LADATOS[83]["CRESULT"],
                "Marcha :",
                LADATOS[84]["CRESULT"],
            ],
            [4, (self.l_w - 4) * 0.5, (self.l_w - 4) * 0.1, (self.l_w - 4) * 0.4],
        )
        loPdf.set_borders([1, 1, 0, 1])
        loPdf.set_aligns(["L", "L", "L", "C"])
        loPdf.row(
            ["Columna vertebral :", LADATOS[85]["CRESULT"], "", "Tacto Rectal"],
            [4, (self.l_w - 4) * 0.55, (self.l_w - 4) * 0.05, (self.l_w - 4) * 0.4],
        )
        loPdf.cell(2, self.l_h, "Abdomen :", 1, 0, "L")
        loPdf.cell(
            (self.l_w - 4) * 0.55 + 2, self.l_h, LADATOS[86]["CRESULT"], 1, 1, "L"
        )
        loPdf.cell((self.l_w - 4) * 0.05)
        loPdf.set_xy(loPdf.get_x(), loPdf.get_y() + 0.1)
        self.check_h(loPdf, 6.4, 0.4, LADATOS[87])
        loPdf.ln()

        loPdf.set_border(1)
        loPdf.row(
            [
                "Anillos Inguinales",
                LADATOS[88]["CRESULT"],
                "Hernias",
                LADATOS[89]["CRESULT"],
                "Várices",
                LADATOS[90]["CRESULT"],
            ],
            [
                self.l_w * 0.13,
                self.l_w * 0.27,
                self.l_w * 0.08,
                self.l_w * 0.22,
                self.l_w * 0.08,
                self.l_w * 0.22,
            ],
        )
        loPdf.row(
            [
                "Órganos Genitales",
                LADATOS[91]["CRESULT"],
                "Ganglios :",
                LADATOS[92]["CRESULT"],
            ],
            [self.l_w * 0.13, self.l_w * 0.37, self.l_w * 0.08, self.l_w * 0.42],
        )
        loPdf.set_border(0)

        loPdf.cell(
            self.l_w,
            self.l_h,
            "Lenguaje, Atención, memoria, orientación, Inteligencia, Afectividad:",
            1,
            1,
            "L",
        )
        loPdf.multi_cell(self.l_w, self.l_h, LADATOS[93]["CRESULT"], 1, "L")
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "LECTURA DE LA PLACA DE TORAX", 1, 1, "C")
        loPdf.set_font("Arial", "", 6)
        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.set_border(1)
        loPdf.row(
            ["Calidad:", LADATOS[94]["CRESULT"], "Símbolos:", LADATOS[95]["CRESULT"]],
            [self.l_w * 0.2, self.l_w * 0.3, self.l_w * 0.2, self.l_w * 0.3],
        )
        loPdf.row(
            [
                "Vértices:",
                LADATOS[96]["CRESULT"],
                "Campos pulmonares:",
                LADATOS[97]["CRESULT"],
            ],
            [self.l_w * 0.2, self.l_w * 0.3, self.l_w * 0.2, self.l_w * 0.3],
        )
        loPdf.row(
            ["Hilos:", LADATOS[98]["CRESULT"], "Senos:", LADATOS[99]["CRESULT"]],
            [self.l_w * 0.2, self.l_w * 0.3, self.l_w * 0.2, self.l_w * 0.3],
        )
        loPdf.row(
            [
                "Mediastinos:",
                LADATOS[100]["CRESULT"],
                "Senos:",
                LADATOS[101]["CRESULT"],
            ],
            [self.l_w * 0.2, self.l_w * 0.3, self.l_w * 0.2, self.l_w * 0.3],
        )
        loPdf.row(
            [
                "Silueta cardiovascular:",
                LADATOS[102]["CRESULT"],
            ],
            [self.l_w * 0.2, self.l_w * 0.8],
        )
        loPdf.ln()
        loPdf.set_border(0)

        self.check_h(loPdf, self.l_w, 0.4, LADATOS[103])
        loPdf.ln()
        self.check_h(loPdf, self.l_w, 0.4, LADATOS[104])
        loPdf.ln()
        self.check_h(loPdf, self.l_w, 0.4, LADATOS[105])
        loPdf.ln()
        self.check_h(loPdf, self.l_w, 0.4, LADATOS[106])
        loPdf.ln()

        # LABORATORIO
        loPdf.ln()
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "LABORATORIO", 1, 1, "C")
        loPdf.set_font("Arial", "", 6)
        loPdf.set_border(1)
        loPdf.row(
            [
                "GRUPO SANGUÍNEO",
                LADATOS[107]["CRESULT"],
                "FACTOR",
                LADATOS[108]["CRESULT"],
                "Hemoglobina",
                LADATOS[109]["CRESULT"],
                "gr. %",
                "Hematocrito",
                LADATOS[110]["CRESULT"],
                "%",
                "Reacciones serológicas a Lúes",
            ],
            [
                self.l_w * 0.14,
                self.l_w * 0.08,
                self.l_w * 0.08,
                self.l_w * 0.08,
                self.l_w * 0.08,
                self.l_w * 0.08,
                self.l_w * 0.05,
                self.l_w * 0.08,
                self.l_w * 0.08,
                self.l_w * 0.05,
                self.l_w * 0.2,
            ],
        )

        x = loPdf.get_x()
        y = loPdf.get_y()
        loPdf.row(
            [
                "Glucosa",
                LADATOS[111]["CRESULT"],
                "Colesterol",
                LADATOS[112]["CRESULT"],
                "Trigliceridos",
                LADATOS[113]["CRESULT"],
                "HDL",
                LADATOS[114]["CRESULT"],
                "LDL",
                LADATOS[115]["CRESULT"],
                "Creatinina",
                LADATOS[116]["CRESULT"],
            ],
            [
                self.l_w * 0.06,
                self.l_w * 0.07,
                self.l_w * 0.07,
                self.l_w * 0.07,
                self.l_w * 0.08,
                self.l_w * 0.07,
                self.l_w * 0.05,
                self.l_w * 0.07,
                self.l_w * 0.05,
                self.l_w * 0.07,
                self.l_w * 0.07,
                self.l_w * 0.07,
            ],
        )
        loPdf.ln()

        loPdf.row(["Orina", LADATOS[117]["CRESULT"]], [self.l_w * 0.1, self.l_w * 0.9])
        loPdf.set_border(0)
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_odontologia(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "O001",
            "O002",
            "O003",
            "O004",
            "O005",
            "O006",
            "O007",
            "O008",
            "O009",
            "O010",
            "O011",
            "O012",
            "O013",
            "O014",
            "O015",
            "O016",
            "O017",
            "O018",
            "O019",
            "O020",
            "O021",
            "O022",
            "O023",
            "O024",
            "O025",
            "O026",
            "O027",
            "O028",
            "O029",
            "O030",
            "O031",
            "O032",
            "O033",
            "O034",
            "O035",
            "O036",
            "O037",
            "O038",
            "O039",
            "O040",
            "O041",
            "O042",
            "O043",
            "O044",
            "O045",
            "O046",
            "O047",
            "O048",
            "O049",
            "O050",
            "O051",
            "O052",
            "O053",
            "O054",
            "O055",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)
        # INIT EXEC #
        self.print_title(
            loPdf,
            "ODONTOGRAMA",
        )
        w11 = self.l_w * 0.11
        w13 = self.l_w * 0.13
        w17 = self.l_w * 0.17
        w21 = self.l_w * 0.21
        # DO EXEC #
        ancho = 0.84
        ancho_s = 0.625
        loPdf.set_font("Arial", "", 6)
        loPdf.set_x(4.4)
        loPdf.set_border(1)
        loPdf.set_align("C")
        loPdf.set_bold("B")
        loPdf.row(
            [
                "18",
                "17",
                "16",
                "15",
                "14",
                "13",
                "12",
                "11",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
            ],
            [ancho] * 5 + [ancho_s] * 6 + [ancho] * 5,
        )
        loPdf.set_x(4.4)
        loPdf.row(
            [
                LADATOS[0]["CRESULT"],
                LADATOS[1]["CRESULT"],
                LADATOS[2]["CRESULT"],
                LADATOS[3]["CRESULT"],
                LADATOS[4]["CRESULT"],
                LADATOS[5]["CRESULT"],
                LADATOS[6]["CRESULT"],
                LADATOS[7]["CRESULT"],
                LADATOS[8]["CRESULT"],
                LADATOS[9]["CRESULT"],
                LADATOS[10]["CRESULT"],
                LADATOS[11]["CRESULT"],
                LADATOS[12]["CRESULT"],
                LADATOS[13]["CRESULT"],
                LADATOS[14]["CRESULT"],
                LADATOS[15]["CRESULT"],
            ],
            [ancho] * 5 + [ancho_s] * 6 + [ancho] * 5,
        )
        loPdf.ln()
        loPdf.set_x(4.4)
        loPdf.image(
            Config.PATH_PDF_SRC + "/odontologia1.jpg",
            loPdf.get_x(),
            loPdf.get_y(),
            12.29,
            1.48,
        )
        loPdf.ln(2)
        loPdf.set_x(6.95)
        loPdf.set_bold("B")
        loPdf.row(
            [
                "55",
                "54",
                "53",
                "52",
                "51",
                "61",
                "62",
                "63",
                "64",
                "65",
            ],
            [ancho] * 2 + [ancho_s] * 6 + [ancho] * 2,
        )
        loPdf.set_x(6.95)
        loPdf.row(
            [
                LADATOS[16]["CRESULT"],
                LADATOS[17]["CRESULT"],
                LADATOS[18]["CRESULT"],
                LADATOS[19]["CRESULT"],
                LADATOS[20]["CRESULT"],
                LADATOS[21]["CRESULT"],
                LADATOS[22]["CRESULT"],
                LADATOS[23]["CRESULT"],
                LADATOS[24]["CRESULT"],
                LADATOS[25]["CRESULT"],
            ],
            [ancho] * 2 + [ancho_s] * 6 + [ancho] * 2,
        )

        loPdf.ln()
        loPdf.set_x(6.95)
        loPdf.image(
            Config.PATH_PDF_SRC + "/odontologia2.jpg",
            loPdf.get_x(),
            loPdf.get_y(),
            7.2,
            1.48,
        )
        loPdf.ln(1.7)
        loPdf.set_x(6.95)
        loPdf.image(
            Config.PATH_PDF_SRC + "/odontologia3.jpg",
            loPdf.get_x(),
            loPdf.get_y(),
            7.36,
            1.55,
        )
        loPdf.ln(2)
        loPdf.set_x(6.95)
        loPdf.set_bold("B")
        loPdf.row(
            [
                "85",
                "84",
                "83",
                "82",
                "81",
                "71",
                "72",
                "73",
                "74",
                "75",
            ],
            [ancho] * 2 + [ancho_s] * 6 + [ancho] * 2,
        )
        loPdf.set_x(6.95)
        loPdf.row(
            [
                LADATOS[26]["CRESULT"],
                LADATOS[27]["CRESULT"],
                LADATOS[28]["CRESULT"],
                LADATOS[29]["CRESULT"],
                LADATOS[30]["CRESULT"],
                LADATOS[31]["CRESULT"],
                LADATOS[32]["CRESULT"],
                LADATOS[33]["CRESULT"],
                LADATOS[34]["CRESULT"],
                LADATOS[35]["CRESULT"],
            ],
            [ancho] * 2 + [ancho_s] * 6 + [ancho] * 2,
        )
        loPdf.ln()
        loPdf.set_x(4.4)
        loPdf.image(
            Config.PATH_PDF_SRC + "/odontologia4.jpg",
            loPdf.get_x(),
            loPdf.get_y(),
            12.35,
            1.44,
        )
        loPdf.ln(2)
        loPdf.set_x(4.4)
        loPdf.set_bold("B")
        loPdf.row(
            [
                "48",
                "47",
                "46",
                "45",
                "44",
                "43",
                "42",
                "41",
                "31",
                "32",
                "33",
                "34",
                "35",
                "36",
                "37",
                "38",
            ],
            [ancho] * 5 + [ancho_s] * 6 + [ancho] * 5,
        )
        loPdf.set_x(4.4)
        loPdf.row(
            [
                LADATOS[36]["CRESULT"],
                LADATOS[37]["CRESULT"],
                LADATOS[38]["CRESULT"],
                LADATOS[39]["CRESULT"],
                LADATOS[40]["CRESULT"],
                LADATOS[41]["CRESULT"],
                LADATOS[42]["CRESULT"],
                LADATOS[43]["CRESULT"],
                LADATOS[44]["CRESULT"],
                LADATOS[45]["CRESULT"],
                LADATOS[46]["CRESULT"],
                LADATOS[47]["CRESULT"],
                LADATOS[48]["CRESULT"],
                LADATOS[49]["CRESULT"],
                LADATOS[50]["CRESULT"],
                LADATOS[51]["CRESULT"],
            ],
            [ancho] * 5 + [ancho_s] * 6 + [ancho] * 5,
        )
        loPdf.ln()
        loPdf.set_bolds(["B", "", "B", "", "B", ""])
        loPdf.row(
            [
                "NUMERO DE CARIES",
                LADATOS[52]["CRESULT"],
                "PIEZAS FALTANTES",
                LADATOS[53]["CRESULT"],
                "REMANENTE RADICULAR",
                LADATOS[54]["CRESULT"],
            ],
            [w17, w13, w17, w21, w21, w11],
        )
        loPdf.set_border(0)
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_musculo_esqueletica(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
            "M366",
            "M367",
            "M368",
            "M369",
            "M370",
            "M371",
            "M372",
            "M373",
            "M374",
            "M375",
            "M376",
            "M377",
            "M378",
            "M379",
            "M380",
            "M381",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)
        # INIT EXEC #
        self.print_title(
            loPdf,
            "FICHA DE EVALUACION MUSCULO ESQUELETICA BASICA",
        )
        # DO EXEC #
        w05 = self.l_w * 0.05
        w09 = self.l_w * 0.09
        w094 = self.l_w * 0.094
        w15 = self.l_w * 0.15
        w2 = self.l_w * 0.2
        w25 = self.l_w * 0.25
        w282 = self.l_w * 0.282
        w32 = self.l_w * 0.32
        w36 = self.l_w * 0.36
        loPdf.set_border(1)
        loPdf.set_font("Arial", "B", 6)
        loPdf.cell(self.l_w, self.l_h, "APTITUD DE ESPALDA", 1, 1, "C")
        loPdf.ln(0.2)
        loPdf.set_align("C")
        loPdf.set_bold("B")
        loPdf.set_x(w15)
        loPdf.row(
            [
                "Flexibilidad Fuerza",
                "Excelente: 1",
                "Promedio: 2",
                "Regular: 3",
                "Pobre: 4",
                "Ptos.+",
                "OBSERVACIONES",
            ],
            [
                w2,
                w09,
                w09,
                w09,
                w09,
                w05,
                w2,
            ],
        )
        # imprimir imagenes
        loPdf.ln(0.1)
        text = ["ABDOMEN", "CADERA", "MUSLO", "ABDOMEN LATERAL"]
        x = loPdf.get_x()
        y = loPdf.get_y()
        text_i = 0
        for i in range(0, 8, 2):
            loPdf.set_x(w15)
            loPdf.set_row_square(1.1)
            loPdf.row(
                [
                    text[text_i],
                    " ",
                    LADATOS[i]["CRESULT"],
                    LADATOS[i + 1]["CRESULT"],
                ],
                [w2, w36, w05, w2],
            )
            text_i += 1
        loPdf.image(
            Config.PATH_PDF_SRC + "/evaluacion_musculo_esqueletica_1.jpg",
            x + 6,
            y + 0.1,
            w32,
            4,
        )
        # segunda imagen
        loPdf.ln(0.6)
        loPdf.multi_cell(
            self.l_w,
            self.l_h,
            "En puntos colocar el grado que corresponde a la capacidad del paciente. Repetir cada movimiento contra resistencia leve a moderada y evaluar fortaleza y presencia de dolor.",
            0,
            "C",
        )
        loPdf.ln(0.6)
        loPdf.set_align("C")
        loPdf.set_bold("B")
        loPdf.set_x(w15)
        loPdf.row(
            [
                "Rangos Articulares",
                "Optimo: 1",
                "Limitado: 2",
                "Muy limitado: 3",
                "Ptos.+",
                "Dolor contra resistencia",
            ],
            [
                w282,
                w094,
                w094,
                w094,
                w05,
                w2,
            ],
        )
        # loPdf.set_h_square(1)
        text = [
            "Abduccion de hombro (Normal 0-180)",
            "Abduccion de hombro (Normal 0-60)",
            "Rotación externa (Normal 0-90)",
            "Rotación externa de hombro (interna)",
        ]
        x = loPdf.get_x()
        y = loPdf.get_y()
        text_i = 0
        for i in range(8, 16, 2):
            loPdf.set_x(w15)
            loPdf.set_row_square(1.2)
            loPdf.row(
                [
                    text[text_i],
                    " ",
                    LADATOS[i]["CRESULT"],
                    LADATOS[i + 1]["CRESULT"],
                ],
                [w282, w282, w05, w2],
            )
            text_i += 1
        loPdf.image(
            Config.PATH_PDF_SRC + "/evaluacion_musculo_esqueletica_2.jpg",
            x + 7.5,
            y + 0.5,
            w25,
            4,
        )
        loPdf.ln(self.l_h)
        loPdf.ln()
        return True

    @exception_handler(False)
    def print_jsonactividad(self, loPdf) -> bool:
        # VAL #
        arr_ind = [
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
            "M018",
        ]
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)
        # INIT EXEC #
        self.print_title(
            loPdf,
            "INFORME MEDICO",
        )
        # DO EXEC #
        w2 = self.l_w * 0.2
        w3 = self.l_w * 0.3
        w4 = self.l_w * 0.4
        w5 = self.l_w * 0.5
        w6 = self.l_w * 0.6
        w7 = self.l_w * 0.7
        w8 = self.l_w * 0.8
        loPdf.cell(self.l_w, self.l_h, "DATOS", 1, 1, "L")
        loPdf.row(
           [
                "PESO: " + self.paDatos[0]["CRESULT"],
                "TALLA: " + self.paDatos[1]["CRESULT"],
                "IMC: " + self.paDatos[2]["CRESULT"],
            ],
                [w3, w3, w3],
            )
        loPdf.row(
            ["PRESION ARTERIAL: ", self.paDatos[3]["CRESULT"]], [w3, w6]
        )
        loPdf.row(
            ["FRECUENCIA CARDIACA: ", self.paDatos[4]["CRESULT"]],
            [w3, w6],
        )
        loPdf.ln(self.l_h)
        loPdf.cell(self.l_w, self.l_h, "LABORATORIO", 1, 1, "L")
        loPdf.ln(self.l_h)
        loPdf.cell(w2, self.l_h, "HEMOGRAMA", 0, 0, "L")
        self.opt_v_coment(
            loPdf,
            w8,
            self.l_h,
            self.paDatos[5],
            self.paDatos[6]
        )
        loPdf.ln(self.l_h)
        loPdf.cell(w2, self.l_h, "EXAMEN DE ORINA", 0, 0, "L")
        self.opt_v_coment(
            loPdf,
            w8,
            self.l_h,
            self.paDatos[7],
            self.paDatos[8]
        )
        loPdf.ln(self.l_h)
        loPdf.row(
            ["Hemoglobina", self.paDatos[9]["CRESULT"], self.paDatos[9]["CRANGO"]],
            [w4, w3, w3],
        )
        loPdf.row(
            ["Glucosa", self.paDatos[10]["CRESULT"], self.paDatos[10]["CRANGO"]],
            [w4, w3, w3],
        )
        loPdf.row(
            [
                "Colesterol Total",
                self.paDatos[11]["CRESULT"],
                self.paDatos[11]["CRANGO"],
            ],
                [w4, w3, w3],
        )
        loPdf.row(
            [
                "Trigliceridos",
                self.paDatos[12]["CRESULT"],
                self.paDatos[12]["CRANGO"],
                ],
                [w4, w3, w3],
            )
        loPdf.row(
            ["Creatinina", self.paDatos[13]["CRESULT"], self.paDatos[13]["CRANGO"]],
            [w4, w3, w3],
        )
        loPdf.ln(self.l_h)
        loPdf.cell(self.l_w, self.l_h, "EXAMENES MEDICOS AUXILIARES", 1, 1, "L")
        for item in self.paDatos[14:22]:
            loPdf.row([item["CIMPRIM"], item["CRESULT"]], [w3, w7])
        loPdf.ln(self.l_h)
        self.mx__print_cie10_for_json_actividad(loPdf)
        loPdf.ln(self.l_h)
        self.mx_print_extras(loPdf)
        self.mx_print_aptitud(loPdf)
        loPdf.ln(self.l_h)
        loPdf.set_bold("B")
        loPdf.set_align("C")
        loPdf.set_border(1)
        loPdf.row(
            ["Nombre del Medico calificador", "Nombre del Medico auditor"],
            [w5, w5],
        )
        loPdf.set_border(0)
        loPdf.ln(0.1)
        y = loPdf.get_y()
        loPdf.cell(w5, self.l_h, "Dra Lizbeth Zegarra Quiroz", 0, 1, "C")
        x = loPdf.get_x()
        loPdf.cell(w5, self.l_h, "Medico Evaluador", 0, 1, "C")
        loPdf.cell(w5, self.l_h, "C.M.P 094678", 0, 1, "C")
        loPdf.set_xy(x + w5, y)
        loPdf.cell(w5, self.l_h, "Dra Nadieshda Flores Barriga", 0, 1, "C")
        loPdf.set_xy(x + w5, y + self.l_h)
        loPdf.cell(w5, self.l_h, "Director Medico Ocupacional", 0, 1, "C")
        loPdf.set_xy(x + w5, y + 0.8)
        loPdf.cell(w5,self.l_h, "C.M.P 054801", 0, 1, "C")
        loFirma = Config.PATH_PDF_SRC + "/" + self.paData["CUSUFIR"] + ".jpg"
        if Path(loFirma).is_file():
            loPdf.image(loFirma, 13, 26, 3.5, 2.5)
        loPdf.ln(self.l_h)
        return True

    
    @exception_handler(False)
    def print_base(self, loPdf) -> bool:
        # VAL #
        arr_ind = []
        arr_ind_aux = arr_ind[:]
        LADATOS = []
        for item in arr_ind_aux:
            find = next((d for d in self.paDatos if d.get("CCODIND") == item), None)
            if find is None:
                raise AssertionError(
                    f"VARIABLE NO DEFINIDA :'{item}' \n {json.dumps(self.paDatos, indent=3, sort_keys=True)}"
                )
            LADATOS.append(find)
            arr_ind.remove(item)
        # INIT EXEC #
        self.print_title(
            loPdf,
            "TRIAJE",
        )
        # DO EXEC #
        loPdf.ln()
        return True

    # END PRINT ACTIVITIES #

    # MAIN ACTIVITY #
    @exception_handler(False)
    def print_actividad(self) -> bool:
        if self.paData is None:
            raise ValueError("DATA NO DEFINIDA")
        # BODY
        if self.paDatos is None:
            raise ValueError("DATOS NO DEFINIDOS")

        if self.paExamen is None:
            raise ValueError("EXAMENES NO DEFINIDOS")
        # INIT EXEC
        loPdf = PYFPDF()
        loPdf.set_margins(1, 1.6, 1)
        self.setWidth(loPdf._width())
        self.setHeigth(0.4)
        loPdf.alias_nb_pages()
        loPdf.add_page()
        i = 1
        lnpage = len(self.paExamen)
        for lafila in self.paExamen:
            lccodexa = lafila["CCODIGO"]
            lctipser = lafila["CTIPSER"]
            switch = {
                "000000": [
                    self.print_triaje,
                    self.print_signature_by_cnrodni,
                ],
                "200213": [
                    self.print_oftalmologico,
                    self.print_signature_by_cnrodni,
                ],
                "200214": [
                    self.print_oftalmologico,
                    self.print_oftalmologico_especializado,
                    self.print_signature_by_cnrodni,
                ],
                "S00001": [
                    self.print_triaje,
                    self.sub_antecedentes,
                    self.print_signature_by_cnrodni,
                ],
                "210301": [
                    self.print_audiologico,
                    self.print_signature_by_cnrodni,
                ],
                "XXXX01": [
                    self.print_osteomioarticular,
                    self.print_signature_by_cnrodni,
                ],
                "XXXX03": [
                    self.print_sintomas_musculo_tendinoso,
                    self.print_signature_by_cnrodni,
                ],
                "210201": [
                    self.print_electrocardiograma,
                    self.print_signature_by_cnrodni,
                ],
                "200302": [
                    self.print_psicologica,
                    self.print_signature_by_cnrodni,
                ],
                "XXXX04": [
                    self.print_musculo_esqueletica,
                    self.print_signature_by_cnrodni,
                ],
                "900000": [
                    self.print_odontologia,
                    self.print_signature_by_cnrodni,
                ],
                "XXXX09": [
                    self.print_rm_312,
                    self.print_signature_by_cnrodni,
                ],
                "XXXX10": [
                    self.print_anexo_16_a,
                    self.print_signature_by_cnrodni,
                ],
                "XXXX11": [
                    self.print_anexo_16,
                    self.print_signature_by_cnrodni,
                ],
                "XXXXXX": [
                    self.print_jsonactividad,
                ],
            }
            self.sub_header(loPdf)
            if lccodexa in switch:
                lafunction = switch[lccodexa]
                for lafunc in lafunction:
                    print("---------------------FUNCTION----------------------")
                    print(lafunc)
                    if not lafunc(loPdf):
                        return False
            if i != lnpage:
                loPdf.add_page()
            i += 1

        loPdf.output(self.lcPath + "/" + self.lcCodigo + ".pdf", "F")
        print("------------------PATH--------------")
        print(self.lcPath + "/" + self.lcCodigo + ".pdf")
        return True

    # END MAIN ACTIVITY #
