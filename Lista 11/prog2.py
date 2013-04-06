#encoding: utf-8
slowa = []

for slowo in open("slowa_utf8.txt"):
  slowo = unicode(slowo.rstrip(), "utf-8")
  if len(slowo) == 4 or len(slowo) == 5:
    slowa.append(slowo)

znaki = list(u"aąbcćdeęfghijklłmnńoóprsśtuwyzźż")

def fwd(start):
  wierzcholki = []
  start = list(start)
  temp = []
  for x in range(len(znaki)):
    for z in range(len(start)):
      temp = start[:]
      temp[z] = znaki[x]
      temp = "".join(temp)
      if temp in slowa:
        wierzcholki.append(temp)
  return wierzcholki

def bfs(start,koniec,droga):
  w = fwd(start)
  kolejka = w
  odwiedzone = list(w)
  odwiedzone.append(start)
  for i in kolejka:
    if koniec == i:
      droga.append(koniec)
      return droga
  while kolejka != []:
    x = kolejka[0]
    del kolejka[0]
    for y in fwd(x):
      if y not in odwiedzone:
        odwiedzone.append(y)
        kolejka.append(y)
        if y == koniec:
          droga.append(koniec)
          return bfs(start, x, droga)

def znajdzDroge(start,koniec):
  droga = bfs(start,koniec,[])
  droga.append(start)
  for i in range(len(droga)-1,-1,-1):
    print droga[i],
  print ""

znajdzDroge("woda","wino")