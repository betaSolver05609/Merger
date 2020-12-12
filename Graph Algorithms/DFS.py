# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 11:17:16 2020

@author: Someindra Kumar Singh
"""


from collections import defaultdict;

class Graph: 
    #Adjacency list
    def __init__(self):
        self.graph=defaultdict(list)
    #In list we add edge specifying 2 verctices
    #So it would look something like this
    #[{0: [1]}] where it is a set to exclude repeatations
    #u is the origin vertex and v is the final vertex
    def AddEdgeToGraph(self, u, v):
        self.graph[u].append(v); #append v to the list of edges
        
    #Execute the DFS
    #visit a node and search for neighbours. If neighbours are there
    #recursively call them and keep pushing values onto visited
    
    #Recursive Execution
    def dfs(self, v, visited):
        visited.add(v)
        print(v, end=' is visited \n')
        for neighbourNodes in self.graph[v]:
            if neighbourNodes not in visited:
                self.dfs(neighbourNodes, visited)
    
    #Non-Recursive Execution
    def dfsIterative(self, v, visited):
        stack=[];
        stack.append(v)        
        while(len(stack)):
            print(stack)
            currentNode=stack.pop();
            if currentNode not in visited:
                print(currentNode, end=' is visited \n')
                visited.add(currentNode)
            for neighbourNodes in self.graph[currentNode]:
                if neighbourNodes not in visited:
                    stack.append(neighbourNodes)
            
            
#Create the graph
g=Graph();

g.AddEdgeToGraph(0,1)
g.AddEdgeToGraph(1,2)
g.AddEdgeToGraph(2,3)
g.AddEdgeToGraph(3,4)
g.AddEdgeToGraph(4,5)
g.AddEdgeToGraph(5,6)
g.AddEdgeToGraph(1,3)
g.AddEdgeToGraph(2,4)

#Execute dfs
visited=set();
g.dfs(0, visited)




        
    
    






