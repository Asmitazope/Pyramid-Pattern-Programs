#pattern 6   
n=10
k=n
num=0
for i in range(0,n):
    for j in range(0,k):
        print(end=' ')
    k=k-1
    for j in range(0,i):
        num=num+1
        print(num, end=' ')
    print('\r')

