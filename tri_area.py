def Tri_area(b,h):
    res =0.5*b*h
    print(res)
a,b = map(int, input().split())
if (a >= 1000000 and b >= 1000000):
    print("Input value should be less than 1000000")
else:
    Tri_area(a,b)
