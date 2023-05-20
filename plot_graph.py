import networkx as nx
import k2tree_gen as k2t
import huffman_gen as huff
import matplotlib.pyplot as plt

# Parameters for the Barabasi Albert Graph
n = 50  # Number of nodes
m = 3  # Number of edges to attach from a new node to existing nodes

# Create the random graph
G = nx.barabasi_albert_graph(n, m)

# plot and save the graph
nx.draw(G)
plt.savefig("graph.png")