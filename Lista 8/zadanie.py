def equi ( A ):
  if A == []:
    return -1
  if len(A) == 1:
    return 0
  suma_zbioru = sum(A)
  suma = 0
  suma2 = 0
  for a in xrange(len(A)):
    suma = suma_zbioru - suma2 - A[a]
    if suma == suma2:
      return a
    suma2 += A[a]
  return -1

A = [-7, 1, 5, 2, -4, 3, 0]
print equi(A)