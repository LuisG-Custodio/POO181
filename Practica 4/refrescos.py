import pyodbc
direccion_servidor = 'LAPTOP-1NJS76GT\TRYOUT'
nombre_bd = 'Refrescos'
nombre_usuario = 'dba_User'
password = '12345'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("conexion")
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)





with conexion.cursor() as cursor:
        cursor.execute("select * from Refrescos")         
        refrescos = cursor.fetchall()         
        for refresco in refrescos:
            print(refresco)

conexion.close()