slowa = []
for s in open("Lalka.txt"):
    s = unicode(s.rstrip(), "utf-8")
    rozbite = s.split()
    for s2 in rozbite:
      slowa.append(s2[0])

wyraz = "".join(slowa)
wyraz = wyraz.lower()

for s in open("ukryte_przeslania.txt"):
  if s.rstrip() in wyraz:
    print "Znaleziono: " + s