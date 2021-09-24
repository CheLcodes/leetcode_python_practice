"""
https://www.1point3acres.com/bbs/thread-761353-1-1.html
給定一個圖，輸入形式是一群邊，輸出指定起點A到終點B的最短路徑
Input:
[[1, 2], [2, 3]], A = 1, B = 3

Follow-up: 若開車從A到B，油箱一開始有V單位油，
每走一個邊就用掉一單位，用完就不能再前進，
在這之前有經過加油站的‍‌‌‌‌‍‍‍‌‍‌‍‍‌‍‍‍‍‍話可以把油加滿，一樣求最短路徑
"""

import collections

def shortestPath(edges, A, B):
    graph = collections.defaultdict(list)
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    
    queue = collections.deque([])
    queue.append((A, 0))
    vis = set()
    vis.add(A)

    while queue:
        node, steps = queue.popleft()
        if node == B:
            return steps
        for n in graph[node]:
            if n not in vis:
                vis.add(n)
                queue.append((n, steps + 1))
    return -1

# res = shortestPath([[1, 2], [2, 3]], 1, 3)
# print('1', res)



def shortestPathV2(edges, stations, A, B, V):
    graph = collections.defaultdict(list)

    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    
    vis = set()
    vis.add((A, V))
    queue = collections.deque([(A, [A], V)]) # (node, path, fuel)
    while queue:
        node, path, fuel = queue.popleft()
        if node == B:
            return len(path) - 1
        for n in graph[node]:
            if n in stations and (n, V) not in vis:
                queue.append((n, path + [n], V))
                vis.add((n, V))
            elif n not in stations and fuel - 1 >= 0 and (n, fuel - 1) not in vis:
                queue.append((n, path + [n], fuel - 1))
                vis.add((n, fuel - 1))
    return -1

res2 = shortestPathV2([[1, 2], [2, 3], [3, 4]], [3], 1, 4, 3)
print('v2', res2)