N = int(input())
S = input()
K = int(input())

for s in S:
    if s == S[K-1]: #これは一旦外で a=S[K-1]と定数にすべし
        print(s, end="")
    else:
        print('*', end="")
    
print('')

#----早い人の正解は下記が多いね。
# ans = ''
# k = S[K-1]
# for i in S:
#    if i != k:
#        ans += '*'
#    else:
#        ans += i
# print(ans)

#----- ちなみに一番早い人はリストを使って、
#      それをjoinを使って文字列にしてた
#
# S=list(input())
# t=S[K-1]
# for i in range(N):
#    if S[i]!=t:
#        S[i]="*"
# print("".join(S))

