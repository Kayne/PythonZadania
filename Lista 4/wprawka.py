#encoding: utf-8
def ocenaListy(lista):
  suma = 0
  iloczyn = 1
  for element in lista:
    suma += int(element)
    iloczyn *= int(element)
  if suma > iloczyn:
    slowo = "suma"
    wynik = suma
  elif suma < iloczyn:
    slowo = "iloczyn"
    wynik = iloczyn
  else:
    slowo = "rowne"
    wynik = suma
  return slowo, wynik

print ocenaListy([0,1,2])
print ocenaListy([1,2,4])
print ocenaListy([1,2,3])