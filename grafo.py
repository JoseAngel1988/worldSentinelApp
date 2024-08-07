from collections import deque

# Datos de ejemplo (reemplaza esto con tus datos reales)
longitud = [71.686965, 71.856679, 71.850773, 71.738926, 71.882279]
latitud = [2.804070, 2.761626, 2.756696, 2.754243, 2.748895]

# Implementación básica de BFS
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        visited.add(current_node)

        # Agrega los vecinos no visitados a la cola
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)

# Crear el grafo (en este caso, simplemente consideramos todos los nodos como vecinos)
graph = {i: range(len(longitud)) for i in range(len(longitud))}

# Ejecutar BFS desde el nodo inicial (por ejemplo, el primer nodo)
bfs(graph, start_node=0)
