import sys
n = int(input())
S = input()

i = S.find('#')
if i < 0:
    print(0)
    sys.exit()

a = 0
c = S.count('.')
Min = 200000


for j in range(i, n):
    if S[j] == '#':
        b = c - (j-a)
        Min = min(Min, a+b)
        print('j,a,b,c, Min =',j,a,b,c,Min)
        a += 1
        
print(Min)

#-----下記で通った

#n = int(input())
#S = input()
 
#c = S.count('.')
#Min = c
 
#for j in range(n):
#    if S[j] == '#':
#        c += 1
#    else:
#        c -= 1
#    Min = min(Min, c)
#        
#print(Min)