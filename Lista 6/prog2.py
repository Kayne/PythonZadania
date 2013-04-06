#encoding: utf-8
from prog1 import ukladalne

def wczytaj_slowa(plik):
  f = open(plik)
  slowa = []
  for s in f:
    #s = unicode(s.rstrip(), "utf-8")
    s = s.lower()
    s = s.rstrip()
    slowa.append(s)
  return slowa

def znajdz_i_wydrukuj(slowa, slowo):
  for slowko in set(slowa):
    if ukladalne(slowo, slowko):
      print slowko

if __name__ == "__main__":
  slowa = wczytaj_slowa('rzeczowniki_utf8.txt')
  znajdz_i_wydrukuj(slowa, 'przepieprzenie')