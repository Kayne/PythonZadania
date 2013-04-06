def na_slownik(wyraz):
  dic = {}
  for char in wyraz:
    if char in dic:
      dic[char] += 1
    else:
      dic[char] = 1
  return dic

def ukladalne(start, koniec):
  start_dic = na_slownik(start)
  koniec_dic = na_slownik(koniec)
  for char in start_dic:
    if char in koniec_dic:
      if start_dic[char] >= koniec_dic[char]:
        start_dic[char] = 0
        koniec_dic[char] = 0
      else:
        break
  for char in koniec_dic:
    if koniec_dic[char] > 0:
      return False
      break
  return True


if __name__ == "__main__":
  if ukladalne("kapelmistrzowanie", "zdyskwalifikowanie"):
    print "Tak"
  else:
    print "Nie"

  if ukladalne("lokomotywa", "aktyw"):
    print "Tak"