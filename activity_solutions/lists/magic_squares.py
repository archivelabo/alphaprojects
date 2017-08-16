import sys

input = sys.stdin.readline

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

s = 0
for i in range(4):
    s += a[i]
for i in range(4):
    for j in (a, b, c, d):
        e = 0
        for k in range(4):
            e += j[k]
        if a[i] + b[i] + c[i] + d[i] != s:
            m = 0
        elif e != s:
            m = 0
        else:
            m = 1
if not m:
  print('muggle')
else:
  print('magic')
