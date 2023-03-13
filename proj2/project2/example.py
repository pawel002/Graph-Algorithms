from data import runtests

# Paweł Jarosz
# zlozoność algorytmu to E + V log V
# na poczatku w czasie liniowym względem ilości krawędzi
# znajdujemy stopnie wszytskich wierzchołków - E
# następnie bierzemy te S wierzchołków, które mają najwiekszy stopień 
# oraz spełniają dla każdego v z S: deg(v) > len(S) - są to wierzchołki tworzące graf pełny
# ten krok możemy wykonać w czasie  V log V ze względu na sortowanie
# na koniec sprawdzamy, czy istnieją jakieś krawędzie nienależące do grafu 
# pełnego, które są połączone miedzy sobą. jeżeli tak -> zwracamy none,
# jeżeli nie -> zwracamy ilość wierzchołków w znalezionej wcześniej klice
# zastosowałem także dodatkowe usprawnienie na edge case'y - grafy pełne i puste

def my_solve(N, channels):

    if len(channels) == 0: return 1
    if N*(N-1)//2 == len(channels): return N-1

    edgeCount = [[0, i] for i in range(N)]
    for x, y in channels:
        edgeCount[x-1][0] += 1
        edgeCount[y-1][0] += 1

    edgeCount.sort(reverse=True)

    notClique = [True]*N
    i = 0

    while edgeCount[i][0] > i:
        notClique[edgeCount[i][1]] = False
        i += 1

    for x, y in channels:
        if notClique[x-1] and notClique[y-1]: 
            return None

    return i

runtests(my_solve)