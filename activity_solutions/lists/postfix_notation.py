a = input().split()
b = []
for x in a:
  try:
    b.append(int(x))
  except:
    last = b.pop()
    b.append(eval(str(b.pop()) + x.replace("^", "**") + str(last)))
print(b[0])
