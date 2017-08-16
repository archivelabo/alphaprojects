def day(m, d):
    if m == 2 and d < 18:
      print("Before")
    elif m == 2 and d > 18 :
      print("After")
    elif m < 2:
      print("Before")
    elif m > 2:
      print("After")
    else:
      print("Special")

m = int(input())
d = int(input())
day(m, d)