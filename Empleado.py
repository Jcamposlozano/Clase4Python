

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

    def setSueldo(self, sueldo : str):
        self.__sueldo = sueldo    

    def setCedula(self, cedula : str):
        self.__cedula = cedula
  

