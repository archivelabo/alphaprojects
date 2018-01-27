import sys
input = sys.stdin.readline
w, h, n = map(int, input().split())

f = [[0] * (w + 1)] * (h + 1)
for i in range(1, h + 1):
  f[i] = [0] + list(map(int, input().split(" ")))

for i in range(1, h + 1):
	for j in range(1, w + 1):
		f[i][j] += f[i - 1][j] + f[i][j - 1] - f[i - 1][j - 1];
ans = 0
if w == h and w * h == n + 1:
  i = h - 1
  wi = w
  for j in range(1, h - i + 2):
    for k in range(1, w - wi + 2):
      if ans < f[j + i - 1][k + wi - 1] - f[j - 1][k + wi - 1] - f[j + i - 1][k - 1] + f[j - 1][k - 1]:
        ans = f[j + i - 1][k + wi - 1] - f[j - 1][k + wi - 1] - f[j + i - 1][k - 1] + f[j - 1][k - 1]
  i = h
  wi = w - 1
  print(ans)
else:
  for i in range(1, h + 1):
    wi = n // i
    if i * wi > n:
      continue
    for j in range(1, h - i + 2):
      for k in range(1, w - wi + 2):
          if ans < f[j + i - 1][k + wi - 1] - f[j - 1][k + wi - 1] - f[j + i - 1][k - 1] + f[j - 1][k - 1]:
            ans = f[j + i - 1][k + wi - 1] - f[j - 1][k + wi - 1] - f[j + i - 1][k - 1] + f[j - 1][k - 1]
  print(ans)
