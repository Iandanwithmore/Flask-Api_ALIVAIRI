#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path

from app.adapters.PYFPDF import PYFPDF
from app.config import Config
from app.decorators import exception_handler
from app.fn_base import FnBase


class CConsentimiento(FnBase):
    loBase = FnBase()

    def __init__(self, p_cPath, p_cCodigo):
        self.lcPath = p_cPath
        Path(p_cPath).mkdir(parents=True, exist_ok=True)
        self.lcCodigo = p_cCodigo
        self.paData = None
        self.paConsentimiento = None
        self.paExamenes = None
        self.tmp = None
        self.error = None
        self.l_w = None
        self.l_h = None

    def setData(self, data):
        self.paData = data

    def setConsentimiento(self, consentientos):
        self.paConsentimiento = consentientos

    def setExamenes(self, examen):
        self.paExamenes = examen

    def setWidth(self, w):
        self.l_w = w

    def setHeigth(self, h):
        self.l_h = h

    @exception_handler(False)
    def print_head(self, loPdf):
        w1 = self.l_w * 0.1
        w15 = self.l_w * 0.15
        w2 = self.l_w * 0.2
        w25 = self.l_w * 0.25
        w4 = self.l_w * 0.4
        w8 = self.l_w * 0.8
        loPdf.set_border(1)
        loPdf.set_font("Arial", "", 6)
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
                self.paData["CNOMBRE"] + "   (SEXO : " + self.paData["CDESSEX"] + ")",
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
        loPdf.ln()
        return True

    @exception_handler(False)
    def mx_hoja_ruta(self, loPdf):
        w7 = self.l_w * 0.7
        w3 = self.l_w * 0.3
        if self.paExamenes is not None:
            for item in self.paExamenes:
                # aexamen = item["ADESEXA"].replace(",", "\n")
                loPdf.set_row_square(1)
                loPdf.cell(
                    self.l_w,
                    0.4,
                    item["CDESSER"],
                    1,
                    1,
                    "L",
                )
                loPdf.set_border(1)
                loPdf.row([item["ADESEXA"], ""], [w7, w3])
                loPdf.ln()
            loPdf.row(["HORA DE SALIDA", ""], [w7, w3])
            loPdf.set_border(0)
            return True

    @exception_handler(False)
    def print_consentimiento(self):
        loPdf = PYFPDF()
        if self.paData is None:
            raise ValueError("DATA NO DEFINIDA")
        i = 0
        if self.paConsentimiento is None:
            raise ValueError("DATA NO DEFINIDA")
        if self.paExamenes is None:
            raise ValueError("ERROR EN HOJA DE RUTA")
        j = len(self.paConsentimiento) if len(self.paConsentimiento) < 0 else 1
        loPdf.set_margins(1, 1.6, 1)
        self.setWidth(loPdf._width())
        self.setHeigth(0.4)
        w5 = self.l_w * 0.5
        if self.paConsentimiento is not None:
            for laFila in self.paConsentimiento:
                lcCodigo = laFila["CCODIGO"]
                lcEncabezado = f"""Yo, {self.paData["CNOMBRE"]} identificado(a) con {self.paData["CDESDOC"]} N.?? {self.paData["CNRODOC"]} de {self.paData["NEDAD"]} a??os. De ocupaci??n {self.paData["CDESPUE"]}"""
                switch = {
                    "1": lcEncabezado
                    + " en pleno uso de mis facultades mentales, y de mis derechos de salud, en cumplimiento del art??culo 25 de la Ley 26842, Ley General de Salud, luego de haber recibido y entendido la informaci??n brindada con claridad por el personal m??dico de la CL??NICA ALIVIARI con respecto al Examen M??dico Ocupacional, as?? mismo, entendiendo mi derecho de exigir la reserva del acto m??dico, y de consentir los procedimientos que se me realicen, por medio de la presente autorizo y doy CONSENTIMIENTO que se me practique el examen m??dico y todos los procedimientos aplicables relacionados al mismo, conforme a lo solicitado por mi empleador.\nAs?? mismo, doy mi CONSENTIMIENTO para que los resultados, recomendaciones y conclusiones m??dicas sean remitidos al ??rea de Medicina Ocupacional de mi empresa para su evaluaci??n y tramite conforme a la R. M. 312-2011/MINSA.\nSoy conocedor que la firma del presente documento no es de car??cter irrevocable y que el cualquier momento y sin necesidad de dar explicaci??n alguna puedo expresar la revocaci??n del consentimiento",
                    "2": lcEncabezado,
                    "3": lcEncabezado
                    + ", entiendo que someterse a un An??lisis de Droga y/o Alcohol es una condici??n del empleo con este empleador. Entiendo adem??s que, si los resultados de mi prueba fueran positivos o me negara al an??lisis, ser?? sujeto de acci??n disciplinaria por parte de la compa????a, incluyendo posible despido.\nEntiendo as?? mismo, que una muestra alterada o adulterada ser?? considerada una negativa a la prueba, que puede resultar en un posible despido.\nPor la presente doy mi consentimiento a que se revelen los resultados de mi an??lisis de orina y/o sangre a la(s) persona(s) o departamento(s) o agente especificado de mi empleador, con el fin de determinar la presencia de alcohol y/o drogas en mi cuerpo mientras dure mi empleo.\nAutorizo a la compa????a a discutir los resultados con sus asesores legales y a usar los resultados de la prueba como defensa para cualquier acci??n legal de la que yo sea parte.\nAdem??s libero a la CL??NICA ALIVIARI de cualquier responsabilidad que surja de la comunicaci??n de los resultados, reporte escrito, registros m??dicos y datos relacionados con la prueba a los funcionarios correspondientes del Empleador.\nACEPTO comunicar los resultados a la compa????a y/o funcionario de Revisi??n M??dica de la Empresa.",
                    "4": lcEncabezado
                    + ", he sido informada de los beneficios del an??lisis s??rico de laboratorio devenido del dosaje de la Hormona Gonadotrofina Cori??nica Humana - HCG previo al examen radiol??gico.\nHe tenido la oportunidad de efectuar preguntas sobre el an??lisis, el procedimiento, y he recibido respuestas satisfactorias y suficientes.\nTambi??n he sido informada sobre la protecci??n de mis datos personales, mismos que ser??n incluidos en mi examen m??dico seg??n el DS-055-2010-EM.\nEn consideraci??n a lo anteriormente mencionado, otorgo mi consentimiento y permito que se me tome la muestra de sangre para que luego sea utilizada para alcanzar los objetivos de la evaluaci??n m??dica en la Cl??nica Aliviari.\nEl presente documento se ampara en el Articulo 15, octavo p??rrafo de la Ley General de Salud N?? 26842.",
                    "5": lcEncabezado
                    + " declaro aceptar que se me realice el examen m??dico ocupacional y doy fe de que la informaci??n brindada al Centro M??dico Evaluador (CLINICA ALIVIARI) encargado del examen m??dico ocupacional es ver??dica.\nAdem??s doy mi consentimiento para que mantenga en custodia toda la informaci??n resultante de mi examen m??dico ocupacional, as?? mismo entregue la misma al M??DICO OCUPACIONAL de la empresa para su informaci??n y fines correspondientes.",
                    "6": lcEncabezado
                    + " declaro aceptar que se me realice el examen de Reagina Plasm??tica R??pida, la prueba de RPR no es para diagn??stico de S??filis sino para detectar la presencia de anticuerpos presentes en la sangre de personas que pueden tener la enfermedad. De salir positivo, debe realizarse una prueba confirmatoria m??s espec??fica.",
                    "7": lcEncabezado
                    + " certifico que: he le??do (o se me ha le??do) el documento sobre consentimiento informado que contiene la informaci??n sobre el prop??sito y beneficio de la prueba, su interpretaci??n, sus limitaciones y riesgos, y que entiendo su contenido.\nHe recibido asesor??a preprueba (actividad realizada por un profesional de la salud para prepararme y confortarme con relaci??n a mis conocimientos, pr??cticas y conductas) antes de realizarme las pruebas diagn??sticas. Tambi??n certifico que dicha persona me brindo la asesor??a y que seg??n su compromiso, recibir?? una asesor??a posprueba (procedimiento mediante el cual se me entregaran mis resultados) y que estoy de acuerdo con el proceso.\nEntiendo que la toma de la muestra es voluntaria y que puedo retirar mi consentimiento en cualquier momento antes de que sea tomado el examen. Fui informado(a) de las medidas que se tomaran para proteger la confidencialidad de mis resultados.\nACEPTO realizarme la prueba presuntiva o diagnostica de VIH.",
                    "8": lcEncabezado
                    + ", declaro que:\n   1. Durante los ??ltimos 3 d??as he tomado alg??n medicamento:\n      Si la respuesta es Si:\n      Nombre del medicamento:\n      Desde cu??ndo y que dosis:\n   2. Durante los ??ltimos 3 d??as no he consumido sustancias que contengan coca (ejemplo: chacchar coca, caramelo de coca, mate de coca, etc.):\n      Si la respuesta es Si:\n      Fecha en la que consum??:\n      ??Qu?? es lo que consumi???:",
                    "9": lcEncabezado
                    + " autorizo el uso de mi Firma Electr??nica y Huella exclusivamente para la impresi??n de informes m??dicos realizados, as?? mismo, doy fe de que la informaci??n referida es ver??dica as?? como la informaci??n de los ex??menes realizados en el centro de Salud.",
                    "A": lcEncabezado
                    + " declaro no estar en periodo de gestaci??n, por lo tanto estoy en condiciones de someterme al examen radiol??gico solicitado por mi empresa.\nFecha ultima de regla:_________________",
                    "B": lcEncabezado
                    + ", declaro no ser sintom??tico respiratorio (No presento tos ni expectoraci??n por m??s de 15 d??as).",
                    "C": lcEncabezado
                    + ", mediante la presente DECLARO que, he sido informado acerca del conjunto de ex??menes que forman parte de mi Evaluaci??n M??dico Ocupacional y la importancia de cada una de ellas; sin embargo, por decisi??n propia y de manera voluntaria, NO DESEO realizarme la(s) prueba(s) o ex??menes que a continuaci??n se mencionan:\nPor lo que EXONERO a la CL??NICA ALIVIARI de toda responsabilidad relacionada a la negativa voluntaria propia que he tomado con relaci??n a la(s) prueba(s) o ex??menes arriba se??alados.",
                }
                if lcCodigo in switch:
                    loPdf.alias_nb_pages()
                    loPdf.add_page()
                    loPdf.setHeader("FORMATOS DE ESPECIALES")
                    self.print_head(loPdf)
                    print("----------------SWITCH------------------")
                    print(switch[lcCodigo])
                    txt = switch[lcCodigo] or ""
                    loPdf.multi_cell(self.l_w, self.l_h, txt, 0, "J")
                    loPdf.ln()
                    loPdf.set_row_square(2)
                    loPdf.set_border(1)
                    loFirma = (
                        Config.PATH_PDF_SRC + "/" + self.paData["CUSUCOD"] + ".jpg"
                    )
                    if Path(loFirma).is_file():
                        loPdf.image(loFirma, 1, 20, 3.5, 2.5)
                    loHuella = (
                        Config.PATH_PDF_SRC + "/" + self.paData["CUSUCOD"] + ".jpg"
                    )
                    if Path(loHuella).is_file():
                        loPdf.image(loHuella, 1, 20, 3.5, 2.5)
                    loPdf.set_row_square(0.4)
                    loPdf.row(["FIRMA", "HUELLA"], [w5, w5])
                    loPdf.set_border(0)
                    if lcCodigo == 2:
                        self.recordatorio()
                    if not (i == j - 1):
                        loPdf.add_page()
                        i += 1
        loPdf.add_page()
        loPdf.setHeader("HOJA DE RUTA")
        self.print_head(loPdf)
        self.mx_hoja_ruta(loPdf)
        loPdf.ln()
        print("------------------PATH--------------")
        print(self.lcPath + "/" + self.lcCodigo + ".pdf")
        loPdf.output(self.lcPath + "/" + self.lcCodigo + ".pdf", "F")
        return True
