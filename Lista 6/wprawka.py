def znajdzZmienna(zmienna, dic):
  for key,value in dic.iteritems():
    if key == zmienna:
      return value

def obliczSume(wyrazenie, dic):
  wyrazenie = wyrazenie.split("+")
  wartosc = 0
  for i in wyrazenie:
    if dic:
      if i in dic:
        wartosc += znajdzZmienna(i, dic)
      else:
        wartosc += int(i)
    else:
      wartosc += int(i)
  return wartosc

print obliczSume("a+b+100", {"a": 5, "b": 10})
print obliczSume("55+34", None)
print obliczSume("a+c+d+e", {"a": 1, "c": 2, "d": 3, "e": 4})