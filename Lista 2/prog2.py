
def szachownica(n, k):
  for i in range(n*2):
    if (i % 2 == 0):
      for w in range(k):
        for j in range(n*2):
          if (j % 2 == 0):
            for l in range(k):
              print(" "),
          else:
            for l in range(k):
              print ("#"),
        print("")
    else:
      for w in range(k):
        for j in range(n*2):
          if (j % 2 == 0):
            for l in range(k):
              print("#"),
          else:
            for l in range(k):
              print (" "),
        print("")


szachownica(6,6)
