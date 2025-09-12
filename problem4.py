# Problem4: Return a list of all prime numbers less than or equal to n.

def primes_upto(n):
    primes = []
    for num in range(2, n+1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

print(primes_upto(10))
