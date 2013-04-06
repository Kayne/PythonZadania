def bin(N): # N jest liczba
  if N == 0: return [ [] ]
  r = bin(N-1)
  return [ [0] + x for x in r] + [ [1] + x for x in r]

preferencje = [unicode(x.rstrip(), "utf-8") for x in open("dane.txt")]

osoby = set()
osoby_na_preferencje = {}
for p in preferencje:
  p = p.split()
  osoby.add(p[0])
  osoby_na_preferencje[(p[0], p[1])] = int(p[2])

osoby = list(osoby)

kombinacje = bin(len(osoby))

maxik = len(osoby)

maksymalne_szczescie = []

i = 0
for z in kombinacje:
  maksymalne_szczescie.append(0)
  for x in range(len(z)):
    if z[x] == 1:
      for x2 in range(len(z)):
        if x2 == x:
          continue
        if z[x2] == 1:
          if (osoby[x2], osoby[x]) in osoby_na_preferencje:
            if osoby_na_preferencje[(osoby[x2], osoby[x])] > 0:
              maksymalne_szczescie[-1] += osoby_na_preferencje[(osoby[x2], osoby[x])]
  i += 1