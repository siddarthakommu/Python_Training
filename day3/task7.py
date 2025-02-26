def isprime(n):
    if n == 1 or not n:
        return False
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return True if count == 2 else False

print(set(x for x in range(1, 51) if isprime(x)))