#encoding: utf-8
def na_slownik(wyraz):
  dic = {}
  for char in wyraz:
    if char in dic:
      dic[char] += 1
    else:
      dic[char] = 1
  return dic

def wczytaj_slowa(plik):
  f = open(plik)
  slowa = []
  for s in f:
    s = unicode(s.rstrip(), "utf-8")
    s = s.lower()
    slowa.append(s)
  return slowa

def ukladalne(start, koniec):
  for char in start:
    if char in koniec:
      if start[char] >= koniec[char]:
        continue
      else:
        return False
  return True

slowa = wczytaj_slowa('rzeczowniki_utf8.txt')
slowa.sort(key=len)

dic = {}
slownikowe = {}
uzyte = set()

for slowo in set(slowa):
  slownikowe[slowo] = na_slownik(slowo)

for i in reversed(xrange(len(slowa))):
  #if slowa[i] in uzyte:
  #  continue
  for j in xrange(i):
    if ukladalne(slownikowe[slowa[i]], slownikowe[slowa[j]]):
      uzyte.add(slowa[j])
      try:
        dic[slowa[i]] += 1
      except:
        dic[slowa[i]] = 0

print max(dic, key=dic.get)
#for key,value in dic.iteritems():
#  print key + " - " + str(value)