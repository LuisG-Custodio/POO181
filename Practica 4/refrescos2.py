listaRefrescos=[]
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
        
        
def registrarRefreso():
        id = int(input("Ingresa tu id: "))
        nombre = str(input("Ingresa nombre: "))
        clasificacion = str (input("Ingresa clasificacion: "))
        marca = str(input("Ingresa la marca: "))
        precio = float(input("Ingresa el precio: "))
        objRefr = Refrescos(id, nombre, clasificacion, marca, precio)
        listaRefrescos.append(objRefr) 
        
def mostrarRefrescos(): 
        print("Lista de refrescos")
        for objRefr in listaRefrescos: 
            objRefr.get()
            
def buscarRefrescos():
    print("Buscar refrescos")
    id = int(input("Ingresa id del refresco a buscar:")) 
    for objRefr in listaRefrescos:
        if id ==objRefr.id:
            objRefr.get() 
            
def eliminarRefrescos():
    print("Eliminar bebida")
    id = int(input("Ingresa id de la bebida a eliminar: "))
    for objRefr in listaRefrescos:
        if id == objRefr.id:
            objRefr.clear()
            print("Bebida Eliminada")
            
def modificarRefrescos():
    print("Modificar datos de bebida")
    id = int(input("Ingresa id de la bebida a modificar: "))
    for objRefr in listaRefrescos:
        if id == objRefr.id:
            nombre = str(input("Ingrese el nuevo nombre: "))
            clasificacion = str(input("Ingrese la nueva clasificacion: "))
            marca = str(input("Ingresa la nueva marca: ")) 
            precio = float(input("Ingresa el nuevo precio: ")) 
            objRefr.set (nombre, clasificacion, marca,precio)
            objRefr.get()
            
def precioprom():
    print("Precio promedio de las bebidas")
    for objRefr in listaRefrescos: 
        objRefr.get()
            

def salir():
    print("Salir del programa")
    exit()


def main():  #main es el metodo principal donde uniremos todos los metodos para que realice diferentes funciones
        while True:
            print("             MENU          ")
            print("1.- Registrar Bebida")
            print("2.- Eliminar Bebida")
            print("3.- Mostrar Bebidas")
            print("4.- Buscar Bebidas")
            print("5.- Editar datos de bebida")
            print("6.- Salir")
            opcion = int(input("Opcion: "))

            if opcion == 1:
                registrarRefreso()
            elif opcion == 2:
                eliminarRefrescos()
            elif opcion == 3:
                mostrarRefrescos()
            elif opcion == 4:
                buscarRefrescos()
            elif opcion == 5:
                modificarRefrescos()
            elif opcion == 6:
                salir()

if __name__ == '__main__':
    main()