def kombinacje(liczby, n):
  if n==0: yield []
  else:
    for i in xrange(len(liczby)):
      for cc in kombinacje(liczby[i+1:],n-1):
        if all(x<=y for x, y in zip([liczby[i]]+cc, [liczby[i]]+cc[1:])):
          yield [liczby[i]]+cc


print list(kombinacje(range(1,6), 3))

