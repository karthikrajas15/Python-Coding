#print the prime numbers from 1 to n
N=int(input())
for i in range(1,N):
    flag=0
    for j in  range(2,int(i/2)+1):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print("{}".format(i))
 