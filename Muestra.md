# Resolviendo un problema de rutas usando grafos

## Problema Planteado: Rutas entre ciudades de España 🇪🇸

### Preguntas

- ¿Cuál es el camino más corto de Murcia a Badajoz?

- ¿Existen caminos entre todos los pares de ciudades?

- ¿Cuál es la ciudad más lejana a Barcelona?

- ¿Cuál es la ciudad más céntrica?

- ¿Cuántos caminos distintos existen de Sevilla a Zaragoza?

- ¿Cómo hacer un tour entre todas las ciudades en el menor tiempo posible?

![problema](image.png)

### Solución

Para resolver el problema planteado, se siguieron los siguientes pasos:

#### 1. Importación de librerías:

```python
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.approximation import traveling_salesman_problem
```

Se importaron las librerías necesarias: `networkx` para la creación y manipulación de grafos, `matplotlib.pyplot` para la visualización del grafo, y el algoritmo `traveling_salesman_problem` para resolver el problema del viajante.

#### 2. Creación del grafo:

```python
G = nx.Graph()
```

Se creó un grafo no dirigido utilizando `networkx`.

#### 3. Añadir nodos (ciudades):

```python
ciudades = ["Murcia", "Badajoz", "Barcelona", "Sevilla", "Zaragoza", "Madrid"]
G.add_nodes_from(ciudades)
```

Se añadieron los nodos al grafo, representando las ciudades.

#### 4. Añadir aristas con pesos (distancias):

```python
aristas = [
    ("Murcia", "Badajoz", 500),
    ("Murcia", "Barcelona", 600),
    ("Barcelona", "Zaragoza", 300),
    ("Zaragoza", "Madrid", 320),
    ("Madrid", "Badajoz", 400),
    ("Sevilla", "Badajoz", 200),
]
for u, v, peso in aristas:
    G.add_edge(u, v, weight=peso)
```

Se añadieron las aristas al grafo, con los pesos correspondientes que representan las distancias entre las ciudades.

#### 5. Cálculo del camino más corto de Murcia a Badajoz:

```python
camino_corto = nx.shortest_path(G, source="Murcia", target="Badajoz", weight="weight")
print("Camino más corto de Murcia a Badajoz:", camino_corto)
```

Se utilizó el algoritmo de camino más corto de `networkx` para encontrar la ruta más corta entre Murcia y Badajoz.

#### 6. Verificación de la conectividad del grafo:

```python
es_conexo = nx.is_connected(G)
print("¿El grafo es conexo?", es_conexo)
```

Se verificó si el grafo es conexo, es decir, si existe un camino entre cualquier par de nodos.

#### 7. Determinación de la ciudad más lejana a Barcelona:

```python
distancias = nx.single_source_dijkstra_path_length(G, source="Barcelona", weight="weight")
ciudad_lejana = max(distancias, key=distancias.get)
print("La ciudad más lejana a Barcelona es:", ciudad_lejana)
```

Se calcularon las distancias desde Barcelona a todas las demás ciudades y se determinó cuál es la más lejana.

#### 8. Determinación de la ciudad más céntrica:

```python
ciudad_centrica = nx.center(G)
print("La ciudad más céntrica es:", ciudad_centrica)
```

Se determinó la ciudad más céntrica del grafo utilizando la función `center` de `networkx`.

#### 9. Cálculo de los caminos distintos de Sevilla a Zaragoza:

```python
caminos_distintos = list(nx.all_simple_paths(G, source="Sevilla", target="Zaragoza"))
print("Cantidad de caminos distintos de Sevilla a Zaragoza:", len(caminos_distintos))
```

Se calcularon todos los caminos simples entre Sevilla y Zaragoza.

#### 10. Resolución del problema del viajante:

```python
tour = traveling_salesman_problem(G, weight="weight")
print("Tour mínimo:", tour)
```

Se resolvió el problema del viajante para encontrar el tour más corto que visita todas las ciudades.

#### 11. Visualización del grafo:

```python
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_color="#d8b3d8", font_weight="bold", node_size=1500)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo de Ciudades")
plt.savefig("GRAFOO.png")
```

Se visualizó el grafo utilizando matplotlib, mostrando los nodos, aristas y sus pesos.

Estos pasos permitieron resolver el problema planteado y obtener la información solicitada sobre las ciudades y sus conexiones.

# Código completo

```python
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.approximation import traveling_salesman_problem

# Crear el grafo
G = nx.Graph()

# Añadir nodos (ciudades)
ciudades = ["Murcia", "Badajoz", "Barcelona", "Sevilla", "Zaragoza", "Madrid"]
G.add_nodes_from(ciudades)

# Añadir aristas con pesos (distancias entre ciudades como ejemplo)
aristas = [
    ("Murcia", "Badajoz", 500),
    ("Murcia", "Barcelona", 600),
    ("Barcelona", "Zaragoza", 300),
    ("Zaragoza", "Madrid", 320),
    ("Madrid", "Badajoz", 400),
    ("Sevilla", "Badajoz", 200),
]

# Añadir las conexiones al grafo
for u, v, peso in aristas:
    G.add_edge(u, v, weight=peso)

# 1. ¿Cuál es el camino más corto de Murcia a Badajoz?
camino_corto = nx.shortest_path(
    G, source="Murcia", target="Badajoz", weight="weight")
print("Camino más corto de Murcia a Badajoz:", camino_corto)

# 2. ¿Existen caminos entre todos los pares de ciudades?
es_conexo = nx.is_connected(G)
print("¿El grafo es conexo?", es_conexo)

# 3. ¿Cuál es la ciudad más lejana a Barcelona?
distancias = nx.single_source_dijkstra_path_length(
    G, source="Barcelona", weight="weight")
ciudad_lejana = max(distancias, key=distancias.get)
print("La ciudad más lejana a Barcelona es:", ciudad_lejana)

# 4. ¿Cuál es la ciudad más céntrica?
ciudad_centrica = nx.center(G)
print("La ciudad más céntrica es:", ciudad_centrica)

# 5. ¿Cuántos caminos distintos existen de Sevilla a Zaragoza?
caminos_distintos = list(nx.all_simple_paths(
    G, source="Sevilla", target="Zaragoza"))
print("Cantidad de caminos distintos de Sevilla a Zaragoza:", len(caminos_distintos))

# 6. ¿Cómo hacer un tour entre todas las ciudades en el menor tiempo posible?
tour = traveling_salesman_problem(G, weight="weight")
print("Tour mínimo:", tour)

# Visualización del grafo
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_color="#d8b3d8", # purpura claro = #d8b3d8
        font_weight="bold", node_size=1500)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo de Ciudades")
plt.savefig("GRAFOO.png") # Guardar imagen del grafo generado
```