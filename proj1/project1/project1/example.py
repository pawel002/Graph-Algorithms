from data import runtests
import heapq

# Paweł Jarosz
# GREEDY nmlog(m) + klog(n)
# Na początku zamienamy wartości w wages na tablice oraz dodajemy do nich cene ekwipuny - ona nic nie zmienia.
# Sortujemy występy po koszcie.
# Zauważmy, że cena za wwystępy w kolejności 1, 2 zapłacimy tyle samo co za występy w kolejności 2, 1
# co pozwala na zastosowanie algorymtmu zachłannego -> kolejnoścć wyborów nie ma znaczenia dlatego bierzemy ten najtańsze.
# Osiagamyto za pomocą posortowania n tablic z maksymalnie m wartościami -> nmlog(m)
# Następnie dodajemy posortowane wartości do wypłat podstawowych -> nm
# Na koniec K razy wybieramy najtańsze wystąpienie z posortowanych rosnąco tablic.
# Osiagam to dzięki tablicy zawierającej indeksy i odpowiednie wartości w strykturze heapq, 
# która pozwala na dodawanie i usuwanie elementów w czasie log(n), stąd -> klog(n)
# Podsumowując nmlog(m) + nm + klog(n) ~ nmlog(m) + klog(n)

def my_solve(N, M, K, bases, wages, eq_cost):
    # dodanie eq
    for i in range(len(wages)):
        for j in range(len(wages[i])):
            wages[i][j] = [wages[i][j][0] - 1, wages[i][j][1] + eq_cost[wages[i][j][0] - 1]]
    
    #sortowanie
    for wage in wages:
        wage.sort(key=lambda x: x[1])
    
    # dodanie do bases
    for i in range(len(bases)):
        sum = 0
        L = min(len(wages[i]), len(bases[i]))
        empty = [0 if j == 0 else bases[i][j-1] for j in range(L+1)]
        for j in range(L):
            sum += wages[i][j][1]
            empty[j+1] += sum
        bases[i] = empty

    # heap oraz suma
    S = 0
    queue = []
    
    for i, base in enumerate(bases):
        if len(base) > 1:
            heapq.heappush(queue, (base[1], i))

    # wybranie K najmniejszych
    for _ in range(K):
        val, index = heapq.heappop(queue)
        
        bases[index][0] += 1
        S += val

        if bases[index][0] < len(bases[index]) - 1:
            newval = bases[index][bases[index][0] + 1] - bases[index][bases[index][0]]
            heapq.heappush(queue, (newval, index))

    return S


runtests(my_solve)





