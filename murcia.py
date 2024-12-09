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
plt.savefig("GRAFOO.png")
