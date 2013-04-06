def generuj_liczby(n,n2):
  siodemki = n2*"7"
  x = n - n2
  liczb = 0
  for i in xrange(1, 10**x):
    print str(i).zfill(x)+siodemki
    liczb += 1
  for i in xrange(1,10**x):
    print siodemki+str(i).zfill(x)
    liczb += 1

  for i in xrange(1,10**(x-1)):
    for j in xrange(1,10):
      print str(j) + siodemki + str(i).zfill(x-1)
      liczb += 1
    for j in xrange(1,10):
      print str(i).zfill(x-1) + siodemki + str(j)
      liczb += 1
  print liczb

generuj_liczby(10, 7)