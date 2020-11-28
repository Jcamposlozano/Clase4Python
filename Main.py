'''
from ConectorPostgres import *

c = ConectorPostgres()
c.descargarEmpleados()
'''
'''
from Empleado import *

e1 = Empleado()
e1.setNombre("JONATHAN")
e1.setApellido("CAMPOS")
e1.setSueldo(5000000)
e1.setCedula("103247325")
e1.agregarEmpleado()
'''

from Nomina import *

n1 = Nomina()
n1.setCedula("103247325")
n1.setDiasLiquidados(30)
n1.setFechaNomina("2020-11-28")
n1.setSalario(1500000)
n1.agregarEmpleado()
