# -*- coding: utf-8 -*-

from random import randint
import time



def kostka(k):
  last = 2
  counter = 0
  win = False
  while True:
    for w in xrange(1,101):
      x = randint(0,1)
      if x == 1 and (last == x or last == 2):
        counter += 1
      else:
        counter = 0
      last = x
      if counter == k:
        win = True
        break
    if win == True:
      break
  if win == True:
    return w
  else:
    return 0


def analizaKostki(n, k):
  #ilosc_rzutow = 0
  #najkrotsza_gra = 0
  #najdluzsza_gra = 0
  srednia = []
  #przegranych = 0
  serii = 0.0
  for iteracja in xrange(n):
    serii = kostka(k)
    #if (serii == 0):
    #  przegranych += 1
    #  continue
    #if najkrotsza_gra == 0 or najkrotsza_gra > serii:
    #  najkrotsza_gra = serii
    #if najdluzsza_gra < serii:
    #  najdluzsza_gra = serii
    srednia.append(serii)
  srednich = round(sum(srednia)/float(len(srednia)), 2)  
  #print "Liczba gier: " + str(n)
  #print "Najkrótsza gra: " + str(najkrotsza_gra)
  #print "Najdłuższa gra: " + str(najdluzsza_gra)
  #print "Średnia gra: " + str(srednich)
  #print "Mediana: " + str(mediana(srednia))
  #print "Przegranych gier: " + str(przegranych)
  return srednich

wynik = {}
for z in xrange(2,15):
  kkk = analizaKostki(1000, z)
  wynik[z] = int(kkk)

def find_key(dic, val):
  for i in dic.keys():
    if dic[i] == val:
      return i
      break

maks = max(wynik.values())
print "Średnia: " + str(maks) + " K: " + str(find_key(wynik, maks))