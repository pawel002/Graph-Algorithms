from dimacs import *
import os
import time


(V,L) = loadWeightedGraph(os.path.abspath('lab1\graphs\grid100x100'))     # wczytaj graf

def union(V, L):
    L.sort(key=lambda x: x[2], reverse=True)
    parent = [i for i in range(V + 1)]
    idx = 0

    while True:
        v1, v2 = L[idx][0], L[idx][1]

        while v1 != parent[v1]:
            v1 = parent[v1]
        
        while v2 != parent[v2]:
            v2 = parent[v2]
        
        idx += 1
        if v1 == v2:
            continue

        parent[v2] = v1

        A, B = 1, 2

        while A != parent[A]:
            A = parent[A]
        
        while B != parent[B]:
            B = parent[B]
        
        if A == B:
            return L[idx-1][2]



# tester
cum_time = 0
tests_passed = 0
tests_count = len(os.listdir("lab1/graphs"))
for i, graph in enumerate(os.listdir("lab1/graphs")):
    (V, L) = loadWeightedGraph(os.path.abspath("lab1/graphs/" + graph))
    name = graph.split("/")[-1]
    solution = readSolution(os.path.abspath("lab1/graphs/" + graph))
    start = time.time()
    result = union(V, L)
    stop = time.time()
    if result == int(solution):
        tests_passed += 1
        print("TEST ", i, ", ", name ," PASSED. TIME ", stop - start, " ms.", sep="")
    else:
        print("TEST ", i, ", ", name ," FAILED. TIME ", stop - start, " ms.", sep="")
        print("Your solution: ", result, ". Expected: ", solution, ".", sep="")
    cum_time += stop - start

print("PASSED " , tests_passed, "/", tests_count, ".", sep="")
print("TESTS TOOK:", cum_time)

    

