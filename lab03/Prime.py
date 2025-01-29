def filter_prime(list):
    maxNum=max(list)
    primes=[]
    prime = [i for i in range(maxNum + 1)]
    prime[1] = 0
    i = 2
    while i <= maxNum:
        if prime[i] != 0:
            j = i + i
            while j <= maxNum:
                prime[j] = 0
                j = j + i
        i += 1
    prime = [i for i in prime if i != 0]
    for i in list:
        if i in prime:
            primes.append(i)
    return primes