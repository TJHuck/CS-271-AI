## NECCESSARY IMPORTS
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

img = plt.imread("C:/Users/golde/OneDrive/Pictures/Screenshots/ALBION COLLEGE CAMPUS.png")
G = nx.Graph()

G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

pos = {1: np.array([0, 0]), 2: np.array([1, 1]), 3: np.array([1, 0]), 4: np.array([2, 1])}
plt.imshow(img)

nx.draw(G, with_labels=True, node_color='skyblue', node_size=100, edge_color='black', font_size=12)

plt.show()
## Locations

