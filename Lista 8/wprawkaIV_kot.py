#encoding: utf-8
"""
Wprawka IV

Napisz funkcję partition(fun, data) która bierze jednoargumentową funkcję oraz listę danych i rozrzuca dane do kubełków wyznaczanych przez działanie funkcji.
Innymi słowy tworzy słownik który wartości y przypisuje listę takich x, że fun(x)=y i x należy do data.

Przykład działania funkcji:
>>> partition(lambda x: x%3, [1, 2, 3, 4, 5])
{0: [3], 1: [1, 4], 2: [2, 5]}
>>> partition(lambda q: True, "alibaba")
{True: ['a', 'l', 'i', 'b', 'a', 'b', 'a']}
"""

def partition(fun, data):
  wynik = {}
  for i in data:
    w = fun(i)
    try:
      wynik[w].append(i)
    except:
      wynik[w] = []
      wynik[w].append(i)
  return wynik

print partition(lambda x: x%3, [1, 2, 3, 4, 5])
print partition(lambda q: True, "alibaba")