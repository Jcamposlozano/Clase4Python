import getpass
from ConectorPostgres import *

class Empleado:

    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__sueldo = None
        self.__cedula = None


    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getSueldo(self):
        return self.__sueldo        

    def getCedula(self):
        return self.__cedula           

    def setNombre(self, nombre : str):
        self.__nombre = nombre

    def setApellido(self, apellido : str):
        self.__apellido = apellido        

    def setSueldo(self, sueldo : float):
        self.__sueldo = sueldo    

    def setCedula(self, cedula : str):
        self.__cedula = cedula
  
    def ejecutaConsulta(self):
        return str("INSERT INTO empresa.empleado (nombre,apellido,sueldo,cedula,usuario) " +
                    "VALUES ('" + self.__nombre + "','" + self.__apellido +
                    "'," + str(self.__sueldo) + "," + str(self.__cedula) + ",'" + getpass.getuser() + "');")

    def agregarEmpleado(self):
        c = ConectorPostgres()
        c.ejecutaConsulta(self.ejecutaConsulta())