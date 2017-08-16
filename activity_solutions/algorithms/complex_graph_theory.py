import sys
input = sys.stdin.readline
sys.setrecursionlimit(999999999)
n, r = map(int, input().split())
adj = [[] for x in range(n + 1)]
for i in range(n - 1):
  a, b = map(int, input().split())
  adj[a].append(b)
  adj[b].append(a)
rabbits = [0 for x in range(n + 1)]
for i in range(r):
  rabbits[int(input())] = 1
x, y = map(int, input().split())
v = [0 for _ in range(n + 1)]
path = []
def dfs(node, p):
  global path
  if node == y:
    path = p
    return
  for i in adj[node]:
    if not v[i]:
      v[i] = 1
      dfs(i, p + [i])

dfs(x, [x])

ans = n
for node in path:
  if rabbits[node]:
    ans = 0
    break
  q = []
  q.append(node)
  q.append(None)
  v = [0 for _ in range(n + 1)]
  v[node] = 1
  d = 0
  while q:
    t = q.pop(0)
    if t == None:
      d += 1
      q.append(None)
      continue
    if rabbits[t] and d < ans:
      ans = d
      break
    if d > ans:
      break
    for i in adj[t]:
      if not v[i]:
        q.append(i)
        v[i] = 1
print(ans)
