import sys
import pymysql


class Conector:
    def __init__(self, server='localhost', usuario='root', password='', basedato='crud'):
        self.__server = server
        self.__usuario = usuario
        self.__password = password
        self.__basedato = basedato
        self.__conn = ""
        self.__conector = ""

    def conectar(self):
        try:
            self.__conn = pymysql.connect(host=self.__server, user=self.__usuario, password=self.__password,
                                          db=self.__basedato)
            self.__conector = self.__conn.cursor()
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
            print("Conexion Fallida", ex)
            sys.exit(1)

    def cerrar(self):
        self.__conn.close()  # cerramos los dos objetos
        self.__conector.close()

    @property
    def conector(self):
        return self.__conector  # esta varible objeto, abre la conexion

    @property
    def conn(self):
        return self.__conn

