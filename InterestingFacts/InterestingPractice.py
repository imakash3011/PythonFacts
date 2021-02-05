from itertools import product, chain, combinations, permutations
from collections import Counter
import math
import heapq
from statistics import mean, median, mode
import functools

l1 = [1, 1, 2, 3, 4]
l2 = [5, 6, 7, 8]
str1 = "abc"

print(list(product(l1,l2)))
print(list(chain(l1,l2)))
print(list(combinations(str1,2)))
print(Counter(l1))
print(math.factorial(5))

heapq.heapify(l1)
print(heapq.nlargest(1, l2))

print(mean(l1))
print(median(l2))
print(mode(l1))
print(list(permutations(str1)))
print(functools.reduce(lambda x,y:x*y, l2))


