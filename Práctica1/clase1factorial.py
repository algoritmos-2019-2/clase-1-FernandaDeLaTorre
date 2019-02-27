#!/usr/bin/env python

def factorial():
        num= int(input("Ingresa numero:"))
        factorial= 1
        for i in range(num): 
                factorial= factorial*num
                num= num-1
        print(factorial) 
factorial()

                
             


