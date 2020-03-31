def Bit_and(lst):
  for i in range(len(lst)):
    a = lst[i-1] & lst[i]
  print(a)
n = int(input())
res = [int(x) for x in input().split(" ", n-1)]
if n in range(100000):
  Bit_and(res)
else:
  print("Error")
