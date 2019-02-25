#!/usr/bin/env python

nterms = int(input("¿Cuantos termino quieres?"))

n1 = 0
n2 = 1
count = 0

if nterms <= 0:
   print("Por favor digita un entero positivo")
elif nterms == 1: 
   print("Serie de Fibonacci",nterms,":")
  print(n1)
else: 
  print("Serie de Fibonacci hasta",nterms,":")
  while count < nterms: 
      print(n1,end=' , ')
  nth = n1 + n2
n1 = n2
n2 = nth 
count += 1

