   # for wage in wages:
    #     wage.sort(key=lambda x: x[1])
    
    # for i in range(len(bases)):
    #     sum = 0
    #     L = min(len(wages[i]), len(bases[i]))
    #     empty = [0 if j == 0 else bases[i][j-1] for j in range(L+1)]
    #     for j in range(L):
    #         sum += wages[i][j][1]
    #         empty[j+1] += sum
    #     bases[i] = empty

    # S = 0
    # queue = []
    # for i, base in enumerate(bases):
    #     if len(base) > 1:
    #         heapq.heappush(queue, (base[1], i))

    # for _ in range(K):
    #     val, index = heapq.heappop(queue)
        
    #     bases[index][0] += 1
    #     S += val

    #     if bases[index][0] < len(bases[index]) - 1:
    #         newval = bases[index][bases[index][0] + 1] - bases[index][bases[index][0]]
    #         heapq.heappush(queue, (newval, index))
