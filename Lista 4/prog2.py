import random
from random import randint

def randperm(n):
  return random.sample([i for i in xrange(1,n)], n-1)

#x = randperm(10 ** 6)
print randperm(10)