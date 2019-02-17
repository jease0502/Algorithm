def bellman_ford(G, s):
    D, P = {s: 0}, {s: None}
    for _ in G: # 轮数等于节点数
        improved = False
        for u in G:
            for v in G[u]:
                if relax(G, u, v, D, P):
                    improved = True
        if not improved: # 如果某轮没有任何改进
            break        # 说明问题已经解决，退出循环
    else:                # 否则，说明第n轮也有改进，存在负权环
        raise ValueError('negative cycle')
    return D, P
inf = float('inf')

