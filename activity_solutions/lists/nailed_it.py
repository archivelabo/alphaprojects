import sys
input = sys.stdin.readline

boards = [0 for x in range(2001)]
heights = [0 for x in range(4002)]
n = int(input())
t = list(map(int, input().split()))
for x in t:
  boards[x] += 1

for i in range(2001):
  if boards[x]:
    for j in range(i, 2001):
      if i == j:
        heights[i + j] += boards[i] / 2
      elif boards[j]:
        heights[i + j] += min(boards[i], boards[j])

a = 0
aa = 0
for i in range(1, 4001):
  if heights[i] > a:
    a = heights[i]
    aa = 1
  elif heights[i] == a:
    aa += 1
if a:
  print(str(a) + " " + str(aa))
else:
  print("1 " + str(n))