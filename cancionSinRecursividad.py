class Cancion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
        self.siguiente = None
        self.anterior = None


class ListaReproduccion:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_cancion(self, nombre, duracion):
        nueva = Cancion(nombre, duracion)

        if self.cabeza is None:
            self.cabeza = self.cola = nueva
        else:
            self.cola.siguiente = nueva
            nueva.anterior = self.cola
            self.cola = nueva

        print("Cancion agregada")

    def mostrar(self):
        if self.cabeza is None:
            print("Lista vacia")
            return

        actual = self.cabeza
        i = 1
        print("\nLista de canciones:")
        while actual:
            print(f"{i}. {actual.nombre} - {actual.duracion} min")
            actual = actual.siguiente
            i += 1

    def obtener_cancion(self, pos):
        actual = self.cabeza
        contador = 1

        while actual:
            if contador == pos:
                return actual
            actual = actual.siguiente
            contador += 1

        return None


class Reproductor:
    def __init__(self, lista):
        self.lista = lista
        self.actual = lista.cabeza

    def reproducir(self):
        if self.actual:
            print("\nReproduciendo:")
            print("Cancion:", self.actual.nombre)
            print("Duracion:", self.actual.duracion, "min")
        else:
            print("No hay canciones")

    def siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            self.reproducir()
        else:
            print("No hay siguiente cancion")

    def anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            self.reproducir()
        else:
            print("No hay cancion anterior")

    def elegir(self, pos):
        cancion = self.lista.obtener_cancion(pos)
        if cancion:
            self.actual = cancion
            self.reproducir()
        else:
            print("Numero invalido")


lista = ListaReproduccion()

lista.agregar_cancion("arcangel", 3.5)
lista.agregar_cancion("Bad buuny", 4.2)
lista.agregar_cancion("tego calderon", 3.8)
lista.agregar_cancion("daddy yankee", 4.0)

reproductor = Reproductor(lista)

while True:

    print("\n======= MENU REPRODUCTOR =======")
    print("1. Ver canciones")
    print("2. Reproducir actual")
    print("3. Siguiente cancion")
    print("4. Cancion anterior")
    print("5. Elegir cancion")
    print("6. Agregar cancion")
    print("0. Salir")

    opcion = input("Seleccione opcion: ")

    if opcion == "1":
        lista.mostrar()

    elif opcion == "2":
        reproductor.reproducir()

    elif opcion == "3":
        reproductor.siguiente()

    elif opcion == "4":
        reproductor.anterior()

    elif opcion == "5":
        lista.mostrar()
        try:
            num = int(input("Numero de cancion: "))
            reproductor.elegir(num)
        except ValueError:
            print("Entrada invalida")

    elif opcion == "6":
        nombre = input("Nombre cancion: ")
        try:
            dur = float(input("Duracion (min): "))
            lista.agregar_cancion(nombre, dur)
        except ValueError:
            print("Duracion invalida")

    elif opcion == "0":
        print("Programa finalizado")
        break

    else:
        print("Opcion incorrecta")
