#encoding: utf-8
import random
def modulo(a,b,c):
  x = 1
  y = a
  while b>0:
    if b%2==1:
      x = (x*y)%c
    y = (y*y)%c
    b = b/2
  return x%c
        
def millerRabin(N,iteration):
  if N<2:
    return False
  if N!=2 and N%2==0:
    return False
  d=N-1
  while d%2==0:
    d = d/2
  
  for i in range(iteration):
    a = random.randint(1, N-1)
    temp = d
    x = modulo(a,temp,N)
    while (temp!=N-1 and x!=1 and x!=N-1):
      x = (x*x)%N
      temp = temp*2
  
    if (x!=N-1 and temp%2==0):
      return False
  
  return True

def generuj_liczby(n,n2):
  siodemki = n2*"7"
  x = n - n2
  najwieksza = 0

  for i in xrange(1, 10**x):
    if millerRabin(int(str(i).zfill(x)+siodemki), 5) == True:
      najwieksza = str(i).zfill(x)+siodemki
  for i in xrange(1,10**x):
    if millerRabin(int(siodemki+str(i).zfill(x)), 5) == True:
      najwieksza = siodemki+str(i).zfill(x)

  # To modyfikować dla innych wartości
  for i in xrange(1,10**(x-1)):
    for j in xrange(1,10):
      if millerRabin(int(str(j) + siodemki + str(i).zfill(x-1)), 5) == True:
        najwieksza = str(j) + siodemki + str(i).zfill(x-1)
    for j in xrange(1,10):
      if millerRabin(int(str(i).zfill(x-1) + siodemki + str(j)), 5) == True:
        najwieksza = str(i).zfill(x-1) + siodemki + str(j)

  return najwieksza

print generuj_liczby(10,7)