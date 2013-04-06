class Gra:

  dozwoloneKolory = ["a", "b", "c", "d", "e", "f"]
  wybranyKolor = ""
  limitRuchow = 1
  ileGraczy = 2
  aktualnyGracz = 1
  komputer = 1
  ruchyGraczy = [limitRuchow, limitRuchow]

  def wybierzKolor(self):
    if self.ileGraczy > 1 and self.komputer == 0:
      wpisane = raw_input("Gracz " + str(self.aktualnyGracz) + " - Wybierz kolor (a,b,c,d,e,f): ")
    else:
      wpisane = raw_input("Wybierz kolor (a,b,c,d,e,f): ")
    if wpisane in self.dozwoloneKolory:
      self.wybranyKolor = wpisane
      if self.aktualnyGracz == 1:
        self.ruchyGraczy[0] -= 1
      else:
        self.ruchyGraczy[1] -= 1
      return True
    return False

  def zmienGracza(self):
    if self.ileGraczy > 1:
      if self.aktualnyGracz == 1:
        self.aktualnyGracz = 2
      else:
        self.aktualnyGracz = 1

  def wyzerujKolor(self):
    self.wybranyKolor = ""

  def sprawdzPrzegana(self):
    if self.ileGraczy > 1:
      if max(self.ruchyGraczy) == 0:
        if self.ruchyGraczy[self.aktualnyGracz-1] <= 0:
          return True
    else:
      if self.ruchyGraczy[0] == 0:
        return True
    return False

  def sprawdzWygrana(self, plansza):
    if self.ileGraczy == 1 and self.komputer == 0:
      if plansza.wszystkiePolaGracza():
        return True
    else:
      if plansza.wolnePole():
        return False
      if plansza.ilePol(1) > plansza.ilePol(2):
        return 1
      elif plansza.ilePol(2) > plansza.ilePol(1):
        return 2
      else:
        return 3
    return False

  def pozostaloRuchow(self):
    return self.ruchyGraczy[self.aktualnyGracz-1]

  def ustawRuchy(self):
    self.ruchyGraczy = [self.limitRuchow, self.limitRuchow]