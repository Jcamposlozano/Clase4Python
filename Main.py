'''
from ConectorPostgres import *

c = ConectorPostgres()
c.descargarEmpleados()
'''

from Empleado import *

e1 = Empleado()
e1.setNombre("JONATHAN")
e1.setApellido("CAMPOS")
e1.setSueldo(5000000)
e1.setCedula("103247325")
e1.agregarEmpleado()
