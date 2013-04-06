#encoding: utf-8
LITERKI = u"aąbcćdeęfghijklłmnńoóprsśtuwyzźż"

def wczytaj_listy(plik):
  slowa = []
  plik = open(plik)
  for slowo in plik:
    slowo = unicode(slowo.rstrip(), "utf-8")
    slowa.append(slowo)
  return slowa

def odszyfruj(zdanie, przesuniecie = 1):
  output = ""
  for char in zdanie:
    if char != " ":
      if LITERKI.index(char)+przesuniecie > len(LITERKI)-1:
        move = 32 - abs(LITERKI.index(char)+przesuniecie)
        if move < 0:
          move *= (-1)
      else:
        move = LITERKI.index(char)+przesuniecie
      output += LITERKI[move]
    else:
      output += " "
  return output

def wczytaj_slowa(plik):
  slowa = set()
  plik = open(plik)
  for slowo in plik:
    slowo = unicode(slowo.rstrip(), "utf-8")
    slowa.add(slowo)
  return slowa


if __name__ == "__main__":

  listy = wczytaj_listy("listy.txt")
  slowa = wczytaj_slowa("slowa_utf8.txt")
  w = 0
  for slowo in listy:
    w += 1
    print "List numer " + str(w)
    for i in xrange(33):
      nie_ma = False
      slowo = odszyfruj(slowo, i)
      slowo2 = slowo.split()
      for s in slowo2:
        if s in slowa:
          continue
        else:
          nie_ma = True
          break
      if nie_ma != True:
        print slowo