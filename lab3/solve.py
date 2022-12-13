from unicodedata import name
from dimacs import *
import os
import time
import collections
import heapq
import signal
from networkx.algorithms.connectivity.stoerwagner import stoer_wagner
import networkx as nx

(V, L) = loadDirectedWeightedGraph(os.path.abspath('lab3\\graphs\\clique5 copy'))     # wczytaj graf

def stoer_wagner(V, L):
    graph = [[] for _ in range(V)]
    edges = [0 for i in range(V)]
    visited = [False for i in range(V)]
    s = [0 for i in range(V)]

    for (u, v, e) in L:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    min_edge, min_edges = 0, len(graph[0])
    for i, x in enumerate(graph):
        if len(x) < min_edges:
            min_edge = i
    que = [[0, min_edge]]
    
    for i in range(V):
        while True:
            u = heapq.heappop(que)[1]
            if not visited[u]:
                break
        
        s[i] = u
        visited[u] = True
        if i == V - 1:
            final_connectivity = edges[u]

        for v in graph[u]:
            if visited[v]:
                continue
            edges[v] += 1
            heapq.heappush(que, (-edges[v], v))

    curr_connectivity = 0
    merged_weights = [0 for i in range(V)]
    merged_visited = [False for i in range(V)]
    for u in s[:-1]:
        merged_visited[u] = True
        curr_connectivity -= merged_weights[u]
        for v in graph[u]:
            if not merged_visited[v]:
                merged_weights[v] += 1
                curr_connectivity += 1
        final_connectivity = min(curr_connectivity, final_connectivity)

    return final_connectivity
    
# tester
def tester(func, time_limit, path):

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
        elif result == "timeout":
            print(f"{'TEST'}{i+1 : >3}{' FAILED. TIMEOUT ERR'}{'s. Test Name: '}{name}{'.'}")
        else:
            print(f"{'TEST'}{i+1 : >3}{' FAILED. TIME: '}{stop - start :.2f}{'s. Test Name: '}{name}{'.'}")
            print(f"{'Your solution: '}{result}{'.'}")
            print(f"{'Correct value: '}{solution}{'.'}")
        cum_time += stop - start

    print("-" * 50)
    print(f"{'PASSED '}{tests_passed}{'/'}{tests_count}{'.'}")
    print(f"{'TESTS TOOK: '}{cum_time :.2f}{'s.'}")

tester(stoer_wagner, 5,"lab3/graphs")



