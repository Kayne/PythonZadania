import random

class Plansza:
  plansza = list()
  kolory = list()
  kolumn = 15
  wierszy = 15
  gracz = 1

  def __init__(self, kolory, graczy = 1, kolumn = 15, wierszy = 15):
    self.kolory = kolory
    self.kolumn = kolumn
    self.wierszy = wierszy
    for x in xrange(kolumn):
      self.plansza.append(list())
      for y in xrange(wierszy):
        self.plansza[x].append(self.losujKolor())
    self.plansza[0][0] = "*"
    if graczy > 1:
      self.plansza[self.kolumn-1][self.wierszy-1] = "+"

  def drukujPlansze(self):
    for x in self.plansza:
      for y in x:
        print y,
      print ""

  def losujKolor(self):
    return random.choice(self.kolory)

  def poleGracza(self, x, y):
    if self.gracz == 1:
      if self.plansza[x][y] == "*":
        return True
    else:
      if self.plansza[x][y] == "+":
        return True
    return False

  def kolorPola(self, x, y):
    return self.plansza[x][y]

  def sasiadujacePola(self, x, y):
    pola = []
    if (x+1 < self.kolumn):
      pola.append([x+1, y])
    if x-1 >= 0:
      pola.append([x-1, y])
    if y+1 < self.wierszy:
      pola.append([x, y+1])
    if y-1 >= 0:
      pola.append([x, y-1])
    return pola

  def zamalujOsiagalnePolaNaKolor(self, kolor):
    if self.gracz == 1:
      for x in xrange(self.kolumn):
        for y in xrange(self.wierszy):
          if self.poleGracza(x,y):
            for z in self.sasiadujacePola(x,y):
              if self.kolorPola(z[0],z[1]) == kolor:
                self.plansza[z[0]][z[1]] = "*"
    else:
      for x in reversed(xrange(self.kolumn)):
        for y in reversed(xrange(self.wierszy)):
          if self.poleGracza(x,y):
            for z in self.sasiadujacePola(x,y):
              if self.kolorPola(z[0],z[1]) == kolor:
                self.plansza[z[0]][z[1]] = "+"

  def wszystkiePolaGracza(self):
    for x in xrange(self.kolumn):
      for y in xrange(self.wierszy):
        if not self.poleGracza(x,y):
          return False
    return True

  def wolnePole(self):
    for x in xrange(self.kolumn):
      for y in xrange(self.wierszy):
        if self.plansza[x][y] != "*" and self.plansza[x][y] != "+":
          return True
    return False

  def ilePol(self, gracz):
    zliczacz = 0
    for x in xrange(self.kolumn):
      for y in xrange(self.wierszy):
        if gracz == 1:
          if self.kolorPola(x,y) == "*":
            zliczacz += 1
        else:
          if self.kolorPola(x,y) == "+":
            zliczacz += 1
    return zliczacz

  def aktualnyGracz(self, gracz):
    self.gracz = gracz

  def zwrocPlansze(self):
    return self.plansza

  def nadpiszPlansze(self, plansza):
    self.plansza = plansza