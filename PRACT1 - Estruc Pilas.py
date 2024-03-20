class Pila:
    def __init__(self, tamanio_max):
        self.tope = 0
        self.pila = [None] * tamanio_max

    def esta_vacia(self):
        return self.tope == 0

    def esta_llena(self):
        return self.tope == len(self.pila)

    def insertar(self, dato):
        if self.esta_llena():
            print("Error: Desbordamiento de la pila")
        else:
            self.pila[self.tope] = dato
            self.tope += 1

    def eliminar(self):
        if self.esta_vacia():
            print("Error: Subdesbordamiento de la pila")
        else:
            self.tope -= 1
            return self.pila[self.tope]


pila = Pila(8)

pila.insertar("X")
pila.insertar("Y")

pila.eliminar()
pila.eliminar()
pila.eliminar()

pila.insertar("V")
pila.insertar("W")

pila.eliminar()

pila.insertar("R")


print("Elementos en la pila:", pila.pila[:pila.tope])

"""""
La pila se quedo con dos elementos ['V', 'R'] y si hubo 3 errores de subdesbordamiento
