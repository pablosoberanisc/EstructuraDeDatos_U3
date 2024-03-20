import queue
def sumar_colas(cola1, cola2):
  cola_suma = queue.Queue()
  while not cola1.empty() and not cola2.empty():
    valor1 = cola1.get()
    valor2 = cola2.get()
    suma = valor1 + valor2
    cola_suma.put(suma)
  return cola_suma
cola1 = queue.Queue()
cola2 = queue.Queue()

cola1.put(2)
cola1.put(2)
cola1.put(3)
cola2.put(10)
cola2.put(9)
cola2.put(8)

cola_suma = sumar_colas(cola1, cola2)

while not cola_suma.empty():
  print(cola_suma.get())






   


