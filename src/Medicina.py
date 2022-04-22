from flask import Blueprint, jsonify, request
import json

from CSql import CSql
from CBase import CBase
from src.PDF.CActividad import CActividad

loSql = CSql()
loBase = CBase()
loActividad = CActividad('D:/72539751.pdf', 'MEDICINA', 'X-01-01')

Medicina = Blueprint('Medicina', __name__)
#ANTCEDENTES DE LA PERSONA
@Medicina.route('/MED/<string:p_cCodAct>', methods=['GET'])
def get_actividad(p_cCodAct):
    if  len(p_cCodAct) != 8:
        return jsonify({'OK':0, 'DATA':'CODIGO DEL PLAN NO VALIDO'})
    R1 = {'OK':0, 'DATA':''}
    lcSql = "SELECT  * FROM Medicina.Triaje WHERE _cCodPla = '{}'".format(p_cCodAct)
    loSql.ExecRS(lcSql)
    if loSql.data is None:
        R1['DATA'] = 'SIN TRIJAE ASOCIADO'
    else:
        R1['OK'] = 1
        R1['DATA']= loSql.data
    return jsonify(R1)

@Medicina.route('/MED', methods=['POST'])
def  post_actividad():
    R1 = {'OK':0, 'DATA':''}
    data = request.get_json()
    llOK = val_post_antecedente_by(data)
    if  llOK != None:
        R1['DATA'] = llOK
        return jsonify(R1)
    try:
        lcSql = "SELECT Rx.P_R001('{}')".format(json.dumps(data))
        loSql.ExecRS(lcSql)
        if loSql.data is None:
            raise ValueError('RESPUESTA VACIA')
        laFila = loSql.data
        if(not loBase.json_to_str(laFila[0][0])):
            raise ValueError('ERROR EN EJECCION')
        R1['OK'] = 1
        R1 = json.loads(laFila[0][0])
    except Exception as err: 
        R1['DATA'] =str(err)
    return jsonify(R1)

def  val_post_antecedente_by(data):
    error = None
    if data == None:
        error ="FALLO EN DATOS DE ENVIO"
    return error

@Medicina.route('/MED/PDF/<string:p_cCodAct>', methods=['GET'])
def  pdf_actividad(p_cCodAct):
    R1 = {'OK':0, 'DATA':''}
    data = {"CCODACT":p_cCodAct}
    try:
        lcSql = "SELECT Clinica.F_R100('{}')".format(json.dumps(data))
        loSql.ExecRS(lcSql)
        if loSql.data is None:
            raise ValueError('RESPUESTA VACIA')
        laFila = loSql.data
        if(not loBase.json_to_str(laFila[0][0])):
            raise ValueError('ERROR EN EJECCION')
        R1['OK'] = 1
        R1 = json.loads(laFila[0][0])
    except Exception as err: 
        R1['DATA'] =str(err)
    
    R2 = {'OK':0, 'DATA':''}
    try:
        #lcSql = "SELECT rx.F_R210('{}', '{}', '{}')".format(p_cCodAct, '900200', 1)
        #lcSql = "SELECT Medicina.F_R110('{}', '{}', '{}')".format(p_cCodAct, '600300', 1)
        #lcSql = "SELECT Medicina.F_R110('{}', '{}', '{}')".format(p_cCodAct, '600100', 1)
        lcSql = "SELECT Medicina.F_R110('{}', '{}', '{}')".format(p_cCodAct, '600400', 1)
        #lcSql = "SELECT Medicina.F_R110('{}', '{}', '{}')".format(p_cCodAct, '600500', 1)
        #lcSql = "SELECT Medicina.F_R110('{}', '{}', '{}')".format(p_cCodAct, '600101', 1)
        #lcSql = "SELECT Medicina.F_R110('{}', '{}', '{}')".format(p_cCodAct, '600102', 1)
        #lcSql = "SELECT Medicina.F_R110('{}', '{}', '{}')".format(p_cCodAct, '600202', 1)
        #lcSql = "SELECT Medicina.F_R110('{}', '{}', '{}')".format(p_cCodAct, '600203', 1)
        #lcSql = "SELECT Medicina.F_R110('{}', '{}', '{}')".format(p_cCodAct, '600600', 1)
        #lcSql = "SELECT Medicina.F_R110('{}', '{}', '{}')".format(p_cCodAct, '900100', 1)
        #lcSql = "SELECT Medicina.F_R110('{}', '{}', '{}')".format(p_cCodAct, '600204', 1)
        #lcSql = "SELECT Medicina.F_R110('{}', '{}', '{}')".format(p_cCodAct, '600200', 1)
        
        loSql.ExecRS(lcSql)
        if loSql.data is None:
            raise ValueError('RESPUESTA VACIA')
        laFila = loSql.data
        if(not loBase.json_to_str(laFila[0][0])):
            raise ValueError('ERROR EN EJECCION')
        R2['OK'] = 1
        R2 = json.loads(laFila[0][0])
    except Exception as err: 
        R2['DATA'] =str(err)

    loActividad.setData(R1['DATA'])
    loActividad.setDatos(R2)
    
    #llOK = loActividad.print_rayos_x()

    #llOK = loActividad.print_actividad_rx()
    #llOK = loActividad.print_examen_oftalmologico()
    #llOK = loActividad.print_ficha_psicologica()
    llOK = loActividad.print_cuestionario_osteomioarticular()
    #llOK = loActividad.print_cuestionario_sintomas_musculo_tendinoso()
    #llOK = loActividad.print_informe_psicologico()
    #llOK = loActividad.print_espirometria()
    #llOK = loActividad.print_evaluacion_trabajos_altura_1_8()
    #llOK = loActividad.print_screening_dermatologico()
    #llOK = loActividad.print_electrocardiograma()
    #llOK = loActividad.print_examen_audiologico()
    #llOK = loActividad.print_test_de_somnolencia()
    #llOK = loActividad.print_anexo_16_a()
    #OTROS SIN EXAMEN NI INDICADORES
    #llOK = loActividad.print_evaluacion_musculo_esqueletica()
    #llOK = loActividad.print_odontologia()
    #llOK = loActividad.print_ekg_riesgo_cardiovascular()
    #llOK = loActividad.print_triaje()
    #llOK = loActividad.print_ecografia()
    #llOK = loActividad.print_informe_aptitud_espacio_confinado()
    #llOK = loActividad.print_anexo_16()
    #llOK = loActividad.print_ficha_medica_rm_312()
    #llOK = loActividad.print_evaluacion_osteomioarticular()
    #llOK = loActividad.print_nutricion()
    #llOK = loActividad.print_antecedentes_ocupacionales()
    #llOK = loActividad.print_oftalmologia_basica()
    #llOK = loActividad.print_oftalmologia_especializada()
    
    if not llOK:
        R1['DATA'] = loActividad.error
    return R1