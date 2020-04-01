def RPS(a,b):
    print("R") if ((a=="R" and b =="S") or (a == "s" and b == "R")) else print("P") if ((a=="R" and b =="P") or (a == "P" and b == "R")) else print("S") if ((a=="S" and b =="P") or (a == "P" and b == "S")) else print("D") if (a == b) else print()
p,q = map(str, input().split())
RPS(p.upper(),q.upper())
