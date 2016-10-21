# some methods to get primes

#3到100内的素数
prime1 = [x for x in range(3, 101, 2) 
    if not [y for y in range(3, int(x**0.5)+1, 2) if x%y ==0]]
print(prime1)

#判断一个数是不是素数
def isPrime(n):
    return True if n in [x for x in range(3, n+1, 2) if not [y for y in range(3, int(x**0.5)+1, 2) if x%y ==0]] else False
    
print(isPrime(20))