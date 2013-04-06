#encoding: utf-8
"""
Wprawka V

Drzewo trzymające dane jedynie w liściach można reprezentować w Pythonie jako wielokrotnie zagnieżdżone listy. Wtedy listy te reprezentują wierzchołki drzewa a ich elementami są poddrzewa danego wierzchołka.
Napisz funkcję treeFlatten które bierze takie drzewo i spłaszcza je, tzn. tworzy listę liści tego drzewa w kolejności od lewej do prawej.

Przykład działania funkcji:
>>> treeFlatten([1, [2, 3, [4, 5], [6]], [7]])
[1, 2, 3, 4, 5, 6, 7]
"""

def treeFlatten(drzewo):
  if type(drzewo) != list:
    return [drzewo]
  else:
    return sum(map(treeFlatten, drzewo), [])

print treeFlatten([1, [2, 3, [4, 5], [6]], [7]])
print treeFlatten([1, [2, 3, 4, 5, 7]])
print treeFlatten([[2, 1], 3])