def Idx(a,b):
  print(pow(a,b)) if (a in range(6) and b in range(1, 51)) else print("error")
p, q = map(int, input().split())
Idx(p,q)
