#encoding: utf-8
"""
Wprawka 6 (13.12) dla grupy MSZ
"""

rzeczowniki_z_popularnoscia = {}
for s in open("popularnosc_rzeczownikow_utf8.txt"):
  s = unicode(s.rstrip(), "utf-8")
  sl = s.split()
  pop = sl[1]
  sl = sl[0]
  rzeczowniki_z_popularnoscia[sl] = pop.lower()

slowa = []
slowa_cale = []

for s in open("dziewczynailalka.txt"):
  s = unicode(s.rstrip(), "utf-8")
  rozbite = s.split()
  for s2 in rozbite:
    if s2 == "-":
      continue
    for i in "+-.,:' ":
      s2 = s2.replace(i, "")
    slowa.append(s2.lower())

calosc = 0
policzonych_slow = 0
for i in slowa:
  try:
    calosc += int(rzeczowniki_z_popularnoscia[i])
    policzonych_slow += 1
  except:
    pass

print "Popularność sumaryczna: " + str(calosc)
print "Policznych słów: " + str(policzonych_slow)
print "Popularność średnia:" + str(calosc/policzonych_slow)