dic = {}

def reprezentacja(s):
  L = list(s)
  L.sort()
  return ''.join(L)

for s in open("slowa_utf8.txt"):
  s = unicode(s.rstrip(), "utf-8")
  try:
    dic[reprezentacja(s)].append(s)
  except:
    dic[reprezentacja(s)] = []
    dic[reprezentacja(s)].append(s)

K = 5

for key,value in dic.iteritems():
  #if len(value) in xrange(2,K):
  if len(value) >= K:
    print " ".join(value)