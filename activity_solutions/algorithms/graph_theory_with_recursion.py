import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [set() for _ in range(n + 1)]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].add(b)

ans = "Y"

def dfs(n):
  global ans
  global v
  if v_two[n]:
    return
  if v[n]:
    ans = "N"
    return
  v[n] = 1

  for x in graph[n]:
    dfs(x)
  v[n] = 0
  v_two[n] = 1
v = [0 for x in range(n + 1)] # visited array
v_two = [0 for x in range(n + 1)]
for i in range(1, n + 1):
  if not v_two[i]:
    dfs(i)
print(ans)