def Num_prime(a,b):
    res = 0
    for i in range(a, b+1):
        if i>1:
            for n in range(2,i):
                if (i%n)==0:
                    break
            else:
                res +=1
    print(res)
                    
a,b = map(int,input().split())
Num_prime(a,b)
