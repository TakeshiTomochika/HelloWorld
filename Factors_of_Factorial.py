N = int(input())

ans = 1
soin = {}

for i in range(2, N+1):
    k = i
    for j in range(2, i+1):
        while(k//j == k/j): # (k%j == 0)でよかった
            if j in soin:
                soin[j] += 1
            else:
                soin[j] = 1
            k //= j

        if k == 1:
            break

for v in soin.values():
    ans = (ans * (v+1)) % (10**9 + 7)
print(ans) 