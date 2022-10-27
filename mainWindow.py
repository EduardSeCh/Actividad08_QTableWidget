#from cgitb import text
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from regex import R
from ui_mainWindow import Ui_MainWindow
#incluir clases particlas 
from Actividad05_ClasesyObjetos.particulas import Particulas
from Actividad05_ClasesyObjetos.particula import Particula
class MainWindow(QMainWindow):
    def __init__(self): 
        super(MainWindow, self).__init__() #Contructor de QMainWindow
        #Guardar particulas
        self.particulas = Particulas()
        
        self.ui = Ui_MainWindow()
        #mandar los datos de self.ui a la ventana
        self.ui.setupUi(self)
        # Eventos en botones
        self.ui.pbAgregarInicio.clicked.connect(self.click_agregarInicio)
        self.ui.pbAgregaFinal.clicked.connect(self.click_agregarFinal)
        self.ui.pbMostrar.clicked.connect(self.click_mostrar)
        #Ad Archivo
        self.ui.actionAbrir_archivo.triggered.connect(self.actionOpenFile)
        self.ui.actionGuardar_archivo.triggered.connect(self.actionSaveFile)
        #Table
        self.ui.btnMostrarTabla.clicked.connect(self.mostrarTabla)
    
    @Slot()
    def mostrarTabla(self):
        self.ui.tableWidget.setColumnCount(10)
        headers = ["id","origen_x","origen_y","destino_x",
                  "destino_y","velocidad","red","green","blue","distancia"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)    
        self.ui.tableWidget.setRowCount(len(self.particulas))
        row = 0
        for particula in self.particulas:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tableWidget.setItem(row,0,id_widget)
            self.ui.tableWidget.setItem(row,1,origen_x_widget)
            self.ui.tableWidget.setItem(row,2,origen_y_widget)
            self.ui.tableWidget.setItem(row,3,destino_x_widget)
            self.ui.tableWidget.setItem(row,4,destino_y_widget)
            self.ui.tableWidget.setItem(row,5,velocidad_widget)
            self.ui.tableWidget.setItem(row,6,red_widget)
            self.ui.tableWidget.setItem(row,7,green_widget)
            self.ui.tableWidget.setItem(row,8,blue_widget)
            self.ui.tableWidget.setItem(row,9,distancia_widget)
            
            row += 1
        
    @Slot()
    def actionOpenFile(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,'Exito',
                'Se abrio el archivo'+ubicacion
            )
        else:
            QMessageBox.critical(
                self,'Error',
                'Error al abrir el archivo'+ubicacion
            )
    def actionSaveFile(self):
        #print("Guardar archivo")
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,"Exito","Archivo guardado"+ubicacion
            )
        else:
            QMessageBox.critical(
                self,"Error","No se pudo guardar el archivo"+ ubicacion
            )
    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        #self.particulas.mostrar()
        self.ui.salida.insertPlainText(str(self.particulas))
        
    @Slot() #Guardar los datos obenidos
    def click_agregarInicio(self):
        id = self.ui.leId.text()
        origenx = self.ui.leOrigenx.text()
        origeny = self.ui.leOrigenY.text()
        destinox = self.ui.leDestinoX.text()
        destinoy = self.ui.leDestinoY.text()
        velocidad = self.ui.leVelocidad.text()
        red = self.ui.sbRed.value()
        green = self.ui.sbGreen.value()
        blue = self.ui.sbBlue.value()
        #Crear particla
        particula = Particula(int(id),int(origenx),int(origeny),int(destinox),int(destinoy),int(velocidad),red,green,blue)
        self.particulas.agregar_inicio(particula)
        
    @Slot() #Guardar los datos obenidos
    def click_agregarFinal(self):
        id = self.ui.leId.text()
        origenx = self.ui.leOrigenx.text()
        origeny = self.ui.leOrigenY.text()
        destinox = self.ui.leDestinoX.text()
        destinoy = self.ui.leDestinoY.text()
        velocidad = self.ui.leVelocidad.text()
        red = self.ui.sbRed.value()
        green = self.ui.sbGreen.value()
        blue = self.ui.sbBlue.value()
        #Crear particla
        particulafinal = Particula(int(id),int(origenx),int(origeny),int(destinox),int(destinoy),int(velocidad),red,green,blue)
        self.particulas.agregar_final(particulafinal)