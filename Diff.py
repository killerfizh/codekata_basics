def Diff(a,b):
  c = a-b
  print(c) if (c >= 0) else print(-c)
  
a,b = map(int, input().split())
Diff(a,b)
