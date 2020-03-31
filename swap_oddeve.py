def Sw_oddeve(s):
    lst = []
    for i in range(len(s)):
        lst.append(s[i])
    for j in range(len(lst)):
        if j%2 == 0:
            lst[j], lst[j+1] = lst[j+1], lst[j]
    for k in lst:
        print(k, end="")
stri = str(input())
Sw_oddeve(stri)
