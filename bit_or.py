def Bit_or(res):
    fin = res[0]
    for i in range(len(res)):
        fin |= res[i]
    print(fin)
n = int(input())
res = [int(x) for x in input().split(" ", n-1)]
Bit_or(res)
