from random import randint

# Powinien dzialac zarowno dla Pythona 2.x jak i Pythona 3.x

PUSTE = " "
PELNE = "*"

         
def pustyRysunek(n):
   """ Funkcja zwraca pusty rysunek o boku n, czyli n elementowa liste, ktorej elementami sa listy zawierajace po n pustych pol"""
   wynik = []
   for i in range(n):
      wynik.append([])
      for j in range(n):
         wynik[-1].append(PUSTE)  # wynik[-1] == ostatni dodany wiersz
   return wynik
   
def rysuj(R):
   for w in R:
      print ("".join(w))  # sklejone elementy danego wiersza rysunku

def dodajKwadrat(R, x, y, bok):
   """ UWAGA: funkcja niekompletna!
       Funkcja powinna w rysunku R (czyli w liscie list) wstawiac kwadrat o boku "bok" z lewym gornym rogiem w polu x,y.
       Kwadrat powinien byc pusty w srodku.
       Mozesz zalozyc, ze wielkosc rysunku jest wystarczajaca (czyli ze kwadrat sie zmiesci).
   """
   for i in range(bok):
    for j in range(bok):
      if i == 0 or j == 0 or i == bok-1 or j == bok-1:
        R[y+i][x+j] = "*"
   
   # R[y][x] = PELNE # To troche za malo, powinienes wypelnic rowniez inne punkty
      
      
def obrazek0():
  R = pustyRysunek(20)
  dodajKwadrat(R, 4, 6, 7)  # Przykladowy kwadrat, ktory miesci sie z rezerwa na rysunku
  dodajKwadrat(R, 0, 0, 15) # obramowanie dla calego rysunku. Byc moze warto na poczatku nie wykonywac tego testu.
  rysuj(R) 

def obrazek1(n):
  """
     Ta funkcja jest poprawnie zdefiniowana. Musisz zatem jedynie zrozumiec jej dzialanie.
  """
  R = pustyRysunek(n)
  for start in range(0, n/2 - 1, 2):  # Sprawdz co to jest list(range(0,10,2)) albo list(range(0,10,2))
    bok = n - 2 * start
    dodajKwadrat(R, start, start, bok)    
  rysuj(R)
  
def obrazek2(n,k):
   R = pustyRysunek(n)
   
   # Tu musisz umiescic kod, ktory losuje k kwadratow (mieszczacych sie na rysunku o boku n)
   # i wpisuje je do rysunku R.  
   # Pamietaj, by losowac liczby z wlasciwego zakresu!
   for z in range(1,randint(1,k)+1):
    dodajKwadrat(R,randint(1,n/2),randint(1,n/2),randint(1,n/2))
  
   rysuj(R)   
      

print ("Demonstracja kwadratow")

obrazek0()


print("") 

obrazek1(20)

print("") 

obrazek2(20,6)
