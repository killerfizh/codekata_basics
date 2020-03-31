def Eve_odd_res(a,b):
  res = a+b
  if (res%2 == 0):
    print("even")
  else:
    print("odd")
p,q = map(int,input().split())
Eve_odd_res(p,q)
