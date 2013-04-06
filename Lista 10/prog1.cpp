#include <stdio.h>
#include <time.h>
#include <stdlib.h>


int rnd(int min, int max)
{
    int tmp;
    if (max>=min)
        max-= min;
    else
    {
        tmp= min - max;
        min= max;
        max= tmp;
    }
    return max ? (rand() % max + min) : min;
}

int randIfGlassBulb() {
  if (rnd(1,100) >= 10) {
    return 1;
  } else {
    return 0;
  }
}

void drawOnePartOfTree(int maxInLine, int moved = 0) {
  int rysuj = (int) maxInLine/2;
  int rysuj2 = (int) maxInLine/2;
  for (int i = 0; i < maxInLine; ++i)
  {
    for (int j = 0; j < moved; ++j)
    {
      printf(" ");
    }
    for (int j = 0; j < maxInLine; ++j)
    {
      if (j >= rysuj2 && j <= rysuj) {
        if (randIfGlassBulb()) {
          printf("*");
        } else {
          printf("0");
        }
      } else {
        printf(" ");
      }
    }
    printf("\n");
    rysuj++;
    if (rysuj >= maxInLine) {
      break;
    }
    rysuj2--;
    if (rysuj2 <= 0) {
      break;
    }
  }
}

int main () {
  srand(time(NULL));
  drawOnePartOfTree(10, 4);
  drawOnePartOfTree(14, 2);
  drawOnePartOfTree(18);
}