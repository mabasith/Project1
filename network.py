import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
# l=[1,2,3]
# G.add_nodes_from(l)
# G.add_edge(1,2)
# G.add_edge(2,3)
# G.add_edge(1,3)
# G.add_node(1)

# G= nx.complete_graph(20)
# G=nx.gnp_random_graph(50,0.3)
# print(G.nodes())
# print(G.edges())
# print(G.degree(0))
G=nx.barabasi_albert_graph(50,2)
nx.write_gexf(G,'analysis.gexf')
nx.draw(G)
plt.show()