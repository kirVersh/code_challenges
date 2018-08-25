###############################################################
# 1. Multiples of 3 and 5
###############################################################

# # var.1

# a = list (range(0,1000))
# b = 0
# for i in a:
#     if i%3 == 0:
#         if not i%5 == 0:
#             b+=i
#     if i%5 == 0:
#         if not i%3 == 0:
#             b+=i
#     if i%5 == 0 and i%3 == 0:
#         b+=i
# print(b)

# # var.2

# l = [x for x in range(1,1000)]
# print(sum(list(filter(lambda x:x%3==0 or x%5==0,l))))

###############################################################
# 2. Even Fibonacci numbers
###############################################################

# # var.1

# def fib_recursive(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib_recursive(n-1) + fib_recursive(n-2)

# a = [fib_recursive(i) for i in range(34)]

# l = [x for x in a]

# print(sum(list(filter(lambda x:x%2 == 0,l))))

# # var.2

# def even_fibs(n):
#     a, b = 0, 2
#     while b < n:
#         a, b = b, 4 * b + a
#     return (a + b - 2) / 4

# print (int(even_fibs(4000000)))

###############################################################
# 3. Largest prime factor
###############################################################

# # var.1

# n = 600851475143
# i = 2
# while i * i < n:
#      while n % i == 0:
#          n = n / i
#      i = i + 1

# print (n)

# # var.2

# import math
# def lowestprimefactor(num):
#     primes=[2]
#     if num%2==0:
#         return 2
#     for i in range(2,num+1):
#         for k in primes:
#             if i%k==0:
#                 break
#             elif k>=math.ceil(i**0.5):
#                 primes.append(i)
#                 if num%i==0:
#                     return i
#                 break
#             else:
#                 continue

# def primefactors(num):
#     x=num
#     primelist=[]
#     while lowestprimefactor(x)<x:
#         primelist.append(lowestprimefactor(x))
#         x=int(x/lowestprimefactor(x))
#     primelist.append(x)
#     print (primelist)

# primefactors(600851475143)

###############################################################
# 4. Largest palindrome product
###############################################################

# # var.1

# l = list(range((100*100),(999*999)))
# a = []
# for x in l:
#     if len(str(x)) == 5:
#         if str(x)[0] == str(x)[-1] and str(x)[1] == str(x)[-2] and str(x)[2] == str(x)[-3]:
#             a.append(x)
#     if len(str(x)) == 6:
#         if str(x)[0] == str(x)[-1] and str(x)[1] == str(x)[-2] and str(x)[2] == str(x)[-3] and str(x)[3] == str(x)[-4]:
#             a.append(x)

# b = list(range(100,1000))
# c = list(range(100,1000))
# d = list(m*i for m in b for i in c)
# e = list(filter(lambda x: x in a, d))

# e.sort()

# print(e)

# # var.2

# p = 999
# n = 0
# max = 0
# while p > 0:
#     while n != p:
#         num = p * (p-n)
#         if num > max:
#             if num == int(str(num)[::-1]):
#                 max = num
#         n += 1
#     else:
#         p -= 1
#         n = 0
# else:
#     print (max)

# #var.3

# nums =[]
# for i in range(100, 1000):
#     for j in range(100, 1000):
#         if str(i * j) == str(i * j)[::-1]:
#             nums.append(i * j)
# print("The largest palindrome product is", max(nums))

###############################################################
# 5. Smallest multiple
###############################################################

# # var.1

# f = math.factorial(20)
# # f = 931170240
# # f = 232792560
# i = 2
# l = []
# while i != 20:
#     f = f/i
#     i2 = 2
#     f2 = f
#     l.append(int(f))
#     while i2 != 20:
#         f2 = f2/i2
#         l.append(int(f2))
#         i2 += 1
#     i += 1

# a = list(set(l))
# a.sort()
# print(a)

# def div_by(self):
#     l2 = a
#     for i in range(2, self):
#         l1 = [x for x in a if x % i == 0]
#         l3 = set(l2) & set(l1)
#         l2 = l3
#     l3 = list(l3)
#     l3.sort()
#     return l3

