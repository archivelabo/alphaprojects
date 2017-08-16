from heapq import heappush, heappop
import sys
input = sys.stdin.readline

class Graph:
    def __init__(self, n):
        self.adj = [[] for _ in range(n + 1)]

    def add_edge(self, x, y, weight):
        self.adj[x].append((y, z))
        self.adj[y].append((x, z))

    def connected_nodes(self, root):
        return self.adj[root]

n, m = map(int, input().split())

d = [-1 for _ in range(n + 1)]
v = [0 for _ in range(n + 1)]

g = Graph(n)

for l in range(m):
    x, y, z = map(int, input().split())
    g.add_edge(x, y, z)

q = [(0, 1)]
while q:
    dist, node = heappop(q)
    if d[node] != -1:
        continue
    d[node] = dist
    for dest, add in g.connected_nodes(node):
        heappush(q, (dist + add, dest))

for l in range(1, n + 1):
    print(d[l])
