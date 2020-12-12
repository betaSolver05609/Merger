# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:47:38 2020

@author: Someindra Kumar Singh
"""

from collections import defaultdict;

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def AddEdgeToGraph(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, v):
        visited=set();
        queue=[];
        queue.append(v);
        visited.add(v);
        while queue:
            print(queue)
            startNode=queue.pop(0)
            print(startNode, end = " Visited \n")
            for neighbour in self.graph[startNode]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
            
g=Graph();

g.AddEdgeToGraph(0,1)
g.AddEdgeToGraph(1,2)
g.AddEdgeToGraph(2,3)
g.AddEdgeToGraph(3,4)
g.AddEdgeToGraph(4,5)
g.AddEdgeToGraph(5,6)
g.AddEdgeToGraph(1,3)
g.AddEdgeToGraph(2,4)

print(g.bfs(0))        
        
        
        