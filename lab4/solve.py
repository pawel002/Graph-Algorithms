from unicodedata import name
from dimacs import *
import os
import time
import collections
import heapq
import signal
from tester import tester

(V, L) = loadDirectedWeightedGraph(os.path.abspath('lab4/graphs/chordal/AT'))     # wczytaj graf

def LexBFS_(graph):
    verticies = [0 for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]
    currlist = [0]

    for i in range(len(graph)):
        pass

    return verticies

def LexBFS(graph):
    verticies = [0 for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]
    search = [set([0]), set([i for i in range(1, len(graph))])]

    for j in range(len(graph)):
        u = search[0].pop()
        if not search[0]:
            search.pop(0)
        verticies[j] = u
        visited[u] = True

        i = 0
        s = set([v for v in graph[u] if not visited[v]])
        while i < len(search):
            u = s & search[i]
            if u:
                search[i] -= u
                if not search[i]:
                    search[i] = u
                    i += 1
                else:
                    search.insert(i, u)
                    i += 2
            else:
                i += 1
    
    return verticies

def chordal(V, L):
    graph = [[] for _ in range(V)]
    for edge in L:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    verts = LexBFS(graph)
    sets = [set(graph[verts[i]]) & set(verts[:i]) for i in range(len(graph))]
    parents = [0 for _ in range(len(graph))]
    for i, v in enumerate(verts):
        for j in range(i, -1, -1):
            if verts[j] in graph[v]:
                parents[i] = verts[j]
                break
    
    for i, v in enumerate(verts[1:]):
        a = sets[i+1] - set([parents[i+1]])
        b = sets[verts.index(parents[i+1])]
        if not a.issubset(b):
            return 0

    return 1

def maxclique(V, L):
    graph = [[] for _ in range(V)]
    for edge in L:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    verts = LexBFS(graph)
    M = 0
    for i in range(len(graph)):
        M = max(M, len(set(graph[verts[i]]) & set(verts[:i])))
    
    return M+1

def coloring(V, L):
    graph = [[] for _ in range(V)]
    for edge in L:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    verts = LexBFS(graph)
    colors = [0 for _ in range(len(graph))]

    for v in verts:
        color = set()

        for u in graph[v]:
            color.add(colors[u])

        i = 1
        while i in color:
            i += 1
        colors[v] = i
    
    return max(colors)

def vcover(V, L):
    graph = [[] for _ in range(V)]
    for edge in L:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    verts = LexBFS(graph)
    I = set()

    for v in verts[::-1]:
        N = set(graph[v])
        if not N & I:
            I.add(v)
    
    return len(graph) - len(I)

def checkLexBFS(G, vs):
    n = len(G)
    pi = [None] * n
    for i, v in enumerate(vs):
        pi[v] = i

    for i in range(n-1):
        for j in range(i+1, n-1):
            Ni = G[vs[i]]
            Nj = G[vs[j]]

            verts = [pi[v] for v in [x for x in Nj if x not in Ni] if pi[v] < i]
            if verts:
                viable = [pi[v] for v in [x for x in Ni if x not in Nj]]
                if not viable or min(verts) <= min(viable):
                    return False
    return True

# chordal(V, L)
# tester(chordal, 5,"lab4/graphs/chordal")
# tester(maxclique, 5,"lab4/graphs/maxclique")
# tester(coloring, 5,"lab4/graphs/coloring")
# tester(vcover, 5,"lab4/graphs/vcover")

G = [[j for j in range(1000) if j!=i] for i in range(1000)]
A = time.time()
LexBFS(G)
print(time.time() - A)

