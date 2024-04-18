import networkx as nx
import matplotlib.pyplot as plt

estados = ["Chiapas", "Ciudad de México", "Coahuila", "Durango", "Guanajuato", "Guerrero", "Hidalgo"]

costos = {
    ("Chiapas", "Ciudad de México"): 500,
    ("Ciudad de México", "Coahuila"): 600,
    ("Coahuila", "Durango"): 400,
    ("Durango", "Guanajuato"): 250,
    ("Guanajuato", "Guerrero"): 450,
    ("Guerrero", "Hidalgo"): 200,
    ("Hidalgo", "Chiapas"): 300,
    ("Ciudad de México", "Durango"): 800,  
}

G = nx.DiGraph()

for estado in estados:
    G.add_node(estado)

for (origen, destino), costo in costos.items():
    G.add_edge(origen, destino, costo=costo)

def shortest_path_without_repetition():
    total_cost = 0
    path = dict(nx.shortest_path(G)) 

    if len(path) > 0:  
        for i in range(len(path) - 1):
            estado = list(path.keys())[i]  
            siguiente_estado = list(path.keys())[i + 1]
            costo_tramo = G[estado][siguiente_estado]["costo"]
            total_cost += costo_tramo
            print(f"{i+1}. {estado} -> {siguiente_estado}: ${costo_tramo}")
    else:
        print("No se encontró un camino que visite todos los estados sin repeticiones.")

    print(f"\nCosto total del recorrido sin repeticiones: ${total_cost}")


def shortest_path_with_repetition():
    total_cost = 0
    path = nx.shortest_path(G, method="dijkstra")
    for i, estado in enumerate(path.keys()):
        if i < len(path) - 1:
            siguiente_estado = list(path.keys())[i + 1]
            costo_tramo = G[estado][siguiente_estado]["costo"]
            total_cost += costo_tramo
            print(f"{i+1}. {estado} -> {siguiente_estado}: ${costo_tramo}")
    print(f"\nCosto total del recorrido con repeticiones: ${total_cost}")

shortest_path_without_repetition()
shortest_path_with_repetition()

nx.draw_planar(G, node_size=500, node_color="lightblue", with_labels=True)

edge_labels = nx.get_edge_attributes(G, 'costo')
nx.draw_networkx_edge_labels(G, pos=nx.planar_layout(G), edge_labels=edge_labels)

plt.show()

