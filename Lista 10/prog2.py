import itertools


def rozwiaz(zagadka):
  print zagadka
  zagadka = zagadka.replace("=", "==")
  zagadka = zagadka.replace("+", "==")
  for i in "-/* ":
    zagadka = zagadka.replace(i, "")
  zagadka = zagadka.split("==")
  unikalnych = len(set([i for i in "".join(["%s" % el for el in zagadka])]))
  koniec = {}

  for i in itertools.permutations("9876543210", unikalnych):
    koniec = {}
    lewa = ""
    prawa = ""
    ostatnie = ""
    wylosowana = "".join(["%s" % el for el in i])
    counter = 0
    for j in set([i for i in "".join(["%s" % el for el in zagadka])]):
      koniec[j] = wylosowana[counter]
      counter += 1
    lewa_str = [str(i) for i in zagadka[0]]
    prawa_str = [str(i) for i in zagadka[1]]
    ostatnie_str = [str(i) for i in zagadka[2]]
    przesuniecie = 0

    for j in xrange(len(lewa_str)):
      lewa += koniec[lewa_str[j]]
    for j in xrange(len(prawa_str)):
      prawa += koniec[prawa_str[j]]
    for j in xrange(len(ostatnie_str)):
      ostatnie += koniec[ostatnie_str[j]]
    
    if int(lewa) + int(prawa) == int(ostatnie):
      break
  if int(lewa) + int(prawa) == int(ostatnie):
    print lewa," + ",prawa," = ",int(ostatnie)
    return koniec
  return {}

print rozwiaz("send + more = money")
print rozwiaz("choo + choo = train")
print rozwiaz("ciacho + ciacho = nadwaga")
print rozwiaz("abcde + fghij = g")