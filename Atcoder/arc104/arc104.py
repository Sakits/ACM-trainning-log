n, K, m = map(int, input().split())

sum = 0
f = [[0] * (n * (n + 1) // 2 * K + 1)] + [0] * n
f[0][0] = 1

for i in range(1, n + 1) : 
    sum += i * K
    f[i] = f[i - 1][:]
    for j in range(i, sum + 1) :
        f[i][j] += f[i][j - i]
        if f[i][j] >= m : f[i][j] -= m
    
    for j in range(sum, i * (K + 1) - 1, -1) :
        f[i][j] -= f[i][j - i * (K + 1)]
        if f[i][j] < 0 : f[i][j] += m


for x in range(1, n + 1) :
    ans = 0
    for i in range(sum + 1) : 
        ans += f[x - 1][i] * f[n - x][i]
    print((ans * (K + 1) - 1) % m)
