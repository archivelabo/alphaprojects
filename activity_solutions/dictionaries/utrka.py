n = int(input())
contestants = {}
for i in range(n * 2 - 1):
  name = input()
  if not name in contestants:
    contestants[name] = 0
  contestants[name] += 1

for x in contestants.keys(): # .keys() will get the names of the contestants
  if contestants[x] % 2 == 1:
    print(x)