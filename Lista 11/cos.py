import sys

def balwan(rozmiary):
  maksymum = 0
  r = -1
  p = 0
  pold = 0
  for rozmiar in rozmiary:
    if rozmiar > maksymum:
      maksymum = rozmiar
  print maksymum
  for n in rozmiary:
    pold = p
    p = maksymum - n / 2
    for i in range(n):
      if i <= r or i >= (n-1-r):
        continue
      for j in range(n+p):
        if (j-n/2-p)**2 + (i-n/2)**2 <= (n/2)**2+1:
          sys.stdout.write("#")
        else:
          sys.stdout.write(" ")
        j = j + 1
      print ""
      i = i + 1
    if pold < p:
      r = r - 1
    else:
      r = r + 1

balwan([7,9,11,13,19,27])