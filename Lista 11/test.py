#-*- coding: utf-8 -*-
slowa=[]
for w in open(u"slowa_utf8.txt", "r"):
    slowa.append(w[:-1]) ##slowa z kodowaniem
slowa2=[]
slowo=u"woda"
wynik=u"wino"
for i in range (len(slowa)):
  if len(slowa[i])==len(slowo):
    kurde=slowa[i]
    kurde.lower()
    slowa2.append(kurde)

def ukladalne(slowo):
  ukladalne=[]
  for i in range(len(slowa2)):
    poprawnosc=0
    kurde=slowa2[i]
    for j in range(len(slowo)):
      try:
        if slowo[j] in kurde[j]:
          poprawnosc+=1
        if poprawnosc==len(slowo)-1:
          ukladalne.append(slowa2[i])
      except UnicodeDecodeError:
        poprawnosc=poprawnosc
# licznik=len(ukladalne)-1
# while licznik>0:
#   if ukladalne[licznik]==slowo:
#     del ukladalne[licznik]
#   licznik-=1
  return ukladalne

def polaczenie(string1,string2,droga):
  w=ukladalne(string1)
  Q=w
  V=list(w)
  V.append(string1)
  for i in Q:
    if string2 == i:
      droga.append(string2)
      return droga
  while Q != []:
    w=ukladalne(Q[0])
    a=Q[0]
    del Q[0]
    for w1 in range(len(w)):
      if w[w1] not in V:
        V.append(w[w1])
        Q.append(w[w1])
        if w[w1]==string2:
          droga.append(string2)
          return polaczenie(string1,a,droga)
def wypisz(string1,string2):
  droga=polaczenie(string1,string2,[])
  droga.append(string1)
  for i in range(len(droga)-1,-1,-1):
    print droga[i]
wypisz("woda","wata")
#print polaczenie("woda","wino",[])