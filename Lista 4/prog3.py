# -*- coding: utf-8 -*-

from random import randint

def mediana(lista):
  posortowana = sorted(lista)
  dlugosc = len(lista)
  if not dlugosc % 2:
    return (posortowana[dlugosc / 2] + posortowana[dlugosc / 2 - 1]) / 2.0
  return posortowana[dlugosc / 2]

def smok():
  g = 0
  a = 1
  b = c = d = e = f = x = 0
  while True:
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
        win = True
        break
    if win == True:
      return g
      break

def analizaSmoka(n):
  ilosc_rzutow = 0
  najkrotsza_gra = 0
  najdluzsza_gra = 0
  srednia = []
  for iteracja in range(n):
    serii = smok()
    if najkrotsza_gra == 0 or najkrotsza_gra > serii:
      najkrotsza_gra = serii
    if najdluzsza_gra < serii:
      najdluzsza_gra = serii
    srednia.append(serii)
    
  print "Liczba gier: " + str(n)
  print "Najkrótsza gra: " + str(najkrotsza_gra)
  print "Najdłuższa gra: " + str(najdluzsza_gra)
  print "Średnia gra: " + str(round(sum(srednia)/float(len(srednia)), 2))
  print "Mediana: " + str(mediana(srednia))

analizaSmoka(1000)