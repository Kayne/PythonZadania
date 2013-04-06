def dzieli(a, b):
  if b == 0:
    return False
  if (a % b == 0):
    return True
  return False

def cyfry(liczba):
  return [int(i) for i in str(liczba)]

def suma(liczba):
  return sum(cyfry(liczba))

def iloczyn(liczba):
  iloczyn_cyfr = 1
  for i in cyfry(liczba):
    iloczyn_cyfr *= i
  return iloczyn_cyfr

def czyFajna(liczba):
  if dzieli(liczba, suma(liczba)) and dzieli(liczba, iloczyn(liczba)):
    return True
  return False

def sprawdzLiczbyCzySaFajne(liczba):
  return filter(czyFajna, range(liczba+1))

print sprawdzLiczbyCzySaFajne(5000)