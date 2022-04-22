#!/usr/bin/env python
#-*- coding: utf-8 -*-
from src.PDF.PYFPDF import PYFPDF
from CBase import CBase
class CActividad(CBase):
    def __init__(self, p_cPath, p_cTitulo, p_cCodigo):
        self.lcPath     = p_cPath
        self.lcTitulo   =p_cTitulo
        self.lcCodigo =p_cCodigo
        self.paData     =[]
        self.paDatos   =[]
        self.error        =''

    def setData(self, data):
        self.paData = data

    def setDatos(self, datos):
        self.paDatos = datos

    def x_boolean(self, boolean=None):
        try:
            if int(boolean) == 1:
                res = ['SI    (X)', 'NO']
            else:
                raise Exception
        except:
            res = ['SI', 'NO   (X)']
        return res
    
    def x_boolean_multi(self, boolean):
        try:
            if int(boolean) == 1:
                res = ['X', ' ']
            else:
                raise Exception
        except:
            res = [' ', 'X']
        return res

    def x_boolean_checkbox(self, boolean):
        try:
            if int(boolean) == 0:
                return [' ']
            else:
                raise Exception
        except:
            return ['X']

    def x_select(self, dict_data):
        tmp = []
        for laFila in dict_data:
            if laFila['CFLAGSE'] == 1:
                tmp += [laFila['CDESCRI']+'   (X)']
            else:
                tmp += [laFila['CDESCRI']+' ']
        return tmp
    
    def x_select_check(self, p_aOpcion, p_cResult):
        if int(p_aOpcion['NORDEN']) == int(p_cResult):
            return [p_aOpcion['CDESCRI'], 'X']
        return [p_aOpcion['CDESCRI'], ' ']

    def print_signatures(self, p_oPdf):
        p_oPdf.image("./src/PDF/assets/9999.jpg" , 1, 26, 3.5, 2.5)
        p_oPdf.image("./src/PDF/assets/9999.jpg" , 9, 26, 3.5, 2.5)
        p_oPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3.5, 2.5)
        p_oPdf.text(2.2,26, 'PACIENTE')
        p_oPdf.text(10,26, 'HUELLA DIGITAL')
        p_oPdf.text(18.5,26, 'MEDICO')

    def print_title(self, p_oPdf, p_cTitle):
        wr = p_oPdf._width()
        font_size = 17
        p_oPdf.set_font('Arial', 'B', font_size)
        while p_oPdf.get_string_width(p_cTitle) > wr:
            font_size -= 1
            p_oPdf.set_font('Arial', 'B', font_size)
        p_oPdf.cell(0, 1, p_cTitle, 0, 1, 'C')
        p_oPdf.set_font('Arial', '' , 6)

    def Head(self, p_oPDf):
        p_oPDf.set_border(1)
        p_oPDf.set_font('Arial', '' , 6)
        wr=p_oPDf._width()
        p_oPDf.set_bolds(['B', ' ', 'B', ' '])
        p_oPDf.Row(['COD.ATENCION :',self.paData['OACTIVI']['CCODACT'],'FECHA ATENCIÓN',self.paData['OACTIVI']['TFIN'][0:9]], [wr*0.2, wr*0.25, wr*0.15, wr*0.4])
        p_oPDf.set_bolds( ['B', ' ', 'B', ' ', 'B', ' '])
        p_oPDf.Row(['DOC.IDENTIDAD :',self.paData['OPERSON']['CNRODOC'],'F.NACIMIENTO',self.paData['OPERSON']['TNACIMI'], ' EDAD :',self.paData['OPERSON']['NEDAD']], [wr*0.2, wr*0.25, wr*0.15, wr*0.1, wr*0.2, wr*0.1])
        p_oPDf.set_bolds(['B', ' '])
        p_oPDf.Row(['APELLIDOS Y NOMBRES:',self.paData['OPERSON']['CNOMBRES']+'   (SEXO : '+self.paData['OPERSON']['CDESSEX']+')'], [wr*0.2, wr*0.8])
        if self.paData['OPLAACT']['CTIPPLA'] != 'E':
            p_oPDf.set_bolds(['B', ' '])
            p_oPDf.Row(['EMPRESA :',self.paData['OEMPRES']['CDESCRI']], [wr*0.2, wr*0.8])
            p_oPDf.set_bolds(['B', ' ', 'B', ' '])
            p_oPDf.Row(['TIPO EXAMEN :',self.paData['OPLAACT']['CDESTIP'],'PERFIL',self.paData['OPLAACT']['CDESPER']], [wr*0.2, wr*0.25, wr*0.15, wr*0.4])
            p_oPDf.set_bolds(['B', ' '])
            p_oPDf.Row(['PUESTO LABORAL :',self.paData['OPLAACT']['CDESPUE']], [wr*0.2, wr*0.8])
        p_oPDf.set_border(0)
        p_oPDf.ln(0.2)

    def val_examen_audiologico(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = ['0001','0002','0003','0004','0005','0006','0007','0008','0009','0010','0011','0012','0013','0014','0015','0016','0017','0018','0019','0020','0021','0022','0023','0024','0025','0026','0027','0028','0029','0030','0031','0032','0033','0034','0035','0036','0037','0038','0039','0040','0041','0042','0043','0044','0045','0046','0047','0048']
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True

    def print_audiologico_cuadro(self, p_oPdf, p_lLado, p_nX, p_nY):
        xo = p_nX
        yo = p_nY
        len_x = 0.75 #ancho de la celda
        len_y = 0.45 #alto de la celda

        png = ["./src/PDF/assets/x-blue.png", "./src/PDF/assets/bracket-left-red.png","./src/PDF/assets/bracket-right-blue.png","./src/PDF/assets/circle-red.png","./src/PDF/assets/less_red.png","./src/PDF/assets/more_blue.png","./src/PDF/assets/triangle-red.png"]
        valores_eje_x = ['250','500','1000','2000','3000','4000','6000','8000']
        valores_eje_y = ['-10','0','10','20','30','40','50','60','70','80','90','100','110']
        #indicadores
        li = ['0017','0018','0019','0020','0021','0022','0023','0024','0025','0026','0027','0028','0029','0030','0031','0032','0033','0034','0035','0036','0037','0038','0039','0040','0041','0042','0043','0044','0045','0046','0047','0048']
        i = 0
        tmp = []
        for laFila in self.paDatos:
            if laFila['CCODIND'] in li:
                tmp.append(int(laFila['CRESULT']))
                li.remove(laFila['CCODIND'])
            i+=1
        v_aerea_d = tmp[0:8]
        v_aerea_i = tmp[8:16]
        v_osea_d = tmp[16:24]
        v_osea_i = tmp[24:32]

        cant_lineas_ver = len(valores_eje_x)
        cant_lineas_hor = len(valores_eje_y)
        #dibujar lineas del plano cartesiano
        p_oPdf.set_line_width(0.01)
        p_oPdf.set_draw_color(200)
        #dibujar lineas del plano cartesiano horizontales
        x = xo
        y = yo + len_y
        for i in range(1, cant_lineas_hor):
            p_oPdf.line(x - 0.1, y, x + ((cant_lineas_ver - 1) * len_x) + 0.1, y)
            y += len_y
        yf = y + len_y #yf para saber donde acaba el gráfico
        #dibujar lineas del plano cartesiano verticales
        x = xo + len_x
        y = yo
        for i in range(1, cant_lineas_ver - 1):
            p_oPdf.line(x, y - 0.1, x, y + ((cant_lineas_hor - 1) * len_y) + 0.1)
            x += len_x
        #dibujar linea resultado
        p_oPdf.set_line_width(0.04)
        if p_lLado == 0: #0 der, 1 izq
            #aerea
            x = xo
            y = yo + (v_aerea_d[0] + 10) / 10 * len_y
            p_oPdf.image(png[3], x - 0.1, y - 0.1, 0.2, 0.2)
            p_oPdf.set_draw_color(255, 0, 0)
            for i in range(1, cant_lineas_ver):
                x2 = x + len_x
                y2 = yo + (v_aerea_d[i] + 10) / 10 * len_y
                p_oPdf.line(x, y, x2, y2)
                p_oPdf.image(png[3], x2 - 0.1, y2 - 0.1, 0.2, 0.2)
                x = x2
                y = y2
            #osea
            x = xo
            y = yo + (v_osea_d[0] + 10) / 10 * len_y
            p_oPdf.image(png[4], x - 0.1, y - 0.1, 0.2, 0.2)
            for i in range(1, cant_lineas_ver):
                x2 = x + len_x
                y2 = yo + (v_osea_d[i] + 10) / 10 * len_y
                p_oPdf.image(png[4], x2 - 0.1, y2 - 0.1, 0.2, 0.2)
                x = x2
                y = y2
        else:
            #aerea
            x = xo
            y = yo + (v_aerea_i[0] + 10) / 10 * len_y
            p_oPdf.image(png[0], x - 0.1, y - 0.1, 0.2, 0.2)
            p_oPdf.set_draw_color(0, 0, 255)
            for i in range(1, cant_lineas_ver):
                x2 = x + len_x
                y2 = yo + (v_aerea_i[i] + 10) / 10 * len_y
                p_oPdf.line(x, y, x2, y2)
                p_oPdf.image(png[0], x2 - 0.1, y2 - 0.1, 0.2, 0.2)
                x = x2
                y = y2
            #osea
            x = xo
            y = yo + (v_osea_i[0] + 10) / 10 * len_y
            p_oPdf.image(png[5], x - 0.1, y - 0.1, 0.2, 0.2)
            for i in range(1, cant_lineas_ver):
                x2 = x + len_x
                y2 = yo + (v_osea_i[i] + 10) / 10 * len_y
                p_oPdf.image(png[5], x2 - 0.1, y2 - 0.1, 0.2, 0.2)
                x = x2
                y = y2
        #dibujar ejes del plano cartesiano
        p_oPdf.set_draw_color(0)
        p_oPdf.set_line_width(0.02)
        p_oPdf.set_font('Arial', '' , 6)
        #dibujar eje x del plano cartesiano
        x = xo
        y = yo
        p_oPdf.line(x - 0.1, y, x + ((cant_lineas_ver - 1) * len_x) + 0.1, y)
        x = xo - 0.22
        y = yo - 0.2
        for i in range(cant_lineas_ver):
            p_oPdf.text(x, y, valores_eje_x[i])
            x += len_x
        #dibujar ejes y del plano cartesiano
        x = xo
        y = yo
        p_oPdf.line(x, y - 0.1, x, y + ((cant_lineas_hor - 1) * len_y) + 0.1)
        x = xo + len_x * (cant_lineas_ver - 1)
        p_oPdf.line(x, y - 0.1, x, y + ((cant_lineas_hor - 1) * len_y) + 0.1)
        x = xo - 0.48
        y = yo + 0.06
        x1 = xo + len_x * (cant_lineas_ver - 1) + 0.16
        for i in range(cant_lineas_hor):
            p_oPdf.text(x, y, valores_eje_y[i])
            p_oPdf.text(x1, y, valores_eje_y[i])
            y += len_y
        #dibujar lineas intermedia
        p_oPdf.set_line_width(0.04)
        x = xo + len_x * (cant_lineas_ver - 1)
        y = yo + (25 + 10) / 10 * len_y
        p_oPdf.line(xo, y, x, y)
        
        p_oPdf.set_line_width(0.02) #reverts to default
        p_oPdf.set_xy(xo, yf)#p_oPdf.set_xy(xo, yf + 0.4)#setea el puntero en el punto X donde inició el cuadro y en el punto Y donde acabó
        # p_oPdf.set_y(y+plus)

    def print_examen_audiologico(self):
        loPdf  = PYFPDF()
        llOK = self.val_examen_audiologico()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('AUDIOMETRIA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()
            
            self.print_title(loPdf, 'EXAMEN AUDIOLÓGICO')
            #cuadro antecedentes y detalle (en una row, antecedentes a la izquiera y detalle a la derecha)
            loPdf.set_border(1)
            loPdf.set_bolds(['B', 'B', 'B', 'B'])
            loPdf.set_aligns(['L', 'C', 'C', 'L'])
            loPdf.Row([self.paDatos[0]['CIMPRIM'], 'SI', 'NO', self.paDatos[9]['CIMPRIM']], [wr*0.40, wr*0.05, wr*0.05, wr*0.5])
            
            loPdf.set_aligns(['L', 'C', 'C'])
            boolean = self.x_boolean_multi(self.paDatos[1]['CRESULT'])
            loPdf.Row([self.paDatos[1]['CIMPRIM']]+boolean+[self.paDatos[10]['CIMPRIM'], self.paDatos[10]['CRESULT']], [wr*0.40, wr*0.05, wr*0.05, wr*0.20, wr*0.30])
            loPdf.set_aligns(['L', 'C', 'C'])
            boolean = self.x_boolean_multi(self.paDatos[2]['CRESULT'])
            xselect = self.x_select(self.paDatos[11]['MTABLA'])
            loPdf.Row([self.paDatos[2]['CIMPRIM']]+boolean+[self.paDatos[11]['CIMPRIM']] + [xselect[0]] + [xselect[1]], [wr*0.40, wr*0.05, wr*0.05, wr*0.20, wr*0.15, wr*0.15])
            loPdf.set_aligns(['L', 'C', 'C'])
            boolean = self.x_boolean_multi(self.paDatos[3]['CRESULT'])
            loPdf.Row([self.paDatos[3]['CIMPRIM']]+boolean+['', 'AUDIÓMETRO'], [wr*0.40, wr*0.05, wr*0.05, wr*0.20, wr*0.30])
            loPdf.set_aligns(['L', 'C', 'C'])
            boolean = self.x_boolean_multi(self.paDatos[4]['CRESULT'])
            loPdf.Row([self.paDatos[4]['CIMPRIM']]+boolean+['', 'Marca:'], [wr*0.40, wr*0.05, wr*0.05, wr*0.20, wr*0.30])
            loPdf.set_aligns(['L', 'C', 'C'])
            boolean = self.x_boolean_multi(self.paDatos[5]['CRESULT'])
            loPdf.Row([self.paDatos[5]['CIMPRIM']]+boolean+['', 'Modelo:'], [wr*0.40, wr*0.05, wr*0.05, wr*0.20, wr*0.30])
            loPdf.set_aligns(['L', 'C', 'C'])
            boolean = self.x_boolean_multi(self.paDatos[6]['CRESULT'])
            loPdf.Row([self.paDatos[6]['CIMPRIM']]+boolean+['', 'Serie:'], [wr*0.40, wr*0.05, wr*0.05, wr*0.20, wr*0.30])
            loPdf.set_aligns(['L', 'C', 'C'])
            boolean = self.x_boolean_multi(self.paDatos[7]['CRESULT'])
            loPdf.Row([self.paDatos[7]['CIMPRIM']]+boolean+['', 'Fecha calibración:'], [wr*0.40, wr*0.05, wr*0.05, wr*0.20, wr*0.30])
            loPdf.set_aligns(['L', 'C', 'C'])
            boolean = self.x_boolean_multi(self.paDatos[8]['CRESULT'])
            loPdf.Row([self.paDatos[8]['CIMPRIM']]+boolean+['', ''], [wr*0.40, wr*0.05, wr*0.05, wr*0.20, wr*0.30])
            #SINTOMAS ACTUALES
            loPdf.ln()
            loPdf.set_bolds(['B'])
            xselect = self.x_select(self.paDatos[12]['MTABLA'])
            loPdf.Row([self.paDatos[12]['CIMPRIM']] + [xselect[0]] + [xselect[1]] + [xselect[2]] + [xselect[3]], [wr*0.15, wr*0.22, wr*0.21, wr*0.21, wr*0.21])
            loPdf.Row([self.paDatos[13]['CIMPRIM']], [wr*1])
            loPdf.Row([self.paDatos[13]['CRESULT']], [wr*1])
            #EXAMEN CLINICO OTOSCOPIA
            loPdf.ln()
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(w, h, self.paDatos[14]['CIMPRIM'],0, 1, 'L')
            loPdf.set_font('Arial', '' , 6)
            xselect1 = self.x_select(self.paDatos[15]['MTABLA'])
            xselect2 = self.x_select(self.paDatos[17]['MTABLA'])
            loPdf.Row([self.paDatos[15]['CIMPRIM'], xselect1[0], xselect1[1], self.paDatos[16]['CRESULT']], [wr*0.15, wr*0.15, wr*0.15, wr*0.55])
            loPdf.Row([self.paDatos[17]['CIMPRIM'], xselect2[0], xselect2[1], self.paDatos[18]['CRESULT']], [wr*0.15, wr*0.15, wr*0.15, wr*0.55])
            #AUDIOGRAMAS
            loPdf.ln()
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(10.3, h, self.paDatos[19]['CIMPRIM'] + ' OD',0, 0, 'C')
            loPdf.cell(5.8, h, self.paDatos[19]['CIMPRIM'] + ' OI',0, 1, 'C')
            loPdf.set_font('Arial', '' , 6)
            loPdf.ln()

            xo=loPdf.get_x()
            yo=loPdf.get_y()
            self.print_audiologico_cuadro(loPdf, 0, xo + 2.5, yo)
            self.print_audiologico_cuadro(loPdf, 1, xo + 10.6, yo)
            loPdf.set_x(xo)
            #CUADRO SIMBOLOGIA
            xo=loPdf.get_x()
            yo=loPdf.get_y()
            png = ["./src/PDF/assets/x-blue.png", "./src/PDF/assets/bracket-left-red.png","./src/PDF/assets/bracket-right-blue.png","./src/PDF/assets/circle-red.png","./src/PDF/assets/less_red.png","./src/PDF/assets/more_blue.png","./src/PDF/assets/triangle-red.png"]
            esp = 14 #espacio a la derecha para dibujar el cuadro leyenda
            loPdf.set_x(xo + esp + 1.3)
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(1, h, 'SIMBOLOGIA',0, 1, 'L')
            loPdf.set_font('Arial', '' , 4)
            loPdf.set_x(xo + esp + 2.73)
            loPdf.Row(['enmascaramiento'],[wr*0.08])
            loPdf.set_font('Arial', '' , 6)
            loPdf.set_x(xo + esp)
            loPdf.Row(['','OD','OI','OD','OI'], [wr*0.07, wr*0.04, wr*0.04, wr*0.04, wr*0.04])
            loPdf.set_x(xo + esp)
            loPdf.Row(['Via aérea','','','',''], [wr*0.07, wr*0.04, wr*0.04, wr*0.04, wr*0.04])
            loPdf.image(png[3], xo+esp+1.55 + 0.72*0, yo+h*3+0.1, 0.2, 0.2)
            loPdf.image(png[0], xo+esp+1.55 + 0.72*1, yo+h*3+0.1, 0.2, 0.2)
            loPdf.image(png[6], xo+esp+1.55 + 0.72*2, yo+h*3+0.1, 0.2, 0.2)
            loPdf.image(png[6], xo+esp+1.55 + 0.72*3, yo+h*3+0.1, 0.2, 0.2)
            loPdf.set_x(xo + esp)
            loPdf.Row(['Via ósea','','','',''], [wr*0.07, wr*0.04, wr*0.04, wr*0.04, wr*0.04])
            loPdf.image(png[4], xo+esp+1.55 + 0.72*0, yo+h*4+0.1, 0.2, 0.2)
            loPdf.image(png[5], xo+esp+1.55 + 0.72*1, yo+h*4+0.1, 0.2, 0.2)
            loPdf.image(png[1], xo+esp+1.55 + 0.72*2, yo+h*4+0.1, 0.2, 0.2)
            loPdf.image(png[2], xo+esp+1.55 + 0.72*3, yo+h*4+0.1, 0.2, 0.2)
            loPdf.set_x(xo + esp)
            loPdf.Row(['Color','Rojo','Azul','Rojo','Azul'], [wr*0.07, wr*0.04, wr*0.04, wr*0.04, wr*0.04])
            #CONCLUSION Y RECOMENDACIONES
            loPdf.set_xy(xo, yo)
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(13,h, 'CONCLUSIÓN',1, 2, 'L')
            loPdf.set_font('Arial', '' , 6)
            if(self.paData['OACTIVI']['MCONCLU'] is not None):
                loPdf.multi_cell(13,h, self.paData['OACTIVI']['MCONCLU'],1, 'L')
            else:
                loPdf.cell(13,h, ' ',1, 2, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(13,h, 'RECOMENDACIONES',1, 2, 'L')
            loPdf.set_font('Arial', '' , 6)
            if(self.paData['OACTIVI']['MRECOME'] is not None):
                loPdf.multi_cell(13, h, self.paData['OACTIVI']['MRECOME'],1, 'L')
            else:
                loPdf.cell(13, h, ' ',1, 2, 'L')
            
            self.print_signatures(loPdf)

            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False


    def val_actividad_rx(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA';
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS';
            return False
        li=[]
        i=1
        while i<61: 
            li.append(str(i).zfill(4))
            i+=1
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True

    def print_actividad_rx(self):
        loPdf  = PYFPDF()
        llOK = self.val_actividad_rx()
        if not llOK:
            return False;
        try:
            w = 0;
            h = 0.4;
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('IMAGENOLOGIA', 'M-01-01',self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wt = loPdf._width()

            loPdf.set_font('', 'B' , 7)
            loPdf.cell(wt,h,'DETALLE RADIOGRAFIA', 1,0, 'C')
            loPdf.ln()

            loPdf.cell(wt*0.15,h,self.paDatos[0]['CIMPRIM'], 0,0, 'L')
            loPdf.set_font('', '' , 8)
            loPdf.data_in_checktable(self.paDatos[0]['MTABLA'], wt*0.85)
            
            loPdf.set_font('', 'B' , 7)
            loPdf.cell(wt*0.15,h,self.paDatos[1]['CIMPRIM'], 0,0, 'L')
            loPdf.set_font('', '' , 8)
            loPdf.data_in_checktable(self.paDatos[1]['MTABLA'], wt*0.85)
            loPdf.set_bolds(['B'])
            loPdf.Row([self.paDatos[2]['CIMPRIM'], self.paDatos[2]['CRESULT']],[wt*0.15, wt*0.85])

            loPdf.set_font('', 'B' , 7)
            loPdf.cell(wt,h,'ANORMALIDADES PARENQUIMATOSAS', 1,0, 'C')
            loPdf.ln()

            loPdf.set_font('', 'B' , 7)
            tmp_y = loPdf.get_y()
            loPdf.cell(wt*0.15,h*3,'ZONAS AFECTADAS', 0,0, 'L')
            tmp_x = loPdf.get_x()
            loPdf.set_xy(tmp_x,tmp_y)
            loPdf.set_borders([0,1,1])
            loPdf.Row(['SUPERIOR ',self.paDatos[3]['CRESULT'],self.paDatos[4]['CRESULT']], [wt*0.25, wt*0.3,wt*0.3])
            loPdf.set_xy(tmp_x,tmp_y+h)
            loPdf.set_borders([0,1,1])
            loPdf.Row(['MEDIA',self.paDatos[5]['CRESULT'],self.paDatos[6]['CRESULT']], [wt*0.25, wt*0.3,wt*0.3])
            loPdf.set_xy(tmp_x,tmp_y+h+h)
            loPdf.set_borders([0,1,1])
            loPdf.Row(['INFERIOR',self.paDatos[7]['CRESULT'],self.paDatos[8]['CRESULT']], [wt*0.25, wt*0.3,wt*0.3])
            loPdf.ln()

            loPdf.set_font('', 'B' , 7)
            tmp_x = wt*0.4
            tmp_y = loPdf.get_y()
            loPdf.Row([self.paDatos[9]['CIMPRIM']], [tmp_x])
            loPdf.set_xy(tmp_x+1.3,tmp_y)
            loPdf.data_in_checktable(self.paDatos[9]['MTABLA'], wt*0.6)
            loPdf.ln()

            loPdf.set_font('', 'B' , 7)
            tmp_x = wt*0.15
            tmp_y = loPdf.get_y()
            loPdf.cell(tmp_x,h*3,'FORMA Y TAMAÑO', 0,0, 'L')
            loPdf.set_xy(tmp_x+1.3,tmp_y)
            loPdf.cell(tmp_x,h,self.paDatos[10]['CIMPRIM'], 0,0, 'L')
            loPdf.set_x(tmp_x+5.8)
            loPdf.data_in_checktable(self.paDatos[10]['MTABLA'], wt*0.60)
            loPdf.set_xy(tmp_x+1.3,tmp_y+h)
            loPdf.cell(tmp_x,h,self.paDatos[11]['CIMPRIM'], 0,0, 'L')
            loPdf.set_x(tmp_x+5.8)
            loPdf.data_in_checktable(self.paDatos[11]['MTABLA'], wt*0.6)
            loPdf.ln()

            loPdf.set_font('', 'B' , 7)
            tmp_x = wt*0.4
            tmp_y = loPdf.get_y()
            loPdf.Row([self.paDatos[12]['CIMPRIM']], [tmp_x])
            loPdf.set_xy(tmp_x+1.3,tmp_y)
            loPdf.data_in_checktable(self.paDatos[12]['MTABLA'], wt*0.6)
            loPdf.ln()

            loPdf.set_font('', '' , 8)
            rpta = self.x_boolean(self.paDatos[13]['CRESULT'])
            loPdf.set_borders([0,1,1])
            loPdf.Row([self.paDatos[13]['CIMPRIM']]+rpta, [wt*0.7,wt*0.15,wt*0.15])
            loPdf.set_font('', 'B' , 7)
            loPdf.ln()
            loPdf.cell(w,h,'PLACAS PLEURALES 0:NINGUNA, D:HEMITORAX DERECHO, I:HERMITORAZ IZQUIERDO', 1,1, 'C')

            loPdf.Row([' ','SITIO', 'CALCIFICACION'],[wt*0.4,wt*0.3,wt*0.3])
            loPdf.ln(0.2)
            tmp_x = loPdf.get_x()
            tmp_y = loPdf.get_y()
            loPdf.cell(wt*0.4,h,'Pared toracica de Perfil', 0,0, 'L')
            loPdf.set_xy(wt*0.4+1.3,tmp_y)
            loPdf.data_in_checktable(self.paDatos[14]['MTABLA'], wt*0.3)
            loPdf.set_xy(tmp_x,tmp_y+h)
            loPdf.cell(wt*0.4,h,'Frente', 0,0, 'L')
            loPdf.set_xy(wt*0.4+1.3,tmp_y+h)
            loPdf.data_in_checktable(self.paDatos[15]['MTABLA'], wt*0.3)
            loPdf.set_xy(tmp_x,tmp_y+h*2)
            loPdf.cell(wt*0.4,h,'Diafragma', 0,0, 'L')
            loPdf.set_xy(wt*0.4+1.3,tmp_y+h*2)
            loPdf.data_in_checktable(self.paDatos[16]['MTABLA'], wt*0.3)
            loPdf.set_xy(tmp_x,tmp_y+h*3)
            loPdf.cell(wt*0.4,h,'Otro(s) sitio(s)', 0,0, 'L')
            loPdf.set_xy(wt*0.4+1.3,tmp_y+h*3)
            loPdf.data_in_checktable(self.paDatos[17]['MTABLA'], wt*0.3)
            loPdf.set_xy(wt*0.7+1.3,tmp_y)
            loPdf.data_in_checktable(self.paDatos[18]['MTABLA'], wt*0.3)
            loPdf.set_xy(wt*0.7+1.3,tmp_y+h)
            loPdf.data_in_checktable(self.paDatos[19]['MTABLA'], wt*0.3)
            loPdf.set_xy(wt*0.7+1.3,tmp_y+h*2)
            loPdf.data_in_checktable(self.paDatos[20]['MTABLA'], wt*0.3)
            loPdf.set_xy(wt*0.7+1.3,tmp_y+h*3)
            loPdf.data_in_checktable(self.paDatos[21]['MTABLA'], wt*0.3)
            loPdf.ln(0.2)

            tmp_x = loPdf.get_x()
            tmp_y = loPdf.get_y()
            loPdf.cell(wt*0.3,h,'EXTENSION Pared lateral del Torax', 0,0, 'L')
            loPdf.set_xy(wt*0.3+1.3,tmp_y)
            loPdf.cell(wt*0.3,h,'x <1/4', 0,0, 'L')
            loPdf.set_xy(wt*0.3+1.3,tmp_y+h)
            loPdf.cell(wt*0.3,h,'1/4<x<1/2', 0,0, 'L')
            loPdf.set_xy(wt*0.3+1.3,tmp_y+h*2)
            loPdf.cell(wt*0.3,h,'x>1/2', 0,0, 'L')
            loPdf.set_xy(wt*0.6+1.3,tmp_y)
            loPdf.data_in_checktable(self.paDatos[22]['MTABLA'], wt*0.4)
            loPdf.set_xy(wt*0.6+1.3,tmp_y+h)
            loPdf.data_in_checktable(self.paDatos[23]['MTABLA'], wt*0.4)
            loPdf.ln(0.2)

            tmp_x = loPdf.get_x()
            tmp_y = loPdf.get_y()
            loPdf.cell(wt*0.3,h,'ANCHO', 0,0, 'L')
            loPdf.set_xy(wt*0.3+1.3,tmp_y)
            loPdf.cell(wt*0.3,h,'3<x<5', 0,0, 'L')
            loPdf.set_xy(wt*0.3+1.3,tmp_y+h)
            loPdf.cell(wt*0.3,h,'5<=x<10', 0,0, 'L')
            loPdf.set_xy(wt*0.3+1.3,tmp_y+h*2)
            loPdf.cell(wt*0.3,h,'x>10', 0,0, 'L')
            loPdf.set_xy(wt*0.6+1.3,tmp_y)
            loPdf.data_in_checktable(self.paDatos[24]['MTABLA'], wt*0.4)
            loPdf.set_xy(wt*0.6+1.3,tmp_y+h)
            loPdf.data_in_checktable(self.paDatos[25]['MTABLA'], wt*0.4)
            loPdf.ln(0.2)
            loPdf.set_font('', 'B' , 7)
            loPdf.cell(wt*0.6,h,self.paDatos[26]['CIMPRIM'], 0,0, 'L')
            loPdf.data_in_checktable(self.paDatos[26]['MTABLA'], wt*0.4)

            loPdf.set_font('', 'B' , 7)
            loPdf.cell(w,h,'ENGROSAMENTO DIFUSO DE LA PLEURA', 1,1, 'C')
            loPdf.Row([' ','SITIO', 'CALCIFICACION'],[wt*0.4,wt*0.3,wt*0.3])
            loPdf.ln(0.2)
            tmp_x = loPdf.get_x()
            tmp_y = loPdf.get_y()
            loPdf.cell(wt*0.4,h,'Perfil', 0,0, 'L')
            loPdf.set_xy(wt*0.4+1.3,tmp_y)
            loPdf.data_in_checktable(self.paDatos[27]['MTABLA'], wt*0.3)
            loPdf.set_xy(tmp_x,tmp_y+h)
            loPdf.cell(wt*0.4,h,'Frente', 0,0, 'L')
            loPdf.data_in_checktable(self.paDatos[28]['MTABLA'], wt*0.3)
            loPdf.set_xy(wt*0.7+1.3,tmp_y)
            loPdf.data_in_checktable(self.paDatos[29]['MTABLA'], wt*0.3)
            loPdf.set_xy(wt*0.7+1.3,tmp_y+h)
            loPdf.data_in_checktable(self.paDatos[30]['MTABLA'], wt*0.3)
            loPdf.ln(0.2)

            tmp_x = loPdf.get_x()
            tmp_y = loPdf.get_y()
            loPdf.cell(wt*0.4,h,'EXTENSION', 0,0, 'L')
            loPdf.set_xy(wt*0.6+1.3,tmp_y)
            loPdf.data_in_checktable(self.paDatos[31]['MTABLA'], wt*0.4)
            loPdf.set_xy(wt*0.6+1.3,tmp_y+h)
            loPdf.data_in_checktable(self.paDatos[32]['MTABLA'], wt*0.4)
            loPdf.ln(0.2)

            tmp_x = loPdf.get_x()
            tmp_y = loPdf.get_y()
            loPdf.cell(wt*0.6,h,'ANCHO', 0,0, 'L')
            loPdf.set_xy(wt*0.6+1.3,tmp_y)
            loPdf.data_in_checktable(self.paDatos[33]['MTABLA'], wt*0.4)
            loPdf.set_xy(wt*0.6+1.3,tmp_y+h)
            loPdf.data_in_checktable(self.paDatos[34]['MTABLA'], wt*0.4)
            loPdf.ln(0.2)

            loPdf.set_font('', 'B' , 7)
            loPdf.cell(w,h,'SIMBOLOS', 1,1, 'C')
            loPdf.set_font('', '' , 8)
            rpta = self.x_boolean(self.paDatos[35]['CRESULT'])
            loPdf.set_borders([0,1,1])
            loPdf.Row([self.paDatos[35]['CIMPRIM']]+rpta, [wt*0.7,wt*0.15,wt*0.15])
            loPdf.ln(0.2)

            w=1
            for i in range(36,50):
                if self.paDatos[i]['CRESULT'] == 1:
                    loPdf.cell(w,h,self.paDatos[i]['CIMPRIM']+'   X', 1,0, 'L')
                else:
                    loPdf.cell(w,h,self.paDatos[i]['CIMPRIM'], 1,0, 'L')
            loPdf.ln()

            for i in range(50,65):
                if self.paDatos[i]['CRESULT'] == 1:
                    loPdf.cell(w,h,self.paDatos[i]['CIMPRIM']+'   X', 1,0, 'L')
                else:
                    loPdf.cell(w,h,self.paDatos[i]['CIMPRIM'], 1,0, 'L')
        
            # for y in list_y:
            #     loPdf.set_line_width(0.005)
            #     loPdf.line(0,y,wt+3,y)
            # loPdf.set_line_width(0.002)
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_examen_oftalmologico(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = ['0049','0050','0051','0052','0053','0054','0055','0056','0057','0058','0059','0060','0061','0062','0063','0064','0065','0066','0067','0068','0069','0070','0071','0072','0073','0074','0075','0076','0077','0078','0079','0080','0081','0082','0083','0084','0085','0086']
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True

    def print_examen_oftalmologico(self):
        loPdf  = PYFPDF()
        llOK = self.val_examen_oftalmologico()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'EXAMEN OFTALMOLÓGICO')
            loPdf.set_border(1)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, self.paDatos[0]['CIMPRIM'],0, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            check1 = self.x_boolean_checkbox(self.paDatos[1]['CRESULT'])
            check2 = self.x_boolean_checkbox(self.paDatos[2]['CRESULT'])
            check3 = self.x_boolean_checkbox(self.paDatos[3]['CRESULT'])
            for i in range(1, 4):
                check = self.x_boolean_checkbox(self.paDatos[i]['CRESULT'])
                loPdf.cell(0.4, h, check[0], 1, 0, 'C')
                loPdf.cell(loPdf.get_string_width(self.paDatos[i]['CIMPRIM']) + loPdf.c_margin*2 + 0.5, h, self.paDatos[i]['CIMPRIM'], 0, 0, 'L')
            loPdf.ln()

            boolean = self.x_boolean_multi(self.paDatos[4]['CRESULT'])
            loPdf.cell(loPdf.get_string_width(self.paDatos[4]['CIMPRIM']) + loPdf.c_margin*2, h, self.paDatos[4]['CIMPRIM'] + ": ", 0, 0, 'L')
            loPdf.cell(loPdf.get_string_width('No ') + loPdf.c_margin*2, h, 'No ', 0, 0, 'L')
            loPdf.cell(0.4, h, boolean[1], 1, 0, 'C')
            loPdf.cell(0.5)
            loPdf.cell(loPdf.get_string_width('Si ') + loPdf.c_margin*2, h, 'Si ', 0, 0, 'L')
            loPdf.cell(0.4, h, boolean[0], 1, 1, 'C')
            
            loPdf.cell(w, h, self.paDatos[5]['CIMPRIM'] + ': ' + self.paDatos[5]['CRESULT'],0, 1, 'L')
            loPdf.ln()
            loPdf.cell(w, h, self.paDatos[6]['CIMPRIM'] + ': ' + self.paDatos[6]['CRESULT'],0, 1, 'L')
            loPdf.ln()

            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, self.paDatos[7]['CIMPRIM'],0, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_bolds(['B', 'B', 'B'])
            loPdf.Row(['', 'SIN CORRECTORES', 'CON CORRECTORES'], [wr*0.20, wr*0.20, wr*0.20])
            loPdf.set_bolds(['B', 'B', 'B', 'B', 'B'])
            loPdf.Row(['AGUDEZA VISUAL', 'OD', 'OI', 'OD', 'OI'], [wr*0.20, wr*0.10, wr*0.10, wr*0.10, wr*0.10])
            loPdf.Row(['VISION DE LEJOS', self.paDatos[8]['CRESULT'], self.paDatos[9]['CRESULT'], self.paDatos[10]['CRESULT'], self.paDatos[11]['CRESULT']], [wr*0.20, wr*0.10, wr*0.10, wr*0.10, wr*0.10])
            loPdf.Row(['VISION DE CERCA', self.paDatos[12]['CRESULT'], self.paDatos[13]['CRESULT']], [wr*0.20, wr*0.20, wr*0.20])
            loPdf.Row(['VISION BINOCULAR', self.paDatos[14]['CRESULT'], self.paDatos[15]['CRESULT']], [wr*0.20, wr*0.20, wr*0.20])
            loPdf.ln()
            loPdf.set_bolds(['B'])
            loPdf.Row([self.paDatos[16]['CIMPRIM'], self.paDatos[16]['CRESULT']], [wr*0.20, wr*0.40])
            loPdf.set_bolds(['B'])
            loPdf.Row(['Filtro UV', self.paDatos[17]['CIMPRIM'], self.paDatos[17]['CRESULT'], self.paDatos[18]['CIMPRIM'], self.paDatos[18]['CRESULT']], [wr*0.20, wr*0.10, wr*0.10, wr*0.10, wr*0.10])
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, self.paDatos[19]['CIMPRIM'], 'TLR', 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.multi_cell(w,h, self.paDatos[19]['CRESULT'], 'BLR', 'L')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, self.paDatos[20]['CIMPRIM'], 'TLR', 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.multi_cell(w,h, self.paDatos[20]['CRESULT'], 'BLR', 'L')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'FONDO DE OJO (Polo Posterior)', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_bolds(['B'])
            loPdf.Row([self.paDatos[21]['CIMPRIM'], self.paDatos[21]['CRESULT']], [wr*0.20, wr*0.80])
            loPdf.set_bolds(['B'])
            loPdf.Row([self.paDatos[22]['CIMPRIM'], self.paDatos[22]['CRESULT']], [wr*0.20, wr*0.80])
            loPdf.ln()
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(w,h, 'DIAGNOSTICOS DE LA ESPECIALIDAD',1, 2, 'L')
            loPdf.set_font('Arial', '' , 6)
            loPdf.multi_cell(w,h, '#REEMPLAZAR#', 1, 'L')
            #if(self.paData['OACTIVI']['MRECOME'] is not None):
                #loPdf.multi_cell(w,h, self.paData['OACTIVI']['MRECOME'],1, 'L')
            #else:
                #loPdf.cell(w,h, ' ',1, 2, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(w,h, self.paDatos[23]['CIMPRIM'], 0, 1, 'L')
            loPdf.set_font('Arial', '' , 6)
            posX = loPdf.get_x()
            posY = loPdf.get_y()
            #
            loPdf.set_aligns(['C'])
            loPdf.set_bolds(['B'])
            loPdf.Row(['LEJOS'], [wr*0.40])
            loPdf.set_bolds(['B', 'B', 'B', 'B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.Row(['', 'SF', 'CYL', 'EJE', 'DIP', 'AV'], [wr*0.05, wr*0.07, wr*0.07, wr*0.07, wr*0.07, wr*0.07])
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.set_bolds(['B'])
            #loPdf.set_borders([1, 1, 1, 1, 'TLR', 1])
            loPdf.Row(['OD', self.paDatos[24]['CRESULT'], self.paDatos[26]['CRESULT'], self.paDatos[28]['CRESULT'], self.paDatos[30]['CRESULT'], self.paDatos[31]['CRESULT']], [wr*0.05, wr*0.07, wr*0.07, wr*0.07, wr*0.07, wr*0.07])
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.set_bolds(['B'])
            #loPdf.set_borders([1, 1, 1, 1, 'BLR', 1])
            loPdf.Row(['OI', self.paDatos[25]['CRESULT'], self.paDatos[27]['CRESULT'], self.paDatos[29]['CRESULT'], '', self.paDatos[32]['CRESULT']], [wr*0.05, wr*0.07, wr*0.07, wr*0.07, wr*0.07, wr*0.07])
            #
            loPdf.set_xy(posX + 9, posY)
            #
            loPdf.set_aligns(['C'])
            loPdf.set_bolds(['B'])
            loPdf.Row(['CERCA'], [wr*0.40])
            loPdf.set_x(posX + 9)
            loPdf.set_bolds(['B', 'B', 'B', 'B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.Row(['', 'SF', 'CYL', 'EJE', 'DIP', 'AV'], [wr*0.05, wr*0.07, wr*0.07, wr*0.07, wr*0.07, wr*0.07])
            loPdf.set_x(posX + 9)
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.set_bolds(['B'])
            #loPdf.set_borders([1, 1, 1, 1, 'TLR', 'TLR'])
            loPdf.Row(['OD', self.paDatos[33]['CRESULT'], self.paDatos[35]['CRESULT'], self.paDatos[37]['CRESULT'], self.paDatos[39]['CRESULT'], self.paDatos[40]['CRESULT']], [wr*0.05, wr*0.07, wr*0.07, wr*0.07, wr*0.07, wr*0.07])
            loPdf.set_x(posX + 9)
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.set_bolds(['B'])
            #loPdf.set_borders([1, 1, 1, 1, 'BLR', 'BLR'])
            loPdf.Row(['OI', self.paDatos[34]['CRESULT'], self.paDatos[36]['CRESULT'], self.paDatos[38]['CRESULT'], '', ''], [wr*0.05, wr*0.07, wr*0.07, wr*0.07, wr*0.07, wr*0.07])
            
            loPdf.ln()
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(w,h, 'RECOMENDACIONES',1, 2, 'L')
            loPdf.set_font('Arial', '' , 6)
            if(self.paData['OACTIVI']['MRECOME'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MRECOME'],1, 'L')
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(w,h, 'OBSERVACIONES',1, 2, 'L')
            loPdf.set_font('Arial', '' , 6)
            if(self.paData['OACTIVI']['MOBSERV'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MOBSERV'],1, 'L')
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            
            # self.image("./assets/Docs/PACIENTE/"+self.paData['OPERSON']['CNRODNI']+"/FIRMA.jpg" , 1, 1, 3, 2);
            loPdf.image("./src/PDF/assets/9999.jpg" , 1, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 9, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_cuestionario_osteomioarticular(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = ['0087', '0088', '0089', '0090', '0091', '0092', '0093', '0094', '0095', '0096', '0097', '0098', '0099', '0100', '0101', '0102', '0103', '0104', '0105', '0106', '0107', '0108', '0109', '0110', '0111', '0112', '0113', '0114', '0115', '0116', '0117', '0118', '0119', '0120', '0121', '0122', '0123', '0124', '0125', '0126', '0127', '0128', '0129', '0130', '0131', '0132', '0133', '0134', '0135', '0136', '0137', '0138', '0139', '0140']
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True

    def print_cuestionario_osteomioarticular(self):
        loPdf  = PYFPDF()
        llOK = self.val_cuestionario_osteomioarticular()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'EVALUACION OSTEOMIOARTICULAR ARTICULACIONES')
            loPdf.cell(wr/3, h, 'RESPONDA EN TODOS LOS CASOS', 1, 0, 'C')
            loPdf.cell(wr*2/3, h, 'RESPONDA SOLAMENTE SI HA TENIDO PROBLEMAS', 1, 1, 'C')
            xo = loPdf.get_x()
            yo = loPdf.get_y()
            loPdf.multi_cell(wr/3, h, 'Usted ha tenido en los últimos 12 meses problemas (dolor, curvaturas, etc) a nivel de:', 0, 'C')
            loPdf.set_xy(xo, yo)
            loPdf.cell(wr/3, h*2, '', 1, 0, 'C')
            loPdf.multi_cell(wr/3, h, 'Durante los últimos doce meses ha estado incapacitado/a para su trabajo (en casa o fuera) por causa del problema', 0, 'C')
            loPdf.set_xy(xo + wr/3, yo)
            loPdf.cell(wr/3, h*2, '', 1, 0, 'C')
            loPdf.multi_cell(wr/3, h, '¿Ha tenido problemas en los últimos siete días?', 0, 'C')
            loPdf.set_xy(xo + wr/3 * 2, yo)
            loPdf.cell(wr/3, h*2, '', 1, 1, 'C')

            loPdf.cell(wr/3*0.5, h, '', 1, 0, 'C')
            loPdf.cell(wr/3*0.25, h, 'SI', 1, 0, 'C')
            loPdf.cell(wr/3*0.25, h, 'NO', 1, 0, 'C')
            loPdf.cell(wr/3*0.5, h, 'SI', 1, 0, 'C')
            loPdf.cell(wr/3*0.5, h, 'NO', 1, 0, 'C')
            loPdf.cell(wr/3*0.5, h, 'SI', 1, 0, 'C')
            loPdf.cell(wr/3*0.5, h, 'NO', 1, 1, 'C')
            ###
            xo = loPdf.get_x()
            yo = loPdf.get_y()
            cants = [1, 3, 3, 3, 2, 2, 2, 2]
            margen = 0.4
            indicador = 0
            for i in range(len(cants)):
                x1 = loPdf.get_x()
                y1 = loPdf.get_y()
                if i in [1, 2, 3, 5, 6, 7]:
                    loPdf.set_font('Arial', 'B', 6)
                    loPdf.cell(wr/3, h, self.paDatos[indicador]['CIMPRIM'], 0, 0, 'L')
                    loPdf.set_font('Arial', '', 6)
                    loPdf.set_xy(x1, y1)
                    indicador += 1
                for j in range(cants[i]):
                    if j == 0:
                        loPdf.set_xy(x1 + margen, y1 + margen)
                    else:
                        loPdf.set_xy(x1 + margen, yf)
                    for k in range(3):
                        if (k == 0):
                            loPdf.cell(wr/6 - 0.25, 0.5, self.paDatos[indicador]['CIMPRIM'], 0, 0, 'L')
                            loPdf.set_x(x1 + wr/3*0.5)
                            ancho = wr/3*0.25
                        else:
                            loPdf.set_x(x1 + wr / 3 * k)
                            ancho = wr/3*0.5
                        result = self.x_boolean_multi(self.paDatos[indicador]['CRESULT'])
                        #if int(self.paDatos[indicador]['CRESULT']) == 0:
                        #    result = ['X', '']
                        #else:
                        #    result = ['', 'X']
                        loPdf.set_font('Arial', '', 14)
                        loPdf.cell(ancho, 0.5, result[0], 'LR', 0, 'C')
                        loPdf.cell(ancho, 0.5, result[1], 'LR', 0, 'C')
                        loPdf.set_font('Arial', '', 6)
                        '''
                        loPdf.set_font('Arial', 'B', 6)
                        loPdf.cell(0.5, 0.5, 'SI', 0, 0, 'L')
                        loPdf.set_font('Arial', '', 14)
                        loPdf.cell(0.5, 0.5, result[0], 1, 0, 'C')
                        loPdf.cell(0.5)
                        loPdf.set_font('Arial', 'B', 6)
                        loPdf.cell(0.5, 0.5, 'NO', 0, 0, 'L')
                        loPdf.set_font('Arial', '', 14)
                        loPdf.cell(0.5, 0.5, result[1], 1, 0, 'C')
                        loPdf.set_font('Arial', '', 6)
                        '''
                        indicador += 1
                    loPdf.ln(0.7)
                    yf = loPdf.get_y()
                loPdf.set_xy(x1, y1)
                loPdf.cell(wr/3, yf - 0.2 + margen - y1, '', 1, 0, 'L')
                loPdf.cell(wr/3, yf - 0.2 + margen - y1, '', 1, 0, 'L')
                loPdf.cell(wr/3, yf - 0.2 + margen - y1, '', 1, 1, 'L')
            
            yf = loPdf.get_y()
            loPdf.line(xo + wr/3*0.5, yo, xo + wr/3*0.5, yf)
            loPdf.line(xo + wr/3*0.75, yo, xo + wr/3*0.75, yf)
            loPdf.line(xo + wr/6*3, yo, xo + wr/6*3, yf)
            loPdf.line(xo + wr/6*5, yo, xo + wr/6*5, yf)
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_cuestionario_sintomas_musculo_tendinoso(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = ['0141','0142','0143','0144','0145','0146','0147','0148','0149','0150','0151','0152','0153','0154','0155','0156','0157','0158','0159','0160','0161','0162','0163','0164','0165','0166','0167','0168','0169','0170','0171','0172','0173','0174','0175','0176','0177','0178','0179','0180','0181','0182','0183','0184','0185','0186','0187','0188','0189','0190','0191','0192','0193','0194','0195','0196','0197','0198','0199','0200','0201','0202','0203','0204','0205','0206','0207','0208','0209','0210','0211','0212','0213','0214','0215','0216','0217','0218','0219','0220','0221','0222','0223','0224','0225','0226','0227','0228','0229','0230','0231','0232','0233','0234','0235','0236','0237','0238','0239','0240','0241','0242','0243','0244','0245','0246','0247','0248','0249','0250','0251','0252','0253','0254']
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True

    def print_cuestionario_sintomas_musculo_tendinoso(self):
        loPdf  = PYFPDF()
        llOK = self.val_cuestionario_sintomas_musculo_tendinoso()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'CUESTIONARIO DE SINTOMAS MUSCULO TENDINOSOS')
            altura = 0.3*5
            indicador = 0
            for i in range(11):
                if i in [0, 1, 4]:
                    loPdf.ln(h)
                    loPdf.set_font('Arial', 'B', 6)
                    loPdf.cell(wr, h, self.paDatos[indicador]['CIMPRIM'], 1, 1, 'L')
                    loPdf.set_font('Arial', '', 6)
                    indicador += 1
                for j in range(10):
                    x = loPdf.get_x()
                    y = loPdf.get_y()
                    if i == 0:
                        if j == 0:
                            loPdf.set_font('Arial', 'B', 6)
                            loPdf.cell(wr/10, h, 'PREGUNTAS', 1, 2, 'C')
                            loPdf.set_font('Arial', '', 6)
                        else:
                            #loPdf.cell(wr/10, h, self.paDatos[indicador]['CIMPRIM'], 1, 2, 'C')
                            xaux = loPdf.get_x()
                            yaux = loPdf.get_y()
                            loPdf.set_font('Arial', 'B', 6)
                            loPdf.multi_cell(wr/10, 0.2, self.paDatos[indicador]['CIMPRIM'], 0, 'C')
                            loPdf.set_font('Arial', '', 6)
                            loPdf.set_xy(xaux, yaux)
                            loPdf.cell(wr/10, h, '', 1, 2, 'C')

                            
                        #x = loPdf.get_x()
                        y = loPdf.get_y()
                    if j == 0:
                        loPdf.cell(wr/10, 0.03, '', 0, 2, 'L')
                        loPdf.multi_cell(wr/10, 0.21, self.paDatos[indicador]['CIMPRIM'], 0, 'L')
                    elif i == 0:
                        if j in [1, 3, 4]:
                            xboolean = self.x_boolean_multi(self.paDatos[indicador]['CRESULT'])
                            loPdf.cell(wr/10*0.5, altura/3, 'SI', 1, 0, 'C')
                            loPdf.cell(wr/10*0.5, altura/3, 'NO', 1, 1, 'C')
                            loPdf.set_x(x)
                            loPdf.cell(wr/10*0.5, altura/3*2, xboolean[0], 1, 0, 'C')
                            loPdf.cell(wr/10*0.5, altura/3*2, xboolean[1], 1, 1, 'C')
                            '''
                            xaux = x + 0.3
                            loPdf.set_x(xaux)
                            loPdf.cell(0.5, altura/3, 'SI', 0, 0, 'L')
                            loPdf.cell(0.5, altura/3, 'X', 1, 1, 'C')
                            loPdf.set_x(xaux)
                            loPdf.cell(0.5, altura/3, 'NO', 0, 0, 'L')
                            loPdf.cell(0.5, altura/3, 'X', 1, 1, 'C')
                            '''
                        else:
                            xaux = x
                            loPdf.set_x(xaux)
                            loPdf.cell(0.5, altura/3, 'SI', 0, 0, 'L')
                            loPdf.cell(0.4, altura/3, 'X', 1, 1, 'C')
                            loPdf.set_x(xaux)
                            loPdf.cell(0.5, altura/3, 'NO', 0, 0, 'L')
                            loPdf.cell(0.4, altura/3, 'X', 1, 1, 'C')
                            indicador += 1
                            xaux = x + wr/10 - 0.88
                            loPdf.set_xy(xaux, y)
                            for k in range(len(self.paDatos[indicador]['MTABLA'])):
                                loPdf.cell(0.5, altura/3, self.paDatos[indicador]['MTABLA'][k]['CDESCRI'], 0, 0, 'R')
                                if k == int(self.paDatos[indicador]['CRESULT']):
                                    loPdf.cell(0.38, altura/3, 'X', 1, 1, 'C')
                                else:
                                    loPdf.cell(0.38, altura/3, '', 1, 1, 'C')
                                loPdf.set_x(xaux)
                    elif i in [1, 4, 6]:
                        for k in range(len(self.paDatos[indicador]['MTABLA'])):
                            if i == 4 and k == 2:
                                xaux = loPdf.get_x()
                                yaux = loPdf.get_y()
                                loPdf.multi_cell(wr/10 - 0.38, 0.2, self.paDatos[indicador]['MTABLA'][k]['CDESCRI'], 0, 'R')
                                loPdf.set_xy(xaux, yaux)
                                loPdf.cell(wr/10 - 0.38, altura/4, '', 0, 0, 'R')
                            else:
                                loPdf.cell(wr/10 - 0.38, altura/4, self.paDatos[indicador]['MTABLA'][k]['CDESCRI'], 0, 0, 'R')
                            if k == int(self.paDatos[indicador]['CRESULT']):
                                loPdf.cell(0.38, altura/4, 'X', 1, 1, 'C')
                            else:
                                loPdf.cell(0.38, altura/4, '', 1, 1, 'C')
                            loPdf.set_x(x)
                    elif i in [2, 3, 7, 8]:
                        xboolean = self.x_boolean_multi(self.paDatos[indicador]['CRESULT'])
                        loPdf.cell(wr/10*0.5, altura/3, 'SI', 1, 0, 'C')
                        loPdf.cell(wr/10*0.5, altura/3, 'NO', 1, 1, 'C')
                        loPdf.set_x(x)
                        loPdf.cell(wr/10*0.5, altura/3*2, xboolean[0], 1, 0, 'C')
                        loPdf.cell(wr/10*0.5, altura/3*2, xboolean[1], 1, 1, 'C')
                        ''' ANTIGUO
                        xaux = x + 0.3
                        loPdf.set_x(xaux)
                        loPdf.cell(0.5, altura/3, 'SI', 0, 0, 'L')
                        loPdf.cell(0.5, altura/3, 'X', 1, 1, 'C')
                        loPdf.set_x(xaux)
                        loPdf.cell(0.5, altura/3, 'NO', 0, 0, 'L')
                        loPdf.cell(0.5, altura/3, 'X', 1, 1, 'C')
                        '''
                    elif i in [5, 9]:
                        for k in range(len(self.paDatos[indicador]['MTABLA'])):
                            loPdf.cell(wr/10 - 0.38, altura/5, self.paDatos[indicador]['MTABLA'][k]['CDESCRI'], 0, 0, 'R')
                            if k == int(self.paDatos[indicador]['CRESULT']):
                                loPdf.cell(0.38, altura/5, 'X', 1, 1, 'C')
                            else:
                                loPdf.cell(0.38, altura/5, '', 1, 1, 'C')
                            loPdf.set_x(x)
                    elif i == 10:
                        for k in range(len(self.paDatos[indicador]['MTABLA'])):
                            loPdf.cell(wr/10 - 0.38, altura/4, self.paDatos[indicador]['MTABLA'][k]['CDESCRI'], 1, 0, 'L')
                            if k == int(self.paDatos[indicador]['CRESULT']):
                                loPdf.cell(0.38, altura/4, 'X', 1, 1, 'C')
                            else:
                                loPdf.cell(0.38, altura/4, '', 1, 1, 'C')
                            loPdf.set_x(x)
                        indicador += 1
                        loPdf.cell(wr/10, altura/4, self.paDatos[indicador]['CRESULT'], 0, 1, 'L')
                    loPdf.set_xy(x, y)
                    if j == 9:
                        loPdf.cell(wr/10, altura, '', 1, 1, 'C')
                    else:
                        loPdf.cell(wr/10, altura, '', 1, 0, 'C')
                    if i == 0 and j != 9:
                        loPdf.set_xy(loPdf.get_x(), loPdf.get_y() - h)
                    indicador += 1

            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_electrocardiograma(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = ['0255','0256','0257','0258','0259','0260','0261','0262','0263','0264','0265','0266','0267']
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True

    def print_electrocardiograma(self):
        loPdf  = PYFPDF()
        llOK = self.val_electrocardiograma()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('CARDIOLOGIA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'FORMATO EKG')
            loPdf.set_border(1)
            loPdf.Row([self.paDatos[0]['CIMPRIM'], self.paDatos[0]['CRESULT'], self.paDatos[1]['CIMPRIM'], self.paDatos[1]['CRESULT'], self.paDatos[2]['CIMPRIM'], self.paDatos[2]['CRESULT']], [wr*0.08, wr*0.24, wr*0.05, wr*0.13, wr*0.14, wr*0.36])
            for i in range(3, 12, 2):
                loPdf.Row([self.paDatos[i]['CIMPRIM'], self.paDatos[i]['CRESULT'], self.paDatos[i + 1]['CIMPRIM'], self.paDatos[i + 1]['CRESULT']], [wr*0.14, wr*0.36, wr*0.14, wr*0.36])
            
            loPdf.ln()
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(w,h, 'CONCLUSIÓN',1, 2, 'L')
            loPdf.set_font('Arial', '' , 6)
            if(self.paData['OACTIVI']['MCONCLU'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MCONCLU'],1, 'L')
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(w,h, 'COMENTARIOS',1, 2, 'L')
            loPdf.set_font('Arial', '' , 6)
            if(self.paData['OACTIVI']['MCONCLU'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MCONCLU'],1, 'L') #TODO no existe mcoment...
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            
            self.print_signatures(loPdf)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_ficha_psicologica(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = ['0268','0269','0270','0271','0272','0273','0274','0275','0276','0277','0278','0279','0280','0281','0282','0283','0284','0285','0286','0287','0288','0289','0290','0291','0292','0293','0294','0295','0296','0297','0298','0299','0300','0301','0302','0303','0304','0305','0306','0307']
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_ficha_psicologica(self):
        loPdf  = PYFPDF()
        llOK = self.val_ficha_psicologica()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('PSICOLOGIA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'HISTORIA 1')
            loPdf.set_border(1)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'I. MOTIVO DE LA EVALUACION', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.multi_cell(w, h, '', 1, 'L')#TODO de donde se saca?
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'II. DATOS OCUPACIONALES', 1, 1, 'L')
            loPdf.cell(w, h, 'EMPRESA ACTUAL (postura, trabaja o trabajo)', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(w, h, 'Nombre de la empresa: ' + self.paData['OEMPRES']['CDESCRI'], 0, 1, 'L')
            loPdf.cell(w, h, 'Actividad de la empresa: ' + '', 0, 1, 'L')#TODO de donde se sacan estas cosas...
            loPdf.cell(6, h, 'Área de trabajo: ' + '', 0, 0, 'L')#TODO de donde se sacan estas cosas...
            loPdf.cell(loPdf.get_string_width('Superficie') + loPdf.c_margin*2, h, 'Superficie', 0, 0, 'L')
            loPdf.cell(0.3, 0.3, 'X', 1, 0, 'C')
            loPdf.cell(0.4)
            loPdf.cell(loPdf.get_string_width('Subsuelo') + loPdf.c_margin*2, h, 'Subsuelo', 0, 0, 'L')
            loPdf.cell(0.3, 0.3, 'X', 1, 0, 'C')
            loPdf.cell(0.3)
            loPdf.cell(w, h, 'Tiempo laborado: ', 0, 1, 'L')
            loPdf.cell(w, h, 'Puesto: ' + '', 0, 1, 'L')#TODO de donde se sacan estas cosas...

            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'PRINCIPALES RIESGOS', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.multi_cell(w, h, '', 1, 'L')#TODO de donde se saca?
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'MEDIDAS DE SEGURIDAD', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.multi_cell(w, h, '', 1, 'L')#TODO de donde se saca?
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'EMPRESAS ANTERIORES (experiencia laboral)', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.set_bolds(['B', 'B', 'B', 'B', 'B', 'B'])
            loPdf.Row(['FECHA', 'NOMBRE DE LA EMPRESA', 'ACTIVIDAD DE LA EMPRESA', 'PUESTO', 'TIEMPO SUP-SUB', 'CAUSA DE RETIRO'], [wr*0.16, wr*0.18, wr*0.18, wr*0.16, wr*0.16, wr*0.16])
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.Row(['-', '-', '-', '-', '-', '-'], [wr*0.16, wr*0.18, wr*0.18, wr*0.16, wr*0.16, wr*0.16])
            #loPdf.Row(['', '', '', '', '', ''], [wr*0.16, wr*0.18, wr*0.18, wr*0.16, wr*0.16, wr*0.16])
            #loPdf.Row(['', '', '', '', '', ''], [wr*0.16, wr*0.18, wr*0.18, wr*0.16, wr*0.16, wr*0.16])
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'III. '+self.paDatos[0]['CIMPRIM'], 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.multi_cell(w, h, self.paDatos[0]['CRESULT'], 1, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'IV. '+self.paDatos[1]['CIMPRIM'], 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.multi_cell(w, h, self.paDatos[1]['CRESULT'], 1, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'V. '+self.paDatos[2]['CIMPRIM'], 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            #loPdf.cell(w, h, self.paDatos[3]['CIMPRIM'], 1, 1, 'L')
            loPdf.multi_cell(w, h, self.paDatos[3]['CRESULT'], 1, 'L')
            
            loPdf.cell(loPdf.get_string_width(self.paDatos[4]['CIMPRIM']) + loPdf.c_margin*2, h, self.paDatos[4]['CIMPRIM'], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, self.x_boolean_checkbox(self.paDatos[4]['CRESULT'])[0], 1, 0, 'C')
            loPdf.cell(0.5)
            loPdf.cell(loPdf.get_string_width(self.paDatos[5]['CIMPRIM']) + loPdf.c_margin*2, h, self.paDatos[5]['CIMPRIM'], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, self.x_boolean_checkbox(self.paDatos[5]['CRESULT'])[0], 1, 0, 'C')
            loPdf.cell(0.5)
            loPdf.cell(loPdf.get_string_width(self.paDatos[6]['CIMPRIM']) + loPdf.c_margin*2, h, self.paDatos[6]['CIMPRIM'], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, self.x_boolean_checkbox(self.paDatos[6]['CRESULT'])[0], 1, 1, 'C')
            
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'VI. OTRAS OBSERVACIONES', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.multi_cell(w, h, '', 1, 'L')#TODO de donde se saca?
            loPdf.ln()

            loPdf.setHeader('HISTORIA 2', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.add_page()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'VII. '+self.paDatos[7]['CIMPRIM'], 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            #
            xo = loPdf.get_x()
            yo = loPdf.get_y()
            margen = 0.4
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(11.2, h, self.paDatos[8]['CIMPRIM'], 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.set_xy(x + margen, y + margen)

            loPdf.cell(2.5, h, self.paDatos[9]['CIMPRIM'], 0, 2, 'L')
            loPdf.cell(2.5, h, self.paDatos[10]['CIMPRIM'], 0, 2, 'L')
            loPdf.cell(2.5, h, 'Discurso', 0, 2, 'L')
            loPdf.cell(0, h, '', 0, 2, 'L')
            loPdf.cell(0, h, '', 0, 2, 'L')
            loPdf.cell(2.5, h, 'Orientación', 0, 0, 'L')
            x = loPdf.get_x()
            loPdf.set_xy(x, y + margen)
            loPdf.cell(0.3, h, ':', 0, 2, 'C')
            loPdf.cell(0.3, h, ':', 0, 2, 'C')
            loPdf.cell(0.3, h, ':', 0, 2, 'C')
            loPdf.cell(0, h, '', 0, 2, 'L')
            loPdf.cell(0, h, '', 0, 2, 'L')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            x1 = loPdf.get_x()
            x = x1
            loPdf.set_xy(x, y + margen)
            longitud = (11.2 - (x - xo) - margen*2 - 0.3*2) / 2
            xselect = self.x_select_check(self.paDatos[9]['MTABLA'][0], self.paDatos[9]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[9]['MTABLA'][1], self.paDatos[9]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            loPdf.set_xy(x, loPdf.get_y() + 0.1)
            xselect = self.x_select_check(self.paDatos[10]['MTABLA'][0], self.paDatos[10]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[10]['MTABLA'][1], self.paDatos[10]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            y = y + margen + h*2
            loPdf.set_xy(x1, y)
            x1 = loPdf.get_x()
            loPdf.cell(0.9, h, self.paDatos[11]['CIMPRIM'], 0, 2, 'L')
            loPdf.cell(0.9, h, self.paDatos[12]['CIMPRIM'], 0, 0, 'L')
            x = loPdf.get_x()
            loPdf.set_xy(x, y)
            loPdf.cell(0.3, h, ':', 0, 2, 'C')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            x = loPdf.get_x()
            loPdf.set_xy(x, y)
            longitud = (11.2 - (x - xo) - margen*3 - 0.3*3) / 3
            xselect = self.x_select_check(self.paDatos[11]['MTABLA'][0], self.paDatos[11]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[11]['MTABLA'][1], self.paDatos[11]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[11]['MTABLA'][2], self.paDatos[11]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            loPdf.set_xy(x, loPdf.get_y() + 0.1)
            xselect = self.x_select_check(self.paDatos[12]['MTABLA'][0], self.paDatos[12]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[12]['MTABLA'][1], self.paDatos[12]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[12]['MTABLA'][2], self.paDatos[12]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            #imprimir los de 2
            y = y + h*2
            loPdf.set_xy(x1, y)
            loPdf.cell(1.6, h, self.paDatos[13]['CIMPRIM'], 0, 2, 'L')
            loPdf.cell(1.6, h, self.paDatos[14]['CIMPRIM'], 0, 2, 'L')
            loPdf.cell(1.6, h, self.paDatos[15]['CIMPRIM'], 0, 2, 'L')
            loPdf.cell(1.6, h, self.paDatos[16]['CIMPRIM'], 0, 0, 'L')
            x = loPdf.get_x()
            loPdf.set_xy(x, y)
            loPdf.cell(0.3, h, ':', 0, 2, 'C')
            loPdf.cell(0.3, h, ':', 0, 2, 'C')
            loPdf.cell(0.3, h, ':', 0, 2, 'C')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            x1 = loPdf.get_x()
            x = x1
            loPdf.set_xy(x, y)
            longitud = (11.2 - (x - xo) - margen*2 - 0.3*2) / 2
            xselect = self.x_select_check(self.paDatos[13]['MTABLA'][0], self.paDatos[13]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[13]['MTABLA'][1], self.paDatos[13]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            loPdf.set_xy(x, loPdf.get_y() + 0.1)
            xselect = self.x_select_check(self.paDatos[14]['MTABLA'][0], self.paDatos[14]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[14]['MTABLA'][1], self.paDatos[14]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            loPdf.set_xy(x, loPdf.get_y() + 0.1)
            xselect = self.x_select_check(self.paDatos[15]['MTABLA'][0], self.paDatos[15]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[15]['MTABLA'][1], self.paDatos[15]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            loPdf.set_xy(x, loPdf.get_y() + 0.1)
            xselect = self.x_select_check(self.paDatos[16]['MTABLA'][0], self.paDatos[16]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[16]['MTABLA'][1], self.paDatos[16]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            loPdf.set_xy(x, loPdf.get_y() + 0.1)
            #dibujar el cuadro
            altura = loPdf.get_y() - yo
            loPdf.set_xy(xo, yo + h)
            loPdf.cell(11.2, altura, '', 1, 1)
            #imprimir cuadro de pruebas psicologicas
            loPdf.set_xy(xo + 11.2, yo)
            x = loPdf.get_x()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(2, h, 'PTJ', 1, 0, 'C')
            loPdf.cell(5.2, h, self.paDatos[17]['CIMPRIM'], 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            y = loPdf.get_y()
            for i in range(18, 34):
                loPdf.set_xy(x, y)
                loPdf.cell(2, h*2, self.paDatos[i]['CRESULT'], 1, 0, 'C')
                xaux = loPdf.get_x()
                yaux = loPdf.get_y()
                loPdf.multi_cell(5.2, 0.4, self.paDatos[i]['CIMPRIM'], 0, 'C')
                loPdf.set_xy(xaux, yaux)
                loPdf.cell(5.2, h*2, '', 1, 1, 'C')
                y = loPdf.get_y()
            yf = loPdf.get_y()
            #imprimir cuadro procesos cognitivos
            loPdf.set_xy(xo, yo + h + altura)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(11.2, h, self.paDatos[34]['CIMPRIM'], 1, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            xo = loPdf.get_x()
            yo = loPdf.get_y()
            #imprimir contenido de procesos cognitivos
            loPdf.set_xy(xo + margen, yo + margen)
            x1 = loPdf.get_x()
            longitud = 11.2 - margen*2 - 2.3 - 0.3
            for i in range(35, 38):
                loPdf.cell(2.3, h, self.paDatos[i]['CIMPRIM'], 0, 0, 'L')
                loPdf.cell(0.3, h, ':', 0, 0, 'C')
                loPdf.cell(longitud, h, self.paDatos[i]['CRESULT'], 0, 1, 'L')
                loPdf.set_x(x1)
            #   memoria
            loPdf.cell(2.3, h, self.paDatos[38]['CIMPRIM'], 0, 0, 'L')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            x = xo + 11.2 - margen - (loPdf.get_string_width('Plazo.') + loPdf.c_margin*2)
            loPdf.set_x(x)
            loPdf.cell(loPdf.get_string_width('Plazo.') + loPdf.c_margin*2, h, 'Plazo.', 0, 0, 'C')
            longitud = (x - (x1 + 2.3 + 0.3) - margen*3 - 0.3*3) / 3
            loPdf.set_x(x1 + 2.3 + 0.3)
            xselect = self.x_select_check(self.paDatos[38]['MTABLA'][0], self.paDatos[38]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[38]['MTABLA'][1], self.paDatos[38]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[38]['MTABLA'][2], self.paDatos[38]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            loPdf.set_y(loPdf.get_y() + 0.1)
            #inteligencia
            loPdf.set_x(x1)
            loPdf.cell(2.3, h, self.paDatos[39]['CIMPRIM'], 0, 0, 'L')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            x = loPdf.get_x()
            longitud = (11.2 - (x - xo) - margen*3 - 0.3*3) / 3
            xselect = self.x_select_check(self.paDatos[39]['MTABLA'][0], self.paDatos[39]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[39]['MTABLA'][1], self.paDatos[39]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[39]['MTABLA'][2], self.paDatos[39]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            loPdf.set_xy(x, loPdf.get_y()+0.1)
            xselect = self.x_select_check(self.paDatos[39]['MTABLA'][3], self.paDatos[39]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[39]['MTABLA'][4], self.paDatos[39]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[39]['MTABLA'][5], self.paDatos[39]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            loPdf.set_xy(x, loPdf.get_y()+0.1)
            longitud = (11.2 - (x - xo) - margen*2 - 0.3*2) / 2
            xselect = self.x_select_check(self.paDatos[39]['MTABLA'][6], self.paDatos[39]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[39]['MTABLA'][7], self.paDatos[39]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            loPdf.set_xy(x, loPdf.get_y()+0.1)
            xselect = self.x_select_check(self.paDatos[39]['MTABLA'][8], self.paDatos[39]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 0, 'C')
            loPdf.cell(margen)
            xselect = self.x_select_check(self.paDatos[39]['MTABLA'][9], self.paDatos[39]['CRESULT'])
            loPdf.cell(longitud, h, xselect[0], 0, 0, 'L')
            loPdf.cell(0.3, 0.3, xselect[1], 1, 1, 'C')
            loPdf.set_y(loPdf.get_y()+0.1)
            #el resto
            loPdf.set_x(x1)
            longitud = 11.2 - margen*2 - 2.3 - 0.3
            for i in range(40, 45):
                if i != 43:#43 es sexualidad
                    loPdf.cell(2.3, h, self.paDatos[i]['CIMPRIM'], 0, 0, 'L')
                    loPdf.cell(0.3, h, ':', 0, 0, 'C')
                    loPdf.cell(longitud, h, self.paDatos[i]['CRESULT'], 0, 1, 'L')
                    loPdf.set_x(x1)
            #dibujar el cuadro
            #altura = loPdf.get_y() + margen - yo
            altura = yf - yo
            loPdf.set_xy(xo, yo)
            loPdf.cell(11.2, altura, '', 1, 1)

            #loPdf.cell(18.4, 4, '', 1, 1, 'L')
            #loPdf.cell(0, 10, '', 1, 1, 'L')
            #loPdf.set_xy(xo + margen, y + margen)

            

            #

            #loPdf.add_page()
            loPdf.ln(h)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'VIII. DIAGNOSTICO FINAL',1, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            if(self.paData['OACTIVI']['MCONCLU'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MCONCLU'],1, 'L') #TODO no existe MDIAGNO...
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            
            loPdf.image("./src/PDF/assets/9999.jpg" , 1, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 9, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_informe_psicologico(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = ['0308','0309','0310','0311','0312']
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_informe_psicologico(self):
        loPdf  = PYFPDF()
        llOK = self.val_informe_psicologico()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('PSICOLOGIA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'INFORME PSICOLOGICO OCUPACIONAL')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, self.paDatos[0]['CIMPRIM'], 1, 1, 'L')
            loPdf.cell(w, h, 'Evaluación Médica Ocupacional', 0, 1, 'C')
            loPdf.ln()
            loPdf.cell(w, h, self.paDatos[1]['CIMPRIM'], 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            #loPdf.cell(w, h, '#REEMPLAZAR POR DATOS DE FICHA PSICOLOGICA#', 0, 1, 'C')
            loPdf.ln(0.2)
            xo = loPdf.get_x()
            yo = loPdf.get_y()
            margen = 0.4
            ancho = 1.5
            alto = 0.5
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(1.9, alto, 'PRESENTACION', 1, 0, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(ancho, alto, 'Adecuado', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.cell(margen)
            loPdf.cell(ancho, alto, 'Inadecuado', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.ln(alto)
            loPdf.ln(0.2)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(1.9, alto, 'POSTURA', 1, 0, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(ancho, alto, 'Erguida', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.cell(margen)
            loPdf.cell(ancho, alto, 'Encorvada', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.ln(alto)
            loPdf.ln(0.2)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(1.9, alto, 'DISCURSO', 1, 0, 'L')
            loPdf.cell(ancho + alto, alto, 'Ritmo :', 0, 0, 'R')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(ancho, alto, 'Lento', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.cell(margen)
            loPdf.cell(ancho, alto, 'Rápido', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.cell(margen)
            loPdf.cell(ancho, alto, 'Fluido', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.ln(alto)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(1.9, alto, '', 0, 0, 'L')
            loPdf.cell(ancho + alto, alto, 'Tono :', 0, 0, 'R')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(ancho, alto, 'Bajo', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.cell(margen)
            loPdf.cell(ancho, alto, 'Moderado', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.cell(margen)
            loPdf.cell(ancho, alto, 'Alto', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.ln(alto)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(1.9, alto, '', 0, 0, 'L')
            loPdf.cell(ancho + alto, alto, 'Articulación :', 0, 0, 'R')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(ancho, alto, 'Con dificultad', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.cell(margen)
            loPdf.cell(ancho, alto, 'Sin dificultad', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.ln(alto)
            loPdf.ln(0.2)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(1.9, alto, 'ORIENTACION', 1, 0, 'L')
            loPdf.cell(ancho + alto, alto, 'Tiempo :', 0, 0, 'R')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(ancho, alto, 'Orientado', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.cell(margen)
            loPdf.cell(ancho, alto, 'Desorientado', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.ln(alto)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(1.9, alto, '', 0, 0, 'L')
            loPdf.cell(ancho + alto, alto, 'Espacio :', 0, 0, 'R')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(ancho, alto, 'Orientado', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.cell(margen)
            loPdf.cell(ancho, alto, 'Desorientado', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.ln(alto)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(1.9, alto, '', 0, 0, 'L')
            loPdf.cell(ancho + alto, alto, 'Persona :', 0, 0, 'R')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(ancho, alto, 'Orientado', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.cell(margen)
            loPdf.cell(ancho, alto, 'Desorientado', 0, 0, 'R')
            loPdf.cell(alto, alto, '', 1, 0, 'C')
            loPdf.ln(alto)
            #
            loPdf.ln(h)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, self.paDatos[2]['CIMPRIM'], 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            margen = 0.6
            for i in range(3, 8):
                loPdf.cell(margen)
                loPdf.cell(2.8, h, '-  ' + self.paDatos[i]['CIMPRIM'], 0, 0, 'L')
                loPdf.cell(0.3, h, ':', 0, 0, 'C')
                loPdf.cell(0, h, self.paDatos[i]['CRESULT'], 0, 1, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'CONCLUSIONES',1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            if(self.paData['OACTIVI']['MCONCLU'] is not None):
                loPdf.multi_cell(w, h, self.paData['OACTIVI']['MCONCLU'], 1, 'J')
            else:
                loPdf.cell(w, h, ' ',1, 1, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'RECOMENDACIONES',1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            if(self.paData['OACTIVI']['MRECOME'] is not None):
                loPdf.multi_cell(w, h, self.paData['OACTIVI']['MRECOME'], 1, 'J')
            else:
                loPdf.cell(w,h, ' ',1, 1, 'L')
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False
    
    def val_espirometria(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = ['0313','0314','0315','0316','0317','0318','0319','0320','0321','0322','0323','0324','0325','0326','0327','0328','0329','0330','0331','0332','0333','0334','0335','0336']
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_espirometria(self):
        loPdf  = PYFPDF()
        llOK = self.val_espirometria()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'CUESTIONARIO ESPIROMETRIA')
            loPdf.set_border(1)
            loPdf.set_borders([0, 0, 1, 1])
            loPdf.set_aligns(['C', 'L', 'C', 'C'])
            loPdf.Row(['','','SI', 'NO'], [wr*0.04, wr*0.88, wr*0.04, wr*0.04])
            for i in range(0, 5):
                xboolean = [' ', 'X'] if int(self.paDatos[i]['CRESULT']) == 1 else ['X', '']
                loPdf.set_aligns(['C', 'L', 'C', 'C'])
                loPdf.Row([str(i + 1), self.paDatos[i]['CIMPRIM'], xboolean[1], xboolean[0]], [wr*0.04, wr*0.88, wr*0.04, wr*0.04])
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, self.paDatos[5]['CIMPRIM'], 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.ln()
            x = loPdf.get_x()
            y = loPdf.get_y()
            for i in range(6, 17):
                if i == 6:
                    loPdf.set_borders([0, 0, 1, 1])
                    loPdf.set_aligns(['C', 'L', 'C', 'C'])
                    loPdf.Row(['','','SI', 'NO'], [wr*0.04, wr*0.33, wr*0.04, wr*0.04])
                elif i == 12:
                    x = x + wr*0.55
                    loPdf.set_xy(x, y)
                    loPdf.set_borders([0, 0, 1, 1])
                    loPdf.set_aligns(['C', 'L', 'C', 'C'])
                    loPdf.Row(['','','SI', 'NO'], [wr*0.04, wr*0.33, wr*0.04, wr*0.04])
                    loPdf.set_x(x)
                xboolean = [' ', 'X'] if int(self.paDatos[i]['CRESULT']) == 1 else ['X', '']
                loPdf.set_aligns(['C', 'L', 'C', 'C'])
                loPdf.Row([str(i - 5), self.paDatos[i]['CIMPRIM'], xboolean[1], xboolean[0]], [wr*0.04, wr*0.33, wr*0.04, wr*0.04])
                loPdf.set_x(x)
            loPdf.ln()
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, self.paDatos[17]['CIMPRIM'], 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.ln()
            loPdf.set_borders([0, 0, 1, 1])
            loPdf.set_aligns(['C', 'L', 'C', 'C'])
            loPdf.Row(['','','SI', 'NO'], [wr*0.04, wr*0.88, wr*0.04, wr*0.04])
            i = 18
            cont = 1
            while i < 26:
                xboolean = [' ', 'X'] if int(self.paDatos[i]['CRESULT']) == 1 else ['X', '']
                text = self.paDatos[i]['CIMPRIM']
                if i == 22:
                    i += 1
                    if xboolean[1] == 'X':
                        text += ' SI (X) Cuántos: ' + self.paDatos[i]['CRESULT']
                loPdf.set_aligns(['C', 'L', 'C', 'C'])
                loPdf.Row([str(cont), text, xboolean[1], xboolean[0]], [wr*0.04, wr*0.88, wr*0.04, wr*0.04])
                i += 1
                cont += 1
            
            loPdf.image("./src/PDF/assets/9999.jpg" , 1, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 9, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_evaluacion_trabajos_altura_1_8(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = ['0337','0338','0339','0340','0341','0342','0343','0344','0345','0346','0347','0348','0349','0350','0351','0352','0353','0354','0355','0356','0357','0358','0359','0360','0361','0362','0363','0364','0365','0366','0367','0368','0369','0370','0371','0372','0373','0374']
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_evaluacion_trabajos_altura_1_8(self):
        loPdf  = PYFPDF()
        llOK = self.val_evaluacion_trabajos_altura_1_8()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'EXAMEN PARA TRABAJOS SOBRE ALTURA ESTRUCTURAL MATOR A 1.8 METROS')
            loPdf.set_border(1)
            loPdf.set_bolds(['B', 'B', 'B', 'B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.Row([self.paDatos[0]['CIMPRIM'],'SI', 'NO',self.paDatos[0]['CIMPRIM'],'SI', 'NO'], [wr*0.42, wr*0.04, wr*0.04, wr*0.42,wr*0.04, wr*0.04])
            for i in range(1, 15):
                xboolean1 = [' ', 'X'] if int(self.paDatos[i]['CRESULT']) == 1 else ['X', '']
                xboolean2 = [' ', 'X'] if int(self.paDatos[i + 14]['CRESULT']) == 1 else ['X', '']
                loPdf.set_aligns(['L', 'C', 'C', 'L', 'C', 'C'])
                loPdf.Row([self.paDatos[i]['CIMPRIM'],xboolean1[1], xboolean1[0], self.paDatos[i + 14]['CIMPRIM'], xboolean2[1], xboolean2[0]], [wr*0.42, wr*0.04, wr*0.04, wr*0.42,wr*0.04, wr*0.04])
            loPdf.ln()
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(w,h, 'COMENTARIOS',1, 2, 'L')
            loPdf.set_font('Arial', '' , 6)
            if(self.paData['OACTIVI']['MCONCLU'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MOBSERV'],1, 'L') #TODO no existe mcoment...
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            loPdf.ln()
            loPdf.set_borders([0, 1])
            loPdf.set_bolds(['B', 'B'])
            loPdf.set_aligns(['C', 'C'])
            loPdf.Row(['', 'NORMAL'], [wr*0.62, wr*0.08])
            loPdf.set_bolds(['B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([self.paDatos[29]['CIMPRIM'], 'SI', 'NO'], [wr*0.62, wr*0.04, wr*0.04])
            for i in range(30, 40):
                xboolean = [' ', 'X'] if int(self.paDatos[i]['CRESULT']) == 1 else ['X', '']
                loPdf.set_aligns(['L', 'C', 'C'])
                loPdf.Row([str(i - 29)+'. '+self.paDatos[i]['CIMPRIM'], xboolean[1], xboolean[0]], [wr*0.62, wr*0.04, wr*0.04])
            loPdf.ln()
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.cell(w,h, 'OBSERVACIONES',1, 2, 'L')
            loPdf.set_font('Arial', '' , 6)
            if(self.paData['OACTIVI']['MOBSERV'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MOBSERV'],1, 'L')
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B' , 6)
            loPdf.Row(['APTITUD PARA LABORAR POR ENCIMA DE 1.8 METROS SOBRE EL SUELO'], [wr*1])
            loPdf.set_font('Arial', '' , 6)
            loPdf.ln(0.2)
            loPdf.set_x(loPdf.get_x() + wr*0.35)
            loPdf.cell(1, h, 'APTO', 0, 0, 'L')
            loPdf.cell(1, h, 'X', 1, 0, 'C')
            loPdf.cell(0.5)
            loPdf.cell(1.2, h, 'NO APTO', 0, 0, 'L')
            loPdf.cell(1, h, 'X', 1, 0, 'C')
            
            loPdf.image("./src/PDF/assets/9999.jpg" , 1, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 9, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_evaluacion_musculo_esqueletica(self):
        #validar datos para imprimir actividad
        return True #TODO borrar
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True

    def print_evaluacion_musculo_esqueletica(self):
        loPdf  = PYFPDF()
        llOK = self.val_evaluacion_musculo_esqueletica()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'FICHA DE EVALUACION MUSCULO ESQUELETICA BASICA')
            loPdf.set_border(1)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'APTITUD DE ESPALDA', 1, 1, 'C')
            loPdf.ln(0.2)
            loPdf.set_font('Arial', '', 6)
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.set_bolds(['B', 'B', 'B', 'B', 'B', 'B', 'B'])
            loPdf.set_x(wr*0.27)
            loPdf.Row(['Flexibilidad/\nFuerza', 'Excelente: 1', 'Promedio: 2', 'Regular: 3', 'Pobre: 4', 'Ptos.+', 'OBSERVACIONES'], [wr*0.10, wr*0.08, wr*0.08, wr*0.08, wr*0.08, wr*0.05, wr*0.15])
            #imprimir imagenes
            loPdf.set_x(wr*0.27)
            x = loPdf.get_x()
            text = ['ABDOMEN','CADERA','MUSLO','ABDOMEN LATERAL']
            for i in range(4):
                xaux = x
                yaux = loPdf.get_y()
                loPdf.cell(0.1, 0.4, '', 0, 2, 'C')
                loPdf.set_font('Arial', 'B', 6)
                loPdf.multi_cell(wr*0.10, 0.4, text[i], 0, 'C')
                loPdf.set_font('Arial', '', 6)
                loPdf.set_xy(xaux, yaux)                
                loPdf.cell(wr*0.10, 1.5, '', 1, 0, 'C')
                loPdf.image("./src/PDF/assets/placeholder.jpg" , loPdf.get_x(), loPdf.get_y(), wr*0.08, 1.5)
                loPdf.cell(wr*0.08, 1.5, '', 1, 0, 'C')
                loPdf.image("./src/PDF/assets/placeholder.jpg" , loPdf.get_x(), loPdf.get_y(), wr*0.08, 1.5)
                loPdf.cell(wr*0.08, 1.5, '', 1, 0, 'C')
                loPdf.image("./src/PDF/assets/placeholder.jpg" , loPdf.get_x(), loPdf.get_y(), wr*0.08, 1.5)
                loPdf.cell(wr*0.08, 1.5, '', 1, 0, 'C')
                loPdf.image("./src/PDF/assets/placeholder.jpg" , loPdf.get_x(), loPdf.get_y(), wr*0.08, 1.5)
                loPdf.cell(wr*0.08, 1.5, '', 1, 0, 'C')
                loPdf.cell(wr*0.05, 1.5, str(i + 1), 1, 0, 'C')
                loPdf.cell(wr*0.15, 1.5, 'EJEMPLO', 1, 1, 'C')
                loPdf.set_x(x)
            loPdf.set_x(wr*0.27)
            loPdf.Row(['', '', '', '', 'TOTAL:', '10', ''], [wr*0.10, wr*0.08, wr*0.08, wr*0.08, wr*0.08, wr*0.05, wr*0.15])
            loPdf.ln()
            loPdf.cell(w, h, 'En puntos colocar el grado que corresponde a la capacidad del paciente. Repetir cada movimiento contra resistencia leve a moderada y evaluar fortaleza y presencia de dolor.', 0, 1, 'C')
            loPdf.ln()
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.set_bolds(['B', 'B', 'B', 'B', 'B', 'B'])
            loPdf.set_x(wr*0.25)
            loPdf.Row(['RANGOS ARTICULARES', 'Optimo: 1', 'Limitado: 2', 'Muy limitado: 3', 'Ptos.*', 'Dolor contra resistencia **'], [wr*0.15, wr*0.12, wr*0.12, wr*0.12, wr*0.05, wr*0.10])
            #imprimir imagenes
            loPdf.set_x(wr*0.25)
            x = loPdf.get_x()
            text = ['Abducción de hombro (Normal 0° - 180°)','Abducción de hombro (Normal 0° - 60°)','Rotacion externa (Normal 0° - 90°)','Rotacion externa de hombro (interna)']
            for i in range(4):
                xaux = x
                yaux = loPdf.get_y()
                loPdf.cell(0.1, 0.4, '', 0, 2, 'C')
                loPdf.multi_cell(wr*0.15, 0.4, text[i], 0, 'C')
                loPdf.set_xy(xaux, yaux)
                loPdf.cell(wr*0.15, 1.5, '', 1, 0, 'C')
                loPdf.image("./src/PDF/assets/placeholder.jpg" , loPdf.get_x(), loPdf.get_y(), wr*0.12, 1.5)
                loPdf.cell(wr*0.12, 1.5, '', 1, 0, 'C')
                loPdf.image("./src/PDF/assets/placeholder.jpg" , loPdf.get_x(), loPdf.get_y(), wr*0.12, 1.5)
                loPdf.cell(wr*0.12, 1.5, '', 1, 0, 'C')
                loPdf.image("./src/PDF/assets/placeholder.jpg" , loPdf.get_x(), loPdf.get_y(), wr*0.12, 1.5)
                loPdf.cell(wr*0.12, 1.5, '', 1, 0, 'C')
                loPdf.cell(wr*0.05, 1.5, str(i + 1), 1, 0, 'C')
                loPdf.cell(wr*0.10, 1.5, 'EJEMPLO', 1, 1, 'C')
                loPdf.set_x(x)
            loPdf.set_x(wr*0.25)
            loPdf.Row(['', '', '', 'TOTAL:', '10', ''], [wr*0.15, wr*0.12, wr*0.12, wr*0.12, wr*0.05, wr*0.10])
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'OBSERVACIONES',1, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            #loPdf.multi_cell(w,h, '#REEMPLAZAR#', 1, 'L')
            if(self.paData['OACTIVI']['MOBSERV'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MOBSERV'],1, 'L')
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            
            
            loPdf.image("./src/PDF/assets/9999.jpg" , 1, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 9, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_odontologia(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_odontologia(self):
        loPdf  = PYFPDF()
        llOK = self.val_odontologia()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('ODONTOLOGIA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            loPdf.set_font('Arial', '', 6)
            loPdf.ln()
            loPdf.set_border(1)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'ODONTOGRAMA', 1, 1, 'C')
            loPdf.ln(0.2)
            loPdf.set_font('Arial', '', 6)
            ancho = 0.84
            ancho_s = 0.625
            loPdf.set_x(4.4)
            for i in range(18, 10, -1):
                if i in [11, 12, 13]:
                    loPdf.cell(ancho_s, h, str(i), 1, 0, 'C')
                else:
                    loPdf.cell(ancho, h, str(i), 1, 0, 'C')
            for i in range(21, 29):
                if i in [21, 22, 23]:
                    loPdf.cell(ancho_s, h, str(i), 1, 0, 'C')
                else:
                    loPdf.cell(ancho, h, str(i), 1, 0, 'C')
            loPdf.ln()
            loPdf.set_x(4.4)
            for i in range(16):
                if i in [5, 6, 7, 8, 9, 10]:
                    loPdf.cell(ancho_s, 0.5, '', 1, 0, 'C')
                else:
                    loPdf.cell(ancho, 0.5, '', 1, 0, 'C')
            loPdf.ln(0.5)
            loPdf.ln(0.1)
            loPdf.set_x(4.4)
            loPdf.image("./src/PDF/assets/odontologia1.jpg", loPdf.get_x(), loPdf.get_y(), 12.29, 1.48)
            loPdf.ln(2)

            loPdf.set_x(6.95)
            for i in range(55, 50, -1):
                if i in [51, 52, 53]:
                    loPdf.cell(ancho_s, h, str(i), 1, 0, 'C')
                else:
                    loPdf.cell(ancho, h, str(i), 1, 0, 'C')
            for i in range(61, 66):
                if i in [61, 62, 63]:
                    loPdf.cell(ancho_s, h, str(i), 1, 0, 'C')
                else:
                    loPdf.cell(ancho, h, str(i), 1, 0, 'C')
            loPdf.ln()
            loPdf.set_x(6.95)
            for i in range(10):
                if i in [2, 3, 4, 5, 6, 7]:
                    loPdf.cell(ancho_s, 0.5, '', 1, 0, 'C')
                else:
                    loPdf.cell(ancho, 0.5, '', 1, 0, 'C')
            loPdf.ln(0.5)
            loPdf.ln(0.1)
            loPdf.set_x(6.95)
            loPdf.image("./src/PDF/assets/odontologia2.jpg", loPdf.get_x(), loPdf.get_y(), 7.2, 1.48)
            loPdf.ln(1.7)
            
            loPdf.set_x(6.95)
            loPdf.image("./src/PDF/assets/odontologia3.jpg", loPdf.get_x(), loPdf.get_y(), 7.36, 1.55)
            loPdf.ln(1.7)
            loPdf.set_x(6.95)
            for i in range(85, 80, -1):
                if i in [81, 82, 83]:
                    loPdf.cell(ancho_s, h, str(i), 1, 0, 'C')
                else:
                    loPdf.cell(ancho, h, str(i), 1, 0, 'C')
            for i in range(71, 76):
                if i in [71, 72, 73]:
                    loPdf.cell(ancho_s, h, str(i), 1, 0, 'C')
                else:
                    loPdf.cell(ancho, h, str(i), 1, 0, 'C')
            loPdf.ln()
            loPdf.set_x(6.95)
            for i in range(10):
                if i in [2, 3, 4, 5, 6, 7]:
                    loPdf.cell(ancho_s, 0.5, '', 1, 0, 'C')
                else:
                    loPdf.cell(ancho, 0.5, '', 1, 0, 'C')
            loPdf.ln(0.5)
            loPdf.ln(0.5)
            
            loPdf.set_x(4.4)
            loPdf.image("./src/PDF/assets/odontologia4.jpg", loPdf.get_x(), loPdf.get_y(), 12.35, 1.44)
            loPdf.ln(1.7)
            loPdf.set_x(4.4)
            for i in range(48, 40, -1):
                if i in [41, 42, 43]:
                    loPdf.cell(ancho_s, h, str(i), 1, 0, 'C')
                else:
                    loPdf.cell(ancho, h, str(i), 1, 0, 'C')
            for i in range(31, 39):
                if i in [31, 32, 33]:
                    loPdf.cell(ancho_s, h, str(i), 1, 0, 'C')
                else:
                    loPdf.cell(ancho, h, str(i), 1, 0, 'C')
            loPdf.ln()
            loPdf.set_x(4.4)
            for i in range(16):
                if i in [5, 6, 7, 8, 9, 10]:
                    loPdf.cell(ancho_s, 0.5, '', 1, 0, 'C')
                else:
                    loPdf.cell(ancho, 0.5, '', 1, 0, 'C')
            loPdf.ln(0.5)

            loPdf.ln(h)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'OBSERVACIONES',1, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            #loPdf.multi_cell(w,h, '#REEMPLAZAR#', 1, 'L')
            if(self.paData['OACTIVI']['MOBSERV'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MOBSERV'],1, 'L')
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            loPdf.set_bolds(['B', '', 'B', '', 'B', ''])
            loPdf.Row(['NUMERO DE CARIES', 'EJEMPLO', 'PIEZAS FALTANTES', 'EJEMPLO', 'REMANENTE RADICULAR', 'EJEMPLO'], [wr*0.17, wr*0.13, wr*0.17, wr*0.21, wr*0.21, wr*0.11])
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'DIAGNOSTICO',1, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            #loPdf.multi_cell(w,h, '#REEMPLAZAR#', 1, 'L')
            if(self.paData['OACTIVI']['MOBSERV'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MOBSERV'],1, 'L')
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'RECOMENDACIONES',1, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            #loPdf.multi_cell(w,h, '#REEMPLAZAR#', 1, 'L')
            if(self.paData['OACTIVI']['MOBSERV'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MOBSERV'],1, 'L')
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            
            loPdf.image("./src/PDF/assets/9999.jpg" , 1, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 9, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_ekg_riesgo_cardiovascular(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_ekg_riesgo_cardiovascular(self):
        loPdf  = PYFPDF()
        llOK = self.val_ekg_riesgo_cardiovascular()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('CARDIOLOGIA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            #self.print_title(loPdf, 'FORMATO EKG')
            self.print_title(loPdf, 'RIESGO CARDIOVASCULAR')
            loPdf.set_border(1)
            #loPdf.Row([self.paDatos[0]['CIMPRIM'], self.paDatos[0]['CRESULT'], self.paDatos[1]['CIMPRIM'], self.paDatos[1]['CRESULT'], self.paDatos[2]['CIMPRIM'], self.paDatos[2]['CRESULT']], [wr*0.08, wr*0.24, wr*0.05, wr*0.13, wr*0.14, wr*0.36])
            #for i in range(3, 12, 2):
            #    loPdf.Row([self.paDatos[i]['CIMPRIM'], self.paDatos[i]['CRESULT'], self.paDatos[i + 1]['CIMPRIM'], self.paDatos[i + 1]['CRESULT']], [wr*0.14, wr*0.36, wr*0.14, wr*0.36])
            #TODO reemplazar por lo de arriba
            tmp = ['INTERVALO QRS', 'INTERVALO QT', 'ONDA P', 'ONDA Q', 'ONDA R', 'ONDA S', 'ONDA T', 'ONDA U', 'SEGMENTO ST', 'EJE QRS']
            loPdf.Row(['RITMO', 'EJEMPLO', 'F.C.', 'EJEMPLO', 'INTERVALO PR', 'EJEMPLO'], [wr*0.08, wr*0.24, wr*0.05, wr*0.13, wr*0.14, wr*0.36])
            for i in range(0, 10, 2):
                loPdf.Row([tmp[i], 'EJEMPLO', tmp[i + 1], 'EJEMPLO'], [wr*0.14, wr*0.36, wr*0.14, wr*0.36])
            #
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'EVALUACION DE RIESGO CARDIOVASCULAR', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(w, h, '2013 ACC/AHA Guideline on the Assessment of Cardiovascular Risk', 0, 1, 'L')
            loPdf.ln(0.2)
            loPdf.cell(2.5, h, 'RAZA', 0, 0, 'L')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            loPdf.cell(2, h, 'Afroamericano', 0, 0, 'L')
            loPdf.cell(0.5)
            loPdf.cell(2, h, 'Otro:', 0, 1, 'L')
            loPdf.ln(0.2)
            loPdf.cell(2.5, h, 'COLESTEROL TOTAL', 0, 0, 'L')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            loPdf.cell(0, h, 'EJEMPLO', 0, 1, 'L')

            loPdf.cell(2.5, h, 'HDL', 0, 0, 'L')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            loPdf.cell(0, h, 'EJEMPLO', 0, 1, 'L')
            loPdf.ln(0.2)
            loPdf.cell(3.6, h, 'PRESION ARTERIAL SISTOLICA', 0, 0, 'L')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            loPdf.cell(0, h, 'EJEMPLO', 0, 1, 'L')

            loPdf.cell(3.6, h, 'PRESION ARTERIAL DIASTOLICA', 0, 0, 'L')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            loPdf.cell(0, h, 'EJEMPLO', 0, 1, 'L')
            loPdf.ln(0.2)
            loPdf.cell(3.6, h, 'TRATAMIENTO PARA HTA', 0, 0, 'L')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            loPdf.cell(0.5, h, 'SI', 0, 0, 'L')
            loPdf.cell(0.5, h, 'X', 1, 0, 'C')
            loPdf.cell(0.5)
            loPdf.cell(0.5, h, 'NO', 0, 0, 'L')
            loPdf.cell(0.5, h, '', 1, 1, 'C')

            loPdf.cell(3.6, h, 'DIABETES MELLITUS', 0, 0, 'L')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            loPdf.cell(0.5, h, 'SI', 0, 0, 'L')
            loPdf.cell(0.5, h, 'X', 1, 0, 'C')
            loPdf.cell(0.5)
            loPdf.cell(0.5, h, 'NO', 0, 0, 'L')
            loPdf.cell(0.5, h, '', 1, 1, 'C')

            loPdf.cell(3.6, h, 'TABACO', 0, 0, 'L')
            loPdf.cell(0.3, h, ':', 0, 0, 'C')
            loPdf.cell(0.5, h, 'SI', 0, 0, 'L')
            loPdf.cell(0.5, h, 'X', 1, 0, 'C')
            loPdf.cell(0.5)
            loPdf.cell(0.5, h, 'NO', 0, 0, 'L')
            loPdf.cell(0.5, h, '', 1, 1, 'C')
            loPdf.ln(0.2)
            loPdf.cell(0, h, 'RIESGO DE ENFERMEDAD CARDÍACA O STROKE A 10 AÑOS', 0, 1, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'CONCLUSION',1, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            #loPdf.multi_cell(w,h, '#REEMPLAZAR#', 1, 'L')
            if(self.paData['OACTIVI']['MOBSERV'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MOBSERV'],1, 'L')
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'COMENTARIOS',1, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            #loPdf.multi_cell(w,h, '#REEMPLAZAR#', 1, 'L')
            if(self.paData['OACTIVI']['MOBSERV'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MOBSERV'],1, 'L')
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            
            loPdf.image("./src/PDF/assets/9999.jpg" , 1, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 9, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)

            loPdf.add_page()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'TRAZADO DEL ELECTROCARDIOGRAFO', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False
    
    def val_screening_dermatologico(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = ['0375','0376','0377','0378','0379','0380','0381','0382','0383','0384','0385','0386','0387','0388','0389','0390','0391']
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_screening_dermatologico(self):
        loPdf  = PYFPDF()
        llOK = self.val_screening_dermatologico()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'FICHA DE SCREENING DERMATOLOGICO')
            loPdf.set_border(1)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, self.paDatos[0]['CIMPRIM'], 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            #imprimir imagenes
            loPdf.ln(0.15)
            loPdf.set_x(3.3)
            loPdf.image("./src/PDF/assets/screening.jpg", loPdf.get_x(), loPdf.get_y(), 14.4, 7)
            loPdf.ln(7.4)
            for i in range(1, 6):
                loPdf.Row([self.paDatos[i]['CIMPRIM'], self.paDatos[i]['CRESULT']], [wr*0.1, wr*0.9])
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, self.paDatos[6]['CIMPRIM'], 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.ln(0.2)
            x_select = self.x_select(self.paDatos[7]['MTABLA'])
            romanos = ['I', 'II', 'III', 'IV', 'V', 'VI']
            y = loPdf.get_y()
            x = loPdf.get_x() + 1
            loPdf.set_x(x)
            for i in range(6):
                loPdf.set_font('Arial', 'B', 6)
                loPdf.cell(1.5, h, 'TIPO ' + romanos[i], 1, 0, 'C')
                loPdf.set_font('Arial', '', 6)
                loPdf.cell(6, h, x_select[i], 1, 1, 'L')
                if (i == 2):
                    loPdf.set_y(y)
                    x = wr / 2 + 1.8
                loPdf.set_x(x)
            #loPdf.data_in_checktable(self.paDatos[7]['MTABLA'], wr*0.8)

            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, self.paDatos[8]['CIMPRIM'], 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            #imprimir imagenes
            for i in range(9, 20):
                if i in [9, 10, 11, 12, 16, 17]:
                    loPdf.Row([self.paDatos[i]['CIMPRIM'], self.paDatos[i]['CRESULT']], [wr*0.35, wr*0.65])
                else:
                    xboolean = [' ', 'X'] if int(self.paDatos[i]['CRESULT']) == 1 else ['X', '']
                    loPdf.set_aligns(['L', 'C', 'L', 'C', 'L'])
                    loPdf.set_bolds(['', 'B', '', 'B', ''])
                    loPdf.Row([self.paDatos[i]['CIMPRIM'], 'SI', xboolean[1], 'NO', xboolean[0]], [wr*0.35, wr*0.65/4, wr*0.65/4, wr*0.65/4, wr*0.65/4])
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'DIAGNOSTICO / CONCLUSION',1, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            #loPdf.multi_cell(w,h, '#REEMPLAZAR#', 1, 'L')
            if(self.paData['OACTIVI']['MOBSERV'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MOBSERV'],1, 'L')
            else:
                loPdf.cell(w,h, ' ',1, 2, 'L')
            
            
            loPdf.image("./src/PDF/assets/9999.jpg" , 1, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 9, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_test_de_somnolencia(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = ['0392','0393','0394','0395','0396','0397','0398','0399']
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_test_de_somnolencia(self):
        loPdf  = PYFPDF()
        llOK = self.val_test_de_somnolencia()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('PSICOLOGIA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()
            
            self.print_title(loPdf, 'CUESTIONARIO DE SOMNOLENCIA DIURNA DE EPWORTH')
            loPdf.multi_cell(w, h, 'Este cuestionario pretende valorar la facilidad para amodorrarse o quedarse dormido en cada una de las diferentes situaciones. Aunque no haya vivido alguna de estas situaciones recientemente, intente imaginar como le habría afectado.', 0, 'J')
            resultado = 0
            for i in range(8):
                loPdf.cell(0.4, h, str(i + 1) + '.-', 0, 0, 'L')
                loPdf.cell(w, h, self.paDatos[i]['CIMPRIM'], 0, 2, 'L')
                resultado += int(self.paDatos[i]['CRESULT'])
                caracter = 97 #letra a
                for i in self.paDatos[i]['MTABLA']:
                    loPdf.cell(w, h, chr(caracter) + ') ' + i['CDESCRI'], 0, 2, 'L')
                    caracter += 1
                loPdf.ln(0)
            loPdf.cell(w, h, 'Baremación del Cuestionario.', 0, 1, 'L')
            loPdf.cell(w, h, 'Asigne los siguientes puntos a cada situación', 0, 1, 'L')
            
            loPdf.cell(2, h, '0 puntos.............', 0, 0, 'L')
            loPdf.cell(w, h, 'Nunca      .............', 0, 1, 'L')
            loPdf.cell(2, h, '1 punto  .............', 0, 0, 'L')
            loPdf.cell(w, h, 'Ligera      .............', 0, 1, 'L')
            loPdf.cell(2, h, '2 puntos.............', 0, 0, 'L')
            loPdf.cell(w, h, 'Moderada.............', 0, 1, 'L')
            loPdf.cell(2, h, '3 puntos.............', 0, 0, 'L')
            loPdf.cell(w, h, 'Alta          .............', 0, 1, 'L')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.ln(0.1)
            loPdf.cell(w, h, 'Suma total : ' + str(resultado), 0, 1, 'L')
            loPdf.ln(0.1)
            loPdf.set_font('Arial', '', 6)
            loPdf.multi_cell(w, h, 'Si su puntuación es inferior a 6 puntos su somnolencia diurna es baja o ausente; si esta comprendida entre 7 y 8, se encuentra en la media de la población y si es superior a 9 su somnolencia es excesiva y debe consultar a un especialista.', 0, 'J')
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_anexo_16_a(self):
        #validar datos para imprimir actividad
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = ['0400', '0401', '0402', '0403', '0404', '0405', '0406', '0407', '0408', '0409', '0410', '0411', '0412', '0413', '0414', '0415']
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_anexo_16_a(self):
        loPdf  = PYFPDF()
        llOK = self.val_anexo_16_a()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'ANEXO 16 A')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, self.paDatos[0]['CIMPRIM'], 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            temp_triaje = ['FC :', 'PA :', 'FR :', 'IMC :', 'Sat O2 :']
            temp_triaje_vals = ['71 x min', '110/70 mm Hg', '20 x min', '25.01 kg/m^2', '95 %']
            for i in range(5):
                loPdf.set_font('Arial', 'B', 6)
                loPdf.cell(wr*0.06, h, temp_triaje[i], 1, 0, 'C')
                loPdf.set_font('Arial', '', 6)
                loPdf.cell(wr*0.14, h, temp_triaje_vals[i], 1, 0, 'L')
            loPdf.ln()
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, self.paDatos[1]['CIMPRIM'], 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.ln(0.2)
            loPdf.set_border(1)
            loPdf.set_borders([0])
            loPdf.set_bolds(['', 'B', 'B'])
            loPdf.set_aligns(['L', 'C', 'C'])
            x = loPdf.get_x() + 1
            loPdf.set_x(x)
            loPdf.Row(['', 'SI', 'NO'], [wr*0.6, wr*0.04, wr*0.04])
            for i in range(2, 17):
                xboolean = self.x_boolean_multi(self.paDatos[i]['CRESULT'])
                loPdf.set_aligns(['L', 'C', 'C'])
                loPdf.set_x(x)
                loPdf.Row(['- ' + self.paDatos[i]['CIMPRIM'], xboolean[0], xboolean[1]], [wr*0.6, wr*0.04, wr*0.04])
            loPdf.set_borders([0, 0])
            loPdf.set_x(x)
            loPdf.Row(['- ' + self.paDatos[17]['CIMPRIM'], self.paDatos[17]['CRESULT']], [wr*0.2, wr*0.8])
            loPdf.set_x(x)
            loPdf.multi_cell(w, h, 'Declaro que las respuestas dadas en el presente documento son verdaderas y estoy consciente que el ocultar o falsear información me puede causar daño por lo que asumo total responsabilidad de ello.', 0, 'J')
            #TODO firmas
            
            loPdf.ln(h*4)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'EKG: (A partir de 45 años)',1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.multi_cell(w,h, '', 1, 'L')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'APTITUD',1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.multi_cell(w,h, '', 1, 'L')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'OBSERVACIONES',1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.multi_cell(w,h, '', 1, 'L')

            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_anexo_16(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_anexo_16(self):
        loPdf  = PYFPDF()
        llOK = self.val_anexo_16()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()
            
            self.print_title(loPdf, 'ANEXO 16')
            loPdf.set_font('Arial', 'B', 6)
            x = loPdf.get_x()
            y = loPdf.get_y()
            #MINERALES EXPLOTADOS O PROCESADOS
            loPdf.set_font('Arial', 'B', 6)
            loPdf.multi_cell(3.7, h, 'MINERALES EXPLOTADOS O PROCESADOS', 0, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_xy(x, y)
            loPdf.cell(3.7, h*2, '', 1, 1, 'L')
            temp_labels = ['SUPERFICIE', 'CONCENTRADORA', 'SUBSUELO'] #TODO reemplazar variables temp
            for i in range(3):
                loPdf.cell(3.2, h, temp_labels[i], 0, 0, 'L')
                loPdf.cell(0.5, h, ' ', 1, 1, 'C')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(0.8, h, 'TIPO', 1, 0, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(2.9, h, '', 1, 1, 'C')
            #ALTURA DE LA LABOR
            x = x + 3.95
            loPdf.set_xy(x, y)
            x1 = x
            ancho = 5.05
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(ancho, h*2, 'ALTITUD DE LA LABOR', 1, 2, 'C')
            loPdf.set_font('Arial', '', 6)
            temp_labels = ['Debajo de 2500 m', '2501 a 3000 m', '3001 a 3500 m', '3501 a 4000 m', '4001 a 4500 m', 'más de 4501 m'] #TODO reemplazar variables temp
            for i in range(6):
                loPdf.cell(1.9, h, temp_labels[i], 0, 0, 'L')
                loPdf.cell(0.4, h, '', 1, 1, 'C')
                loPdf.set_x(x1)
                if i == 2:
                    x1 = x1 + 2.3 + 0.45
                    loPdf.set_xy(x1, y + h*2)
            #EXPUESTO A
            x = x + 5.3
            loPdf.set_xy(x, y)
            x1 = x
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h*2, 'EXPUESTO A', 1, 2, 'C')
            loPdf.set_font('Arial', '', 6)
            ancho = 1
            temp_labels = ['Ruido', 'Polvo', 'Turnos', 'Cargas', 'Vibr. Segmentaria', 'Vibr. Total', 'Cancerígenos', 'Temperaturas', 'Mutagénicos', 'Solventes', 'Posturas', 'Biológicos', 'Metales pesados', 'Mov. Repetidos', 'PVD', 'Otros:'] #TODO reemplazar variables temp
            for i in range(16):
                if i != 15:
                    loPdf.cell(ancho, h, temp_labels[i], 0, 0, 'L')
                    loPdf.cell(0.4, h, '', 1, 1, 'C')
                else: #OTROS
                    loPdf.cell(0.8, h, temp_labels[i], 0, 0, 'L')
                    loPdf.cell(w, h, '', 1, 1, 'L')
                loPdf.set_x(x1)
                if i in [3, 7, 11]:
                    x1 = x1 + 0.5 + ancho
                    if i == 3:
                        ancho = 2
                    elif i == 7:
                        ancho = 1.5
                    elif i == 11:
                        ancho = 1.8
                    loPdf.set_xy(x1, y + h*2)
            #ANTECEDENTES OCUPACIONALES
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'ANTECEDENTES OCUPACIONALES (Ver adjunto Historia Ocupacional)', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            #ANTECEDENTES PERSONALES
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'ANTECEDENTES PERSONALES (Enfermedades y accidentes en el trabajo y fuera del mismo)', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(w, h, '', 1, 1, 'C')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(2.1, h, 'ALERGIAS', 1, 0, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(w, h, '', 1, 1, 'L')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(2.1, h, 'INMUNIZACIONES', 1, 0, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(w, h, '', 1, 1, 'L')
            #ANTECEDENTES FAMILIARES
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'ANTECEDENTES FAMILIARES', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_border(1)
            loPdf.set_bolds(['B', '', 'B', '', 'B', '', 'B', ''])
            loPdf.Row(['Padre:', '', 'Madre:', '','Hermanos:', '', 'N°', ''], [wr*0.1, wr*0.15, wr*0.1, wr*0.15, wr*0.12, wr*0.28, wr*0.05, wr*0.05])
            loPdf.set_bolds(['B', '', 'B', '', 'B', '', 'B', '', 'B', ''])
            loPdf.Row(['Esposo(a):', '', 'Hijos vivos:', '','N°', '','Hijos Fallecidos:', '', 'N°', ''], [wr*0.1, wr*0.15, wr*0.1, wr*0.07, wr*0.05, wr*0.05, wr*0.12, wr*0.26, wr*0.05, wr*0.05])
            #HABITOS
            loPdf.ln()
            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(4, h, 'HABITOS', 1, 2, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(1.3)
            loPdf.cell(0.9, h, 'Tabaco', 0, 0, 'C')
            loPdf.cell(0.9, h, 'Alcohol', 0, 0, 'C')
            loPdf.cell(0.9, h, 'Drogas', 0, 0, 'C')
            loPdf.ln()
            loPdf.cell(1.3, h, 'Nada', 0, 0, 'L')
            loPdf.cell(0.9, h, '', 1, 0, 'C')
            loPdf.cell(0.9, h, '', 1, 0, 'C')
            loPdf.cell(0.9, h, '', 1, 0, 'C')
            loPdf.ln()
            loPdf.cell(1.3, h, 'Poco', 0, 0, 'L')
            loPdf.cell(0.9, h, '', 1, 0, 'C')
            loPdf.cell(0.9, h, '', 1, 0, 'C')
            loPdf.cell(0.9, h, '', 1, 0, 'C')
            loPdf.ln()
            loPdf.cell(1.3, h, 'Habitual', 0, 0, 'L')
            loPdf.cell(0.9, h, '', 1, 0, 'C')
            loPdf.cell(0.9, h, '', 1, 0, 'C')
            loPdf.cell(0.9, h, '', 1, 0, 'C')
            loPdf.ln()
            loPdf.cell(1.3, h, 'Excesivo', 0, 0, 'L')
            loPdf.cell(0.9, h, '', 1, 0, 'C')
            loPdf.cell(0.9, h, '', 1, 0, 'C')
            loPdf.cell(0.9, h, '', 1, 0, 'C')

            #FUNCIONES VITALES
            x = x + 4.25
            loPdf.set_xy(x, y)
            x1 = x
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(4.4, h, 'FUNCIONES VITALES', 1, 2, 'C')
            loPdf.set_font('Arial', '', 6)
            temp_labels = ['SISTOLICA', 'DIASTOLICA', 'F. RESP.', 'F. CARD.', 'Sat. O2', 'Temp.'] #TODO reemplazar
            temp_labels_m = ['mmhg', 'mmhg', 'x min.', 'x min.', '%', '°C'] #TODO reemplazar
            for i in range(6):
                loPdf.cell(1.5, 0.33, temp_labels[i], 0, 0, 'L')
                loPdf.cell(1.9, 0.33, 'x', 1, 0, 'L')
                loPdf.cell(1, 0.33, temp_labels_m[i], 0, 1, 'L')
                loPdf.set_x(x1)
            #BIOMETRIA
            x = x + 4.65
            loPdf.set_xy(x, y)
            x1 = x
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(4, h, 'BIOMETRIA', 1, 2, 'C')
            loPdf.set_font('Arial', '', 6)
            temp_labels = ['Talla', 'Peso', 'IMC', 'Cintura', 'Cadera', 'ICC'] #TODO reemplazar
            temp_labels_m = ['m.', 'Kg', '', 'cm.', 'cm.', 'Kg/m2'] #TODO reemplazar
            for i in range(6):
                loPdf.cell(1.3, 0.33, temp_labels[i], 0, 0, 'L')
                loPdf.cell(1.7, 0.33, 'x', 1, 0, 'L')
                loPdf.cell(1, 0.33, temp_labels_m[i], 0, 1, 'L')
                loPdf.set_x(x1)
            #FUNCION RESPIRATORIA
            x = x + 4.25
            loPdf.set_xy(x, y)
            x1 = x
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(5.25, h, 'FUNCION RESPIRATORIA', 1, 2, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(1.5)
            loPdf.cell(1.875, 0.3, 'Ref.', 0, 0, 'C')
            loPdf.cell(1.875, 0.3, 'Abs %', 0, 1, 'C')
            loPdf.set_x(x)
            temp_labels = ['FVC', 'FEV1', 'FEV1/FVC', 'FEF 25-75%'] #TODO reemplazar
            for i in range(4):
                loPdf.cell(1.5, 0.33, temp_labels[i], 0, 0, 'L')
                loPdf.cell(1.875, 0.33, '', 1, 0, 'L')
                loPdf.cell(1.875, 0.33, '', 1, 1, 'L')
                loPdf.set_x(x)
            loPdf.cell(1.5, 0.33, 'Conclusión', 0, 0, 'L')
            loPdf.cell(3.75, 0.48 + h, '', 1, 1, 'L')
            #CABEZA
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'CABEZA', 0, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(w, h, '', 1, 1, 'L')
            #CUELLO
            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr/2 - 0.2, h, 'CUELLO', 0, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr/2 - 0.2, h, '', 1, 1, 'L')
            #BOCA
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr/2 - 0.2, h, 'BOCA, AMIGDALAS, FARINGE, LARINGE', 0, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr/2 - 0.2, h, '', 1, 1, 'L')
            #NARIZ
            x = x + wr/2 + 0.2
            loPdf.set_xy(x, y)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr/2 - 0.2, h, 'NARIZ', 0, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr/2 - 0.2, h, '', 1, 2, 'L')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(2.4, h, 'Piezas en mal estado:', 1, 0, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(w, h, '', 1, 2, 'L')
            loPdf.set_x(x)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(2.4, h, 'Piezas que faltan:', 1, 0, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(w, h, '', 1, 1, 'L')
            #OJOS
            loPdf.ln(0.2)
            y = loPdf.get_y()
            ancho = (wr/2 - 0.2) / 3
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(ancho, h*2, 'OJOS', 1, 0, 'C')
            loPdf.cell(ancho, h, 'SIN CORREGIR', 1, 0, 'C')
            loPdf.cell(ancho, h, 'CORREGIDA', 1, 1, 'C')
            loPdf.cell(ancho)
            loPdf.cell(ancho/2, h, 'O.D.', 1, 0, 'C')
            loPdf.cell(ancho/2, h, 'O.I.', 1, 0, 'C')
            loPdf.cell(ancho/2, h, 'O.D.', 1, 0, 'C')
            loPdf.cell(ancho/2, h, 'O.I.', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            
            loPdf.cell(ancho, h, 'VISIÓN DE LEJOS', 1, 0, 'L')
            loPdf.cell(ancho/2, h, '', 1, 0, 'C')
            loPdf.cell(ancho/2, h, '', 1, 0, 'C')
            loPdf.cell(ancho/2, h, '', 1, 0, 'C')
            loPdf.cell(ancho/2, h, '', 1, 1, 'C')
            
            loPdf.cell(ancho, h, 'VISIÓN DE CERCA', 1, 0, 'L')
            loPdf.cell(ancho, h, '', 1, 0, 'C')
            loPdf.cell(ancho, h, '', 1, 1, 'C')

            loPdf.cell(ancho, h, 'VISIÓN DE COLORES', 1, 0, 'L')
            loPdf.cell(ancho*2, h, '', 1, 0, 'C')
            #ENFERMEDADES OCULARES
            loPdf.set_xy(x, y)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr/2 - 0.2, h, 'ENFERMEDADES OCULARES:', 0, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr/2 - 0.2, h + h/2, '', 1, 2, 'L')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr/2 - 0.2, h, 'REFLEJOS PUPILARES:', 0, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr/2 - 0.2, h + h/2, '', 1, 2, 'L')
            #OIDOS
            loPdf.ln(0.2)
            ancho = (wr/2 - 0.2) * 0.125
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(4, h, 'OIDOS', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            y = loPdf.get_y()
            loPdf.set_borders([0, 0, 0])
            loPdf.set_bolds(['', 'B', 'B'])
            loPdf.Row(['', 'Audición derecha', '      500  1000 2000 3000 4000 6000 8000'], [ancho, (wr/2-ancho)*0.35, (wr/2-ancho)*0.65])
            loPdf.set_borders([0])
            loPdf.set_aligns(['R', 'C', 'C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.set_bolds(['', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])
            loPdf.Row(['Hz', '500', '1000', '2000', '3000', '4000', '6000', '8000'], [ancho, ancho, ancho, ancho, ancho, ancho, ancho, ancho])
            loPdf.set_borders([0])
            loPdf.set_aligns(['R', 'C', 'C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.Row(['dB (A)', '', '', '2000', '3000', '4000', '6000', '8000'], [ancho, ancho, ancho, ancho, ancho, ancho, ancho, ancho])

            loPdf.set_xy(x, y)
            loPdf.set_borders([0, 0, 0])
            loPdf.set_bolds(['', 'B', 'B'])
            loPdf.Row(['', 'Audición izquierda', '      500  1000 2000 3000 4000 6000 8000'], [ancho, (wr/2-ancho)*0.35, (wr/2-ancho)*0.65])
            loPdf.set_x(x)
            loPdf.set_borders([0])
            loPdf.set_aligns(['R', 'C', 'C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.set_bolds(['', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])
            loPdf.Row(['Hz', '500', '1000', '2000', '3000', '4000', '6000', '8000'], [ancho, ancho, ancho, ancho, ancho, ancho, ancho, ancho])
            loPdf.set_x(x)
            loPdf.set_borders([0])
            loPdf.set_aligns(['R', 'C', 'C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.Row(['dB (A)', '', '', '2000', '3000', '4000', '6000', '8000'], [ancho, ancho, ancho, ancho, ancho, ancho, ancho, ancho])
            #OTOSCOPIA
            loPdf.ln(0.2)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(4, h, 'OTOSCOPIA', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.ln(0.2)
            loPdf.set_borders([0, 1, 0, 0, 1])
            loPdf.set_aligns(['R', 'L', '', 'R', 'L'])
            loPdf.Row(['OD', 'XX', '', 'OI', 'XX'], [0.6, wr/2 - 0.2 - 0.6, 0.4, 0.6, wr/2 - 0.2 - 0.6])
            
            loPdf.add_page()
            #PULMONES
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(4, h, 'PULMONES', 1, 0, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(0.5)
            loPdf.cell(0.8, h, 'Normal', 0, 0, 'R')
            loPdf.cell(0.4, h, 'X', 1, 0, 'C')
            loPdf.cell(0.5)
            loPdf.cell(0.8, h, 'Anormal', 0, 0, 'R')
            loPdf.cell(0.4, h, 'X', 1, 1, 'C')
            
            loPdf.cell(2)
            loPdf.cell(2, h, 'Descripción :', 0, 0, 'R')
            loPdf.cell(w, h, '###', 1, 1, 'L')
            
            loPdf.ln(0.1)
            loPdf.Row(['TORAX :', '', 'CORAZÓN :', ''], [1.4, wr/2 - 1.4, 1.4, wr/2 - 1.4])
            loPdf.ln(0.1)
            loPdf.Row(['Miembros superiores :', ''], [4, wr - 4])
            loPdf.Row(['Miembros inferiores :', ''], [4, wr - 4])
            loPdf.set_borders([1, 1, 0, 1])
            loPdf.Row(['Reflejos Osteo-tendinos', '', 'Marcha :', 'XX'], [4, (wr - 4)*0.5, (wr - 4)*0.1, (wr - 4)*0.4])
            loPdf.set_borders([1, 1, 0, 1])
            loPdf.set_aligns(['L', 'L', 'L', 'C'])
            loPdf.Row(['Columna vertebral :', 'XX', '', 'Tacto Rectal'], [4, (wr - 4)*0.55, (wr - 4)*0.05, (wr - 4)*0.4])
            
            loPdf.cell(2, h, 'Abdomen :', 1, 0, 'L')
            loPdf.cell((wr-4)*0.55 + 2, h, 'XX', 1, 0, 'L')
            loPdf.cell((wr-4)*0.05)
            loPdf.set_xy(loPdf.get_x(), loPdf.get_y() + 0.1)
            loPdf.cell(1.2, h, 'No se hizo', 0, 0, 'R')
            loPdf.cell(0.4, h, 'X', 1, 0, 'C')
            loPdf.cell(0.4)
            loPdf.cell(1.2, h, 'Normal', 0, 0, 'R')
            loPdf.cell(0.4, h, 'X', 1, 0, 'C')
            loPdf.cell(0.4)
            loPdf.cell(1.2, h, 'Anormal', 0, 0, 'R')
            loPdf.cell(0.4, h, 'X', 1, 1, 'C')
            loPdf.ln(0.1)

            loPdf.Row(['Anillos Inguinales', '', 'Hernias', '', 'Várices', ''], [wr*0.13, wr*0.27, wr*0.08, wr*0.22, wr*0.08, wr*0.22])

            loPdf.Row(['Órganos Genitales', '', 'Ganglios :', ''], [wr*0.13, wr*0.37, wr*0.08, wr*0.42])

            loPdf.cell(wr, h, 'Lenguaje, Atención, memoria, orientación, Inteligencia, Afectividad:', 1, 1, 'L')
            loPdf.cell(wr, h, '', 1, 1, 'L')

            #LECTURA DE LA PLACA DE TORAX
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'LECTURA DE LA PLACA DE TORAX', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.ln()
            loPdf.cell(2.4)
            x1 = loPdf.get_x()
            temp_labels = ['N° Rx:', 'Fecha:', 'Calidad:', 'Símbolos:'] #TODO REEMPLAZAR
            for i in range(4):
                loPdf.cell(1.2, h, temp_labels[i], 0, 0, 'R')
                loPdf.cell(2.8, h, 'xx', 1, 1, 'L')
                loPdf.set_x(x1)
            loPdf.ln()
            y1 = loPdf.get_y()
            loPdf.set_xy(x, y)
            loPdf.cell(x1 + 2.9, y1 - y, '', 1, 0, 'C')

            ancho = wr - (x1 + 2.9)
            x = loPdf.get_x()
            loPdf.set_borders([0])
            loPdf.set_aligns(['R', 'L', 'R', 'L'])
            loPdf.Row(['Vértices :\n ', '', 'Senos :\n ', ''], [ancho*0.15, ancho*0.35, ancho*0.15, ancho*0.35])
            loPdf.set_x(x)
            loPdf.set_borders([0])
            loPdf.set_aligns(['R', 'L', 'R', 'L'])
            loPdf.Row(['Campos pulmonares :', '', 'Mediastinos :', ''], [ancho*0.15, ancho*0.35, ancho*0.15, ancho*0.35])
            loPdf.set_x(x)
            loPdf.set_borders([0])
            loPdf.set_aligns(['R', 'L', 'R', 'L'])
            loPdf.Row(['Hilos :', '', 'Silueta cardiovascular :', ''], [ancho*0.15, ancho*0.35, ancho*0.15, ancho*0.35])
            loPdf.set_x(x)
            loPdf.set_borders([0])
            loPdf.set_aligns(['R', 'L'])
            loPdf.Row(['Conclusiones Radiograficas:', ''], [ancho*0.15, ancho*0.85])

            loPdf.ln(0.2)
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.Row(['', '', '', '', '', '', '', '', ''], [wr*0.0909, wr*0.0909, wr*0.0909, wr*0.0909, wr*0.0909, wr*0.0909, wr*0.0909, wr*0.0909, wr*0.0909])
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.Row(['0/0', '1/0', '1/1,1/2', '2/1,2/2,2/3', '3/2,3/3,3/+', 'A,B,C', 'St.'], [wr*0.0909, wr*0.0909, wr*0.0909, wr*0.0909*2, wr*0.0909*2, wr*0.0909, wr*0.0909])
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.Row(['CERO', '1/0', 'UNO', 'DOS', '', 'TRES', 'CUATRO', ''], [wr*0.0909, wr*0.0909, wr*0.0909, wr*0.0909*2, wr*0.0909, wr*0.0909, wr*0.0909, wr*0.0909])

            loPdf.ln(0.2)
            x1 = loPdf.get_x()
            y1 = loPdf.get_y()
            loPdf.multi_cell(wr*0.0909, h, 'Sin neumoconiosis', 0, 'C')
            loPdf.set_xy(x1, y1)
            loPdf.cell(wr*0.0909, h*5, '', 'TLR', 0, 'C')
            x1 = loPdf.get_x()
            y1 = loPdf.get_y()
            loPdf.multi_cell(wr*0.0909, h, 'Imagen radiografica de Exposicion a polvo', 0, 'C')
            loPdf.set_xy(x1, y1)
            loPdf.cell(wr*0.0909, h*5, '', 'TLR', 0, 'C')
            x1 = loPdf.get_x()
            y1 = loPdf.get_y()
            loPdf.multi_cell(wr*0.0909*7, h, 'Con Neumoconiosis', 0, 'C')
            loPdf.set_xy(x1, y1)
            loPdf.cell(wr*0.0909*7, h*5, '', 'TLR', 1, 'C')

            loPdf.cell(wr*0.0909, h, '"NORMAL"', 'BLR', 0, 'C')
            loPdf.cell(wr*0.0909, h, '"SOSPECHA"', 'BLR', 0, 'C')
            loPdf.cell(wr*0.0909*7, h, '', 'BLR', 1, 'C')

            #LABORATORIO
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'LABORATORIO', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['GRUPO SANGUÍNEO', '', 'FACTOR', '', 'Hemoglobina', '', 'gr. %', 'Hematocrito', '', '%', 'Reacciones serológicas a Lúes'], [wr*0.14, wr*0.08, wr*0.08, wr*0.08, wr*0.08, wr*0.08, wr*0.05, wr*0.08, wr*0.08, wr*0.05, wr*0.2])
            
            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.set_borders([0])
            loPdf.Row(['Glucosa', '', 'Colesterol', '', 'Trigliceridos', '', 'HDL', '', 'LDL', '', 'Creatinina', ''], [wr*0.06, wr*0.07, wr*0.07, wr*0.07, wr*0.08, wr*0.07, wr*0.05, wr*0.07, wr*0.05, wr*0.07, wr*0.07, wr*0.07])

            loPdf.set_borders([0])
            loPdf.Row(['Orina', ''], [wr*0.06, wr*0.74])

            loPdf.set_xy(x + wr*0.8, y)
            loPdf.cell(1.5, h, 'Negativo', 0, 0, 'R')
            loPdf.cell(0.4, h, 'X', 1, 1, 'R')
            loPdf.set_x(x + wr*0.8)
            loPdf.cell(1.5, h, 'Positivo', 0, 0, 'R')
            loPdf.cell(0.4, h, 'X', 1, 1, 'R')
            loPdf.set_xy(x + wr*0.8, y)
            loPdf.cell(wr*0.2, h*2, '', 1, 1, 'C')

            #OTROS EXAMENES
            loPdf.ln(h)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'OTROS EXAMENES', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr, h, '', 1, 1, 'L')

            #DIAGNOSTICO MEDICO OCUPACIONAL
            loPdf.ln()
            loPdf.set_bolds(['B', 'B'])
            loPdf.Row(['DIAGNOSTICO MEDICO OCUPACIONAL', 'CIE - 10'], [wr*0.85, wr*0.15])
            loPdf.Row(['1.', 'P', 'D', 'R', ''], [wr*0.79, wr*0.02, wr*0.02, wr*0.02, wr*0.15])
            loPdf.Row(['2.', 'P', 'D', 'R', ''], [wr*0.79, wr*0.02, wr*0.02, wr*0.02, wr*0.15])
            loPdf.Row(['3.', 'P', 'D', 'R', ''], [wr*0.79, wr*0.02, wr*0.02, wr*0.02, wr*0.15])
            
            #APTITUD
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(1.5, h, 'APTO', 1, 0, 'C')
            loPdf.cell(1.5, h, '', 1, 0, 'C')
            loPdf.cell(3.35)
            loPdf.cell(3.7, h, 'APTO CON RESTRICCIONES', 1, 0, 'C')
            loPdf.cell(1.5, h, '', 1, 0, 'C')
            loPdf.cell(3.35)
            loPdf.cell(2, h, 'NO APTO', 1, 0, 'C')
            loPdf.cell(1.5, h, '', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)

            loPdf.ln()
            loPdf.set_bolds(['B', 'B'])
            loPdf.Row(['RECOMENDACIONES', 'RESTRICCIONES'], [wr*0.5, wr*0.5])
            loPdf.Row(['xx', 'xx'], [wr*0.5, wr*0.5])

            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_ficha_medica_rm_312(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_ficha_medica_rm_312_conclusiones(self, p_oPdf, title, text, bool_result):
        wr = p_oPdf._width()
        h = 0.4
        p_oPdf.set_font('Arial', 'B', 6)
        p_oPdf.cell(wr, h, title, 1, 1, 'L')
        p_oPdf.set_font('Arial', '', 6)
        y = p_oPdf.get_y()
        p_oPdf.multi_cell(wr*0.85, h, text, 0, 'J')
        p_oPdf.set_y(y)
        p_oPdf.cell(wr*0.85, h*2, '', 1, 0, 'C')
        x = p_oPdf.get_x()
        result = [' ', 'X'] if int(bool_result) == 1 else ['X', ' ']
        p_oPdf.set_font('Arial', 'B', 6)
        p_oPdf.cell(wr*0.10, h, 'APLICA', 1, 0, 'C')
        p_oPdf.set_font('Arial', '', 6)
        p_oPdf.cell(wr*0.05, h, result[1], 1, 1, 'C')
        p_oPdf.set_x(x)
        p_oPdf.set_font('Arial', 'B', 6)
        p_oPdf.cell(wr*0.10, h, 'NO APLICA', 1, 0, 'C')
        p_oPdf.set_font('Arial', '', 6)
        p_oPdf.cell(wr*0.05, h, result[0], 1, 1, 'C')

    def print_ficha_medica_rm_312(self):
        loPdf  = PYFPDF()
        llOK = self.val_ficha_medica_rm_312()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('FICHA MEDICA RM-312', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'ANTECEDENTES OCUPACIONALES (Ver adjunto Historia Ocupacional', 1, 1, 'C')

            loPdf.ln()
            loPdf.cell(wr, h, 'ANTECEDENTES PATOLOGICOS PERSONALES', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.ln(0.2)

            loPdf.set_border(1)
            loPdf.Row(['Alergias', '', 'Diabetes', '', 'TBC', '', 'Hepatitis B', '', 'H.Col', '', 'Pt. Columna', '', 'Qx.', ''], [wr*0.12, wr*0.02, wr*0.12, wr*0.02, wr*0.13, wr*0.02, wr*0.12, wr*0.02, wr*0.12, wr*0.02, wr*0.13, wr*0.02, wr*0.12, wr*0.02])
            loPdf.Row(['Asma', '', 'HTA', '', 'ITS', '', 'Tifoidea', '', 'Prob CV', '', 'HBP', '', 'Otros', ''], [wr*0.12, wr*0.02, wr*0.12, wr*0.02, wr*0.13, wr*0.02, wr*0.12, wr*0.02, wr*0.12, wr*0.02, wr*0.13, wr*0.02, wr*0.12, wr*0.02])
            loPdf.Row(['Bronquitis', '', 'Neoplasia', '', 'Convulsione', '', 'H.tg', '', 'Atropatía', '', 'Migraña', ''], [wr*0.12, wr*0.02, wr*0.12, wr*0.02, wr*0.13, wr*0.02, wr*0.12, wr*0.02, wr*0.12, wr*0.02, wr*0.13, wr*0.02])

            loPdf.ln(0.2)
            loPdf.Row(['Otros:', ''], [wr*0.15, wr*0.85])
            loPdf.Row(['Quemaduras:', ''], [wr*0.15, wr*0.85])
            loPdf.Row(['Cirugías:', '', 'Intoxicaciones:', ''], [wr*0.15, wr*0.35, wr*0.15, wr*0.35])

            loPdf.ln(0.2)
            loPdf.set_aligns(['C', 'C', 'C', 'C'])
            loPdf.Row(['Hábitos nocivos', 'TIPO', 'CANTIDAD', 'FRECUENCIA'], [wr*0.25, wr*0.25, wr*0.25, wr*0.25])
            loPdf.Row(['Alcohol', '', '', ''], [wr*0.25, wr*0.25, wr*0.25, wr*0.25])
            loPdf.Row(['Tabaco', '', '', ''], [wr*0.25, wr*0.25, wr*0.25, wr*0.25])
            loPdf.Row(['Drogas', '', '', ''], [wr*0.25, wr*0.25, wr*0.25, wr*0.25])
            loPdf.Row(['Medicamentos', '', '', ''], [wr*0.25, wr*0.25, wr*0.25, wr*0.25])

            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'ANTECEDENTES PATOLOGICOS PERSONALES', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['Padre:', '', 'Madre:', '','Hermanos:', '', 'N°', ''], [wr*0.1, wr*0.15, wr*0.1, wr*0.15, wr*0.12, wr*0.28, wr*0.05, wr*0.05])
            loPdf.Row(['Esposo(a):', '', 'Hijos vivos:', '','N°', '','Hijos Fallecidos:', '', 'N°', ''], [wr*0.1, wr*0.15, wr*0.1, wr*0.07, wr*0.05, wr*0.05, wr*0.12, wr*0.26, wr*0.05, wr*0.05])

            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'ABSENTISMO: Enfermedades y Accidentes (asociado a trabajo o no)', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr*0.40, h*2, 'Enfermedad, Accidente', 1, 0, 'C')
            x = loPdf.get_x()
            y = loPdf.get_y() + h
            loPdf.cell(wr*0.20, h, 'Asociado al Trabajo', 1, 0, 'C')
            loPdf.cell(wr*0.20, h*2, 'Año', 1, 0, 'C')
            loPdf.cell(wr*0.20, h*2, 'Días de descanso', 1, 0, 'C')
            loPdf.set_xy(x, y)
            loPdf.cell(wr*0.20/2, h, 'SI', 1, 0, 'C')
            loPdf.cell(wr*0.20/2, h, 'NO', 1, 1, 'C')
            
            loPdf.set_aligns(['L', 'C', 'C', 'C', 'C'])
            loPdf.Row(['', '', '', '', ''], [wr*0.4, wr*0.1, wr*0.1, wr*0.2, wr*0.2])

            loPdf.add_page()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'EVALUACION MEDICA', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)

            loPdf.ln(0.2)
            loPdf.Row(['Anamnesis', ''], [wr*0.15, wr*0.85])

            loPdf.ln(0.2)
            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.multi_cell(wr*0.1, h, 'Examen Clínico', 0, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_xy(x, y)
            loPdf.cell(wr*0.1, h*4, '', 1, 0, 'C')
            x = loPdf.get_x()

            loPdf.set_bolds(['B', '', 'B', '', 'B', '', 'B', ''])
            loPdf.Row(['Triaje', '', 'Triaje', '', 'Triaje', '', 'Triaje', ''], [wr*0.12, wr*0.105, wr*0.12, wr*0.105, wr*0.12, wr*0.105, wr*0.12, wr*0.105])
            loPdf.set_x(x)
            loPdf.set_bolds(['B', '', 'B', '', 'B', '', 'B', ''])
            loPdf.Row(['Triaje', '', 'Triaje', '', 'Triaje', '', 'Triaje', ''], [wr*0.12, wr*0.105, wr*0.12, wr*0.105, wr*0.12, wr*0.105, wr*0.12, wr*0.105])
            loPdf.set_x(x)
            loPdf.set_bolds(['B', '', 'B', '', 'B', ''])
            loPdf.Row(['Triaje', '', 'Triaje', '', 'Triaje', ''], [wr*0.12, wr*0.105, wr*0.12, wr*0.105, wr*0.12, wr*0.105])
            loPdf.set_x(x)
            loPdf.Row(['Otros :', ''], [wr*0.12, wr*0.78])

            loPdf.ln()
            loPdf.Row(['Ectoscopia :', ''], [wr*0.15, wr*0.85])
            loPdf.Row(['Estado Mental :', ''], [wr*0.15, wr*0.85])

            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'EXAMEN FISICO', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.ln(0.2)
            loPdf.set_bolds(['B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row(['Órgano o Sistema', 'Sin Hallazgos', 'Hallazgos'], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Piel', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Cabello', '', ''], [wr*0.2, wr*0.2, wr*0.6])

            loPdf.cell(wr*0.2, h*6, 'Ojos y Anexos', 1, 0, 'L')
            loPdf.cell(wr*0.2, h*6, '', 1, 0, 'L')
            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.cell((wr*0.6)*0.20, h*2, 'Agudeza visual', 1, 0, 'C')
            loPdf.cell((wr*0.6)*0.05, h, 'OD', 1, 0, 'C')
            loPdf.cell((wr*0.6)*0.10, h, '', 1, 0, 'L')
            loPdf.cell((wr*0.6)*0.05, h, 'OI', 1, 0, 'C')
            loPdf.cell((wr*0.6)*0.10, h, '', 1, 0, 'L')
            loPdf.cell((wr*0.6)*0.20, h*2, 'Con Correctores', 1, 0, 'C')
            loPdf.cell((wr*0.6)*0.05, h, 'OD', 1, 0, 'C')
            loPdf.cell((wr*0.6)*0.10, h, '', 1, 0, 'L')
            loPdf.cell((wr*0.6)*0.05, h, 'OI', 1, 0, 'C')
            loPdf.cell((wr*0.6)*0.10, h, '', 1, 1, 'L')
            loPdf.set_x(x)
            loPdf.cell((wr*0.6)*0.20)
            loPdf.cell((wr*0.6)*0.30, h, '', 1, 0, 'L')
            loPdf.cell((wr*0.6)*0.20)
            loPdf.cell((wr*0.6)*0.30, h, '', 1, 1, 'L')
            loPdf.set_x(x)
            loPdf.cell((wr*0.6)*0.20, h*2, 'Fondo de Ojo', 1, 0, 'C')
            loPdf.cell((wr*0.6)*0.30, h*2, '', 1, 0, 'L')
            loPdf.cell((wr*0.6)*0.20, h*2, 'Visión de Colores', 1, 0, 'C')
            loPdf.cell((wr*0.6)*0.30, h*2, '', 1, 1, 'L')
            loPdf.set_x(x)
            loPdf.cell((wr*0.6)*0.20, h*2, 'Visión de Profundidad', 1, 0, 'C')
            loPdf.cell((wr*0.6)*0.80, h*2, '', 1, 1, 'L')

            loPdf.Row(['Oídos', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Nariz', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Boca', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Faringe', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Cuello', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Aparato Respiratorio', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Aparato Cardiovascular', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Aparato Digestivo', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Aparato Genitourinario', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Aparato Locomotor', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Marcha', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Columna', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Miembros Superiores', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Miembros Inferiores', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Sistema Linfático', '', ''], [wr*0.2, wr*0.2, wr*0.6])
            loPdf.Row(['Sistema Nervioso', '', ''], [wr*0.2, wr*0.2, wr*0.6])

            loPdf.ln()
            self.print_ficha_medica_rm_312_conclusiones(loPdf, 'CONCLUSIONES DE EVALUACION PSICOLOGICA', '###', 0)
            loPdf.ln()
            self.print_ficha_medica_rm_312_conclusiones(loPdf, 'CONCLUSIONES RADIOGRAFICAS', '###', 0)
            
            loPdf.add_page()
            self.print_ficha_medica_rm_312_conclusiones(loPdf, 'HALLAZGOS PATOLOGICOS DE LABORATORIO', '###', 0)
            loPdf.ln()
            self.print_ficha_medica_rm_312_conclusiones(loPdf, 'CONCLUSION AUDIOMETRIA', '###', 0)
            loPdf.ln()
            self.print_ficha_medica_rm_312_conclusiones(loPdf, 'CONCLUSION ESPIROMETRIA', '###', 0)
            loPdf.ln()
            self.print_ficha_medica_rm_312_conclusiones(loPdf, 'CONLUSIONES ODONTOLOGIA', '###', 0)
            loPdf.ln()
            self.print_ficha_medica_rm_312_conclusiones(loPdf, 'CONCLUSIONES EKG', '###', 0)
            loPdf.ln()

            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'OTROS', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr, h, '', 1, 1, 'L')

            loPdf.ln()
            loPdf.set_bolds(['B', 'B'])
            loPdf.set_aligns(['L', 'C'])
            loPdf.Row(['DIAGNOSTICO MEDICO OCUPACIONAL', 'CIE - 10'], [wr*0.85, wr*0.15])
            loPdf.Row(['1.', 'P', 'D', 'R', ''], [wr*0.79, wr*0.02, wr*0.02, wr*0.02, wr*0.15])
            loPdf.Row(['2.', 'P', 'D', 'R', ''], [wr*0.79, wr*0.02, wr*0.02, wr*0.02, wr*0.15])
            loPdf.Row(['3.', 'P', 'D', 'R', ''], [wr*0.79, wr*0.02, wr*0.02, wr*0.02, wr*0.15])

            loPdf.ln()
            loPdf.set_bolds(['B'])
            loPdf.Row(['OTROS DIAGNOSTICOS'], [wr])
            loPdf.Row(['4.', 'P', 'D', 'R', ''], [wr*0.79, wr*0.02, wr*0.02, wr*0.02, wr*0.15])
            loPdf.Row(['5.', 'P', 'D', 'R', ''], [wr*0.79, wr*0.02, wr*0.02, wr*0.02, wr*0.15])
            loPdf.Row(['6.', 'P', 'D', 'R', ''], [wr*0.79, wr*0.02, wr*0.02, wr*0.02, wr*0.15])

            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(1.5, h, 'APTO', 1, 0, 'C')
            loPdf.cell(1.5, h, '', 1, 0, 'C')
            loPdf.cell(3.35)
            loPdf.cell(3.7, h, 'APTO CON RESTRICCIONES', 1, 0, 'C')
            loPdf.cell(1.5, h, '', 1, 0, 'C')
            loPdf.cell(3.35)
            loPdf.cell(2, h, 'NO APTO', 1, 0, 'C')
            loPdf.cell(1.5, h, '', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)

            loPdf.ln()
            loPdf.set_bolds(['B', 'B'])
            loPdf.set_aligns(['C', 'C'])
            loPdf.Row(['RECOMENDACIONES', 'RESTRICCIONES'], [wr*0.5, wr*0.5])
            loPdf.Row(['xx', 'xx'], [wr*0.5, wr*0.5])
            
            loPdf.image("./src/PDF/assets/9999.jpg" , 1, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 9, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_rayos_x(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_rayos_x(self):
        loPdf  = PYFPDF()
        llOK = self.val_rayos_x()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('IMAGENOLOGIA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'INFORME RADIOGRAFICO CON METODOLOGIA OIT')
            loPdf.set_border(1)
            #CALIDAD RADIOGRAFICA
            y = loPdf.get_y()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.2, h, self.paDatos[0]['CIMPRIM'], 1, 0, 'C')
            loPdf.set_font('Arial', '', 6)
            x = loPdf.get_x()
            cont = 1
            for i in self.paDatos[0]['MTABLA']:
                loPdf.cell(wr*0.03, h, str(cont), 1, 0, 'C')
                xselect = self.x_select_check(i, self.paDatos[0]['CRESULT'])
                loPdf.cell(wr*0.12, h, xselect[0], 1, 0, 'L')
                loPdf.cell(wr*0.05, h, xselect[1], 1, 1, 'C')
                loPdf.set_x(x)
                cont += 1
            #CAUSA
            loPdf.set_xy(x + wr*0.2 + wr*0.05, y)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.1, h, self.paDatos[1]['CIMPRIM'], 1, 0, 'C')
            loPdf.set_font('Arial', '', 6)
            x = loPdf.get_x()
            y = loPdf.get_y()
            cont = 1
            ancho = wr*0.17
            for i in self.paDatos[1]['MTABLA']:
                loPdf.cell(wr*0.03, h, str(cont), 1, 0, 'C')
                xselect = self.x_select_check(i, self.paDatos[1]['CRESULT'])
                loPdf.cell(ancho, h, xselect[0], 1, 0, 'L')
                loPdf.cell(wr*0.05, h, xselect[1], 1, 1, 'C')
                loPdf.set_x(x)
                if cont == 4:
                    ancho = wr*0.12
                    x = x + wr*0.25
                    loPdf.set_xy(x, y)
                cont += 1
            #COMENTARIO SOBRE DEFECTOS TECNICOS
            loPdf.ln(h + 0.2)
            loPdf.Row([self.paDatos[2]['CIMPRIM'], self.paDatos[2]['CRESULT']], [wr*0.15, wr*0.85])
            #ANORMALIDADES PARENQUIMATOSAS
            loPdf.ln(0.2)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'ANORMALIDADES PARENQUIMATOSAS (SI no hay anormalidades parenquimatosas pase a A. pleurales)', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            #2.1
            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.multi_cell(wr*0.25, h, '2.1 Zonas afectadas (Marque Todas las zonas afectadas).', 0, 'L')
            loPdf.set_xy(x, y)
            loPdf.cell(wr*0.25, h*4, '', 1, 2, 'C')
            
            loPdf.set_bolds(['B', 'B', 'B'])
            loPdf.set_borders([0])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row(['', 'Derecha', 'Izquierda'], [wr*0.25/3, wr*0.25/3, wr*0.25/3])
            loPdf.set_bolds(['B'])
            xbool1 = self.x_boolean_checkbox(self.paDatos[3]['CRESULT'])
            xbool2 = self.x_boolean_checkbox(self.paDatos[4]['CRESULT'])
            loPdf.set_aligns(['L', 'C', 'C'])
            loPdf.Row(['Superior', xbool1[0], xbool2[0]], [wr*0.25/3, wr*0.25/3, wr*0.25/3])
            loPdf.set_bolds(['B'])
            xbool1 = self.x_boolean_checkbox(self.paDatos[5]['CRESULT'])
            xbool2 = self.x_boolean_checkbox(self.paDatos[6]['CRESULT'])
            loPdf.set_aligns(['L', 'C', 'C'])
            loPdf.Row(['Medio', xbool1[0], xbool2[0]], [wr*0.25/3, wr*0.25/3, wr*0.25/3])
            loPdf.set_bolds(['B'])
            xbool1 = self.x_boolean_checkbox(self.paDatos[7]['CRESULT'])
            xbool2 = self.x_boolean_checkbox(self.paDatos[8]['CRESULT'])
            loPdf.set_aligns(['L', 'C', 'C'])
            loPdf.Row(['Inferior', xbool1[0], xbool2[0]], [wr*0.25/3, wr*0.25/3, wr*0.25/3])
            #2.2
            x = x + wr*0.25
            loPdf.set_xy(x, y)
            loPdf.multi_cell(wr*0.25, h, '2.2' + self.paDatos[9]['CIMPRIM'] + '.', 0, 'L')
            loPdf.set_xy(x, y)
            loPdf.cell(wr*0.25, h*4, '', 1, 2, 'C')
            
            xselect = self.x_select(self.paDatos[9]['MTABLA'])
            cont = 0
            for i in xselect:
                loPdf.cell(wr*0.25/3, h, i, 1, 0, 'C')
                if cont in [2, 5, 8]:
                    loPdf.ln()
                    loPdf.set_x(x)
                cont += 1
            
            #2.3
            x = x + wr*0.25
            loPdf.set_xy(x, y)
            loPdf.multi_cell(wr*0.25, h, '2.3 Forma y tamaño (Consúltelas radiografías estándar, se requiere dos símbolos: marque un primario y un secundario)', 0, 'L')
            loPdf.set_xy(x, y)
            loPdf.cell(wr*0.25, h*4, '', 1, 2, 'C')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.25/2, h, 'Primaria', 1, 0, 'C')
            x1 = loPdf.get_x()
            loPdf.cell(wr*0.25/2, h, 'Secundaria', 1, 0, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.ln()
            y1 = loPdf.get_y()
            loPdf.set_x(x)

            xselect = self.x_select(self.paDatos[10]['MTABLA'])
            cont = 0
            for i in xselect:
                loPdf.cell(wr*0.25/4, h, i, 1, 0, 'C')
                if cont in [1, 3]:
                    loPdf.ln()
                    loPdf.set_x(x)
                cont += 1
            loPdf.set_xy(x1, y1)
            xselect = self.x_select(self.paDatos[11]['MTABLA'])
            cont = 0
            for i in xselect:
                loPdf.cell(wr*0.25/4, h, i, 1, 0, 'C')
                if cont in [1, 3]:
                    loPdf.ln()
                    loPdf.set_x(x1)
                cont += 1

            #2.4
            x = x + wr*0.25
            loPdf.set_xy(x, y)
            loPdf.multi_cell(wr*0.25, h, '2.4 Opacidades grandes (Marque 0 si no hay ninguna o marque A, B o C)', 0, 'L')
            loPdf.set_xy(x, y)
            loPdf.cell(wr*0.25, h*4, '', 1, 2, 'C')
            
            loPdf.cell(wr*0.25/3)
            xselect = self.x_select(self.paDatos[12]['MTABLA'])
            for i in xselect:
                loPdf.cell(wr*0.25/3, h, i, 1, 2, 'C')
            
            #ANOMALIDADES PLEURALES
            loPdf.ln(0.2)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.8, h, 'ANORMALIDADES PLEURALES (sI no hay anormalidades pase a simbolos)', 1, 0, 'L')
            xboolean = self.x_boolean_multi(self.paDatos[13]['CRESULT'])
            loPdf.cell(wr*0.06, h, 'Si', 0, 0, 'R')
            loPdf.cell(wr*0.04, h, xboolean[0], 1, 0, 'C')
            loPdf.cell(wr*0.06, h, 'No', 0, 0, 'R')
            loPdf.cell(wr*0.04, h, xboolean[1], 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)

            loPdf.cell(wr, h, '3.1 Placas pleurales (0=Ninguna, D=Hemitorax derecho, I=Hemitorax izquierdo)', 1, 1, 'L')
            
            #SITIO
            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.multi_cell((wr-0.3)*0.25, h, 'Sitio\n(marque las casillas adecuadas)', 0, 'C')
            loPdf.set_xy(x, y)
            loPdf.cell((wr-0.3)*0.25, h*8, '', 1, 2, 'C')
            
            for i in range(14, 18):
                xselect = self.x_select(self.paDatos[i]['MTABLA'])
                loPdf.set_aligns(['L', 'C', 'C', 'C'])
                loPdf.Row([self.paDatos[i]['CIMPRIM'], xselect[0], xselect[1], xselect[2]], [(wr-0.3)*0.25*0.4, (wr-0.3)*0.25*0.2, (wr-0.3)*0.25*0.2, (wr-0.3)*0.25*0.2])
            yf = loPdf.get_y()
            #CALIFICACIONES
            x = x + (wr-0.3)*0.25 + 0.1
            loPdf.set_xy(x, y)
            loPdf.multi_cell((wr-0.3)*0.15, h, 'Calificaciones\n(marque)', 0, 'C')
            loPdf.set_xy(x, y)
            loPdf.cell((wr-0.3)*0.15, h*8, '', 1, 2, 'C')

            for i in range(18, 22):
                xselect = self.x_select(self.paDatos[i]['MTABLA'])
                if i == 18:
                    xselect[0] += '\n '
                    xselect[1] += '\n '
                    xselect[2] += '\n '
                loPdf.set_aligns(['C', 'C', 'C'])
                loPdf.Row([xselect[0], xselect[1], xselect[2]], [(wr-0.3)*0.15*0.33, (wr-0.3)*0.15*0.34, (wr-0.3)*0.15*0.33])
                loPdf.set_x(x)
            #EXTENSION
            x = x + (wr-0.3)*0.15 + 0.1
            loPdf.set_xy(x, y)
            loPdf.multi_cell((wr-0.3)*0.30, h, 'Extension (pared Torácica combinada para placas de perfil y de frente)', 0, 'C')
            loPdf.set_xy(x, y)
            loPdf.cell((wr-0.3)*0.30, h*2, '', 1, 2, 'C')

            loPdf.cell((wr-0.3)*0.30*0.1, h*2, '1', 1, 0, 'C')
            y1 = loPdf.get_y()
            loPdf.multi_cell((wr-0.3)*0.30*0.9, h, '< 1/4 de la pared lateral de tórax', 0, 'C')
            loPdf.set_xy(x + (wr-0.3)*0.30*0.1, y1)
            loPdf.cell((wr-0.3)*0.30*0.9, h*2, '', 1, 1, 'C')
            loPdf.set_x(x)
            
            loPdf.cell((wr-0.3)*0.30*0.1, h*2, '2', 1, 0, 'C')
            y1 = loPdf.get_y()
            loPdf.multi_cell((wr-0.3)*0.30*0.9, h, 'Entre 1/4 y 1/2 de la pared lateral de tórax', 0, 'C')
            loPdf.set_xy(x + (wr-0.3)*0.30*0.1, y1)
            loPdf.cell((wr-0.3)*0.30*0.9, h*2, '', 1, 1, 'C')
            loPdf.set_x(x)

            loPdf.cell((wr-0.3)*0.30*0.1, h*2, '3', 1, 0, 'C')
            y1 = loPdf.get_y()
            loPdf.multi_cell((wr-0.3)*0.30*0.9, h, '> 1/2 de la pared lateral de tórax', 0, 'C')
            loPdf.set_xy(x + (wr-0.3)*0.30*0.1, y1)
            loPdf.cell((wr-0.3)*0.30*0.9, h*2, '', 1, 1, 'C')
            loPdf.set_x(x)

            y1 = loPdf.get_y()
            xselect = self.x_select(self.paDatos[22]['MTABLA'])
            loPdf.set_aligns(['C', 'C'])
            loPdf.Row([xselect[0], 'D'], [(wr-0.3)*0.30*0.25, (wr-0.3)*0.30*0.25])
            loPdf.set_x(x)
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([xselect[1], xselect[2], xselect[3]], [(wr-0.3)*0.30*0.16, (wr-0.3)*0.30*0.17, (wr-0.3)*0.30*0.17])

            x = x + (wr-0.3)*0.30*0.5
            loPdf.set_xy(x, y1)
            xselect = self.x_select(self.paDatos[23]['MTABLA'])
            loPdf.set_aligns(['C', 'C'])
            loPdf.Row([xselect[0], 'I'], [(wr-0.3)*0.30*0.25, (wr-0.3)*0.30*0.25])
            loPdf.set_x(x)
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([xselect[1], xselect[2], xselect[3]], [(wr-0.3)*0.30*0.16, (wr-0.3)*0.30*0.17, (wr-0.3)*0.30*0.17])
            
            #ANCHO
            x = x + (wr-0.3)*0.15 + 0.1
            loPdf.set_xy(x, y)
            loPdf.multi_cell((wr-0.3)*0.30, h, 'Ancho (opcional) ancho mínimo exigido 3 mm', 0, 'C')
            loPdf.set_xy(x, y)
            loPdf.cell((wr-0.3)*0.30, h*2, '', 1, 2, 'C')

            loPdf.cell((wr-0.3)*0.30*0.1, h*2, 'a', 1, 0, 'C')
            y1 = loPdf.get_y()
            loPdf.multi_cell((wr-0.3)*0.30*0.9, h, 'De 3 a 5 mm', 0, 'C')
            loPdf.set_xy(x + (wr-0.3)*0.30*0.1, y1)
            loPdf.cell((wr-0.3)*0.30*0.9, h*2, '', 1, 1, 'C')
            loPdf.set_x(x)
            
            loPdf.cell((wr-0.3)*0.30*0.1, h*2, 'b', 1, 0, 'C')
            y1 = loPdf.get_y()
            loPdf.multi_cell((wr-0.3)*0.30*0.9, h, 'De 5 a 10 mm', 0, 'C')
            loPdf.set_xy(x + (wr-0.3)*0.30*0.1, y1)
            loPdf.cell((wr-0.3)*0.30*0.9, h*2, '', 1, 1, 'C')
            loPdf.set_x(x)

            loPdf.cell((wr-0.3)*0.30*0.1, h*2, 'c', 1, 0, 'C')
            y1 = loPdf.get_y()
            loPdf.multi_cell((wr-0.3)*0.30*0.9, h, 'Mayor a 10 mm', 0, 'C')
            loPdf.set_xy(x + (wr-0.3)*0.30*0.1, y1)
            loPdf.cell((wr-0.3)*0.30*0.9, h*2, '', 1, 1, 'C')
            loPdf.set_x(x)

            y1 = loPdf.get_y()
            xselect = self.x_select(self.paDatos[24]['MTABLA'])
            loPdf.set_aligns(['C'])
            loPdf.Row(['D'], [(wr-0.3)*0.30*0.5])
            loPdf.set_x(x)
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([xselect[0], xselect[1], xselect[2]], [(wr-0.3)*0.30*0.16, (wr-0.3)*0.30*0.17, (wr-0.3)*0.30*0.17])

            x = x + (wr-0.3)*0.30*0.5
            loPdf.set_xy(x, y1)
            xselect = self.x_select(self.paDatos[25]['MTABLA'])
            loPdf.set_aligns(['C'])
            loPdf.Row(['I'], [(wr-0.3)*0.30*0.5])
            loPdf.set_x(x)
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([xselect[0], xselect[1], xselect[2]], [(wr-0.3)*0.30*0.16, (wr-0.3)*0.30*0.17, (wr-0.3)*0.30*0.17])

            #OBLITERACION ANGULO COSTOFRENICO
            loPdf.set_y(yf)
            xselect = self.x_select(self.paDatos[26]['MTABLA'])
            loPdf.set_aligns(['L', 'C', 'C', 'C'])
            loPdf.Row([self.paDatos[26]['CIMPRIM'], xselect[0], xselect[1], xselect[2]], [(wr-0.3)*0.4+0.1, wr*0.05, wr*0.05, wr*0.05])

            #ENGROSAMIENTO DIFUSO DE LA PLEURA
            loPdf.ln(0.2)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'ENGROSAMIENTO DIFUSO DE LA PLEURA (0=Ninguna, D=Hemitorax derecho, I=Hemitorax izquierdo)', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)

            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.06, h, 'De perfil', 1, 1, 'L')
            loPdf.cell(wr*0.06, h, '', 1, 1, 'L')
            loPdf.cell(wr*0.06, h, 'De frente', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            #Pared toracica
            x = x + wr*0.06
            loPdf.set_xy(x, y)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.15, h, 'Pared Torácica', 1, 2, 'C')
            loPdf.set_font('Arial', '', 6)
            xselect = self.x_select(self.paDatos[27]['MTABLA'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([xselect[0], xselect[1], xselect[2]], [wr*0.15/3, wr*0.15/3, wr*0.15/3])
            loPdf.set_x(x)
            loPdf.Row(['', '', ''], [wr*0.15/3, wr*0.15/3, wr*0.15/3])
            loPdf.set_x(x)
            xselect = self.x_select(self.paDatos[28]['MTABLA'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([xselect[0], xselect[1], xselect[2]], [wr*0.15/3, wr*0.15/3, wr*0.15/3])
            #Calcificacion
            x = x + wr*0.15
            loPdf.set_xy(x, y)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.15, h, 'Calcificación', 1, 2, 'C')
            loPdf.set_font('Arial', '', 6)
            xselect = self.x_select(self.paDatos[29]['MTABLA'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([xselect[0], xselect[1], xselect[2]], [wr*0.15/3, wr*0.15/3, wr*0.15/3])
            loPdf.set_x(x)
            loPdf.Row(['', '', ''], [wr*0.15/3, wr*0.15/3, wr*0.15/3])
            loPdf.set_x(x)
            xselect = self.x_select(self.paDatos[30]['MTABLA'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([xselect[0], xselect[1], xselect[2]], [wr*0.15/3, wr*0.15/3, wr*0.15/3])
            yf = loPdf.get_y()
            #Extension
            x = x + wr*0.15 + wr*0.020
            loPdf.set_xy(x, y)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.30, h, 'Extensión', 1, 2, 'C')
            loPdf.set_font('Arial', '', 6)
            y1 = loPdf.get_y()
            xselect = self.x_select(self.paDatos[31]['MTABLA'])
            loPdf.set_aligns(['C', 'C'])
            loPdf.Row([xselect[0], 'D'], [wr*0.15/2, wr*0.15/2])
            loPdf.set_x(x)
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([xselect[1], xselect[2], xselect[3]], [wr*0.15/3, wr*0.15/3, wr*0.15/3])
            
            x = x + wr*0.15
            loPdf.set_xy(x, y1)
            xselect = self.x_select(self.paDatos[32]['MTABLA'])
            loPdf.set_aligns(['C', 'C'])
            loPdf.Row([xselect[0], 'I'], [wr*0.15/2, wr*0.15/2])
            loPdf.set_x(x)
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([xselect[1], xselect[2], xselect[3]], [wr*0.15/3, wr*0.15/3, wr*0.15/3])

            #Ancho
            x = x + wr*0.15 + wr*0.020
            loPdf.set_xy(x, y)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.30, h, 'Ancho', 1, 2, 'C')
            loPdf.set_font('Arial', '', 6)
            y1 = loPdf.get_y()
            xselect = self.x_select(self.paDatos[33]['MTABLA'])
            loPdf.set_aligns(['C'])
            loPdf.Row(['D'], [wr*0.15])
            loPdf.set_x(x)
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([xselect[0], xselect[1], xselect[2]], [wr*0.15/3, wr*0.15/3, wr*0.15/3])
            
            x = x + wr*0.15
            loPdf.set_xy(x, y1)
            xselect = self.x_select(self.paDatos[34]['MTABLA'])
            loPdf.set_aligns(['C'])
            loPdf.Row(['I'], [wr*0.15])
            loPdf.set_x(x)
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row([xselect[0], xselect[1], xselect[2]], [wr*0.15/3, wr*0.15/3, wr*0.15/3])
            
            #SIMBOLOS
            loPdf.set_y(yf)
            loPdf.ln(0.2)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.8, h, 'SIMBOLOS', 1, 0, 'L')
            xboolean = self.x_boolean_multi(self.paDatos[35]['CRESULT'])
            loPdf.cell(wr*0.06, h, 'Si', 0, 0, 'R')
            loPdf.cell(wr*0.04, h, xboolean[0], 1, 0, 'C')
            loPdf.cell(wr*0.06, h, 'No', 0, 0, 'R')
            loPdf.cell(wr*0.04, h, xboolean[1], 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr, h, '(Rodee con un círculo la respuesta adecuada, si rodea od, escriba a continuación un COMENTARIO)', 1, 1, 'L')
            y = loPdf.get_y()
            for i in range(36, 64):
                xboolean = self.x_boolean_checkbox(self.paDatos[i]['CRESULT'])
                loPdf.cell(wr/15, h, self.paDatos[i]['CIMPRIM'] + ('   (' + xboolean[0] + ')' if xboolean[0] == 'X' else ''), 1, 0, 'C')
                if i == 49:
                    loPdf.ln()
            loPdf.set_xy(loPdf.get_x(), y)
            xboolean = self.x_boolean_checkbox(self.paDatos[64]['CRESULT'])
            loPdf.cell(wr/15, h*2, self.paDatos[64]['CIMPRIM'] + ('   (' + xboolean[0] + ')' if xboolean[0] == 'X' else ''), 1, 1, 'C')

            loPdf.ln(0.2)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'COMENTARIOS', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr, h, '', 1, 1, 'L')

            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_evaluacion_osteomioarticular(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_evaluacion_osteomioarticular(self):
        loPdf  = PYFPDF()
        llOK = self.val_evaluacion_osteomioarticular()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()
            
            self.print_title(loPdf, 'EVALUACION OSTEOMIARTICULAR ARTICULACIONES')
            loPdf.set_border(1)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'EXPLORACION CLINICA ESPECIFICA', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)
            #COLUMNA VERTEBRAL DESVIACION DEL EJE ANTERO - POSTERIOR
            loPdf.ln()
            ancho = wr*0.85
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(ancho, h, 'COLUMNA VERTEBRAL DESVIACION DEL EJE ANTERO - POSTERIOR', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_bolds(['B', 'B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C', 'C'])
            loPdf.Row(['CURVAS FISIOLÓGICAS ANT-POST', 'NORMAL', 'AUMENTADA', 'DISMINUIDA'], [ancho*0.4, ancho*0.2, ancho*0.2, ancho*0.2])
            labels = ['Cervical', 'Dorsal', 'Lumbar']
            for i in range(3):
                loPdf.set_aligns(['L', 'C', 'C', 'C'])
                loPdf.set_bolds(['B'])
                loPdf.Row([labels[i], 'x', 'y', 'z'], [ancho*0.4, ancho*0.2, ancho*0.2, ancho*0.2])
            #DESVIACIONES DEL EJE LATERAL
            loPdf.ln()
            ancho = wr*0.85
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(ancho, h, 'DESVIACIONES DEL EJE LATERAL', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_bolds(['B', 'B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C', 'C'])
            loPdf.Row(['EJE LATERAL', 'NORMAL', 'CONCAVIDAD DERECHA', 'CONCAVIDAD IZQUIERDA'], [ancho*0.2, ancho*0.2, ancho*0.3, ancho*0.3])
            labels = ['Dorsal', 'Lumbar']
            for i in range(2):
                loPdf.set_aligns(['L', 'C', 'C', 'C'])
                loPdf.set_bolds(['B'])
                loPdf.Row([labels[i], 'x', 'y', 'z'], [ancho*0.2, ancho*0.2, ancho*0.3, ancho*0.3])
            #MOVILIDAD - DOLOR
            loPdf.ln()
            ancho = wr
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(ancho, h, 'MOVILIDAD - DOLOR', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_bolds(['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.Row(['', 'FLEXIÓN', 'EXTENSIÓN', 'LATERALIZACIÓN IZQUIERDA', 'LATERALIZACIÓN DERECHA', 'ROTACIÓN DERECHA', 'ROTACIÓN IZQUIERDA', 'IRRADIACIÓN'], [ancho*0.12, ancho*0.12, ancho*0.12, ancho*0.14, ancho*0.14, ancho*0.12, ancho*0.12, ancho*0.12])
            labels = ['Cervical', 'Dorso lumbar']
            for i in range(2):
                loPdf.set_aligns(['L', 'C', 'C', 'C', 'C', 'C', 'C', 'C'])
                loPdf.set_bolds(['B'])
                loPdf.Row([labels[i], '1', '2', '3', '4', '5', '6', '7'], [ancho*0.12, ancho*0.12, ancho*0.12, ancho*0.14, ancho*0.14, ancho*0.12, ancho*0.12, ancho*0.12])
            #EXPLORACION
            loPdf.ln()
            ancho = wr*0.6
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(ancho, h, 'EXPLORACION', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_bolds(['B', 'B'])
            loPdf.set_aligns(['C', 'C'])
            loPdf.Row(['SIGNOS', 'PRESENTE O NO'], [ancho*0.7, ancho*0.3])
            loPdf.set_font('Arial', 'B', 6)
            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.cell(ancho*0.45, h*2, 'Lasegüe', 1, 2, 'L')
            loPdf.cell(ancho*0.45, h*2, 'Test de Schober', 1, 2, 'L')
            x = x + ancho*0.45
            loPdf.set_xy(x, y)
            for i in range(2):
                loPdf.cell(ancho*0.25, h, 'Derecho', 1, 2, 'L')
                loPdf.cell(ancho*0.25, h, 'Izquierdo', 1, 2, 'L')
            loPdf.set_font('Arial', '', 6)
            x = x + ancho*0.25
            loPdf.set_xy(x, y)
            for i in range(4):
                loPdf.cell(ancho*0.3, h, 'x', 1, 2, 'C')
            #PALPACION
            loPdf.ln()
            ancho = wr*0.7
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(ancho, h, 'PALPACION', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_bolds(['B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row(['', 'Apófisis espinosas dolorosas', 'Contractura muscular'], [ancho*0.3, ancho*0.35, ancho*0.35])
            labels = ['Columna cervical', 'Columna dorsal', 'Columna lumbar']
            for i in range(2):
                loPdf.set_aligns(['L', 'C', 'C'])
                loPdf.set_bolds(['B'])
                loPdf.Row([labels[i], '1', '2'], [ancho*0.3, ancho*0.35, ancho*0.35])
            #ARTICULACIONES MOVILIDAD - DOLOR
            loPdf.ln()
            ancho = wr*0.7
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(ancho, h, 'ARTICULACIONES MOVILIDAD - DOLOR', 1, 1, 'C')

            loPdf.cell(ancho*0.15, h*2, 'Articulación', 1, 0, 'C')
            loPdf.cell(ancho*0.05, h*2, '', 1, 0, 'C')
            loPdf.set_font('Arial', '', 6)

            ancho_celda = ancho*0.8 / 12
            x = loPdf.get_x()
            loPdf.set_bolds(['B', 'B', 'B', 'B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.Row(['Abducción', 'Aducción', 'Flexión', 'Extens.', 'Rot. Ext.', 'Rot. Int.'], [ancho_celda*2, ancho_celda*2, ancho_celda*2, ancho_celda*2, ancho_celda*2, ancho_celda*2])
            loPdf.set_x(x)
            loPdf.set_bolds(['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'])
            loPdf.Row(['SI', 'NO', 'SI', 'NO', 'SI', 'NO', 'SI', 'NO', 'SI', 'NO', 'SI', 'NO'], [ancho_celda, ancho_celda, ancho_celda, ancho_celda, ancho_celda, ancho_celda, ancho_celda, ancho_celda, ancho_celda, ancho_celda, ancho_celda, ancho_celda])
            y = loPdf.get_y()
            labels = ['Hombro', 'Codo', 'Muñeca', 'Cadera', 'Rodilla', 'Tobillo']
            loPdf.set_font('Arial', 'B', 6)
            for i in range(6):
                loPdf.cell(ancho*0.15, h*2, labels[i], 1, 0, 'L')
                loPdf.cell(ancho*0.05, h, 'Dch.', 1, 2, 'L')
                loPdf.cell(ancho*0.05, h, 'Izq.', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            x = loPdf.get_x() + ancho * 0.2
            loPdf.set_xy(x, y)
            
            for i in range(72):
                xbool = ['X', ' ']
                loPdf.cell(ancho_celda, h, xbool[0], 1, 0, 'C')
                loPdf.cell(ancho_celda, h, xbool[1], 1, 0, 'C')
                if (i+1) % 6 == 0:
                    loPdf.ln()
                    loPdf.set_x(x)
            #EXPLORACION
            loPdf.add_page()
            ancho = wr*0.45
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'EXPLORACION', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            x = loPdf.get_x()
            y = loPdf.get_y()
            loPdf.set_bolds(['B', 'B'])
            loPdf.set_aligns(['C', 'C'])
            loPdf.Row(['TEST', 'PRESENTE O NO'], [ancho*0.7, ancho*0.3])
            y1 = loPdf.get_y()
            labels = ['Test de Phalen', 'Test de Tinel']
            for i in range(2):
                loPdf.set_font('Arial', 'B', 6)
                loPdf.cell(ancho*0.4, h*2, labels[i], 1, 0, 'L')
                loPdf.set_font('Arial', '', 6)
                loPdf.cell(ancho*0.3, h, 'Derecho', 1, 2, 'L')
                loPdf.cell(ancho*0.3, h, 'Izquierdo', 1, 1, 'L')
            loPdf.set_xy(x + ancho*0.7, y1)
            for i in range(4):
                loPdf.cell(ancho*0.3, h, 'x', 1, 2, 'C')

            x = x + wr*0.55
            loPdf.set_xy(x, y)
            loPdf.set_bolds(['B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row(['', 'VARO', 'VALGO'], [ancho*0.5, ancho*0.25, ancho*0.25])
            loPdf.set_x(x)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(ancho*0.25, h*2, 'Codo', 1, 0, 'L')
            loPdf.set_font('Arial', '', 6)
            x1 = loPdf.get_x()
            loPdf.set_aligns(['L', 'C', 'C'])
            loPdf.Row(['Derecho', '1', '2'], [ancho*0.25, ancho*0.25, ancho*0.25])
            loPdf.set_x(x1)
            loPdf.set_aligns(['L', 'C', 'C'])
            loPdf.Row(['Izquierdo', '1', '2'], [ancho*0.25, ancho*0.25, ancho*0.25])
            
            loPdf.set_x(x)
            loPdf.set_bolds(['B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row(['', 'CAVO', 'PLANO'], [ancho*0.5, ancho*0.25, ancho*0.25])
            loPdf.set_x(x)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(ancho*0.25, h*2, 'Pie', 1, 0, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_aligns(['L', 'C', 'C'])
            loPdf.Row(['Derecho', '1', '2'], [ancho*0.25, ancho*0.25, ancho*0.25])
            loPdf.set_x(x1)
            loPdf.set_aligns(['L', 'C', 'C'])
            loPdf.Row(['Izquierdo', '1', '2'], [ancho*0.25, ancho*0.25, ancho*0.25])

            #SISTEMA MOTOR
            loPdf.ln()
            ancho = wr*0.5
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(ancho, h, 'SISTEMA MOTOR', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_bolds(['B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row(['TEST', 'NORMAL', 'ANORMAL'], [ancho*0.4, ancho*0.3, ancho*0.3])
            labels = ['Maniobra de Bare', 'Maniobra de Mingazini']
            for i in range(2):
                loPdf.set_aligns(['L', 'C', 'C'])
                loPdf.set_bolds(['B'])
                loPdf.Row([labels[i], '1', '2'], [ancho*0.4, ancho*0.3, ancho*0.3])
            
            loPdf.set_bolds(['', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.set_borders([0])
            loPdf.Row(['', 'PRESENTE', 'AUSENTE'], [ancho*0.4, ancho*0.3, ancho*0.3])
            labels = ['Mov. Involuntarios', 'Atrofia Muscular', 'Asimetría Muscular', 'Hipotomia Muscular', 'Hipertonia Muscular']
            for i in range(5):
                loPdf.set_aligns(['L', 'C', 'C'])
                loPdf.set_bolds(['B'])
                loPdf.Row([labels[i], '1', '2'], [ancho*0.4, ancho*0.3, ancho*0.3])
            
            loPdf.set_bolds(['', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.set_borders([0])
            loPdf.Row(['', 'NORMAL', 'ANORMAL'], [ancho*0.4, ancho*0.3, ancho*0.3])
            labels = ['Fuerza Muscular']
            for i in range(1):
                loPdf.set_aligns(['L', 'C', 'C'])
                loPdf.set_bolds(['B'])
                loPdf.Row([labels[i], '1', '2'], [ancho*0.4, ancho*0.3, ancho*0.3])
            #COORDINACION
            loPdf.ln()
            ancho = wr*0.5
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(ancho, h, 'COORDINACION', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.set_bolds(['B', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row(['DISMETRIAS', 'NORMAL', 'ANORMAL'], [ancho*0.4, ancho*0.3, ancho*0.3])
            labels = ['Prueba dedo - nariz', 'Prueba dedo - talón', 'Prueba Talón Rodilla']
            for i in range(3):
                loPdf.set_aligns(['L', 'C', 'C'])
                loPdf.set_bolds(['B'])
                loPdf.Row([labels[i], '1', '2'], [ancho*0.4, ancho*0.3, ancho*0.3])
            
            loPdf.set_bolds(['', 'B', 'B'])
            loPdf.set_aligns(['C', 'C', 'C'])
            loPdf.Row(['', 'PRESENTE', 'AUSENTE'], [ancho*0.4, ancho*0.3, ancho*0.3])
            labels = ['Signo de Romberg', 'Nistagmus']
            for i in range(2):
                loPdf.set_aligns(['L', 'C', 'C'])
                loPdf.set_bolds(['B'])
                loPdf.Row([labels[i], '1', '2'], [ancho*0.4, ancho*0.3, ancho*0.3])
            #HALLAZGOS
            loPdf.ln()
            loPdf.set_bolds(['B', 'B'])
            loPdf.set_aligns(['C', 'C'])
            loPdf.Row(['HALLAZGOS', 'CIE-10'], [wr*0.9, wr*0.1])
            loPdf.Row(['xx', 'yy'], [wr*0.9, wr*0.1])
            #RECOMENDACIONES Y PLAN DE ACCION
            loPdf.ln()
            loPdf.set_bolds(['B'])
            loPdf.set_aligns(['C'])
            loPdf.Row(['RECOMENDACIONES Y PLAN DE ACCION'], [wr])
            loPdf.Row(['xx'], [wr])
            #SIGNOS Y SINTOMAS
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.2, h, 'SIGNOS Y SINTOMAS', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            labels = ['Ausencia de signos y síntomas.',
                        'Dolor en reposo y/o existencia de sintomatología sugestiva.',
                        'Grado 1 más contractura y/o dolor a la movilización.',
                        'Grado 2 más dolor a la palpación y/o percusión.',
                        'Grado 3 más limitación funcional evidente clínicamente.']
            for i in range(5):
                loPdf.set_aligns(['C', 'C'])
                loPdf.set_bolds(['', 'B'])
                loPdf.Row(['X', 'Grado ' + str(i), labels[i]], [wr*0.03, wr*0.12, wr*0.55])
            
            #VALORACION DE LA APTITUD MEDICO - LABORAL
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.7, h, 'VALORACION DE LA APTITUD MEDICO - LABORAL', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.ln(0.1)
            loPdf.cell(wr*0.13, h, 'Apto sin restricciones', 0, 0, 'L')
            loPdf.cell(0.6, h, 'X', 1, 0, 'C')
            loPdf.cell(wr*0.20, h, 'Apto con restricciones', 0, 0, 'R')
            loPdf.cell(0.6, h, 'X', 1, 1, 'C')
            loPdf.ln(0.1)
            loPdf.cell(wr*0.13, h, 'No Apto', 0, 0, 'L')
            loPdf.cell(0.6, h, 'X', 1, 0, 'C')
            loPdf.cell(wr*0.20, h, 'En Observación', 0, 0, 'R')
            loPdf.cell(0.6, h, 'X', 1, 1, 'C')

            #OBSERVACIONES
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr, h, 'OBSERVACIONES', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['x'], [wr])

            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_nutricion(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_nutricion(self):
        loPdf  = PYFPDF()
        llOK = self.val_nutricion()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'INFORME NUTRICIONAL')
            loPdf.set_border(1)
            #TRIAJE
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.5, h, 'TRIAJE', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            temp_labels = ['P.A. :', 'F.R. :', 'F.C. :', 'T º :','PESO :', 'TALLA :', 'SAT. O2 :', 'I.M.C. :','CINTURA :', 'CADERA :', 'ICC :']
            temp_labels_m = ['mmHg','x minuto','x minuto','º C','Kg.','metros','%','Kg/m2','cm.','cm.','']
            for i in range(11):
                loPdf.cell(wr*0.10, h, temp_labels[i], 1, 0, 'R')
                loPdf.cell(wr*0.08, h, 'x', 'TLB', 0, 'C')
                loPdf.cell(wr*0.07, h, temp_labels_m[i], 'TRB', 0, 'L')
                if i in [3, 7, 10]:
                    loPdf.ln()
            #ANTECEDENTES
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.5, h, 'ANTECEDENTES', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['x'], [wr]) 
            #ANAMNESIS
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.5, h, 'ANAMNESIS', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['x'], [wr]) 
            #DIAGNOSTICO
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.5, h, 'DIAGNOSTICO', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['x'], [wr]) 
            #RECOMENDACIONES
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.5, h, 'RECOMENDACIONES', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['x'], [wr]) 
            
            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_antecedentes_ocupacionales(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_antecedentes_ocupacionales(self):
        loPdf  = PYFPDF()
        llOK = self.val_antecedentes_ocupacionales()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            self.print_title(loPdf, 'ANTECEDENTES OCUPACIONALES')
            #IMPRIMIR CABECERA
            loPdf.set_font('Arial', 'B', 6)
            anchos = [(wr*0.65)*0.1, (wr*0.65)*0.1, (wr*0.65)*0.12, (wr*0.65)*0.1, (wr*0.65)*0.12, (wr*0.65)*0.12, (wr*0.65)*0.1, (wr*0.65)*0.1, (wr*0.35)*0.2, (wr*0.35)*0.8/7, (wr*0.35)*0.8/7, (wr*0.35)*0.8/7, (wr*0.35)*0.8/7, (wr*0.35)*0.8/7, (wr*0.35)*0.8/7, (wr*0.35)*0.8/7, (wr*0.65)*0.14]
            labels = ['Fecha Inicio', 'Fecha Fin', 'Empresa', 'Altitud(msnm)', 'Área de Trabajo', 'Ocupación', 'Tiempo de trabajo', '', 'Riesgos', 'Tipo de EPP']
            cont = 0
            for i in range(10):
                if i in [6, 8]:
                    y = loPdf.get_y()
                    if i == 6:
                        labels_m = ['Subsuelo', 'Superficie']
                    else:
                        labels_m = ['Ruido', 'Polvo', 'Ergo.', 'Vibra.', 'Elect.', 'Quimi.', 'Otros']
                    ancho = sum(anchos[cont : cont + len(labels_m)])
                    loPdf.cell(ancho, h, labels[i], 1, 2, 'C')
                    for lbl in labels_m:
                        loPdf.cell(anchos[cont], h, lbl, 1, 0, 'C')
                        cont += 1
                    loPdf.set_xy(loPdf.get_x(), y)
                else:
                    loPdf.cell(anchos[cont], h*2, labels[i], 1, 0, 'C')
                    cont += 1
            loPdf.set_font('Arial', '', 6)
            loPdf.ln()

            #DETALLES
            cont = 0
            for i in range(8):
                loPdf.cell(anchos[cont], h*2, 'x', 1, 0, 'L')
                cont += 1
            y = loPdf.get_y()
            x = loPdf.get_x()

            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(anchos[cont], h, 'Hrs de exp.', 1, 0, 'C')
            loPdf.set_font('Arial', '', 6)
            cont += 1
            for i in range(7):
                loPdf.cell(anchos[cont], h, 'x', 1, 0, 'L')
                cont += 1
            
            cont -= 8
            loPdf.ln()
            loPdf.set_x(x)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(anchos[cont], h, '% uso de EPP', 1, 0, 'C')
            loPdf.set_font('Arial', '', 6)
            cont += 1
            for i in range(7):
                loPdf.cell(anchos[cont], h, 'x', 1, 0, 'L')
                cont += 1
            
            loPdf.set_xy(loPdf.get_x(), y)
            loPdf.cell(anchos[cont], h*2, 'x', 1, 1, 'L')



            ####prueba otra linea de detalles
            cont = 0
            for i in range(8):
                loPdf.cell(anchos[cont], h*2, 'x', 1, 0, 'L')
                cont += 1
            y = loPdf.get_y()
            x = loPdf.get_x()
            
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(anchos[cont], h, 'Hrs de exp.', 1, 0, 'C')
            loPdf.set_font('Arial', '', 6)
            cont += 1
            for i in range(7):
                loPdf.cell(anchos[cont], h, 'x', 1, 0, 'L')
                cont += 1
            
            cont -= 8
            loPdf.ln()
            loPdf.set_x(x)
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(anchos[cont], h, '% uso de EPP', 1, 0, 'C')
            loPdf.set_font('Arial', '', 6)
            cont += 1
            for i in range(7):
                loPdf.cell(anchos[cont], h, 'x', 1, 0, 'L')
                cont += 1
            
            loPdf.set_xy(loPdf.get_x(), y)
            loPdf.cell(anchos[cont], h*2, 'x', 1, 1, 'L')


            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_oftalmologia_basica(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_oftalmologia_basica(self):
        loPdf  = PYFPDF()
        llOK = self.val_oftalmologia_basica()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('OFTALMOLOGIA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()
            #ANTECEDENTES
            self.print_title(loPdf, 'EXAMEN OFTALMOLOGICO')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.4, h, 'ANTECEDENTES', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.ln(0.2)
            labels = ['Diabetes', 'Cirugía ocular', 'Exp. Sustancia química', 'Hipertensión', 'Trauma ocular', 'Glaucoma']
            for i in range(6):
                loPdf.cell(2.5, h, labels[i], 0, 0, 'L')
                loPdf.cell(0.4, h, 'X', 1, 0, 'C')
                loPdf.cell(1, h, '', 0, 0, 'C')
                if i in [2, 5]:
                    loPdf.ln()
            loPdf.ln(0.2)
            loPdf.cell(2.9, h, 'Correctores oculares', 0, 0, 'L')
            loPdf.cell(0.5, h, 'SI', 0, 0, 'L')
            loPdf.cell(0.4, h, 'X', 1, 0, 'C')
            loPdf.cell(0.5)
            loPdf.cell(0.6, h, 'NO', 0, 0, 'L')
            loPdf.cell(0.4, h, 'X', 1, 1, 'C')
            loPdf.ln(0.2)
            loPdf.cell(2.9, h, 'Última refracción', 0, 0, 'L')
            loPdf.cell(6, h, 'x', 1, 1, 'L')

            #AGUDEZA VISUAL
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.13, h*2, 'AGUDEZA VISUAL', 1, 0, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr*0.13*2, h, 'SIN CORRECTORES', 1, 0, 'C')
            loPdf.cell(wr*0.13*2, h, 'CON CORRECTORES', 1, 1, 'C')
            loPdf.cell(wr*0.13)
            loPdf.cell(wr*0.13, h, 'OJO DERECHO', 1, 0, 'C')
            loPdf.cell(wr*0.13, h, 'OJO IZQUIERDO', 1, 0, 'C')
            loPdf.cell(wr*0.13, h, 'OJO DERECHO', 1, 0, 'C')
            loPdf.cell(wr*0.13, h, 'OJO IZQUIERDO', 1, 1, 'C')

            loPdf.cell(wr*0.13, h, 'VISION DE LEJOS', 1, 0, 'L')
            loPdf.cell(wr*0.13, h, '1', 1, 0, 'C')
            loPdf.cell(wr*0.13, h, '2', 1, 0, 'C')
            loPdf.cell(wr*0.13, h, '3', 1, 0, 'C')
            loPdf.cell(wr*0.13, h, '4', 1, 1, 'C')

            loPdf.cell(wr*0.13, h, 'VISION DE CERCA', 1, 0, 'L')
            loPdf.cell(wr*0.13*2, h, '1', 1, 0, 'C')
            loPdf.cell(wr*0.13*2, h, '2', 1, 1, 'C')
            #PATOLOGIA
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.4, h, 'PATOLOGIA', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.ln(0.2)
            labels = ['No patología ocular relevante:','Ptosis palpebral :','Pterigion :','Cataratas :','Otro :']
            for i in range(5):
                loPdf.cell(3, h, labels[i], 0, 0, 'R')
                if i != 4:
                    loPdf.cell(1, h, 'x', 1, 1, 'C')
                else:
                    loPdf.cell(3, h, 'xx', 1, 1, 'L')
            #VISION DE COLORES (TEST DE ISHIHARA)
            loPdf.set_border(1)
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.4, h, 'VISION DE COLORES (TEST DE ISHIHARA)', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['###'], [wr])
            #VISION ESTEREOSCOPICA
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.4, h, 'VISION ESTEREOSCOPICA', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['###'], [wr])
            #OTROS
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.4, h, 'OTROS', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['###'], [wr])
            #DIAGNOSTICO / CONCLUSION
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.4, h, 'DIAGNOSTICO / CONCLUSION', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['###'], [wr])
            #INDICACIONES
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.4, h, 'INDICACIONES', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['###'], [wr])

            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False
    
    def val_oftalmologia_especializada(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_oftalmologia_especializada(self):
        loPdf  = PYFPDF()
        llOK = self.val_oftalmologia_especializada()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('OFTALMOLOGIA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()
            
            self.print_title(loPdf, 'EXAMEN OFTALMOLOGICO')
            loPdf.set_border(1)
            #ANTECEDENTES
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.35, h, 'ANTECEDENTES', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['##'], [wr])

            #CORRECTORES OCULARES
            loPdf.ln()
            loPdf.cell(1.8, h, 'Correctores oculares', 0, 0, 'L')
            loPdf.cell(1, h, 'SI', 0, 0, 'R')
            loPdf.cell(0.5, h, 'x', 1, 0, 'C')
            loPdf.cell(1, h, 'NO', 0, 0, 'R')
            loPdf.cell(0.5, h, 'x', 1, 0, 'C')

            loPdf.cell(1)
            loPdf.cell(2, h, 'Última refracción', 0, 0, 'L')
            loPdf.cell(3, h, '##', 1, 1, 'L')

            #AGUDEZA VISUAL
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr/7, h*2, 'AGUDEZA VISUAL', 1, 0, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr/7*2, h, 'SIN CORRECTORES', 1, 0, 'C')
            loPdf.cell(wr/7*2, h, 'CON CORRECTORES', 1, 0, 'C')
            loPdf.cell(wr/7*2, h, 'CON AGUJERO ESTENOPEICO', 1, 1, 'C')
            loPdf.cell(wr/7)
            loPdf.cell(wr/7, h, 'OJO DERECHO', 1, 0, 'C')
            loPdf.cell(wr/7, h, 'OJO IZQUIERDO', 1, 0, 'C')
            loPdf.cell(wr/7, h, 'OJO DERECHO', 1, 0, 'C')
            loPdf.cell(wr/7, h, 'OJO IZQUIERDO', 1, 0, 'C')
            loPdf.cell(wr/7, h, 'OJO DERECHO', 1, 0, 'C')
            loPdf.cell(wr/7, h, 'OJO IZQUIERDO', 1, 1, 'C')

            loPdf.cell(wr/7, h, 'VISION DE LEJOS', 1, 0, 'L')
            loPdf.cell(wr/7, h, '1', 1, 0, 'C')
            loPdf.cell(wr/7, h, '2', 1, 0, 'C')
            loPdf.cell(wr/7, h, '3', 1, 0, 'C')
            loPdf.cell(wr/7, h, '4', 1, 0, 'C')
            loPdf.cell(wr/7, h, '5', 1, 0, 'C')
            loPdf.cell(wr/7, h, '6', 1, 1, 'C')

            loPdf.cell(wr/7, h, 'VISION DE CERCA', 1, 0, 'L')
            loPdf.cell(wr/7*2, h, '1', 1, 0, 'C')
            loPdf.cell(wr/7*2, h, '2', 1, 0, 'C')
            loPdf.cell(wr/7*2, h, '3', 1, 1, 'C')

            #REFRACCION
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.16, h, 'REFRACCION', 1, 0, 'C')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(wr*0.16, h, 'ESFERICO', 1, 0, 'C')
            loPdf.cell(wr*0.16, h, 'CILINDRICO', 1, 0, 'C')
            loPdf.cell(wr*0.16, h, 'EJE', 1, 0, 'C')
            loPdf.cell(wr*0.16, h, 'DIP', 1, 1, 'C')

            loPdf.cell(wr*0.16, h, 'LEJOS OJO DERECHO', 1, 0, 'L')
            loPdf.cell(wr*0.16, h, '1', 1, 0, 'C')
            loPdf.cell(wr*0.16, h, '2', 1, 0, 'C')
            loPdf.cell(wr*0.16, h, '3', 1, 0, 'C')
            loPdf.cell(wr*0.16, h, '4', 1, 1, 'C')

            loPdf.cell(wr*0.16, h, 'LEJOS OJO IZQUIERDO', 1, 0, 'L')
            loPdf.cell(wr*0.16, h, '1', 1, 0, 'C')
            loPdf.cell(wr*0.16, h, '2', 1, 0, 'C')
            loPdf.cell(wr*0.16, h, '3', 1, 0, 'C')
            loPdf.cell(wr*0.16, h, '4', 1, 1, 'C')

            loPdf.cell(wr*0.16, h, 'CERCA AD', 1, 0, 'L')
            loPdf.cell(wr*0.16, h, '1', 1, 0, 'C')
            loPdf.cell(wr*0.16, h, '2', 1, 0, 'C')
            loPdf.cell(wr*0.16, h, '3', 1, 0, 'C')
            loPdf.cell(wr*0.16, h, '4', 1, 1, 'C')

            #VISION DE COLORES (TEST DE ISHIHARA)
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.3, h, 'VISION DE COLORES (TEST DE ISHIHARA)', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['###'], [wr])
            #VISION ESTEREOSCOPICA
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.3, h, 'VISION ESTEREOSCOPICA', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['###'], [wr])
            #OJO SECO (BUT): 10 SEGUNDOS
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.3, h, 'OJO SECO (BUT): 10 SEGUNDOS', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['###'], [wr])
            #TONOMETRIA
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.3, h, 'TONOMETRIA', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['OD', '##'], [wr*0.05, wr*0.95])
            loPdf.Row(['OI', '###'], [wr*0.05, wr*0.95])
            #FONDO DE OJO
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.3, h, 'FONDO DE OJO', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['OD', '##'], [wr*0.05, wr*0.95])
            loPdf.Row(['OI', '###'], [wr*0.05, wr*0.95])
            #DIAGNOSTICO / CONCLUSION
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.3, h, 'DIAGNOSTICO / CONCLUSION', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['###'], [wr])
            #INDICACIONES
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(wr*0.3, h, 'INDICACIONES', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.Row(['###'], [wr])

            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_triaje(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_triaje(self):
        loPdf  = PYFPDF()
        llOK = self.val_triaje()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('TRIAJE', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()

            loPdf.set_font('Arial', '', 6)
            labels = ['Presion Arterial :', 'Frecuencia Respiratoria :', 'Frecuencia Cardiaca :', 'Temperatura :', 'Peso :', 'Talla :', 'Saturacion O2 :', 'Indice de Masa Corporal :', 'Cintura :', 'Cadera :', 'Indice de Cintura Cadera :']
            unidades = ['mmHg', 'x minuto', 'x minuto', 'º C', 'Kg.', 'metros', '%', 'Kg/m2', 'cm.', 'cm.', '']
            for i in range(11):
                loPdf.cell(3, h, labels[i], 0, 0, 'R')
                loPdf.cell(1, h, '#####', 0, 0, 'L')
                loPdf.cell(w, h, unidades[i], 0, 1, 'L')
                
            loPdf.image("./src/PDF/assets/9999.jpg" , 1, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 9, 26, 3, 2)
            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    def val_ecografia(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_ecografia(self):
        loPdf  = PYFPDF()
        llOK = self.val_ecografia()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('IMAGENOLOGIA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()
            
            self.print_title(loPdf, 'INFORME ECOGRAFICO')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(1.2, h, 'ESTUDIO', 1, 0, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(w, h, 'EJEMPLO', 1, 1, 'L')
            loPdf.ln()

            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'INFORME', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(w, h, '', 1, 1, 'L')

            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w,h, 'CONCLUSIONES',1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            if(self.paData['OACTIVI']['MOBSERV'] is not None):
                loPdf.multi_cell(w,h, self.paData['OACTIVI']['MOBSERV'],1, 'L')
            else:
                loPdf.cell(w,h, ' ',1, 1, 'L')

            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False
    
    def val_informe_aptitud_espacio_confinado(self):
        #validar datos para imprimir actividad
        return True
        if not (self.paData):
            self.error='DATA NO DEFINIDA'
            return False
        if not (self.paDatos):
            self.error='DATOS NO DEFINIDOS'
            return False
        li = []
        llOK = self.val_item_list(self.paDatos, 'CCODIND', li)
        if not llOK:
            return False
        return True    

    def print_informe_aptitud_espacio_confinado(self):
        loPdf  = PYFPDF()
        llOK = self.val_informe_aptitud_espacio_confinado()
        if not llOK:
            return False
        try:
            w = 0
            h = 0.4
            loPdf.set_margins(1.3, 1.6, 1.3)
            loPdf.setHeader('MEDICINA', 'M-01-01', self.paData['OPERSON']['CNRODNI']+'000')
            loPdf.alias_nb_pages()
            loPdf.add_page()
            self.Head(loPdf)
            wr=loPdf._width()
            
            self.print_title(loPdf, 'INFORME DE APTITUD DE TRABAJOS EN ESPACIO CONFINADO')
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'RESULTADO DE LA EVALUACION', 1, 1, 'L')
            loPdf.set_font('Arial', '', 6)
            loPdf.cell(w, h, ' ', 1, 1, 'L')
            loPdf.ln()
            loPdf.set_font('Arial', 'B', 6)
            loPdf.cell(w, h, 'APTITUD PARA TRABAJOS EN ESPACIO CONFINADO', 1, 1, 'L')
            loPdf.ln(0.2)
            loPdf.cell(1.5, h, 'APTO', 1, 0, 'C')
            loPdf.cell(1.5, h, '', 1, 0, 'C')
            loPdf.cell(3.35)
            loPdf.cell(3.7, h, 'APTO CON RESTRICCIONES', 1, 0, 'C')
            loPdf.cell(1.5, h, '', 1, 0, 'C')
            loPdf.cell(3.35)
            loPdf.cell(2, h, 'NO APTO', 1, 0, 'C')
            loPdf.cell(1.5, h, '', 1, 1, 'C')
            loPdf.set_font('Arial', '', 6)

            loPdf.image("./src/PDF/assets/9999.jpg" , 17, 26, 3, 2)
            
            loPdf.output(self.lcPath, 'F')
            return True
        except Exception as err: 
            print(err)
            self.error = 'ERROR AL GENERAR ARCHIVO'
            return False

    