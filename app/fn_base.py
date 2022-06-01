import csv
import json
import os

from flask import current_app, send_from_directory
from werkzeug.utils import secure_filename


class FnBase:
    def __init__(self):
        self.error = None

    @staticmethod
    def fix_string(txt, length):
        if txt is not None:
            con = len(txt)
            if con < length:
                str = txt.ljust(length - con, " ")
            elif con > length:
                str = txt[0:length]
            elif con == len:
                str = txt
        else:
            str = " " * length
        return str

    @staticmethod
    def isJson(loJson):
        try:
            json.loads(loJson)
        except Exception:
            return False
        return True

    @staticmethod
    def json_respone_by_type(L1, L2, type_response=0):
        if type_response == 0:
            laData = [dict(zip(L1, item)) for item in L2]
        elif type_response == 1:
            laData = L1 + L2
        elif type_response == 2:
            laData = L2
        return laData

    def val_item_list(self, datos, key, li):
        try:
            for laFila in datos:
                if laFila[key] in li:
                    li.remove(laFila[key])
        except Exception:
            self.error = "DATOS DE LA FUNCION ERRONEOS"
            return False
        if li:
            self.error = "ERROR CODIGO NO ENCONTRADO " + ", ".join(li)
            return False
        return True

    def allowed_file(self, filename):
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower()
            in current_app.config["ALLOWED_EXTENSIONS"]
        )

    def download(self, path, filename):
        lcPath = os.path.join(current_app.config["PATH_FILE"], path)
        if not os.path.exists(lcPath):
            return send_from_directory(lcPath, filename, as_attachment=True)
        else:
            self.error = "ARCHIVO NO ENCONTRADO"
            return False

    def upload(self, p_oFile, path, filename=""):
        llOk = self.check_file(p_oFile)
        if not llOk:
            return False
        llOk = self.save_file(p_oFile, path, filename)
        return llOk

    def check_file(self, p_oFile):
        if p_oFile.filename == "":
            self.error = "NINGUN ARCHIVO SELECCIONADO"
            return False
        if p_oFile and self.allowed_file(p_oFile.filename):
            return True
        else:
            self.error = "EXTENSION DEL ARCHIVO INVALIDA"
            return False

    def save_file(self, p_oFile, path, filename=""):
        lcPath = os.path.join(current_app.config["PATH_FILE"], path)
        if not os.path.exists(lcPath):
            os.makedirs(lcPath)
        if filename == "":
            filename = p_oFile.filename
        filename = secure_filename(filename)
        try:
            p_oFile.save(os.path.join(lcPath, filename))
            return True
        except Exception as err:
            self.error = "ERROR AL GUARDAR EL ARCHIVO" + str(err)
            return False

    def read_csv_file(self, p_oFile):
        try:
            csv_reader = csv.reader(p_oFile, delimiter=",")
            line_count = 0
            laHeader = []
            self.paData = list()
            for row in csv_reader:
                if line_count == 0:
                    laHeader = row
                    line_count += 1
                else:
                    laTmpDic = {}
                    for i in range(len(row)):
                        laTmpDic[laHeader[i]] = row[i]
                    self.paData.append(laTmpDic)
                    line_count += 1
            return True
        except Exception as err:
            self.error = "ERROR AL PROCESAR ARCHIVO CSV" + str(err)
            return False

    def format_path_to_file(self, path, filename=""):
        if filename == "":
            return os.path.join(current_app.config["PATH_FILE"], path)
        else:
            return os.path.join(current_app.config["PATH_FILE"], path, filename)

    def fix_json__2(self, data):
        result = None
        if data is not None:
            d = {
                "\xc1": "A",
                "\xc9": "E",
                "\xcd": "I",
                "\xd3": "O",
                "\xda": "U",
                "\xdc": "U",
                "\xd1": "*N",
                "\xc7": "C",
                "\xed": "i",
                "\xf3": "o",
                "\xf1": "n",
                "\xe7": "c",
                "\xe1": "a",
                "\xe2": "a",
                "\xe3": "a",
                "\xe4": "a",
                "\xe5": "a",
                "\xe8": "e",
                "\xe9": "e",
                "\xea": "e",
                "\xeb": "e",
                "\xec": "i",
                "\xed": "i",
                "\xee": "i",
                "\xef": "i",
                "\xf2": "o",
                "\xf3": "o",
                "\xf4": "o",
                "\xf5": "o",
                "\xf0": "o",
                "\xf9": "u",
                "\xfa": "u",
                "\xfb": "u",
                "\xfc": "u",
                "\xe5": "a",
                "\xc3": "S",
                "\x89": "E",
                "\x91": "",
                "\x93": "",
                "\u00d1": "*N",
            }
            for word, initial in d.items():
                data = data.replace(word, initial)
            result = self.fix_json(data)
        return result

    def fix_json(self, json_message=None):
        result = None
        try:
            result = json.loads(json_message)
        except Exception as e:
            # Find the offending character index:
            idx_to_replace = int(e.message.split(" ")[-1].replace(")", ""))
            # Remove the offending character:
            json_message = list(json_message)
            json_message[idx_to_replace] = " "
            new_message = "".join(json_message)
            return self.fix_json_secondstep(json_message=new_message)
        return result
