n = int(input())
for i in range(n):
  a = format(int(input()), "04b")
  if len(a) % 4 != 0:
    for i in range(0, 4 - (len(a) % 4) ):
      a = "0" + a
  for i in range(0, len(a), 4):
    print(a[i:i+4], end=" ")
  print("")