#include <stdio.h>
#include <math.h>


int main() {
  int maksymum = 0;
  int r = -1;
  int p = 0;
  int pold = 0;

  int podzielone_rozmiary = 0;

  int rozmiary[] = {7,13,19,27};

  int rozmiar = sizeof(rozmiary) / sizeof(rozmiary[0]);

  for (int i = 0; i < rozmiar; ++i)
  {
    if (rozmiary[i] > maksymum) {
      maksymum = rozmiary[i];
    }
  }

  for (int n = 0; n < rozmiar; ++n)
  {
    pold = p;
    podzielone_rozmiary = (int)rozmiary[n]/2;
    p = maksymum - podzielone_rozmiary;

    for (int i = 0; i < rozmiary[n]; ++i)
    {
      if (i <= r || i >= (rozmiary[n]-1-r)) {
        continue;
      }
      for (int j = 0; j < rozmiary[n]+p; ++j)
      {
        if (((int)pow(j-podzielone_rozmiary-p, 2) + (int)pow(i-podzielone_rozmiary, 2)) <= (int)pow(podzielone_rozmiary, 2)+1) {
          printf("#");
        } else {
          printf(" ");
        }
        j++;
      }
      printf("\n");
      i++;
    }
    if (pold < p) {
      r--;
    } else {
      r++;
    }
  }
}