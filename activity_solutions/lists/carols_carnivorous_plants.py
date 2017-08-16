n, m = map(int, input().split())
p = sorted(list(map(int, input().split())))[::-1]
c = 0
a = 0
for i in range(n):
  if i % m == 0 and i >= m:
    c += 1
  a += pow(p[i], c)
print(a % (10**9 + 7))