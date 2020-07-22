from Dao import daoCrud

class ctrCrud:

    def consultarCrud(self, tabla, opc):
        ob = daoCrud()
        return ob.consultar(tabla, opc)
    
    def ingresarCrud(self, tabla, descripcion_GC, codigo, grupoid, descripcion_PC, naturaleza, estado):
        ob = daoCrud()
        return ob.ingresar(tabla, descripcion_GC, codigo, grupoid, descripcion_PC, naturaleza, estado)
    
    def modificarCrud(self, tabla, descripcion_GC, idgrupo, idplancuenta, codigo, grupoid, descripcion_PC, naturaleza, estado):
        ob = daoCrud()
        return ob.modificar(tabla, descripcion_GC, idgrupo, idplancuenta, codigo, grupoid, descripcion_PC, naturaleza, estado)

    def eliminarCrud(self, tabla, idgrupo, idplancuenta):
        ob = daoCrud()
        return ob.eliminar(tabla, idgrupo, idplancuenta)