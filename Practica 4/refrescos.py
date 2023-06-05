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



class Refrescos(object):
    def __init__(self, _id, _nombre, _clasificacion, _marca, _precio):
        self.id = _id 
        self.nombre = _nombre
        self.clasificacion = _clasificacion
        self.marca = _marca
        self.precio= _precio
        self.historial = []
    def get(self):
        print("ID: {} Nombre: {} Clasificacion: {} Marca: {} Precio: {}".format(self.id,self.nombre, self.clasificacion, self.marca, self.precio))

    def set(self, _nombre, _clasificacion, _marca, _precio):
        self.nombre = _nombre
        self.clasificacion = _clasificacion
        self.marca = _marca
        self.precio= _precio
        print("Actualizacion realizada")
        
def registrarRefresco():
    with conexion.cursor() as cursor:
        print("Registro de bebida")
        nombre = str(input("Ingresa nombre: "))
        clasificacion = str (input("Ingresa clasificacion: "))
        marca = str(input("Ingresa la marca: "))
        precio = str(input("Ingresa el precio: "))
        cursor.execute("insert into Refrescos values('"+nombre+"','"+clasificacion+"','"+marca+"',"+precio+")")
        cursor.commit()
        print("Registro exitoso")

def eliminarRefresco():
    with conexion.cursor() as cursor:
        print("Eliminacion de bebida")
        id = str(input("Ingresa id de bebida a eliminar: "))
        cursor.execute("delete from Refrescos where id="+id+")")
        cursor.commit()
        print("Eliminacion exitosa")

def mostrarRefrescos():
    with conexion.cursor() as cursor:
        cursor.execute("select * from Refrescos")         
        refrescos = cursor.fetchall()
        print("ID\tNombre\tClasificacion\t\tMarca\t\tPrecio")         
        for refresco in refrescos:
            print(str(refresco[0])+"\t"+refresco[1]+"\t"+refresco[2]+"\t"+refresco[3]+"\t"+str(round(refresco[4],2)))
        
def actualizarRefresco():
    with conexion.cursor() as cursor:
        print("Actualizar informacion de la bebida bebida")
        id = str(input("Ingresa id de bebida a actualizar: "))
        nombre = str(input("Ingresa nuevo nombre: "))
        clasificacion = str (input("Ingrese nueva clasificacion: "))
        marca = str(input("Ingresa nueva marca: "))
        precio = str(input("Ingresa nuevo precio: "))
        cursor.execute("update Refrescos set nombre='"+nombre+"' where id="+id)
        cursor.execute("update Refrescos set clasificacion='"+clasificacion+"' where id="+id)
        cursor.execute("update Refrescos set marca='"+marca+"' where id="+id)
        cursor.execute("update Refrescos set precio='"+precio+"' where id="+id)
        cursor.commit()
        print("Actualizacion exitosa")
    
def precioProm():
    with conexion.cursor() as cursor:
        print("Precio promedio de las bebidas")
        cursor.execute("select AVG(precio) from Refrescos")
        refrescos = cursor.fetchall()
        for refresco in refrescos:
            print("El precio promedio de los refrescos es de: $"+str(round(refresco[0],2)))
        
def bebidaspormarca():
    with conexion.cursor() as cursor:
        print("Cantidad de bebidas por marca")
        cursor.execute("select marca, count(id) from Refrescos group by marca")
        refrescos = cursor.fetchall()         
        for refresco in refrescos:
            print("Marca: "+refresco[0]+"\nCantidad de bebidas: "+str(refresco[1]))
        
def bebidasporclasificacion():
    with conexion.cursor() as cursor:
        print("Cantidad de bebidas por clasificacion")
        cursor.execute("select clasificacion, count(id) from Refrescos group by clasificacion")
        refrescos = cursor.fetchall()         
        for refresco in refrescos:
            print("Clasificacion: "+refresco[0]+"\nCantidad de bebidas: "+str(refresco[1]))
       
def salir():
    conexion.close()
    print("Salir del programa")
    exit()
    
def main():
        while True:
            print("             MENU          ")
            print("1.- Consultar bebidas")
            print("2.- Registrar bebidas")
            print("3.- Eliminar bebidas")
            print("4.- Modificar bebidas")
            print("5.- Precio promedio")
            print("6.- Cantidad por marca")
            print("7.- Cantidad por clasificacion")
            print("8.- Salir")
            opcion = int(input("Opcion: "))

            if opcion == 1:
                mostrarRefrescos()
            elif opcion == 2:
                registrarRefresco()
            elif opcion == 3:
                eliminarRefresco()
            elif opcion == 4:
                actualizarRefresco()
            elif opcion == 5:
                precioProm()
            elif opcion == 6:
                bebidaspormarca()
            elif opcion == 7:
                bebidasporclasificacion()
            elif opcion == 8:
                salir()
            

if __name__ == '__main__':
    main()


