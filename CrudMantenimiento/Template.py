from Controlador import ctrCrud


def GrupoCuentas():
    

    opc1 = 0
    try:
        ob = ctrCrud()
        while opc1 != 5:
            print ("-----------------------------------------------------")
            print("-----------Menu Grupo de Cuentas-----------\n")
            tabla = 1
            print("1)Ingresar\n2)Consultar\n3)Modificar\n" +
                  "4)Eliminar\n5)Retornar al Menu Principal\n")
            opc1 = int(
                input("Seleccione una opcion del Menu Grupo de Cuentas\n"))
            if opc1 == 1:
                descripcion_GC = str(
                    input("Ingrese la descricion del Grupo\n"))
                ob.ingresarCrud(tabla, descripcion_GC, None,
                                None, None, None, None)
            elif opc1 == 2:
                ob.consultarCrud('grupo', tabla)
            elif opc1 == 3:
                print("Datos Actuales")
                ob.consultarCrud('grupo', tabla)
                idgrupo = int(input("Ingrese el Id del Grupo a Modificar\n"))
                descripcion_GC = str(input("Ingrese la Nueva Descripcion\n"))
                ob.modificarCrud(tabla, descripcion_GC, idgrupo,
                                 None, None, None, None, None, None)
                print("Datos Modificados")
                ob.consultarCrud('grupo', tabla)
            elif opc1 == 4:
                print("Vista de todos los Datos")
                ob.consultarCrud("grupo", tabla)
                idgrupo = int(input("Ingrese el Id del Grupo a Eliminar\n"))
                ob.eliminarCrud(tabla, idgrupo, None)
                ob.consultarCrud("grupo", tabla)
            elif opc1 == 5:
                break
            elif opc1 != 1 or 2 or 3 or 4 or 5:
                print("Opcion no valida@n")
        print("A salido del Menu Grupo de Cuentas\n")
    except ValueError:
        print("Valor no Valido\n")


def PlanCuentas():
    print("------------------------------------------------")
    opc1 = 0
    try:
        ob = ctrCrud()
        while opc1 != 5:
            print("-----------Menu Plan de Cuentas-----------\n")
            print("1)Ingresar\n2)Consultar\n3)Modificar\n" +
                  "4)Eliminar\n5)Retornar al Menu Principal\n")
            tabla = 2           
            
            opc1 = int(input("Seleccione una opcion del Menu Plan de Cuentas\n"))
            if opc1 == 1:
                codigo = str(input("Ingrese el Codigo\n"))
                grupo = int(input("Ingrese el Grupo de Cuenta\n"))
                descripcion_PC = str(input("Ingrese la Descripcion del Plan de Cuenta\n"))
                naturaleza = str(input("Ingrese la Naturaleza Deudora/Acredora\n"))
                if naturaleza.lower() == "deudora" or naturaleza.lower() == "acredora":
                    naturaleza = naturaleza[0:1].upper()
                else:
                    print("Ingrese bien la Naturaleza\n")
                    break
                estado = str(input("Ingrese el estado de la Cuenta Verdadero/Falso\n"))
                if estado.lower() == "verdadero":
                    estado = True
                elif estado.lower() == "falso":
                    estado = False
                else:
                    print("Ingrese bien el Estado de la Cuenta")
                    break
                ob.ingresarCrud(tabla, None, codigo, grupo, descripcion_PC, naturaleza, estado)
            elif opc1 == 2:
                ob.consultarCrud('plancuenta', tabla)
            elif opc1 == 3:
                print("Datos Actuales\n")
                ob.consultarCrud('plancuenta', tabla)
                print("Ingrese los datos a Modificar segun el Id Plan de Cuenta\n")
                idplancuenta = int(input("Ingrese el Id para modificar\n"))
                codigo = str(input("Ingrese el Codigo a Modificar\n"))
                grupo = int(input("Ingrese el Grupo de Cuenta a Modificar\n"))
                descripcion_PC = str(input("Ingrese la Descripcion del Plan de Cuenta a Modificar\n"))
                naturaleza = str(input("Ingrese la Naturaleza Deudora/Acredora a Modificar\n"))
                if naturaleza.lower() == "deudora" or naturaleza.lower() == "acredora":
                    naturaleza = naturaleza[0:1].upper()
                else:
                    print("Ingrese bien la Naturaleza\n")
                    break
                estado = str(input("Ingrese el estado de la Cuenta Verdadero/Falso a Modificar\n"))
                if estado.lower() == "verdadero":
                    estado = True
                elif estado.lower() == "falso":
                    estado = False
                else:
                    print("Ingrese bien el Estado de la Cuenta")
                    break
                ob.modificarCrud(tabla, None, None, idplancuenta, codigo, grupo, descripcion_PC, naturaleza, estado)
                print("Datos Modificados\n")
                ob.consultarCrud('plancuenta', tabla)
            elif opc1 == 4:
                print("Vista de todos los datos")
                ob.consultarCrud('plancuenta', tabla)
                idplancuenta = int(input("Ingrese el Id del Plan de Cuenta a Eliminar\n"))
                ob.eliminarCrud(tabla, None, idplancuenta)
            elif opc1 == 5:
                break
            elif opc1 != 1 or 2 or 3 or 4 or 5:
                print("Opcion no valida\n")
        print("A salido del Menu Plan de Cuentas\n")
    except ValueError:
        print("Valor no Valido\n")


opcion = 0

try:
    while opcion != 3:
        print("-----------------------------------------")
        print("------Menu Principal------")
        print("1)Grupo de Cuentas\n" +
              "2)Plan de Cuentas\n" +
              "3)Salir\n")
        try:
            opcion = int(input("Seleccione una opcion del Menu: \n"))
            if opcion == 1:
                GrupoCuentas()
            elif opcion == 2:
                PlanCuentas()
            elif (opcion != 1) or (opcion != 2):
                print("Opcion No valida\n")

        except ValueError as ex:
            print("Valor no valido\n")

    print("Acabo esta huevada")

except Exception as ex:
    print("Fallo el Programa")
