def zagadka(slowa):
  nowe_slowa = []
  for slowo in slowa:
    if len(slowo) > 3:
      nowe_slowa.append(slowo)
    else:
      if len(slowo) == 3:
        nowe_slowa.append("***")
      elif len(slowo) == 2:
        nowe_slowa.append("**")
      else:
        nowe_slowa.append("*")
  return nowe_slowa

print zagadka([])