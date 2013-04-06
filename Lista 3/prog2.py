from math import sqrt

def pierwsza(n):
  for i in range(2, int(sqrt(n))):
    if n % i == 0:
      return False
  return True

for i in range(2,100000):
  if pierwsza(i):
    counter = 0
    last = 0
    for q in str(i):
      if last == q and q == str(7):
        counter = counter + 1
      else:
        last = q
    if counter == 2:
      print i