import getpass
from ConectorPostgres import *

class Nomina:

    def __init__(self):
        self.__cedula = None
        self.__diasLiquidados = None
        self.__fechaNomina = None
        self.__salario = None
        self.__salario_Minimo = 877803
        self.__axulio_anio = 102854
        


    def getCedula(self):
        return self.__cedula  

    def getDiasLiquidados(self):
        return self.__diasLiquidados
    
    def getFechaNomina(self):
        return self.__fechaNomina

    def getSalario(self):
        return self.__salario

    def setCedula(self, cedula : str):
        self.__cedula = cedula

    def setDiasLiquidados(self, diasL : int):
        self.__diasLiquidados = diasL

    def setFechaNomina(self, fecha: str):
        self.__fechaNomina = fecha
    
    def setSalario(self, salario: float):
        self.__salario =  salario

    def SalarioDevengado(self):
        return ((self.__salario/30) * self.__diasLiquidados)

    def Auxilio_transporte(self):
        if (self.SalarioDevengado() > self.__salario_Minimo * 2):
            return 0
        else:
            return (self.__axulio_anio / 30) * self.__diasLiquidados

    def Salud(self):
        return (self.SalarioDevengado() - self.Auxilio_transporte()) * 0.04

    def Pension(self):
        return (self.SalarioDevengado() - self.Auxilio_transporte()) * 0.04

    def ejecutaConsultaNomina(self):
        return str("insert into empresa.nomina (cedula,dias_liquidados,salario_devendado"
                    ",salud,pension,auxilio_trasnporte,fechanomina,usuario)"
                    "values ('"
                    + self.getCedula() + "'," + str(self.getDiasLiquidados()) + "," +
                    str(self.SalarioDevengado()) + "," + str(self.Salud()) + "," +
                    str(self.Pension()) + "," +  str(self.Auxilio_transporte()) + ",'" +
                    self.getFechaNomina() + "','" + getpass.getuser() + "');")

    def agregarEmpleado(self):
        c = ConectorPostgres()
        c.ejecutaConsulta(self.ejecutaConsultaNomina())