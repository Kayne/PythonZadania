# -*- coding: utf-8 -*-
# Marcin Bratek (247919)

# Metoda licząca silnię
def silnia(a):
  w = 1
  for i in range(a):
    w = w * (i+1)
  return w

i = 1
while True:
  if len(str(silnia(i))) <= 100:
    if len(str(silnia(i))) == 1:
      print str(i) + "! ma " + str(len(str(silnia(i)))) + " cyfrę"
    elif len(str(silnia(i))) in range(2,5):
      print str(i) + "! ma " + str(len(str(silnia(i)))) + " cyfry"
    else:
      print str(i) + "! ma " + str(len(str(silnia(i)))) + " cyfr"
    i = i + 1
  else:
    break
