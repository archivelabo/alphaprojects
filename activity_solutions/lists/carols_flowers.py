f, n = map(int, input().split())
p = [None] * f
for i in range(0, f):
  p[i] = int(input())
p.sort()
c = 0
pp = 1
for i in range(n - 1, -1, -1):
  c += pow(p[i], pp)
  pp += 1
print(c % 1000000007)
