#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

class Drawer:
    def __init__(self, solution):
        self.chromosome = solution.chromosome
        self.graph = solution.graph
        self.graph_v = self.graph.v()
        self.colors = solution.colors
        
        self.G = nx.Graph()
        for v in range(self.graph_v):
            self.G.add_node(v)
        for v in range(self.graph_v):
            for w in self.graph.adj(v):
                self.G.add_edge(v, w)
        self.pos = nx.circular_layout(self.G)
        self.DrawOriginalGraph()
        plt.show()
        self.DrawSolutionGraph()
        plt.show()
                
    def DrawOriginalGraph(self):
        nx.draw(self.G, self.pos, with_labels=True, node_color='green', edge_color='black', width=1, alpha=0.7) # with_labels=true is to show the node number in the output graph
        
    def DrawSolutionGraph(self):
        colors = [plt.cm.tab10(i / float(self.colors - 1)) for i in range(self.colors)]
        values = []
        for node in self.G.nodes():
            values.append(colors[self.chromosome[node]])
        nx.draw(self.G, self.pos, with_labels=True, node_color=values, edge_color='black', width=1, alpha=0.7) # with_labels=true is to show the node number in the output graph