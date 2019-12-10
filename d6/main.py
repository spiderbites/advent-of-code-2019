import os
import networkx as nx

f = open(os.path.join(os.getcwd(), "d6/input.txt"))
lines = f.readlines()
orbits = [line.strip().split(')') for line in lines]

# p1
G = nx.DiGraph()
G.add_edges_from(orbits)
print(sum(nx.shortest_path_length(G, 'COM').values()))

# p2
G = nx.Graph()
G.add_edges_from(orbits)
print(nx.shortest_path_length(G, 'SAN', 'YOU') - 2)
