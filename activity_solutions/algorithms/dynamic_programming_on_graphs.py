import sys
input = sys.stdin.readline

n = int(input())
adj = [set() for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]
x, y = map(int, input().split())
while x != 0:
    adj[x].add(y)
    x, y = map(int, input().split())
dp[1] = 1
for node in range(n + 1):
    for node_two in adj[node]:
        dp[node_two] += dp[node]
print(dp[n])
