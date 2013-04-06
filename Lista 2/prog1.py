
def krzyzyk(n):
  for i in range(n*3):
    for j in range(3):
      if (i < n and (j == 0 or j == 2)) or (i >= n*2 and (j == 0 or j == 2)):
        for k in range(n):
          print(" "),
      else:
        for k in range(n):
          print ("*"),
    print("")


krzyzyk(5)
