#
# Symulator maszyny RAM
#

def argument(s, Mem):
  """ Funkcja zwraca wartosc liczbowa dla napisu s przy stanie pamieci Mem
       argument("=5",{})                  == 5
       argument("5", {1: 13, 5 : 222})    == 222
       argument("^1", {1 : 13, 13 : 123}) == 123
  """
  for cos in s:
    if cos == "=":
      return int(s[1])
    else:
      return int(Mem[int(cos)])
   
     
def maszynaRam(Program, Dane):
  """ Funcja zwraca zawartosc tasmy wyjsciowej po wykonaniu programu"""
   
  Dane = Dane[:] # Tasma wejsciowa (kopiujemy ja, bo wowczas mozna bedzie robic "del Dane[0]")
  A = 0          # Akumulator
  PC = 0         # Program counter, czyli licznik wskazujacy nr rozkazu do wykonania  
  Mem = {}       # Pamiec RAM (zakladamy, ze dla kazdej komorki najpierw jest STORE, a dopiero pozniej LOAD)
  Wynik = []     # Tasma wyjsciowa

  while PC < len(Program):
    if Program[PC][0] == "store":
      Mem[argument(Program[PC][1], Mem)] = A

    if Program[PC][0] == "load":
      A = argument(Program[PC][1], Mem)

    if Program[PC][0] == "add":
      A += argument(Program[PC][1], Mem)
      Wynik.append(A)

    if Program[PC][0] == "jzero":
      if A == 0:
        PC = argument(Program[PC][1], Mem)

    if Program[PC][0] == "read":
      Mem[argument(Program[PC][1], Mem)] = Dane[0]
      del(Dane[0])
    if Program[PC][0] == "jump":
      PC = argument(Program[PC][1], Mem)-1



    PC = PC + 1
    pass # Tu wpisz odpowiedni kod 

  if not Wynik:
    Wynik.append(0)
  return Wynik[::-1]      



def zmienTekstNaProg(s):
  """ Musisz sam sprawdzic, co ta funkcja dokladnie robi """
  prog = []
  for wiersz in s.split("\n"):
    instr = wiersz.split()
    if len(instr) == 2:  # poprawna instrukcja ma zawsze 2 czesci
      prog.append(instr)
  return prog
   
   
sumowanieLiczb = zmienTekstNaProg("""
  load =0
  store =2
  read =1
  load 1
  jzero =9
  load 2
  add 1
  store =2
  jump =2
  write 2
""")


def suma(L):
  """ Funkcja oblicza sume liczb na liscie L wykorzystujac maszyne RAM """
  tasmaWyjsciowa = maszynaRam(sumowanieLiczb, L + [0])
  return tasmaWyjsciowa[0]
   
   
print (suma([1,2,3,10,5]))
print (suma(10 * [3]))
print (suma([]))
        
