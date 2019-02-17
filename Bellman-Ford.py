def bellman_ford(G, source):
    dist = {}
    p = {} #path
    max = infinity
    for v in G:
        dist[v] = max  #將點設為無限大完成初始化
        p[v] = None
    dist[source] = 0

    for i in range(len( G ) - 1):
        for u in G:
            for v in G[u]:
                if dist[v] > G[u][v] + dist[u]:
                    dist[v] = G[u][v] + dist[u]
                    p[v] = u    #完成鬆弛計算，p是前一個節點

    for u in G:
        for v in G[u]:
            if dist[v] > dist[u] + G[u][v]:
                return None, None  #判斷是否有迴路

    return dist, p

def test():
    G = {
        's': {'a':  2, 'b':  9, 'c':  1},
        'a': {'b':  3},
        'b': {'c': -1},
        'c': {},
    }
    dist, p = bellman_ford(G, 'a')
    print(dist)
    print(p)


infinity=float("inf")
test()
