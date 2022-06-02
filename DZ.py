# Задача 1
# import math
# n = 14
# m = 21

# print((n * m) // math.gcd(n , m))

# Задача 2
# import math
# from math import pi

# n = pi
# print(n)

# n = 100
# pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))


# Задача 3

# import math

# def is_prime(n):
#     primes = [2]
#     for num in range(3, n + 1, 2):
#         if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
#             primes.append(num)
#     return primes

# def get_prime_factors(n, primes):
#     fact = []
#     for i in primes:
#         while n % i == 0:
#             n = n / i
#             fact.append(i)
#     return fact

# n = int(input('Введите число: '))

# primes = is_prime(n)
# factors = get_prime_factors(n, primes)
# print(factors)

# def testing(n, factors):
#     return math.prod(factors) == n       

# print(testing(n, factors))

# def task3 (n):
#     i = 2
#     array = []
#     while n != 1: 
#         if n % i == 0:
#             array.append(i) #3
#             n = n / i
#             i = 2
#         else: 
#             i += 1
#     return (array)

# print (task3 (5))

 
# Задача 4

# from random import randint

# def list(size, m, n):
#     return [randint(m, n) for i in range(size)]

# def value(list):
#     return [i for i in set(list)]

# size = 10
# m = 1
# n = 10

# origin = list(size, m, n)
# print(origin)
# print(value(origin))