###########################################################
# 1. Sum of all the multiples of 3 or 5
###########################################################

## var.1

# def find(n):
#   l = []
#   nm = 1
#   while nm != n+1:
#       l.append(nm)
#       nm+=1
#   l = sum(list(filter(lambda x:x%3 == 0 or x%5 == 0,l)))

#   return l

# # var.2

# def find(n):
#     return sum(e for e in range(1, n+1) if e % 3 == 0 or e % 5 == 0)
