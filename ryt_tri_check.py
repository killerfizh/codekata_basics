def Ryt_tri_check(a,b,c):
  print("yes") if ((pow(a,2)+pow(b,2) == pow(c,2)) or (pow(b,2)+pow(c,2) == pow(a,2)) or (pow(a,2)+pow(c,2) == pow(b,2))) else print("no")
a,b,c = map(int, input().split())
Ryt_tri_check(a,b,c)
