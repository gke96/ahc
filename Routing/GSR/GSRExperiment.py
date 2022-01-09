from Ahc import Topology
from Channels.Channels import P2PFIFOPerfectChannel
import networkx as nx
from GSRExperimentNodeComponent import GSRExperimentNode
from Routing.GSR.RoutingGSRComponent import RoutingGSRComponent
from Constants import N_NODES

# undirected graph
def draw_random_graph(n):
    k = True
    g_random = None
    while k:
        k = False
        g_random = nx.gnp_random_graph(n, 0.3)
        if not nx.is_connected(g_random):
            k = True
    return g_random

if __name__ == "__main__":
    graph = draw_random_graph(N_NODES)  # nx.Graph()
    print(graph.edges)
    # graph.add_edges_from(edges)

    node_list = graph.nodes

    print(RoutingGSRComponent.__name__)

    topology = Topology()
    topology.construct_from_graph(graph, GSRExperimentNode, P2PFIFOPerfectChannel)
    topology.start()

    while True:
        pass
