## NECCESSARY IMPORTS
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

img = plt.imread("C:/Users/golde/OneDrive/Pictures/Screenshots/ALBION COLLEGE CAMPUS.png")
G = nx.Graph()

G.add_edges_from([('Science_Complex_Entrance', 'Library_Entrance'), ('Science_Complex_Entrance', 3), ('Library_Entrance', 4), (3, 4)])

pos = {'Science_Complex_Entrance': np.array([330, 181.6]), "Library_Entrance": np.array([159, 269]), 3: np.array([1, 0]), 4: np.array([2, 1])}
plt.imshow(img)

nx.draw(G, pos=pos, with_labels=True, node_color='skyblue', node_size=100, edge_color='black', font_size=12, font_color='white')

plt.show()

