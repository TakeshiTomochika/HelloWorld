x = int(input())

ans = ((x-1) // 11 + 1) * 2
if ans // 2 * 11 - x >= 5:
    ans -= 1
print (ans)