def Floyd_Warshall(graph):
  n = len(graph)
  dist = [[] for i in range(n)]
  for i in range(n):
    for j in range(n):
      dist[i].append(graph[i][j]) 
  for k in range(n):
    for i in range(n):
      for j in range(n):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

  print('Distancia más corta entre todo par de nodos:')
  for i in range(n):
    for j in range(n):
      if dist[i][j] == INF:
        print("%7s" % ("INF"), end = ' ')
      else:
        print("%7s" % (dist[i][j]), end = ' ')
    print()
