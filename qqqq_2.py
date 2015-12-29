__author__ = 'iankuoli'

import networkx as nx

G = nx.Graph()

G.add_edge('a', 'b', weight=3)
G.add_edge('b', 'c', weight=1)
G.add_edge('c', 'd', weight=8)
G.add_edge('d', 'e', weight=5)

print(G.degree('b'))