# print(div_by(20))

# # var.2

# smallest=20
# found = False
# while (found==False):
#     check=0
#     for k in range(1,21):
#         if(smallest%k==0):
#             check+=1
#     if(check==20):
#         print (smallest)
#         found=True
#     smallest+=20

# # var.3

# import functools
# print(functools.reduce(lambda x,y:x*y,[5,7,9,11,13,16,17,19]))

###############################################################
# 6. Sum square difference
###############################################################

# # var.1

# import functools

# print(((functools.reduce(lambda x,y:x+y,(list(range(1,101)))))**2)-(functools.reduce(lambda x,y:x+y**2,(list(range(1,101))))))

# # var.2

# def diff(n):
#   return pow(sum([x for x in range(n+1)]),2) - sum([x**2 for x in range(n+1)])
# print (diff(100))

###############################################################
# 7. 10001st prime
###############################################################

# # var.1

# from sympy import sieve

# i = 0
# l = len(sieve._list)

# while l != 10002:
#     i in sieve
#     i += 1
#     l = len(sieve._list)
# print(sieve._list)
# print(len(sieve._list))

# # var.2

# a=[2,3,5,7]
# b=11
# while len(a)<=10001:
#     for x in range(3,int(b**0.5)+1):
#         number=b%x
#         if number==0:
#             b=b+2
#             break
#         elif x==int(b**0.5):
#             a.append(b)
#             b=b+2
# print(a[10000])

###############################################################
# 8. Largest product in a series
###############################################################

# # var.1

# import operator
# import functools

# l = list('7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450')

# n = 1
# i1 = 0
# i2 = 13
# d = {}

# while i2 != 1001:
#     a = [int(x) for x in l[i1:i2]]
#     a = functools.reduce(lambda x,y:x*y,a)
#     d.update({n : a})
#     n += 1
#     i1 += 1
#     i2 += 1

# md = max(d.items(), key=operator.itemgetter(1))[0]

# print(d[md])

# # var.2

# from functools import reduce

# one_thousand_digits = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

# def fn(nr_of_digits):
#     max_nr = idx = 0
#     while idx < len(one_thousand_digits) - nr_of_digits:
#         max_nr = max(
#             max_nr,
#             reduce(
#                 lambda x, y: x * y,
#                 [int(digit) for digit in one_thousand_digits[idx:idx+nr_of_digits]]
#             )
#         )
#         idx += 1
#     return max_nr


# print(fn(13))

###############################################################
# 9. Special Pythagorean triplet
###############################################################

# # var.1

# a = list(map(lambda x: x**2, list(range(0,1000))))

# axs = {}

# i1 = 0
# i2 = 0

# while i1 != 1000:
#     i2 = 0
#     for x in a:
#         xs = a[i1]+x
#         if xs in a:
#             i3 = a.index(xs)
#             n = i1+i2+i3
#             if n == 1000 and i1*i2*i3 != 0:
#                 axs.update({n : xs})
#                 print(i1,i2,i3)
#                 print(i1*i2*i3)
#             if len(axs) == 1:
#                 break
#         i2 += 1
#     i1 += 1


# # var.2

# for a in range(1,1000):
#     for b in range(a+1,1000):
#         if 2*1000*(a+b) == (1000)**2+2*a*b:
#             print (a*b*(1000-(a+b)))

###############################################################
# 10. Summation of primes
###############################################################

# # var.1

# from sympy import sieve
# print(sum([i for i in sieve.primerange(0, 2000000)]))

# # var.2

# def sumOfPrimes(limit):
#     a = [True] * limit
#     a[0]=a[1]=False

#     for counter, candidate in enumerate(a):
#         if not counter % 2:
#             a[counter] = False
#         if candidate:
#             yield counter
#             for n in range(counter**2, limit, counter):
#                 a[n] = False
# print(sum(list(sumOfPrimes(2*10**6))))
