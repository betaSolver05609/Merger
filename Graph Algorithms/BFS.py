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
        
    def dfs(self, v, temp, visited):
        visited.add(v)
        temp.append(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                temp=self.dfs(neighbour, temp, visited)
        return temp
    
    def connectedComponent(self):
        cc=[];
        visited=set();
        for i in range(len(self.graph)):
            if i not in visited:
                temp=[]
                cc.append(self.dfs(i, temp, visited))
        return cc;

g=Graph();

g.AddEdgeToGraph(0,1)
g.AddEdgeToGraph(1,2)
g.AddEdgeToGraph(2,3)
#g.AddEdgeToGraph(3,4)
g.AddEdgeToGraph(4,5)
g.AddEdgeToGraph(5,6)
g.AddEdgeToGraph(1,3)
#g.AddEdgeToGraph(2,4)

print(g.connectedComponent())
        
        
        