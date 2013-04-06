#encoding: utf-8
import itertools
def ukladalne(start, koniec):
  for char in start:
    if char in koniec:
      if start[char] >= koniec[char]:
        continue
      else:
        return False
    else:
      return False
  return True

slowa = set()
for s in open("slowa_utf8.txt"):
  slowa.add(s.rstrip())

def na_slownik(wyraz):
  dic = {}
  for char in wyraz:
    if char in dic:
      dic[char] += 1
    else:
      dic[char] = 1
  return dic

imie = raw_input("Wpisz imię: ")
imie = imie.rstrip()
imie = imie.lower()
imie_slownikowe = na_slownik(imie.replace(" ", ""))

zagadki = set()

# itertools.permutations(imie):
# itertools.imap(lambda x: "".join(x), itertools.permutations(imie)):
for s in itertools.imap(lambda x: "".join(x), itertools.permutations(imie)):
  string = s.split()
  if string[0] in slowa:
    if string[1] in slowa:
      if ukladalne(imie_slownikowe, na_slownik(string[0] + string[1])):
        if not string[1] + " " + string[0] in zagadki:
          zagadki.add(string[0] + " " + string[1])

for s in zagadki:
  print s