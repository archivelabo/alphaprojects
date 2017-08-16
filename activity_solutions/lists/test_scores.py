n, k = map(int, input().split())
m = []
for i in range(n):
  a = int(input())
  if not a < 0:
    m.append(a)
m = sorted(m)
ans = 0
if k >= len(m):
  ans = sum(m)
else:
  for i in range(k):
    ans += m[i - k]
print(ans)
