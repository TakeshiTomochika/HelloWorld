a, b, c = map(int, input().split())

if a < c < b or b < c < a:
    print('Yes')
else:
    print('No')
    
#----一番かっこいいのは下記かな
# A, B, C = map(int, input().split())
# if (A - C) * (B - C) < 0:
#    print("Yes")
# else:
#    print("No")
