def filter_primes(numbers):
    return list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) and x > 1, numbers))