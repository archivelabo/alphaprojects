import sys
input = sys.stdin.readline
n = int(input())
t = [0] * n
for i in range(n): t[i] = int(input())
psa = [0] * (n + 1)
o = open("try.txt", "w")
for i in range(0, n): psa[i + 1] = psa[i] + t[i]
for i in range(int(input())):
  a, b = map(int, input().split())
  o.write(psa[b + 1] - psa[a])