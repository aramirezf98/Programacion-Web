import sys
from Conexion import Conector


class daoCrud(Conector):
    def __init__(self):
        super().__init__()

    def consultar(self, tabla, opc):
        result = False
        try:
            print("Mostrando Resultados")
            sql = 'Select * from ' + tabla
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
            if opc == 1:
                print('id Grupo ; Descripcion')
                for grupo in result:
                    print('{:4}) {:4}'.format(grupo[0], grupo[1]))
            else:
                print(
                    "id P_Cuenta ; Codigo ; GrupoId ; Descripcion; Naturaleza ; Estado")
                for plan_cuenta in result:
                    if plan_cuenta[5] == 1:
                        print("{:4}) ; {:4} ; {:4} ; {:4} ; {:4} ; {}".format(
                            plan_cuenta[0], plan_cuenta[1], plan_cuenta[2], plan_cuenta[3], plan_cuenta[4], "True"))
                    else:
                        print("{:4}) ; {:4} ; {:4} ; {:4} ; {:4} ; {}".format(
                            plan_cuenta[0], plan_cuenta[1], plan_cuenta[2], plan_cuenta[3], plan_cuenta[4], "False"))

        except:
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def ingresar(self, tabla, descripcion_GC, codigo, grupoid, descripcion_PC, naturaleza, estado):
        correcto = True
        try:
            if tabla == 1:
                print("Ingresando Grupo de Cuentas")
                sql = 'insert into grupo (descripcion)  values (%s)'
                self.conectar()
                self.conector.execute(sql, (descripcion_GC))
                print("Se ingreso el nuevo grupo de cuentas")
                self.conn.commit()

            elif tabla == 2:
                print("Ingresando Plan de Cuentas")
                sql = 'insert into plancuenta (codigo, grupoid, descripcion, naturaleza, estado) values (%s, %s, %s, %s, %s)'
                self.conectar()
                self.conector.execute(
                    sql, (codigo, grupoid, descripcion_PC, naturaleza, estado))
                print("Se ingreso el nuevo plan de cuentas")
                self.conn.commit()

        except:
            correcto = False
            self.conn.rollback()
            print("Fallo")
        finally:
            self.cerrar()
        return correcto

    def modificar(self, tabla, descripcion_GC, idgrupo, idplancuenta, codigo, grupoid, descripcion_PC, naturaleza, estado):
        correcto = True
        sql = ""
        try:
            if tabla == 1:
                sql = 'Update grupo set descripcion  = %s where idgrupo = %s'
                print('Modificando Grupo de Cuentas')
                self.conectar()
                self.conector.execute(sql, (descripcion_GC, idgrupo))
                self.conn.commit()
            elif tabla == 2:
                sql = 'Update plancuenta set codigo = %s, grupoid = %s, descripcion = %s, naturaleza = %s, estado = %s where idplancuenta = %s'
                print('Modificando Plan de cuentas')
                self.conectar()
                self.conector.execute(sql, (codigo, grupoid, descripcion_PC, naturaleza, estado, idplancuenta))
                self.conn.commit()
        except:
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto


    def eliminar(self, tabla, idgrupo, idplancuenta):
        correcto = True
        try:
            sql = ""
            if tabla == 1:
                sql = 'delete from grupo where idgrupo = %s'
                self.conectar()
                self.conector.execute(sql, (idgrupo))
                self.conn.commit()
                print("Datos Eliminados")
            elif tabla == 2:
                sql = 'delete from plancuenta where idplancuenta = %s'
                self.conectar()
                self.conector.execute(sql, (idplancuenta))
                self.conn.commit()
            
            print("Datos Eliminados")
        except:
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
