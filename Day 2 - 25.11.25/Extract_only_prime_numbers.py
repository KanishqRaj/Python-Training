nums = [10, 11, 12, 13, 17, 20, 23]

def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(n ** 0.5) +1):
        if n%i ==0:
            return False
    return True

primes = [n for n in nums if isPrime(n)]
print(primes)
