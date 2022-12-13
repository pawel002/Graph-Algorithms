from unicodedata import name
from dimacs import *
import os
import time
import collections
import heapq
import signal
    
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



