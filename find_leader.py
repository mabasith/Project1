import networkx as nx 
import matplotlib.pyplot as plt 
G=nx.read_edgelist('data.txt', create_using=nx.DiGraph(),nodetype=int)
nx.draw(G,with_labels=True)
plt.show()
result=nx.pagerank(G)
print(sorted(result.items(),key=lambda f:f[1]))
