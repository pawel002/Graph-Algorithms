from unicodedata import name
from dimacs import *
import os
import time
import collections

(V, L) = loadDirectedWeightedGraph(os.path.abspath('lab2\\graphs\\flow\\trivial'))     # wczytaj graf

def BFS(start, V, E, parent, gMatrix):
    queue = [start]
    visited = [True] + [False for _ in range(V - 1)]
    while queue:
        curr = queue.pop(0)
        for next in E[curr]:
            if not visited[next] and gMatrix[curr][next] > 0:
                queue.append(next)
                visited[next] = True
                parent[next] = curr
    return visited[V-1]

def ford_fulkerson(V, L):
    G = [[] for _ in range(V)]
    gMatrix = [[0 for _ in range(V)] for _ in range(V)]
    for u, v, c in L:
        gMatrix[u-1][v-1] = c
        G[u-1].append(v-1)
    max_flow = 0
    parent = [-1 for _ in range(V)]

    while BFS(0, V, G, parent, gMatrix):
        flow = float('inf')
        s = V-1
        while s != 0:
            flow = min(flow, gMatrix[parent[s]][s])
            s = parent[s]
        max_flow += flow
        t = V-1
        while t != 0:
            u = parent[t]
            gMatrix[u][t] -= flow
            gMatrix[t][u] += flow
            if u not in G[t]: G[t].append(u)
            t = parent[t]

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
        result = func(V, L)
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
    

tester(ford_fulkerson, "lab2/graphs/flow")

