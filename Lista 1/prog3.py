# -*- coding: utf-8 -*-
# Marcin Bratek (247919)

from random import randint

g = 1
a = 1
b = c = d = e = f = x = 0
while True:
  if a == b and b == c and c == d and d == e:
    print "Najdłuższy podciąg składał się z 5 cyfr w serii " + str(g)
  elif a == b and b == c and c == d:
    print "Najdłuższy podciąg składał się z 4 cyfr w serii " + str(g)
  elif a == b and b == c:
    print "Najdłuższy podciąg składał się z 3 cyfr w serii " + str(g)
  elif a == b:
    print "Najdłuższy podciąg składał się z 2 cyfr w serii " + str(g)

  i = 1
  a = 1
  b = c = d = e = f = 0
  win = False
  
  g = g + 1
  for w in range(100):
    x = randint(1,6)
    if i == 1:
      a = x
    elif i == 2:
      b = x
    elif i == 3:
      c = x
    elif i == 4:
      d = x
    elif i == 5:
      e = x
    elif i == 6:
      f = x
    i = i + 1
    if i > 6:
      i = 1
    if a == b and b == c and c == d and d == e and e == f:
      print "Ostatnia seria:"
      print a,b,c,d,e,f
      win = True
      break
  if win == True:
    print "Odbyło się w sumie " + str(g) + " serii"
    break