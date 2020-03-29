def Sec_max(lst):
    lst.sort()
    print(lst[-2])
n = int(input())
a = list(map(int, input().split()))
Sec_max(a)
