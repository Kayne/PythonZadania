#encoding: utf-8
"""
wprawka 2 msz
Rozważmy listę zawierającą liczby od 0 do N-1. Napisz funkcję która taką listę koduje jednoznacznie do postaci pojedyńczej liczby: mnoży i-tą liczbę z listy przez N**i a następnie sumuje wyniki.

Przykład dla N=8:
koduj([5,1]) zwraca 13 (bo 5 * 8**0 + 1 * 8**1 = 13),
koduj([4,4,4,4]) zwraca 2340.

Dla N=10:
koduj([3,4,5,6,7]) zwraca 76543.
"""

def koduj(lista, N = 8):
  wynik = 0
  i = 0
  for liczba in lista:
    liczba = int(liczba)
    wynik += liczba * (N**i)
    i += 1
  return wynik

print koduj([5,1])
print koduj([4,4,4,4])
print koduj([3,4,5,6,7], 10)