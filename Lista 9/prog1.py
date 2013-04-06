#encoding: utf-8
import re

def zwroc_reszte(rozkaz, odkad=2):
  size = len(rozkaz)-odkad
  rozmiarek = ""
  for s in range(size):
    rozmiarek += rozkaz[odkad+s]
  return rozmiarek

def wczytaj_etykiety(rozkazy):
  PC = -1
  etykiety = {}
  p = re.compile('\w+:')
  while PC < len(rozkazy)-1:
    PC += 1
    rozkaz = rozkazy[PC]
    rozkaz = rozkaz.split(" ")

    if p.match(rozkaz[0]):
      etykiety[rozkaz[0][:-1]] = PC-1
  return etykiety

def wczytaj_liste_rozkazow(rozkazy):
  rozkazy = rozkazy.split("\n")
  etykiety = wczytaj_etykiety(rozkazy)
  zmienne = {}
  p = re.compile('\w+:')

  PC = 0

  while PC < len(rozkazy)-1:
    PC += 1
    rozkaz = rozkazy[PC]
    rozkaz = rozkaz.split(" ")
    if rozkaz[0] == "" or rozkaz[0] == " ":
      continue
    if p.match(rozkaz[0]):
      del(rozkaz[0])
    if rozkaz[0] == "#":
      continue
    elif rozkaz[0] == "print":
      print eval(zwroc_reszte(rozkaz, 1), zmienne)
    elif rozkaz[1] == "=":
      zmienne[rozkaz[0]] = eval(zwroc_reszte(rozkaz), zmienne)
    elif rozkaz[0] == "goto_if_true":
      if zmienne["$$"] == True:
        PC = etykiety[rozkaz[1]]
    elif rozkaz[0] == "goto":
      PC = etykiety[rozkaz[1]]
    


program = """
n = input("Podaj liczbe ")
n0 = n
print n0
sil = 1

start: $$ = n <= 0
goto_if_true koniec
sil = sil * n
n = n - 1 
goto start

koniec: print "Silnia(" + str(n0) + ") = " + str(sil)
"""
program2 = """
w = input("Podaj liczbę: ")
w0 = w
p = input("Podaj potęgę: ")
p0 = p

start: $$ = p <= 1
goto_if_true koniec
w = w * w
p = p - 1
goto start

koniec: print "Potęga liczby " + str(w0) + " stopnia " + str(p0) + " wynosi: " + str(w)
"""
program3 = """
w = input("Podaj liczbę: ")
p = input("Podaj drugą liczbę: ")

z = w + p

print str(w) + " + " + str(p) + " = " + str(z)
"""
program4 = """
w = input("Podaj liczbę: ")
i = w

$$ = w < 0
goto_if_true nie_jest

$$ = w == 1
goto_if_true nie_jest

$$ = w == 2
goto_if_true koniec

podzielone = w / 2
$$ = (podzielone * 2)-1 == 0
goto_if_true nie_jest

dzielnik = 3

while: $$ = dzielnik <= podzielone
print dzielnik,podzielone
goto_if_true sprawdz
print dzielnik,podzielone
goto koniec

sprawdz: $$ = ((int(w) / int(dzielnik)) * int(dzielnik)) - int(w) == 0
goto_if_true nie_jest
((int(w) / int(dzielnik)) * int(dzielnik)) - int(w)

dzielnik = dzielnik + 1
goto while

nie_jest: print "nie jest pierwsza"
goto koniec_2

koniec: print "jest pierwsza"
koniec_2: print ""
"""


etykiety = {}
zmienne = {}

wczytaj_liste_rozkazow(program)
print "Drugi program: "
wczytaj_liste_rozkazow(program2)
print "Trzeci program: "
wczytaj_liste_rozkazow(program3)
print "Czwarty program: "
wczytaj_liste_rozkazow(program4)