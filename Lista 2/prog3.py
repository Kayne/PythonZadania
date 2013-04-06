

def koperta(n):
  w = (2*n)+1
  for i in range(w):
    for j in range(w):
      if i == 0 or j == 0 or i == w-1 or j == w-1 or i == j or i+j == w-1:
        print("*"),
      else:
        print(" "),
    print("")

koperta(4)