# -*- coding: utf-8 -*-
# Marcin Bratek (247919)

# ten brzydki komentarz powyżej umożliwia kodowanie używanie polskich znaków (kodowanie utf-8)
# konieczne w pythonie 2.x
# Kodowanie windowsowe nazywa się cp1250

# po znaku "#" rozpoczyna się komentarz
   
def kwadrat(n):
   for i in range(n):
      for j in range(n):   # pętla w pętli
         print "*",
      print
      
def kwadrat2(n):
   for i in range(n):
      print n * "#"      
  
# wcześniej były definicje, poniżej jest część która się wykonuje

         
w = 0
for i in range(5):
   print "Przebieg",w
   print 20 * "-"
   w = w + 1
   kwadrat(3+2*i)
   print
for i in range(5):
   print "Przebieg",w
   print 20 * "-"
   w = w + 1
   kwadrat2(3+i)
   print