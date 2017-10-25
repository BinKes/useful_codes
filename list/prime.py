# some methods to get primes

#3到100内的素数
prime1 = [x for x in range(3, 101, 2) 
    if not [y for y in range(3, int(x**0.5)+1, 2) if x%y ==0]]
print(prime1)

#判断一个数是不是素数
def isPrime(n):
    return True if n in [x for x in range(3, n+1, 2) if not [y for y in range(3, int(x**0.5)+1, 2) if x%y ==0]] else False
    
print(isPrime(20))

#找回文素數：
#如11到1000的回文素數
n = [w for w in [x for x in range(11, 1001, 2) if not [y for y in range(3, int(x**0.5)+1, 2) if x%y ==0]] if str(w)[0] == str(w)[-1]]
print(n)

print(int(str(123)[::-1]))
#>>> 321
#找出1000之內一共有多數素數：
n = [x for x in range(1, 1001, 2) if not [y for y in range(3, int(x**0.5)+1, 2) if x%y ==0]]
print(len(n))
#>> 168

def get_prime(n):
    prime_dict = [1 for i in range(n)]
    for i in range(3, n, 2):
        prime_dict[i] = 0
    for i in range(3, int(n**0.5)+1, 2):
        if prime_dict[i-1] != 0:
            for j in range(i*i, n, i):
                prime_dict[j-1] = 0
    return prime_dict
num = 10
n1 = get_prime(num)
l1 = [x for x in range(num) if n1[x]==1 ]
print(l1)
print(len(l1))


# 一段 Haskell 代码，lazy 生成所有质数：
primes = sieve [2..] where sieve (p:xs) = p : sieve [x|x <- xs, x `mod` p > 0]

#另外 见：https://leetcode.com/problems/count-primes/