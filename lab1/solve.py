from unicodedata import name
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
def tester(func):
    cum_time = 0
    tests_passed = 0
    tests_count = len(os.listdir("lab1/graphs"))

    print("-" * 20 + "TESTS" + '-' * 20)

    for i, graph in enumerate(os.listdir("lab1/graphs")):
        (V, L) = loadWeightedGraph(os.path.abspath("lab1/graphs/" + graph))
        name = graph.split("/")[-1]
        solution = readSolution(os.path.abspath("lab1/graphs/" + graph))

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

if __name__ == '__main__':
    tester(union)


    

