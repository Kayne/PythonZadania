#encoding: utf-8
def ukladalne(start, koniec):
  for char in start:
    if char in koniec:
      if start[char] >= koniec[char]:
        continue
      else:
        return False
  return True

def na_slownik(wyraz):
  dic = {}
  for char in wyraz:
    if char in dic:
      dic[char] += 1
    else:
      dic[char] = 1
  return dic

slowa = []
slowa_cale = []
for s in open("Lalka.txt"):
  s = unicode(s.rstrip(), "utf-8")
  rozbite = s.split()
  for s2 in rozbite:
    if s2 == "-":
      continue
    slowa.append(s2[0].lower())
    slowa_cale.append(s2.lower())


wyraz = "".join(slowa)
wyraz_slownikowy = na_slownik(wyraz)


rzeczowniki = set()
rzeczowniki_z_popularnoscia = {}
for s in open("popularnosc_rzeczownikow_utf8.txt"):
  s = unicode(s.rstrip(), "utf-8")
  sl = s.split()
  pop = sl[1]
  sl = sl[0]
  if len(sl) in xrange(3,8):
    if ukladalne(wyraz_slownikowy, na_slownik(sl)):
      rzeczowniki.add(sl.lower())
      rzeczowniki_z_popularnoscia[sl] = pop

secik = set()

for s in rzeczowniki:
  if s in wyraz:
    secik.add(s)

secik2 = set()

maksik = len(max(secik, key=len))
for s in secik:
  if len(s) == maksik:
    secik2.add(s)

ostatnie = set()
poprzednie = 0
nazwa = ""
for key in secik2:
  if poprzednie == 0:
    poprzednie = rzeczowniki_z_popularnoscia[key]
    nazwa = key
    continue
  else:
    if rzeczowniki_z_popularnoscia[key] > poprzednie:
      poprzednie = rzeczowniki_z_popularnoscia[key]
      nazwa = key
    elif rzeczowniki_z_popularnoscia[key] == poprzednie:
      if rzeczowniki_z_popularnoscia[key] < nazwa:
        poprzednie = rzeczowniki_z_popularnoscia[key]
        nazwa = key

print "Ukryte przesłanie to:",
print nazwa
print "Występuje w zdaniu:",

tablica = []
i = 0
ostatni = 0
for s in xrange(len(slowa_cale)):
  if i > len(nazwa)-1:
    i = 0
  if slowa_cale[s][0] == nazwa[i]:
    tablica.append(slowa_cale[s])
    i += 1
  else:
    i = 0
    tablica = []
  if i == len(nazwa):
    ostatni = s
    break

for i in reversed(xrange(3)):
  print slowa_cale[s-len(nazwa)-i],
for i in tablica:
  print i,
for i in xrange(3):
  print slowa_cale[s+i+1],
