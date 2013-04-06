import copy

class Komputer:

  def skopiujListe(self, lista):
    if isinstance(lista, list):
        return list( map(self.skopiujListe, lista) )
    return lista

  def sprawdzOplacalnoscRuchuZPrzewidzeniem(self, plansza, kolory):
    oryginalnaPlansza = self.skopiujListe(plansza.zwrocPlansze())
    plansza.aktualnyGracz(2)

    zamalowane = plansza.ilePol(2)-1

    kolory = self.sprawdzOplacalnoscRuchuKazdegoKoloru(plansza, kolory)
    kolor = ""
    kolor2 = ""
    wybrano = {}

    for k in kolory:
      plansza.aktualnyGracz(2)
      plansza.nadpiszPlansze(self.skopiujListe(oryginalnaPlansza))
      plansza.zamalujOsiagalnePolaNaKolor(k)
      plansza.aktualnyGracz(2)
      wybrano[k] = self.sprawdzOplacalnoscRuchuKazdegoKoloru(plansza, kolory)
      print k,kolory[k],wybrano[k]
      plansza.aktualnyGracz(2)

    print wybrano
    print kolory


    for key in wybrano:
      if kolor == "" and kolor2 == "":
        for z in wybrano[key]:
          if wybrano[key][z] > zamalowane:
            kolor = key
            kolor2 = z
      else:
        for z in wybrano[key]:
          if wybrano[key][z] > zamalowane and wybrano[key][z] > wybrano[kolor][kolor2]:
            kolor = key
            kolor2 = z

    plansza.nadpiszPlansze(self.skopiujListe(oryginalnaPlansza))
    plansza.aktualnyGracz(1)

    return kolor

  def sprawdzOplacalnoscRuchuKazdegoKoloru(self, plansza, kolory):
    oryginalnaPlansza = self.skopiujListe(plansza.zwrocPlansze())
    plansza.aktualnyGracz(2)

    zamalowano = {}
    zamalowane = 0

    zamalowane = plansza.ilePol(2)-1

    for kolor in kolory:
      plansza.zamalujOsiagalnePolaNaKolor(kolor)
      zamalowano[kolor] = plansza.ilePol(2)-1
      plansza.nadpiszPlansze(self.skopiujListe(oryginalnaPlansza))

    plansza.nadpiszPlansze(self.skopiujListe(oryginalnaPlansza))
    plansza.aktualnyGracz(1)

    return zamalowano


  def sprawdzOplacalnoscRuchu(self, plansza, kolory):
    oryginalnaPlansza = self.skopiujListe(plansza.zwrocPlansze())
    plansza.aktualnyGracz(2)

    zamalowano = {}
    zamalowane = 0
    kolor = ""

    zamalowane = plansza.ilePol(2)-1

    for kolor in kolory:
      plansza.zamalujOsiagalnePolaNaKolor(kolor)
      zamalowano[kolor] = plansza.ilePol(2)-1
      plansza.nadpiszPlansze(self.skopiujListe(oryginalnaPlansza))

    for key in zamalowano:
      if kolor == "":
        if zamalowano[key] > zamalowane:
          kolor = key
      else:
        if zamalowano[key] > zamalowane and zamalowano[key] > zamalowano[kolor]:
          kolor = key

    plansza.nadpiszPlansze(self.skopiujListe(oryginalnaPlansza))
    plansza.aktualnyGracz(1)

    return kolor