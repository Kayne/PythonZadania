def fwd(stan, maxik):
  koniec = []
  temp = list(stan)
  # wylewanie
  for i in range(len(stan)):
    temp2 = temp[:]
    temp2[i] = 0
    if temp2[i] != temp[i]:
      koniec.append(temp2)
  # dolewanie
  for i in range(len(stan)):
    temp2 = temp[:]
    temp2[i] = maxik[i]
    if temp2[i] != temp[i]:
      koniec.append(temp2)
  # przelewanie
  for i in range(len(stan)):
    for z in range(len(stan)):
      if i == z:
        continue
      temp2 = temp[:]
      ile_potrzeba = maxik[z] - temp2[z]
      if ile_potrzeba == 0:
        continue
      if ile_potrzeba >= temp2[i]:
        temp2[z] += temp2[i]
        temp2[i] = 0
      elif ile_potrzeba < temp2[i]:
        do_przelania = temp2[i] - temp2[z]
        temp2[z] += do_przelania
        temp2[i] -= do_przelania
      if temp2[i] != temp[i]:
        koniec.append(temp2)

  return koniec

#print fwd((0,0), (5,5))
#print fwd((2,1,0), (5,5,5))
#print fwd((2,1,0), (5,5,2))
#print fwd((5,3,0), (5,5,2))

def szukaj(start, target, maxik):
  if start == target:
    return [start]
  for n in fwd(start, maxik):
    #print n,len(visited)
    if tuple(n) in visited:
      continue
    visited.add(start)
    path = szukaj(tuple(n), target, maxik)
    if path != []:
      return [start] + path
  return []

visited = set()
print szukaj((2,1), (2,2), (2,2))

visited = set()
print szukaj((1,2), (3,2), (2,3))

visited = set()
print szukaj((3,2,0), (3,5,0), (5,5,5))