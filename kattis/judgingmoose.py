l,r = [int(x) for x in input().split()]

if l == 0 and r == 0:
    print("Not a moose")
elif l == r:
    print(f"Even {l+r}")
elif l > r:
    print(f"Odd {2*l}")
elif r > l:
    print(f"Odd {2*r}")
