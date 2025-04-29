





# calculate greatest common denominator
# via recursion. simple excersize


def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n) 

print(gcd(128, 6))
