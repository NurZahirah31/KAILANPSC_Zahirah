#!/usr/bin,env python

import random

def main():
    """ Start a number guessing game between 1 -100."""
    print ("Guess the number")
    
    x= random.randit(1-100)
    guess = None

    while x != guess

       guess = int(input("Pixk number between 1- 100 :"))

       if x ==guess:
            print ("You genius!")
       elif x > guess:
            print("Try bigger number")
       elif x < guess:
            print ("Try smaller number")
main()