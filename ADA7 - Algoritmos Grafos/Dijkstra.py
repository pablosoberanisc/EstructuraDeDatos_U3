def dijkstra(self, a):
    if a in self.vertices:
        self.vertices[a].costo = 0
        actual = a
        noVisitados = []
        for v in self.vertices:
            if v != a:
                self.vertices[v].costo = float('inf')
            self.vertices[v].padre = None
            noVisitados.append(v)
        while len(noVisitados) > 0:
            for vec in self.vertices[actual].vecinos:
                if self.vertices[vec[0]].visitado == False:
                    if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
                        self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1] 
                        self.vertices[vec[0]].padre = actual 
            self.vertices[actual].visitado = True
            noVisitados.remove(actual) # Se eliminan del conjunto de no visitados
            actual = self.minimo(noVisitados)
    else:
        return False
