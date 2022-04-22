#!/usr/bin/env python
# -*- coding: utf-8 -*-
import traceback
from pathlib import Path

import requests
from app.CBase import CBase
from app.config import Config
from app.decorators import exception_handler
from app.PDF.PYFPDF import PYFPDF


class CConsentimiento(CBase):
    loBase = CBase()

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
                lcEncabezado = f"""Yo, {self.paData["CNOMBRE"]} identificado(a) con {self.paData["CDESDOC"]} N.º {self.paData["CNRODOC"]} de {self.paData["NEDAD"]} años. De ocupación {self.paData["CDESPUE"]}"""
                switch = {
                    "1": lcEncabezado
                    + " en pleno uso de mis facultades mentales, y de mis derechos de salud, en cumplimiento del artículo 25 de la Ley 26842, Ley General de Salud, luego de haber recibido y entendido la información brindada con claridad por el personal médico de la CLÍNICA ALIVIARI con respecto al Examen Médico Ocupacional, así mismo, entendiendo mi derecho de exigir la reserva del acto médico, y de consentir los procedimientos que se me realicen, por medio de la presente autorizo y doy CONSENTIMIENTO que se me practique el examen médico y todos los procedimientos aplicables relacionados al mismo, conforme a lo solicitado por mi empleador.\nAsí mismo, doy mi CONSENTIMIENTO para que los resultados, recomendaciones y conclusiones médicas sean remitidos al área de Medicina Ocupacional de mi empresa para su evaluación y tramite conforme a la R. M. 312-2011/MINSA.\nSoy conocedor que la firma del presente documento no es de carácter irrevocable y que el cualquier momento y sin necesidad de dar explicación alguna puedo expresar la revocación del consentimiento",
                    "2": lcEncabezado,
                    "3": lcEncabezado
                    + ", entiendo que someterse a un Análisis de Droga y/o Alcohol es una condición del empleo con este empleador. Entiendo además que, si los resultados de mi prueba fueran positivos o me negara al análisis, seré sujeto de acción disciplinaria por parte de la compañía, incluyendo posible despido.\nEntiendo así mismo, que una muestra alterada o adulterada será considerada una negativa a la prueba, que puede resultar en un posible despido.\nPor la presente doy mi consentimiento a que se revelen los resultados de mi análisis de orina y/o sangre a la(s) persona(s) o departamento(s) o agente especificado de mi empleador, con el fin de determinar la presencia de alcohol y/o drogas en mi cuerpo mientras dure mi empleo.\nAutorizo a la compañía a discutir los resultados con sus asesores legales y a usar los resultados de la prueba como defensa para cualquier acción legal de la que yo sea parte.\nAdemás libero a la CLÍNICA ALIVIARI de cualquier responsabilidad que surja de la comunicación de los resultados, reporte escrito, registros médicos y datos relacionados con la prueba a los funcionarios correspondientes del Empleador.\nACEPTO comunicar los resultados a la compañía y/o funcionario de Revisión Médica de la Empresa.",
                    "4": lcEncabezado
                    + ", he sido informada de los beneficios del análisis sérico de laboratorio devenido del dosaje de la Hormona Gonadotrofina Coriónica Humana - HCG previo al examen radiológico.\nHe tenido la oportunidad de efectuar preguntas sobre el análisis, el procedimiento, y he recibido respuestas satisfactorias y suficientes.\nTambién he sido informada sobre la protección de mis datos personales, mismos que serán incluidos en mi examen médico según el DS-055-2010-EM.\nEn consideración a lo anteriormente mencionado, otorgo mi consentimiento y permito que se me tome la muestra de sangre para que luego sea utilizada para alcanzar los objetivos de la evaluación médica en la Clínica Aliviari.\nEl presente documento se ampara en el Articulo 15, octavo párrafo de la Ley General de Salud N° 26842.",
                    "5": lcEncabezado
                    + " declaro aceptar que se me realice el examen médico ocupacional y doy fe de que la información brindada al Centro Médico Evaluador (CLINICA ALIVIARI) encargado del examen médico ocupacional es verídica.\nAdemás doy mi consentimiento para que mantenga en custodia toda la información resultante de mi examen médico ocupacional, así mismo entregue la misma al MÉDICO OCUPACIONAL de la empresa para su información y fines correspondientes.",
                    "6": lcEncabezado
                    + " declaro aceptar que se me realice el examen de Reagina Plasmática Rápida, la prueba de RPR no es para diagnóstico de Sífilis sino para detectar la presencia de anticuerpos presentes en la sangre de personas que pueden tener la enfermedad. De salir positivo, debe realizarse una prueba confirmatoria más específica.",
                    "7": lcEncabezado
                    + " certifico que: he leído (o se me ha leído) el documento sobre consentimiento informado que contiene la información sobre el propósito y beneficio de la prueba, su interpretación, sus limitaciones y riesgos, y que entiendo su contenido.\nHe recibido asesoría preprueba (actividad realizada por un profesional de la salud para prepararme y confortarme con relación a mis conocimientos, prácticas y conductas) antes de realizarme las pruebas diagnósticas. También certifico que dicha persona me brindo la asesoría y que según su compromiso, recibiré una asesoría posprueba (procedimiento mediante el cual se me entregaran mis resultados) y que estoy de acuerdo con el proceso.\nEntiendo que la toma de la muestra es voluntaria y que puedo retirar mi consentimiento en cualquier momento antes de que sea tomado el examen. Fui informado(a) de las medidas que se tomaran para proteger la confidencialidad de mis resultados.\nACEPTO realizarme la prueba presuntiva o diagnostica de VIH.",
                    "8": lcEncabezado
                    + ", declaro que:\n   1. Durante los últimos 3 días he tomado algún medicamento:\n      Si la respuesta es Si:\n      Nombre del medicamento:\n      Desde cuándo y que dosis:\n   2. Durante los últimos 3 días no he consumido sustancias que contengan coca (ejemplo: chacchar coca, caramelo de coca, mate de coca, etc.):\n      Si la respuesta es Si:\n      Fecha en la que consumí:\n      ¿Qué es lo que consumió?:",
                    "9": lcEncabezado
                    + " autorizo el uso de mi Firma Electrónica y Huella exclusivamente para la impresión de informes médicos realizados, así mismo, doy fe de que la información referida es verídica así como la información de los exámenes realizados en el centro de Salud.",
                    "A": lcEncabezado
                    + " declaro no estar en periodo de gestación, por lo tanto estoy en condiciones de someterme al examen radiológico solicitado por mi empresa.\nFecha ultima de regla:_________________",
                    "B": lcEncabezado
                    + ", declaro no ser sintomático respiratorio (No presento tos ni expectoración por más de 15 días).",
                    "C": lcEncabezado
                    + ", mediante la presente DECLARO que, he sido informado acerca del conjunto de exámenes que forman parte de mi Evaluación Médico Ocupacional y la importancia de cada una de ellas; sin embargo, por decisión propia y de manera voluntaria, NO DESEO realizarme la(s) prueba(s) o exámenes que a continuación se mencionan:\nPor lo que EXONERO a la CLÍNICA ALIVIARI de toda responsabilidad relacionada a la negativa voluntaria propia que he tomado con relación a la(s) prueba(s) o exámenes arriba señalados.",
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
                    loPdf.row(["", ""], [w5, w5])
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
