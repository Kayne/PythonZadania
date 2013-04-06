#include <stdio.h>
#include <stdlib.h> 

int dzieli(int liczba, int modulo) {
  if (modulo != 0)
  {
    if (liczba%modulo == 0) {
      return 1;
    }
  }
  return 0;
}

int iloczyn(int * tablica) {
  int iloczyn = 1;
  for (int i = 0; i <= (sizeof(tablica) / sizeof(tablica[0])); ++i)
  {
    if (tablica[i] == 11) break;
    iloczyn *= tablica[i];
  }
  return iloczyn;
}

int suma(int * tablica) {
  int suma = 0;
  for (int i = 0; i <= (sizeof(tablica) / sizeof(tablica[0])); ++i)
  {
    if (tablica[i] == 11) break;
    suma += tablica[i];
  }
  return suma;
}

int * cyfry(int liczba) {
  int *tablica = (int *) malloc(liczba * sizeof(int));

  int i = 0;
  while (liczba > 0) 
  { 
    tablica[i] = liczba % 10;
    liczba -= liczba % 10; 
    if(liczba != 0) liczba /=10; 
    i++;
  } 
  tablica[i] = 11;

  return tablica;
}

int fajna(int liczba) {
  if (dzieli(liczba, suma(cyfry(liczba))) && dzieli(liczba, iloczyn(cyfry(liczba)))) {
    printf("%d\n", liczba);
  }
}

int main(int argc, char *argv[]) {
  int liczba = 0;
  sscanf(argv[1], "%d", &liczba);
  if (argc > 1) {
    for (int i = 1; i <= liczba; ++i)
    {
      fajna(i);
    }
  } else {
    printf("Podaj liczbę jako argument programu!");
  }
  printf("\n");

  return 0;
}