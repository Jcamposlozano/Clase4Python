import psycopg2

class ConectorPostgres:

    def __init__(self):
        self.database = 'db_datosClase'
        self.user = 'postgres'
        self.password = 'clasepython'
        self.host = '35.239.216.207'
        self.port = '5432'
        self.empleados = []
    
    def descargarEmpleados(self):
        c = psycopg2.connect(database = self.database, user = self.user,password = self.password, host = self.host ,port = self.port)
        try:
            with c.cursor() as cursor:
                sql = str("select nombre,apellido,sueldo,cedula from empresa.empleado;")
                cursor.execute(sql)
                for (nombre,apellido,sueldo,cedula) in cursor:
                    print(nombre)
                    print(apellido)
                    print(sueldo)
                    print(cedula)
                cursor.close()
                c.close()
        finally:
            pass


    def ejecutaConsulta(self, sql):
        try:
            con = psycopg2.connect(database = self.database, user = self.user,password = self.password, host = self.host ,port = self.port)                
            cur = con.cursor()
            cur.execute(str(sql))
            con.commit()
            con.close()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)