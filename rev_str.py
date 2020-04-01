def Str_rev(a):
	a[0], a[1] = a[1], a[0]
	print(a[0], a[1])
s = list(map(str, input().split()))
Str_rev(s)
