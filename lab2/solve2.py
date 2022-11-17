from unicodedata import name
from dimacs import *
import os
import time
import collections
import heapq

(V, L) = loadDirectedWeightedGraph(os.path.abspath('lab2\\graphs\\connectivity\\clique5'))     # wczytaj graf

def BFS(s, t, parent, graph, adj_list, V):
    visited = [False] * V
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()

        for v in adj_list[u]:
            if (visited[v] == False) and (graph[u][v] > 0):
                queue.append(v)
                visited[v] = True
                parent[v] = u

    return visited[t]

def ford_flukerson(V, graph, adj_list, source, sink):
    parent = [-1] * V
    max_flow = 0 
    while BFS(source, sink, parent, graph, adj_list, V):

        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow

def solve1_connectivity(V, L):
    start = 0
    m = 99999
    adj_list = [[] for _ in range(V)]
    for edge in L:
        adj_list[edge[0]-1].append(edge[1] - 1)
        adj_list[edge[1]-1].append(edge[0] - 1)

    for i in range(1, V):
        graph = [[0 for i in range(V)] for j in range(V)]
        for edge in L:
            graph[edge[0] - 1][edge[1] - 1] = edge[2]
            graph[edge[1] - 1][edge[0] - 1] = edge[2]
        m = min(m, ford_flukerson(V, graph, adj_list, start, i))
    return m

def stoer_wagner(V, L):
    graph = [[] for _ in range(V)]
    edges = [0 for i in range(V)]
    visited = [False for i in range(V)]
    s = [0 for i in range(V)]
    que = [[0, 0]]

    for (u, v, e) in L:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
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
    
method = 2
if method == 1:
    tester(solve1_connectivity, "lab2/graphs/connectivity")
else:
    tester(stoer_wagner, "lab2/graphs/connectivity")


