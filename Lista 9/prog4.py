

from copy import deepcopy

Etap = 1

Nazwiska = {}
Zadania = {}
Punktacja = {}

for x in open("dane.txt"):
   L = x.split()
   if len(L) == 0: 
      continue
  
   if x[0] == "#":
      Etap += 1
      continue
     
   if Etap == 1:
      if len(L) == 3:
        Nazwiska[L[0]] = L[1] + " " + L[2]
      elif len(L) == 2:
        Nazwiska[L[0]] = L[1]
      else:
        continue
      Zadania[L[0]] = set()
   elif Etap == 2:
    Punktacja[L[0]] = L[1]
   else:
      if len(L) == 2:
        ksywka, wynikPracowni = L
        for z in wynikPracowni.split(","):
          try:
            Zadania[ksywka].add(z)
          except:
            Zadania[ksywka] = set()
            Zadania[ksywka].add(z)
      else:
        continue


Zadania2 = {}
Zadania3 = deepcopy(Zadania)
for key,value in Zadania.iteritems():
  if value:
    zapas = set()
    while len(value) > 0:
      cos = value.pop()
      if cos in Punktacja:
        zapas.add(float(Punktacja[cos]))
    Zadania2[key] = zapas
    continue

for key, value in Zadania.iteritems():
  try:
    Zadania2[key]
  except:
    Zadania2[key] = set()

print "RAPORT"
for ksywka in sorted( Nazwiska.keys(), key = lambda x: sum(Zadania2[x])):
   print Nazwiska[ksywka], "zdobyl", sum(Zadania2[ksywka]), "pkt za zadania:",
   for i in Zadania3[ksywka]:
    print str(i)+" ",
   print ""