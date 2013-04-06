#encoding: utf-8

slowa = set()
znaki = list(u"aąbcćdeęfghijklłmnńoóprsśtuwyzźż")

def wczytajSlowa(plik, slowa):
  for slowo in open(plik):
    slowo = unicode(slowo.rstrip(), "utf-8")
    if len(slowo) >= 4:
      slowa.add(slowo)

wczytajSlowa("slowa_utf8.txt", slowa)

def fwd(start):
  wierzcholki = set()
  if start[:-1] in slowa:
    wierzcholki.add(start[:-1])
  if start[1:] in slowa:
    wierzcholki.add(start[1:])
  for x in znaki:
    if x+start in slowa:
      wierzcholki.add(x+start)
    if start+x in slowa:
      wierzcholki.add(start+x)
  for x in xrange(len(start)):
    for y in xrange(len(start)):
      temp = list(start)
      q = temp[x]
      temp[x] = temp[y]
      temp[y] = q
      temp = u"".join(temp)
      if temp in slowa:
        wierzcholki.add(temp)
  return list(wierzcholki)

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

def bfs2(start,koniec,droga):
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
          return bfs2(start, x, droga)

def najkrotsze(start,koniec):
  droga = bfs2(start,koniec,[])
  droga.append(start)
  for i in range(len(droga)-1,-1,-1):
    print droga[i],
  print ""

najkrotsze("parka", "lanca")
#print bfs(u"parka")