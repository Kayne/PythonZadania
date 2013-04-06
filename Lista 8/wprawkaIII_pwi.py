#encoding: utf-8
"""
wprawka 3 pwi 
Napisz funkcję slowa, która bierze jako argument listę słów, a zwraca słownik, w którym kluczami są słowa z listy, a odpowiadające im wartości mówią, jak wiele razy dane słowo pojawiła się w słowniku.

>>> slowa(["Ala", "Ela", "Ola", "Ola", "Ela", "Ola"]
{"Ala": 1, Ola: 3, "Ela": 2}
>>> policzWartosci([])
{}
"""

def slowa(lista):
  dic = {}
  for slowo in lista:
    try:
      dic[slowo] += 1
    except:
      dic[slowo] = 1
  return dic

print slowa(["Ala", "Ela", "Ola", "Ola", "Ela", "Ola"])
print slowa([])