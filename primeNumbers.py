
#you can start range from number 2, 1 is not prime
prime_list = [x for x in range(1, 151)
              if not any([x % y == 0 for y in range(2, int(x**0.5)+1)]) and not x == 1]
print(prime_list)
#list comprehension takes more time
def test1():
    primes = []
    for possiblePrime in range(2, 151):
    # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    print(primes)
test1()