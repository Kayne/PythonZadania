#encoding: utf-8
from prog1 import ukladalne, na_slownik
from prog2 import *

POPULARNOSC = 1000

slowa = wczytaj_slowa('popularnosc_rzeczownikow_utf8.txt')
slowa = set(slowa)

def sprawdz_slowo(slowo):
  q = slowo.split()
  if len(q[0]) == 8 or len(q[0]) == 9 or len(q[0]) == 10:
    if int(''.join(slowo.split()[1:])) > POPULARNOSC:
      return True
  return False

def sprawdz_slowo2(slowo):
  q = slowo.split()
  if int(''.join(slowo.split()[1:])) > POPULARNOSC:
    return True
  return False

w = 0
dic = {}

for slowo in slowa:
  sl = slowo.split()
  sl = sl[0]

  if sprawdz_slowo(slowo):
    w += 1
    for slowo2 in slowa:
      sl2 = slowo2.split()
      sl2 = sl2[0]
      if sl == sl2:
        continue
      if sprawdz_slowo2(slowo2):
        if ukladalne(sl, sl2):
          if sl in dic:
            dic[sl] += 1
          else:
            dic[sl] = 1
          continue

if dic:
  print max(dic, key=dic.get)
else:
  print "Nie ma takiego słowa :("
print "Sprawdzono " + str(w) + " liderów."
