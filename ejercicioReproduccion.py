class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos

    def __str__(self):
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return self.titulo + " - " + self.artista + " (" + str(minutos) + ":" + str(segundos).zfill(2) + ")"



class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None

    def esta_vacio(self):
        return self.cabeza is None

    def insertar_final(self, dato):
        nuevo = NodoDoble(dato)

        if self.esta_vacio():
            self.cabeza = nuevo
            self.cola = nuevo
            self.actual = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def eliminar(self, titulo):
        if self.esta_vacio():
            return False

        actual = self.cabeza

        while actual:
            if actual.dato.titulo == titulo:

                if actual == self.cabeza and actual == self.cola:
                    self.cabeza = None
                    self.cola = None
                    self.actual = None

                elif actual == self.cabeza:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None

                elif actual == self.cola:
                    self.cola = actual.anterior
                    self.cola.siguiente = None

                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior

                return True

            actual = actual.siguiente

        return False

    def siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente

    def anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior

    def buscar(self, titulo):
        actual = self.cabeza
        while actual:
            if actual.dato.titulo == titulo:
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        if self.esta_vacio():
            print("Lista vacia")
            return

        actual = self.cabeza

        while actual:
            if actual == self.actual:
                print("▶", actual.dato)
            else:
                print(actual.dato)
            actual = actual.siguiente

    def cancion_actual(self):
        if self.actual:
            print("Sonando:", self.actual.dato)
        else:
            print("No hay canción sonando")


# ===== MENU =====

if __name__ == "__main__":

    lista = ListaDoble()

    while True:

        print("\n1. Agregar canción")
        print("2. Mostrar lista")
        print("3. Canción actual")
        print("4. Siguiente canción")
        print("5. Canción anterior")
        print("6. Eliminar canción")
        print("7. Buscar canción")
        print("0. Salir")

        op = input("Opción: ")

        if op == "1":
            titulo = input("Titulo: ")
            artista = input("Artista: ")
            duracion = int(input("Duracion en segundos: "))

            cancion = Cancion(titulo, artista, duracion)
            lista.insertar_final(cancion)

        elif op == "2":
            lista.mostrar()

        elif op == "3":
            lista.cancion_actual()

        elif op == "4":
            lista.siguiente()

        elif op == "5":
            lista.anterior()

        elif op == "6":
            titulo = input("Titulo a eliminar: ")
            if lista.eliminar(titulo):
                print("Eliminada")
            else:
                print("No encontrada")

        elif op == "7":
            titulo = input("Titulo a buscar: ")
            if lista.buscar(titulo):
                print("Encontrada")
            else:
                print("No encontrada")

        elif op == "0":
            break
