def Num_rep(k,lst):
    my_dict = {k:lst.count(k) for i in lst}
    print(my_dict[k]-1)
n,k = map(int,input().split())
lst = list(map(int, input().split()))
Num_rep(k,lst)
