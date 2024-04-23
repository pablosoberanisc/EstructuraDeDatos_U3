def kruskal(grafo):
  aristas = [(peso, nodo_inicio, nodo_final) for nodo_inicio, nodo_final, peso in grafo.values()]
  aristas.sort(key=lambda arista: arista[0])

  conjunto_disjunto = UnionFind()
  arbol_minimo = []

  for peso, nodo_inicio, nodo_final in aristas:
    if not conjunto_disjunto.mismo_conjunto(nodo_inicio, nodo_final):
      conjunto_disjunto.unir(nodo_inicio, nodo_final)
      arbol_minimo.append((peso, nodo_inicio, nodo_final))

  return arbol_minimo
grafo = {
  ('a', 'b'): 7,
  ('a', 'c'): 9,
  ('a', 'd'): 'inf',
  ('b', 'c'): 10,
  ('b', 'd'): 15,
  ('c', 'd'): 11,
  ('e', 'f'): 4,
  ('f', 'g'): 2,
  ('g', 'h'): 1
}

arbol_minimo = kruskal(grafo)
print(arbol_minimo)
