def NLR(n,l,r):
    print("yes") if ((l<n and n<r) or (r<n and n<l)) else print("no")
a = int(input())
b,c = map(int, input().split())
NLR(a,b,c)
