#using dictionary

def Num_rep(k,lst):
    my_dict = {k:lst.count(k) for i in lst}
    print(my_dict[k]-1)
n,k = map(int,input().split())
lst = list(map(int, input().split()))
Num_rep(k,lst)


#Alternate Code using For Loop

ls2 = list(map(int, input().split()))
k = int(input())
res = 0
for i in range(len(ls2)):
    if ls2[i] == k:
        res += 1
print(res-1)
