import Planes
from Planes import PlanAhorro
import csv
class lista:
    __Plan = []
    def __init__(self):
        self.__Plan = []

    def cargadatos(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo,delimiter=(';'))
        for fila in reader:
            codigo = fila[0]
            modelo = fila[1]
            version = fila [2]
            valor = fila [3]
            vehiculo = PlanAhorro(codigo,modelo,version,valor)
            self.__Plan.append(vehiculo)
        archivo.close()
    def mostrar(self):
        for i in range(len(self.__Plan)):
            self.__Plan[i].mostrarvehiculo()
    def actualizar(self):

        for i in range(len(self.__Plan)):
            self.__Plan[i].actualizarvalor()

    def valordecuota(self):
        valor = int(input("ingrese el valor de cuota que esta dispuesto a pagar\n"))
        for i in range(len(self.__Plan)):
            self.__Plan[i].averiguarvalor(valor)

    def averiguarlisitacion(self):

        for i in range(len(self.__Plan)):
            self.__Plan[i].lisitacion()

    def actualizarlisitacion(self):
        Plan = int(input("ingrese el plan a cambiar la licitacion\n"))
        band = False
        i = 0
        while i <= (len(self.__Plan)) and band == False:
            band = self.__Plan[i].actualizacoutas(Plan)
            i = i + 1







