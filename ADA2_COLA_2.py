from queue import LifoQueue

class CompaniaSeguros:
    def _init_(self):
        self.colas = {}

    def llegada_cliente(self, servicio):
        if servicio not in self.colas:
            self.colas[servicio] = LifoQueue()
        self.colas[servicio].put(servicio)
        return self.colas[servicio].qsize()

    def atender_cliente(self, servicio):
        if servicio in self.colas and not self.colas[servicio].empty():
            return self.colas[servicio].get()
        else:
            return None


def main():
    compania_seguros = CompaniaSeguros()

    while True:
        operacion = input("Ingrese la operación (C para llegada de cliente, A para atender cliente): ").upper()

        if operacion == "C":
            servicio = input("Ingrese el número de servicio del cliente: ")
            numero_atencion = compania_seguros.llegada_cliente(servicio)
            print(f"Número de atención para servicio {servicio}: {numero_atencion}")

        elif operacion == "A":
            servicio = input("Ingrese el número de servicio a atender: ")
            numero_atencion = compania_seguros.atender_cliente(servicio)
            if numero_atencion is not None:
                print(f"Atendiendo servicio {servicio}, número llamado: {numero_atencion}")
            else:
                print(f"No hay clientes en espera para el servicio {servicio}")

        else:
            print("Operación inválida. Por favor, ingrese C para llegada de cliente o A para atender cliente.")


if _name_ == "_main_":
    main()
