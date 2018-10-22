###############################################################
# Day 0: Mean, Median and Mode
###############################################################

# import sys
# from collections import Counter
# from statistics import mode

# cnt = Counter()

# for ln, line in enumerate(sys.stdin):
#     if ln == 0:
#         cnt = line.replace('\n', '')
#     else:
#         l = line.split()
#         l = list(map(int, l))
#         l.sort()
#         print(round((sum(l)/len(l)),1))
#         if len(l) % 2 == 0:
#             print(round(((l[int((len(l)/2))] + l[int((len(l)/2) - 1)])/2),1))
#         else:
#             print(l[int((len(l)/2))])

# mc = Counter(l).most_common()
# mc.sort(key=lambda sl:(-sl[1],sl[0]))

# print(mc[0][0])

###############################################################
# Day 0: Weighted Mean
###############################################################

# import sys

# for ln, line in enumerate(sys.stdin):
#     if ln == 0:
#         pass
#     if ln == 1:
#         l = line.split()
#         x = list(map(int, l))
#     if ln == 2:
#         l = line.split()
#         w = list(map(int,l))

# s = sum([a*b for a,b in zip (x,w)])/sum(w)

# print(round(s,1))

###############################################################
# Day 1: Standard Deviation
###############################################################

# import sys
# import math

# for ln, line in enumerate(sys.stdin):
#     if ln == 0:
#         n = int(line)
#     if ln == 1:
#         l = line.split()
#         x = list(map(int, l))

# mean = sum(x) / n

# sd = math.sqrt(sum([((i - mean)**2) for i in x]) / n)

# print(round(sd, 1))

###############################################################
# Day 1: Quartiles
###############################################################

# import sys
# from statistics import median

# for ln, line in enumerate(sys.stdin):
#     if ln == 0:
#         pass
#     if ln == 1:
#         l = line.split()
#         x = sorted(list(map(int, l)))

# if len(x) % 2 != 0:
#     q1 = median(x[:int((len(x) / 2))])
#     q2 = median(x)
#     q3 = median(x[int((len(x) / 2) + 1):])

# else:
#     q1 = median(x[:int(len(x) / 2)])
#     q2 = median(x)
#     q3 = median(x[int(len(x) / 2):])

# print('{0:.2f}'.format(q1).rstrip('0').rstrip('.'))
# print('{0:.2f}'.format(q2).rstrip('0').rstrip('.'))
# print('{0:.2f}'.format(q3).rstrip('0').rstrip('.'))

###############################################################
# Day 1: Interquartile Range
###############################################################

# import sys
# from statistics import median
# from itertools import chain, repeat

# for ln, line in enumerate(sys.stdin):
#     if ln == 0:
#         pass
#     if ln == 1:
#         l = line.split()
#         n = list(map(int, l))
#     if ln == 2:
#         l = line.split()
#         f = list(map(int, l))

# l = list(zip(n,f))

# l = [list(repeat(i,y)) for i,y in l]

# l = sorted(list(chain.from_iterable(l)))

# if len(l) % 2 != 0:
#     q1 = median(l[:int((len(l) / 2))])
#     q3 = median(l[int((len(l) / 2) + 1):])
# else:
#     q1 = median(l[:int(len(l) / 2)])
#     q3 = median(l[int(len(l) / 2):])

# print(round(float(q3-q1), 1))

###############################################################
# Day 2: Basic Probability
###############################################################

# Task

#     In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.

#Code

# import itertools

# x = [1, 2, 3, 4, 5, 6]

# ap = [p for p in itertools.product(x, repeat=2)]

# aps = [x for x in ap if sum(x) <= 9]

# print(aps)
# print(len(aps))

# print(ap)
# print(len(ap))

# print (round((len(aps)/len(ap)), 2))

# Answer

#     5/6

###############################################################
# Day 2: More Dice
###############################################################

# Task

#     In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die will be different and the two dice have a sum of 6.

#Code

# import itertools

# x = [1, 2, 3, 4, 5, 6]

# ap = [p for p in itertools.product(x, repeat=2)]

# aps = [x for x in ap if sum(x) == 6 and x[0] != x[1]]

# print(aps)
# print(len(aps))

# print(ap)
# print(len(ap))

# print (round((len(aps)/len(ap)), 2))

# Answer

#     1/9

###############################################################
# Day 2: Compound Event Probability
###############################################################

# Task

#     There are 3 urns labeled X, Y, and Z.

# Urn X contains 4 red balls and 3 black balls.
# Urn  contains 5 red balls and 4 black balls.
# Urn  contains 4 red balls and 4 black balls.

# One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?

# Code

# 1. 4/7 r, 3/7 b
# 2. 5/9 r, 4/9 b
# 3. 4/8 r, 4/8 b

#   (4/7)(5/9)(4/8) + (4/7)(4/9)(4/8) + (3/7)(5/9)(4/8)

# Answer

#   17/24

###############################################################
# Day 3: Conditional Probability
###############################################################

# Task

#     Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?

#Code

# import itertools

# x = [0, 1, 0, 1]

# ap = [p for p in itertools.product(x, repeat=2)]

# apall = [x for x in ap if sum(x) >= 1]

# ap2b = [x for x in apall if sum(x) == 2]

# print(len(apall))
# print(len(ap2b))

# print(len(ap2b)/len(apall))

# Answer

#     1/3

###############################################################
# Day 3: Cards of the Same Suit
###############################################################

# Task

#     You draw 2 cards from a standard 52-card deck without replacing them. What is the probability that both cards are of the same suit?

# Answer

    # 12/51

###############################################################
# Day 3: Drawing Marbles
###############################################################

# Task

#     A bag contains 3 red marbles and 4 blue marbles. Then, 2 marbles are drawn from the bag, at random, without replacement. If the first marble drawn is red, what is the probability that the second marble is blue?

# Answer

#     2/3

###############################################################
# Day 4: Binomial Distribution I
###############################################################

# import sys
# import math

# n = 6

# for line in sys.stdin:
#     i,x = line.split()
#     p = float(i) / (1 + float(i))

# k3 = sum([((math.factorial(n) / (math.factorial(k) * math.factorial(n-k))) * (p**k) * ((1 - p)**(n-k))) for k in range(3,7)])

# print(round(k3, 3))

###############################################################
# Day 4: Binomial Distribution II
###############################################################

