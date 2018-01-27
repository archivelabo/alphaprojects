import sys
input = sys.stdin.readline
msg = input().strip()

def edit_distance(buff):
    dp = [[0] * (len(buff)+1) for _ in range(2)]
    for j in range(len(buff)+1):
        dp[0][j] = j
    h = 1
    for i in range(1, len(msg)+1):
        dp[h][0] = i
        for j in range(1, len(buff)+1):
            if msg[i-1] == buff[j-1]:
                dp[h][j] = dp[h^1][j-1]
            else:
                dp[h][j] = min(dp[h^1][j-1], min(dp[h^1][j], dp[h][j-1])) + 1
        h ^= 1
    return dp[len(msg)&1][len(buff)]

N = int(input())
ret = 105 # MAXC
for i in range(N):
    K = input().split()
    K[0] = int(K[0])
    res = 0
    for j in range(1, K[0]+1):
        res += edit_distance(K[j])
    ret = min(1.0 * res / K[0], ret)
print('%.6f' % ret)