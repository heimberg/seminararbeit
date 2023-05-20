import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.colors import LogNorm

# Load data
df = pd.read_csv('comparison_results.csv')

# Calculate average for each n, m
df_avg = df.groupby(['n','m']).mean().reset_index()

# save the average results to a csv
df_avg.to_csv('comparison_results_avg.csv', index=False)

# Define color norm
color_norm = LogNorm(vmin=df_avg['k2tree_compression'].min(), vmax=df_avg['k2tree_compression'].max())

# K2Tree
plt.figure(figsize=(10, 8))
k2tree_scatter = plt.scatter(df_avg['density'], df_avg['k2tree_time'], c=df_avg['k2tree_compression'], 
                             norm=color_norm, cmap='plasma')
plt.title('K2Tree Time vs Density')
plt.xlabel('Density')
plt.ylabel('Time (s)')
plt.colorbar(k2tree_scatter).set_label('Compression Factor')
plt.savefig('k2tree_time_vs_density_compression.png')
plt.show()

# Reset color norm for Huffman
color_norm = LogNorm(vmin=df_avg['huffman_compression'].min(), vmax=df_avg['huffman_compression'].max())

# Huffman
plt.figure(figsize=(10, 8))
huffman_scatter = plt.scatter(df_avg['density'], df_avg['huffman_time'], c=df_avg['huffman_compression'], 
                              norm=color_norm, cmap='plasma')
plt.title('Huffman Time vs Density')
plt.xlabel('Density')
plt.ylabel('Time (s)')
plt.colorbar(huffman_scatter).set_label('Compression Factor')
plt.savefig('huffman_time_vs_density_compression.png')
plt.show()


# plot compression factor vs density for k2tree 
# color the points by the number of nodes
# reset color norm for number of nodes
color_norm = LogNorm(vmin=df_avg['n'].min(), vmax=df_avg['n'].max())

plt.figure(figsize=(10, 8))
k2tree_scatter = plt.scatter(df_avg['density'], df_avg['k2tree_compression'], c=df_avg['n'], 
                             norm=color_norm, cmap='plasma')
plt.title('K2Tree Compression Factor vs Density')
plt.xlabel('Density')
plt.ylabel('Compression Factor')
plt.colorbar(k2tree_scatter).set_label('Number of Nodes')
plt.savefig('k2tree_compression_vs_density.png')
plt.show()

# the same for huffman
color_norm = LogNorm(vmin=df_avg['n'].min(), vmax=df_avg['n'].max())

plt.figure(figsize=(10, 8))
k2tree_scatter = plt.scatter(df_avg['density'], df_avg['huffman_compression'], c=df_avg['n'], 
                             norm=color_norm, cmap='plasma')
plt.title('Huffman Compression Factor vs Density')
plt.xlabel('Density')
plt.ylabel('Compression Factor')
plt.colorbar(k2tree_scatter).set_label('Number of Nodes')
plt.savefig('huffman_compression_vs_density.png')
plt.show()

# compare the compression times for k2tree and huffman
plt.figure(figsize=(10, 8))
plt.scatter(df_avg['density'], df_avg['k2tree_time'], label='K2Tree')
plt.scatter(df_avg['density'], df_avg['huffman_time'], label='Huffman')
plt.title('Compression Time vs Density')
plt.xlabel('Density')
plt.ylabel('Time (s)')
plt.legend()
plt.savefig('compression_time_vs_density.png')
plt.show()

# compare the compression times for k2tree, color by number of nodes
color_norm = LogNorm(vmin=df_avg['n'].min(), vmax=df_avg['n'].max())

plt.figure(figsize=(10, 8))
plt.scatter(df_avg['density'], df_avg['k2tree_time'], c=df_avg['n'], norm=color_norm, cmap='plasma')
plt.title('K2Tree Compression Time vs Density')
plt.xlabel('Density')
plt.ylabel('Time (s)')
plt.colorbar().set_label('Number of Nodes')
plt.savefig('k2tree_compression_time_vs_density.png')
plt.show()

# compare the compression times for huffman, color by number of nodes
color_norm = LogNorm(vmin=df_avg['n'].min(), vmax=df_avg['n'].max())

plt.figure(figsize=(10, 8))
plt.scatter(df_avg['density'], df_avg['huffman_time'], c=df_avg['n'], norm=color_norm, cmap='plasma')
plt.title('Huffman Compression Time vs Density')
plt.xlabel('Density')
plt.ylabel('Time (s)')
plt.colorbar().set_label('Number of Nodes')
plt.savefig('huffman_compression_time_vs_density.png')
plt.show()