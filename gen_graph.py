import networkx as nx
import k2tree_gen as k2t
import huffman_gen as huff
import time
import pandas as pd
import matplotlib.pyplot as plt

def generate_graphs():
    graph_list = []
    adj_list = []
    n_values = [10, 50, 100, 200, 400, 600, 800, 1000]
    m_values = [5, 10, 20, 40, 60, 80, 100, 150, 200, 300, 400, 500,550,600,700,750,800,900,950]
    
    for n in n_values:
        for m in m_values:
            if m < n:
                for _ in range(1):  # Repeat 5 times for each combination of n and m
                    graph = nx.barabasi_albert_graph(n, m)
                    adj = nx.adjacency_matrix(graph).todense().tolist()
                    graph_list.append(graph)
                    adj_list.append(adj)
    
    return graph_list, adj_list

def compare_algorithms(graph_list, adj_list):
    results = []
    
    for graph, adj in zip(graph_list, adj_list):
        n = graph.number_of_nodes()
        m = graph.number_of_edges()
        density = nx.density(graph)
        
        # Measure time for k2tree compression
        start_time = time.time()
        k2_tree = k2t.k2_tree(adj, 4)
        k2tree_time = time.time() - start_time
        k2tree_compression = k2t.count_nodes(k2_tree)/(n**2)
        # Measure time for Huffman compression
        adj_bin = ''.join(str(e) for row in adj for e in row)
        start_time = time.time()
        huffman_compress = huff.compress_binary_data(adj_bin)
        huffman_time = time.time() - start_time
        huffman_compress = len(huffman_compress)/(n**2)
        
        results.append((n, m, density, k2tree_time, k2tree_compression, huffman_time, huffman_compress))
    
    return results

graph_list, adj_list = generate_graphs()
comparison_results = compare_algorithms(graph_list, adj_list)
df = pd.DataFrame(comparison_results, columns=['n', 'm', 'density', 'k2tree_time', 'k2tree_compression', 'huffman_time', 'huffman_compression'])
df.to_csv('comparison_results.csv', index=False)

# Extract the metrics from the comparison results
n_values = [result[0] for result in comparison_results]
m_values = [result[1] for result in comparison_results]
density_values = [result[2] for result in comparison_results]
k2tree_times = [result[3] for result in comparison_results]
k2tree_compressions = [result[4] for result in comparison_results]
huffman_times = [result[5] for result in comparison_results]
huffman_compressions = [result[6] for result in comparison_results]