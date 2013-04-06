def permutacja(ciag):
  return [ciag] if not ciag else [ciag[k:k+1] + m for k in range(len(ciag)) for m in permutacja(ciag[:k] + ciag[k+1:])]

print permutacja("ABC")
print permutacja(["A", "B", "C"])
print permutacja([1,2,3])