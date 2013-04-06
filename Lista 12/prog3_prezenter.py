#encoding: utf-8

class Prezenter:

  def wyswietlWybranyKolor(self, kolor):
    print "Wybrano kolor: " + kolor

  def wyswietlIleZostaloRuchow(self, ruchow):
    print "Pozostało jeszcze: " + str(ruchow) + " ruchów!"

  def wyswietlWygrana(self, gracz):
    if gracz != 3:
      print "Wygrał gracz " + str(gracz) + "!"
    else:
      print "Remis!"

  def wyswietlPrzegrana(self, gracz):
    print "Przegrał gracz " + str(gracz) + "!"