def lisp(E):
  if type(E) == int:
    return E
  values = []
  for e in E[1:]:
    values.append(lisp(e))

  if E[0] == "+":
    wynik = 0
    for e in values:
      wynik += e
  if E[0] == "*":
    wynik = 1
    for e in values:
      wynik *= e
  if E[0] == "-":
    wynik = values[1]
    for e in values:
      wynik -= e
  if E[0] == "/":
    wynik = values[1]
    for e in values:
      wynik /= e
  return wynik

print lisp(("*", 2,3))
print lisp(("-", 2,5))
print lisp( ("*", ("+",2,2), ("+",1,3)))

