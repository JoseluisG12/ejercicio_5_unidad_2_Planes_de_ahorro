class PlanAhorro:
    cantidaCuoTotales = int(60)
    cantidadCuoLisitar = int(10)

    def __init__(self, codigo, modelo, versionVehiculo, valorVehiculo):
        self.__codigo = int(codigo)
        self.__modelo = modelo
        self.__versionVei = versionVehiculo
        self.__valorVei = float(valorVehiculo)

    @classmethod
    def getcuotas(cls):
        return cls.cantidaCuoTotales
    @classmethod
    def getlisitar(cls):
        return cls.cantidadCuoLisitar

    def valorunaCuota(self):
        return ((self.__valorVei / self.getcuotas()) + self.__valorVei * 0.10)

    def mostrarvehiculo(self):
        print("________________")
        print(self.__codigo)
        print(self.__modelo)
        print(self.__versionVei)
        print(self.__valorVei)
        print(self.getcuotas())
        print(self.getlisitar())

    def actualizarvalor(self):
        print("""
           Plan de ahorro {}
              
        modelo de vehiculo:{}
        version del vehiculo:{}
        """.format(self.__codigo,self.__modelo,self.__versionVei))
        self.__valorVei = float(input("ingrese el valor actual del vehiculo\n"))
    def lisitacion(self):
        print("""
        modelo:{}
        version:{}
        monto para licitar de un solo pago:{}$""".format(self.__modelo,self.__versionVei,float(self.getlisitar() * self.__valorVei)))

    def averiguarvalor(self,valor):

        if valor > self.valorunaCuota():
            print("""
                 Plan de ahorro {}
            modelo:{}
            version:{}""".format(self.__codigo,self.__modelo,self.__versionVei))

    def actualizacoutas(self,Plan):
        if self.__codigo == Plan:
                PlanAhorro.cantidadCuoLisitar = int(input("ingrese la cantidad de cuotas actual para lisitar el vehiculo\n"))
                return True
        return False




