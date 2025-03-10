'''
a,b = [int(x) for x in input().split()]

small = min(a,b)
big = max(a,b)
gcd = 1
y = 1
while y <= small:
    if small % y == 0:
        x = small // y
        if big % x == 0:
            gcd = x
    y+=1
print(gcd)

#PRIME FACTORIZATION APPROACH
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
def gcd(a,b):
    prime_factorization_a = []
    while a not in primes:
        for i in range(len(primes)):
            if a % primes[i] == 0:
                prime_factorization_a.append(primes[i])
                a = a//primes[i]
                break
    prime_factorization_a.append(a)

    prime_factorization_b = []
    while b not in primes:
        for i in range(len(primes)):
            if b % primes[i] == 0:
                prime_factorization_b.append(primes[i])
                b = b // primes[i]
                break
    prime_factorization_b.append(b)

    num_prime_factors = min(len(prime_factorization_a),len(prime_factorization_b))
    shared_factors = []
    for i in range(num_prime_factors):
        if prime_factorization_a[i] in prime_factorization_b:
            shared_factors.append(prime_factorization_a[i])
            prime_factorization_b.remove(prime_factorization_a[i])
    gcd = 1
    for factor in shared_factors:
        gcd *=factor
    return gcd
'''
def euclid_gcd(a,b):
    if a == 0:
        return b
    return euclid_gcd(b%a, a)
a,b = [int(x) for x in input().split()]
print(euclid_gcd(a,b))
