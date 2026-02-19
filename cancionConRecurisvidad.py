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

    # ✅ Agregar (se mantiene normal)
    def agregar_cancion(self, nombre, duracion):
        nueva = Cancion(nombre, duracion)

        if self.cabeza is None:
            self.cabeza = self.cola = nueva
        else:
            self.cola.siguiente = nueva
            nueva.anterior = self.cola
            self.cola = nueva

        print("Cancion agregada")

    # ==========================
    # 🔥 MOSTRAR RECURSIVO
    # ==========================

    def mostrar(self):
        if self.cabeza is None:
            print("Lista vacia")
            return
        print("\nLista de canciones:")
        self._mostrar_recursivo(self.cabeza, 1)

    def _mostrar_recursivo(self, nodo, i):
        if nodo is None:
            return
        print(f"{i}. {nodo.nombre} - {nodo.duracion} min")
        self._mostrar_recursivo(nodo.siguiente, i + 1)

    # ==========================
    # 🔥 CONTAR RECURSIVO
    # ==========================

    def contar(self):
        return self._contar_recursivo(self.cabeza)

    def _contar_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_recursivo(nodo.siguiente)

    # ==========================
    # 🔥 OBTENER RECURSIVO
    # ==========================

    def obtener_cancion(self, pos):
        return self._obtener_recursivo(self.cabeza, pos, 1)

    def _obtener_recursivo(self, nodo, pos, contador):
        if nodo is None:
            return None
        if contador == pos:
            return nodo
        return self._obtener_recursivo(nodo.siguiente, pos, contador + 1)

    # ==========================
    # 🔥 ELIMINAR RECURSIVO
    # ==========================

    def eliminar(self, pos):
        self.cabeza = self._eliminar_recursivo(self.cabeza, pos, 1)

    def _eliminar_recursivo(self, nodo, pos, contador):
        if nodo is None:
            return None

        if contador == pos:
            print("Cancion eliminada:", nodo.nombre)

            # Si es el primero
            if nodo.anterior is None:
                if nodo.siguiente:
                    nodo.siguiente.anterior = None
                return nodo.siguiente

            # Si es el ultimo
            if nodo.siguiente is None:
                nodo.anterior.siguiente = None
                self.cola = nodo.anterior
                return nodo

            # Si esta en el medio
            nodo.anterior.siguiente = nodo.siguiente
            nodo.siguiente.anterior = nodo.anterior
            return nodo

        nodo.siguiente = self._eliminar_recursivo(
            nodo.siguiente, pos, contador + 1
        )

        return nodo


class Reproductor:
    def __init__(self, lista):
        self.lista = lista
        self.actual = lista.cabeza

    def reproducir(self):
        if self.actual:
            print("\nReproduciendo:")
            print(self.actual.nombre, "-", self.actual.duracion, "min")
        else:
            print("No hay canciones")


# ==========================
# 🔥 MENU RECURSIVO
# ==========================

def menu(lista, reproductor):
    print("\n======= MENU =======")
    print("1. Ver canciones")
    print("2. Reproducir actual")
    print("3. Elegir cancion")
    print("4. Eliminar cancion")
    print("0. Salir")

    opcion = input("Seleccione opcion: ")

    if opcion == "1":
        lista.mostrar()

    elif opcion == "2":
        reproductor.reproducir()

    elif opcion == "3":
        lista.mostrar()
        num = int(input("Numero: "))
        cancion = lista.obtener_cancion(num)
        if cancion:
            reproductor.actual = cancion
            reproductor.reproducir()
        else:
            print("Numero invalido")

    elif opcion == "4":
        lista.mostrar()
        num = int(input("Numero a eliminar: "))
        lista.eliminar(num)

    elif opcion == "0":
        print("Programa finalizado")
        return

    else:
        print("Opcion incorrecta")

    menu(lista, reproductor)  # 🔥 llamada recursiva


# ==========================
# EJECUCION
# ==========================

lista = ListaReproduccion()

lista.agregar_cancion("Arcangel", 3.5)
lista.agregar_cancion("Bad Bunny", 4.2)
lista.agregar_cancion("Tego Calderon", 3.8)
lista.agregar_cancion("Daddy Yankee", 4.0)

reproductor = Reproductor(lista)

menu(lista, reproductor)
