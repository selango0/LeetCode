# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph: 
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)
    for neighbor in graph[current]: 
        explore(graph, neighbor, visited)
    return True

class Solution(object):
  
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Create an adjacency list keys = nodes, values = edges 
        graph = build_graph(edges)
        print(graph)
        visited = set()
        count = 0
        for node in graph:
            if explore(graph, node, visited) == True:
                count += 1
        
        return count
        
        
        
    
