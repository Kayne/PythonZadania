import random

def fwd(litery, cyfry):
  koniec = []
  for i in range(len(litery)):
    wybrane = random.choice(cyfry)
    litery[i] = wybrane
    del cyfry[cyfry.index(wybrane)]
    koniec.append(litery[i])

  return koniec

print fwd(["a", "b", "c"], [0,1,2,3,4,5,6,7,8,9])

def szukaj(rownanie, start, visited, cyfry):
  i = 1
  lewa = 0
  prawa = 0
  for slowo in rownanie:
    for s in slowo:
      if i <= 2: 
        lewa += start[rownanie.index(s)]
      else:
        prawa += start[rownanie.index(s)]
  for n in fwd(start, cyfry):
    if tuple([n]) in visited:
      continue
    print start
    path = szukaj(rownanie, tuple([n]), visited|{tuple(start)}, cyfry)
    if path != []:
      return [start] + path
  return []

def zagadka(rownanie):
  rownanie = rownanie.split()
  del(rownanie[1])
  del(rownanie[2])
  return szukaj(rownanie, [0,0,0], set(), [0,1,2,3,4,5,6,7,8,9])

zagadka("a + b = c")