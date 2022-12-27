
n=5
num=1
for i in range(0,n):
    print(end=' ')
    for j in range(0,i+1):
        print(num,end=' ')
        num*=2

    print('\r')

