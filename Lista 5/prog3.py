#encoding: utf-8
f = open('slowa_utf8.txt')
slowa = []
slowa2 = []
for s in f:
  s = unicode(s.rstrip(), "utf-8")
  slowa.append(s)
  slowa2.append(s[::-1])

slowa = set(slowa)
slowa2 = set(slowa2)
for s in slowa2:
  if slowa.__contains__(s):
    print s + " - " + s[::-1]
    #slowa.remove(s)
    #slowa2.remove(s)