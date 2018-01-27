from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

d = [-1 for _ in range(n + 1)]
adj = [[] for _ in range(n + 1)]

for l in range(m):
    x, y, z = map(int, input().split())
    adj[x].append((y, z))
    adj[y].append((x, z))

q = [(0, 1)]
while q:
    dist, node = heappop(q)
    if d[node] != -1:
        continue
    d[node] = dist
    for dest, add in adj[node]:
        heappush(q, (dist + add, dest))

for l in range(1, n + 1):
    print(d[l])
