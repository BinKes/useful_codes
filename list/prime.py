# some methods to get primes

#3到100内的素数
prime1 = [x for x in range(3, 101, 2) 
    if not [y for y in range(3, int(x**0.5)+1, 2) if x%y ==0]]


print(prime1)