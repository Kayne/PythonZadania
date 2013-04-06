#encoding: utf-8
import random
from prog3_plansza import *
from prog3_gra import *
from prog3_prezenter import *
from prog3_komputer import *



gra = Gra()

gra.ileGraczy = int(raw_input("Ilu graczy? (1 lub 2): "))
if gra.ileGraczy > 1:
  gra.komputer = int(raw_input("Czy grać z komputerem? (1 dla tak): "))
else:
  gra.limitRuchow = int(raw_input("Jaki limit ruchów?: "))
  gra.ustawRuchy()
  gra.komputer = 0

prezenter = Prezenter()
plansza = Plansza(gra.dozwoloneKolory, gra.ileGraczy, 5, 5)
plansza.drukujPlansze()

if (gra.ileGraczy > 1):
  komputer = Komputer()

while True:
  if gra.ileGraczy > 1:
    wynik = gra.sprawdzWygrana(plansza)
    if wynik in range(1,4):
      prezenter.wyswietlWygrana(wynik)
      break
  else:
    if gra.sprawdzWygrana(plansza):
      prezenter.wyswietlWygrana(gra.aktualnyGracz)
      break
    if gra.sprawdzPrzegana():
      prezenter.wyswietlPrzegrana(gra.aktualnyGracz)
      break
  while gra.wybierzKolor() == False:
    pass
  prezenter.wyswietlWybranyKolor(gra.wybranyKolor)
  if (gra.komputer == 0 and gra.ileGraczy == 1):
    prezenter.wyswietlIleZostaloRuchow(gra.pozostaloRuchow())
  plansza.aktualnyGracz(gra.aktualnyGracz)
  if (gra.komputer == 1 and gra.ileGraczy > 1):
    print "###"
    print komputer.sprawdzOplacalnoscRuchuZPrzewidzeniem(plansza, gra.dozwoloneKolory)
    print "###"
    print komputer.sprawdzOplacalnoscRuchu(plansza, gra.dozwoloneKolory)
    kolor = komputer.sprawdzOplacalnoscRuchu(plansza, gra.dozwoloneKolory)
    gra.zmienGracza()
    plansza.aktualnyGracz(gra.aktualnyGracz)
    plansza.zamalujOsiagalnePolaNaKolor(kolor)
    gra.zmienGracza()
    plansza.aktualnyGracz(gra.aktualnyGracz)
  plansza.zamalujOsiagalnePolaNaKolor(gra.wybranyKolor)
  plansza.drukujPlansze()
  if (gra.komputer == 0 and gra.ileGraczy > 1):
    gra.zmienGracza()
  gra.wyzerujKolor()