# -*- coding: utf-8 -*-
# Marcin Bratek (247919)

from losowanie_fragmentow import losujFragment

def losujHaslo(n):
  need_length = n
  haslo = ""
  ready = False
  # Zakładam, że hasło musi mieć co najmniej dwa znaki
  if n <= 3:
    while True:
      haslo = losujFragment()
      if len(haslo) <= 3:
        break
  else:
    while True:
      wylosowane = losujFragment()
      haslo = haslo + wylosowane
      need_length = need_length - len(wylosowane)
      if need_length <= 1:
        haslo = ""
        need_length = n
      if need_length <= 2:
        while True:
          temp = losujFragment()
          if len(temp) == 2:
            haslo = haslo + temp
            ready = True
            break
        if ready == True:
          break
      if ready == True:
        break
  return haslo

for i in range(10):
  print losujHaslo(8)
for i in range(10):
  print losujHaslo(12)