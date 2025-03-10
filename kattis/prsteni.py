def gcf(a,b):
    if a == 0:
        return b
    return gcf(b%a,a)

def num_rotations(c1, ci):
    gcd = gcf(c1,ci)
    numerator = c1//gcd
    denominator = ci//gcd

    return f"{numerator}/{denominator}"


n = int(input())
rs = [int(x) for x in input().split()]
c1 = 2*rs[0]
for i in range(1,len(rs)):
    print(num_rotations(c1,2*rs[i]))
