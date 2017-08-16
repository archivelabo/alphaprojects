def solve(markers):
    d = {}
    for marker in markers:
        try:
            d[marker] += 1
        except:
            d[marker] = 1
    h = -1
    for key in d.keys():
        if d[key] > h:
            h = d[key]
    return min(h, (n - h) + 1) + (n - h)
n = int(input())
print(solve(input().split()))

