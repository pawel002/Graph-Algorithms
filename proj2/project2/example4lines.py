from data import runtests

def my_solve(N, C):
    if any([len(C) == 0, N*(N-1)//2 == len(C)]): return [1, N-1][[len(C) == 0, N*(N-1)//2 == len(C)].index(True)]
    E = [[sum(row), i] for i, row in enumerate((lambda x : [[1 if (i+1 , j+1) in x or (j+1, i+1) in x else 0 for i in range(N)] for j in range(N)])(set(C)))]
    c = {e[1] for i, e in enumerate(sorted(E, reverse=True)) if e[0] > i}
    return None if any(e[0]-1 not in c and e[1]-1 not in c for e in C) else len(c)


runtests(my_solve)