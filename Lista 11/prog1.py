#encoding: utf-8
import itertools
import random

slownik = {}
slowa = set()
znaki = list(u"aąbcćdeęfghijklłmnńoóprsśtuwyzźż")

def wczytajSlowa(plik, slowa):
  for slowo in open(plik):
    slowo = unicode(slowo.rstrip(), "utf-8")
    if len(slowo) == 4 or len(slowo) == 5:
      slowa.add(slowo)


wczytajSlowa("slowa_utf8.txt", slowa)

def fwd(start):
  wierzcholki = []
  start = list(start)
  temp = []
  for x in range(len(znaki)):
    for z in range(len(start)):
      temp = start[:]
      temp[z] = znaki[x]
      temp = u"".join(temp)
      if temp in slowa:
        wierzcholki.append(temp)
  return wierzcholki

#print fwd("woda")

def bfs(start):
  kolejka = [start]
  odwiedzone = {start}
  while kolejka != []:
    x = kolejka[0]
    del kolejka[0]
    for y in fwd(x):
      y = "".join(y)
      if not y in odwiedzone:
        odwiedzone.add(y)
        kolejka.append(y)
  return odwiedzone

zbior = set()
for x in slowa:
  if x not in zbior:
    wynik = bfs(x)
    zbior |= set(wynik)
    print "-"*5
    print u"Słowo bazowe: " + x
    print u"Wielkość: " + str(len(wynik))
    print u"Reprezentant: " + u"".join(random.sample(wynik, 1))
    if len(wynik)+1 <= 10:
      for z in wynik:
        print z,
      print ""