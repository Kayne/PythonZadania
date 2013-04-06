#include <stdio.h>

void kwadrat(int n) {
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      printf("* ");
    }
    printf("\n");
  }
  printf("\n");
}

void kwadrat2(int n) {
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      printf("#");
    }
    printf("\n");
  }
}

main()
{
  int w = 0;
  for (int i = 0; i < 5; i++) {
    printf("Przebieg %d\n", w);
    w++;
    for (int j = 0; j < 20; ++j) {
      printf("-");
    }
    printf("\n");
    kwadrat(3+2*i);
  }
  for (int i = 0; i < 5; i++) {
    printf("Przebieg %d\n", w);
    w++;
    for (int j = 0; j < 20; ++j) {
      printf("-");
    }
    printf("\n");
    kwadrat2(3+i);
  }
}