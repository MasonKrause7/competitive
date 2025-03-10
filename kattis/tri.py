a,b,c = [int(x) for x in input().split()]

found = False
if a + b == c:
    print(f"{a}+{b}={c}")
    found = True
elif a-b == c:
    print(f"{a}-{b}={c}")
    found = True
elif a*b == c:
    print(f"{a}*{b}={c}")
    found = True
elif a/b == c:
    print(f"{a}/{b}={c}")
    found = True

if not found:
    if b + c == a:
        print(f"{a}={b}+{c}")
    elif b-c == a:
        print(f"{a}={b}-{c}")
    elif b*c==a:
        print(f"{a}={b}*{c}")
    elif b/c == a:
        print(f"{a}={b}/{c}")
