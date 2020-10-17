"""
# Sieve of Eratosthenes
Write a program that expects a positive integer as input.
This input is the upper bound.
Then, the program prints all prime-numbers below that upper bound.

**Hint:** Look up "Sieve of Eratosthenes" and implement this algorithm.
    > 14
    2
    3
    5
    7
    11
    13
"""
x = int(input())
def sieve_of_eratosthenes(max_integer):
    sieve = [True for _ in range(max_integer + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, max_integer + 1):
        if sieve[start]:
            for i in range(2 * start, max_integer + 1, start):
                sieve[i] = False
    primes = []
    for i in range(2, max_integer + 1):
        if sieve[i]:
            primes.append(i)
    return primes
print(*sieve_of_eratosthenes(x), sep="\n")