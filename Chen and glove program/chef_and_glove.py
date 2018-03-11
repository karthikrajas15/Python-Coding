T=int(input())
for i in range(T):
    N=int(input())
    L_F=list(map(int,input().split(' ')))
    L_S=list(map(int,input().split(' ')))
    R_L_S=L_S[::-1]
    both=0
    front=0
    back=0
    for i in range(N):
        if(L_F[i]!=L_S[i]):
            both=1
        if(L_F[i]>L_S[i]):
            front=1
        if(L_F[i]>R_L_S[i]):
            back=1      
    if(both==0):
        print("both")
    elif(front==0):
        print("front")
    elif(back==0):
        print("back")
    else:
        print("none")