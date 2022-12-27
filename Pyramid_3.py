
#3 using while loop
i,j=1,0

while(i<=5):
    while(j<=i-1):
        print('*',end=' ')
        j+=1
    print("\r")
    j=0;i+=1

