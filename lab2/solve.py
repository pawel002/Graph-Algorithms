from unicodedata import name
from dimacs import *
import os
import time
import collections

(V, L) = loadDirectedWeightedGraph(os.path.abspath('lab2\\graphs\\flow\\trivial'))     # wczytaj graf

class Edge:
    def __init__(self, v, flow, C, rev):
        self.v = v
        self.flow = flow
        self.C = C
        self.rev = rev
 
# Residual Graph
 
 
class Graph:
    def __init__(self, V):
        self.adj = [[] for i in range(V)]
        self.V = V
        self.level = [0 for i in range(V)]
 
    # add edge to the graph
    def addEdge(self, u, v, C):
 
        # Forward edge : 0 flow and C capacity
        a = Edge(v, 0, C, len(self.adj[v]))
 
        # Back edge : 0 flow and 0 capacity
        b = Edge(u, 0, 0, len(self.adj[u]))
        self.adj[u].append(a)
        self.adj[v].append(b)
 
    # Finds if more flow can be sent from s to t
    # Also assigns levels to nodes
    def BFS(self, s, t):
        for i in range(self.V):
            self.level[i] = -1
 
        # Level of source vertex
        self.level[s] = 0
 
        # Create a queue, enqueue source vertex
        # and mark source vertex as visited here
        # level[] array works as visited array also
        q = []
        q.append(s)
        while q:
            u = q.pop(0)
            for i in range(len(self.adj[u])):
                e = self.adj[u][i]
                if self.level[e.v] < 0 and e.flow < e.C:
 
                    # Level of current vertex is
                    # level of parent + 1
                    self.level[e.v] = self.level[u]+1
                    q.append(e.v)
 
        # If we can not reach to the sink we
        # return False else True
        return False if self.level[t] < 0 else True
 
    def sendFlow(self, u, flow, t, start):
        # Sink reached
        if u == t:
            return flow
 
        # Traverse all adjacent edges one -by -one
        while start[u] < len(self.adj[u]):
 
            # Pick next edge from adjacency list of u
            e = self.adj[u][start[u]]
            if self.level[e.v] == self.level[u]+1 and e.flow < e.C:
 
                # find minimum flow from u to t
                curr_flow = min(flow, e.C-e.flow)
                temp_flow = self.sendFlow(e.v, curr_flow, t, start)
 
                # flow is greater than zero
                if temp_flow and temp_flow > 0:
 
                    # add flow to current edge
                    e.flow += temp_flow
 
                    # subtract flow from reverse edge
                    # of current edge
                    self.adj[e.v][e.rev].flow -= temp_flow
                    return temp_flow
            start[u] += 1
 
    # Returns maximum flow in graph
    def DinicMaxflow(self, s, t):
 
        # Corner case
        if s == t:
            return -1
 
        # Initialize result
        total = 0
 
        # Augument the flow while there is path
        # from source to sink
        while self.BFS(s, t) == True:
 
            # store how many edges are visited
            # from V { 0 to V }
            start = [0 for i in range(self.V+1)]
            while True:
                flow = self.sendFlow(s, float('inf'), t, start)
                if not flow:
                    break
 
                # Add path flow to overall flow
                total += flow
 
        # return maximum flow
        return total

def solve(V, L, s, t):
    G = Graph(V)
    for e in L:
        G.addEdge(e[0]-1, e[1]-1, e[2])
    
    return G.DinicMaxflow(0, V-1)

def edmonds_karp(V, L, source, sink):

    def bfs(V, matrix, adj, s, t, parent):
        visited = [False] * (V+1)

        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)
            
            for v in adj[u]:
                if visited[v] == False and matrix[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[t]

    MATRIX = [[0 for i in range(V)] for i in range(V)]
    ADJ = [[] for _ in range(V)]
    for edge in L:
        MATRIX[edge[0] - 1][edge[1] - 1] = edge[2]
        ADJ[edge[0] - 1].append(edge[1] - 1)


    parent = [-1] * V
    max_flow = 0
    while bfs(V, MATRIX, ADJ, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, MATRIX[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            MATRIX[u][v] -= path_flow
            MATRIX[v][u] += path_flow
            v = parent[v]

    return max_flow

# tester
def tester(func, path):
    cum_time = 0
    tests_passed = 0
    tests_count = len(os.listdir(path))

    print("-" * 20 + "TESTS" + '-' * 20)

    for i, graph in enumerate(os.listdir(path)):
        (V, L) = loadDirectedWeightedGraph(os.path.abspath(path + "/" + graph))
        name = graph.split("/")[-1]
        solution = readSolution(os.path.abspath(path + "/" + graph))

        start = time.time()
        result = func(V, L, 0, V-1)
        stop = time.time()

        if result == int(solution):
            tests_passed += 1
            print(f"{'TEST'}{i+1 : >3}{' PASSED. TIME: '}{stop - start :.2f}{'s. Test Name: '}{name}{'.'}")
        else:
            print(f"{'TEST'}{i+1 : >3}{' FAILED. TIME: '}{stop - start :.2f}{'s. Test Name: '}{name}{'.'}")
            print(f"{'Your solution: '}{result}{'.'}")
            print(f"{'Correct value: '}{solution}{'.'}")
        cum_time += stop - start

    print("-" * 50)
    print(f"{'PASSED '}{tests_passed}{'/'}{tests_count}{'.'}")
    print(f"{'TESTS TOOK: '}{cum_time :.2f}{'s.'}")
    

tester(edmonds_karp, "lab2/graphs/flow")

