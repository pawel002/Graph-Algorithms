from data import runtests
import bisect
import heapq

def my_solve(N, M, K, bases, wages, eq_cost):
    for i in range(len(wages)):
        for j in range(len(wages[i])):
            wages[i][j] = [wages[i][j][0] - 1, wages[i][j][1] + eq_cost[wages[i][j][0] - 1]]
    
    for wage in wages:
        wage.sort(key=lambda x: x[1])

    for i in range(len(bases)):
        sum = 0
        empty = [x for x in bases[i]]
        L = min(len(wages[i]), len(bases[i]))
        for j in range(L):
            sum += wages[i][j][1]
            empty[j] += sum
        bases[i] = empty[:L]

    S, X = 0, 0
    prevvals = [0 for _ in range(len(bases))]
    indexes = [0 for _ in range(len(bases))]

    for _ in range(K):

        x = X
        while indexes[x] == -1:
            x += 1
        X = x

        index, smallest = x, bases[x][indexes[x]] - prevvals[x]

        for i in range(x, len(bases)):

            if indexes[i] == -1:
                continue

            if bases[i][indexes[i]] - prevvals[i] <= smallest:
                smallest = bases[i][indexes[i]] - prevvals[i]
                index = i

        S += bases[index][indexes[index]] - prevvals[index]
        prevvals[index] = bases[index][indexes[index]]

        if indexes[index] + 1 == len(bases[index]):
            indexes[index] = -1
        else:
            indexes[index] += 1
    
    return S

def cracked(N, M, K, bases, wages, eq_cost):
    for i in range(len(wages)):
        for j in range(len(wages[i])):
            wages[i][j] = [wages[i][j][0] - 1, wages[i][j][1] + eq_cost[wages[i][j][0] - 1]]
    
    for wage in wages:
        wage.sort(key=lambda x: x[1])
    
    for i in range(len(bases)):
        sum = 0
        empty = [0 if j == 0 else bases[i][j-1] for j in range(len(bases[i])+1)]
        L = min(len(wages[i]), len(bases[i]))
        for j in range(L):
            sum += wages[i][j][1]
            empty[j+1] += sum
        bases[i] = empty[:L+1]

    S = 0
    bases.sort(key= lambda x: x[1])
    
    for _ in range(K):

            
        S += bases[0][bases[0][0] + 1]
        if bases[0][0] != 0:
            S -= bases[0][bases[0][0]]
        
        bases[0][0] += 1

        if bases[0][0] == len(bases[0]) - 1:
            bases.pop(0)
        else:
            index = bisect.bisect(bases,
                                  bases[0][bases[0][0] + 1] - bases[0][bases[0][0]],
                                  key=lambda x: x[x[0] + 1] if x[0] == 0 else x[x[0] + 1] - x[x[0]])
            if index != 0:
                t = bases.pop(0)
                bases.insert(index - 1, t)
    
    return S

def cracked_more(N, M, K, bases, wages, eq_cost):
    for i in range(len(wages)):
        for j in range(len(wages[i])):
            wages[i][j] = [wages[i][j][0] - 1, wages[i][j][1] + eq_cost[wages[i][j][0] - 1]]
    
    for wage in wages:
        wage.sort(key=lambda x: x[1])
    
    for i in range(len(bases)):
        sum = 0
        L = min(len(wages[i]), len(bases[i]))
        empty = [0 if j == 0 else bases[i][j-1] for j in range(L+1)]
        for j in range(L):
            sum += wages[i][j][1]
            empty[j+1] += sum
        bases[i] = empty

    S = 0
    queue = []
    for i, base in enumerate(bases):
        if len(base) > 1:
            heapq.heappush(queue, (base[1], i))

    for _ in range(K):
        val, index = heapq.heappop(queue)
        
        bases[index][0] += 1
        S += val

        if bases[index][0] < len(bases[index]) - 1:
            newval = bases[index][bases[index][0] + 1] - bases[index][bases[index][0]]
            heapq.heappush(queue, (newval, index))

    return S

runtests(cracked_more)





