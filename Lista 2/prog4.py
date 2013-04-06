import sys

def kolko(n,p=0,r=-1):
  for i in range(n):
    if i <= r or i >= (n-1-r):
      continue
    for j in range(n+p):
      if (j-n/2-p)**2 + (i-n/2)**2 <= (n/2)**2+1:
        sys.stdout.write("#")
      else:
        sys.stdout.write(" ")
      j = j + 1
    print ""
    i = i + 1

kolko(7,0)
kolko(9,0)
kolko(11,0)