a,b=map(int,input().split())
if((abs(a-b))==1):
    print('Yes')
elif(a==10 or a==1 and b==10 or b==1):
    print('Yes')
else:
    print('No')
