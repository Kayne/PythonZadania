#encoding: utf-8
from prog1 import na_slownik
from prog2 import *
import copy

def ukladalne(start, koniec):
  dictionary = {}
  for char in start:
    if char in koniec:
      if start[char] >= koniec[char]:
        dictionary[char] = 0
      else:
        break
  for char in dictionary:
    if dictionary[char] > 0:
      return False
      break
  return True


slowa = wczytaj_slowa('rzeczowniki_utf8.txt')
slowa2 = sorted(slowa, key=len)
slowa = slowa2[:]
slowa.reverse()

dic = {}
sloweczka = {}
uzyte = set()

uzyte2 = {}
for slowo in set(slowa):
  uzyte2[slowo] = na_slownik(slowo)

w = 0

for slowo in slowa:
  w += 1
  #print w
  if (w / 1000 != 0):
    print w
  if slowo in uzyte:
    continue

  dlugosc = len(slowo)
  slowniczkowo = na_slownik(slowo)

  for slowo2 in slowa2:

    if len(slowo2) > dlugosc:
      break
    if slowo == slowo2:
      continue
    #if ukladalne(slowniczkowo, uzyte2[slowo2]):
    #  try:
    #    dic[slowo] += 1
    #  except:
    #    dic[slowo] = 1
    #  uzyte.add(slowo)

print max(dic, key=dic.get)
print dic["przeintelektualizowanie"]
print dic["kapelmistrzowanie"]