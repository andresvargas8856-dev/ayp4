class NodoDoble:
    def __init__(self, dato):
        self.siguiente = None
        self.anterior = None
        
    def esta_vacio(self):
        """Verifica si la lista esta vacia"""
        return self.cabeza is None
    
    def insertar_inicio(self, dato):
        """Insertar un elemento al incio de la lista"""
        nuevo = NodoDoble(dato)
        
        if self.esta_vacio():
            #Lista vacia: cabeza y cola apuntan al nuevo
            self.cabeza = nuevo
            self.cola = nuevo
            
        else:
            #conectar nuevo con la cola actual 
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
            
    def eliminar_inicio(self):
        if self.esta_vacio():
            return None
        
        dato=self.cabeza.dato
        
        if self.cabeza == self.cola:
            self.cabeza=None
            self.cola=None
            
        else:
            self.cola= self.cola.anterior
            self.cola.siguiente = None
        return dato
    
    def recorrer_adelante(self):
        if self.esta_vacio():
            print("Lista vacia")
            return
        
        print("Inicio -> fin:", end=" ")
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.anterior
            print("<-->".join(elementos))
            
    def buscar(self, dato):
        """Busca un elemento de la lista"""
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False
    
    def __len__(self):
        #retorna la cantidad de elementos
        contador=0
        actual=self.cabeza
        while actual:
            contador+=1
            actual=actual.siguiente
        return contador
    
    def __str__(self):
        if self.esta_vacio():
            return "Lista Vacia"
        
        elementos=[]
        actual=self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual=actual.siguiente
        return "<--> ".join(elementos)
    
    #=========== PRUEBAS ==========
    if __name__ == "__main__":
        lista = listaDoble()
        
        #insertar elementos
        print("Insertar al final: 10,20 , 30")
        lista.insertar_final(10)
        lista.insertar_final(20)
        lista.insertar_final(30)
        print(lista)
    
        
    
    
       
