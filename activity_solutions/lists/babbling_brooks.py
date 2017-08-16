n = int(input())
streams = [0]
for i in range(0, n):
  streams.append(int(input()))

a = 0
while a != 77:
  a = int(input())
  if a == 88:
    b = int(input())
    streams[b] = streams[b] + streams[b + 1]
    streams.pop(b + 1)
  elif a == 99:
    b = int(input())
    p = int(input())
    f = round(streams[b] * (100 - p) / 100)
    o = round(streams[b] * p / 100)
    streams[b] = f
    streams.insert(b, o)

for i in range(1, len(streams)):
  print(str(streams[i]) + " ", end="")
