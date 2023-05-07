from Planes import PlanAhorro
def test():
    opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))
    while opc != 0:
        if opc == 1:
            plan = PlanAhorro(120,'x100','2000','3000000')
            plan.mostrarvehiculo()
            plan.actualizarvalor()
            plan.lisitacion()
            valor = int(input("ingresee el valor de una cuota minima que pueda pagar\n"))
            plan.averiguarvalor(valor)
            codigo = int(input("ingrese el codigo 120 para porbar el medoto actualizarcuotas\n"))
            plan.actualizacoutas(codigo)
            print(plan.getlisitar())
            print(plan.getcuotas())

        if opc == 2:
            plan = PlanAhorro('123-abc', 'x100', '2000', '3000000')
            plan.mostrarvehiculo()
            plan.actualizarvalor()
            plan.lisitacion()
            valor = int(input("ingresee el valor de una cuota minima que pueda pagar\n"))
            plan.averiguarvalor(valor)
            codigo = int(input("ingrese el codigo 120 para porbar el medoto actualizarcuotas\n"))
            plan.actualizacoutas(codigo)
            print(plan.getlisitar())
            print(plan.getcuotas())

        opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))
from ManejardoPlanes import lista
if __name__=='__main__':
    opc = input("desea probar los metodos con la funcion test y = si n = no\n")
    if opc == 'y':
        test()
    print("_______main________")
    lista = lista()
    lista.cargadatos()
    b=(int(input("""
           :Menu principal
1-Para actalizar el precio de un vehiculo 
2-Para conocer que vehiculos estan disponibles segun cuanto pueda pagar el cliente
3-Para conocer el monto que se debe entregar de un solo pago para lisitar un auto
4-Para actualizar la cantidad de cuotas a entregar para licitar
5-para mostrar la lista de vehiculos 
0-Para \n""")))#consultar si cambio la variable de clase para un plan cambiaria para todos


    while b != 0:

        if b == 1:
            lista.actualizar()

        if b == 2:
            lista.valordecuota()
        if b == 3:
            lista.averiguarlisitacion()

        if b == 4:
             lista.actualizarlisitacion()

        if b == 5:
            lista.mostrar()
        b = (int(input("""
                   :Menu principal
1-Para actalizar el precio de un vehiculo 
2-Para conocer que vehiculos estan disponibles segun cuanto pueda pagar el cliente
3-Para conocer el monto que se debe entregar de un solo pago para lisitar un auto
4-Para actualizar la cantidad de cuotas a entregar para licitar
5-para mostrar la lista de vehiculos 
0-Para salir\n""")))



