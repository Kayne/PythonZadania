# -*- coding: utf-8 -*-
# Marcin Bratek (247919)

# Metoda licząca silnię
def silnia(a):
  w = 1
  for i in range(a):
    w = w * (i+1)
  return w

for i in range(4,101):
  if len(str(silnia(i))) in range(5):
    print str(i) + "! ma " + str(len(str(silnia(i)))) + " cyfry"
  else:
    print str(i) + "! ma " + str(len(str(silnia(i)))) + " cyfr"
