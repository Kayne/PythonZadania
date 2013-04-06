def policzWartosci(dictionary):
  wynik = {}
  for k,v in dictionary.iteritems():
    if v in wynik:
      wynik[v] += 1
    else:
      wynik[v] = 1
  return wynik

D = { "ala" : 3, "ola" : 3, "janek" : 5, "bonifacy" : 8, "ela" : 3, "tomek" : 5}
print policzWartosci(D)
print policzWartosci({})