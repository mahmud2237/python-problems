'''
Write a program to store first n prime numbers in an array . After storing return the array.﻿
Input:-
n=5

Output:- Return the output in the form of an array.

2
3
5
7
11

'''
#========== User's Code Starts Here ==========

def prime_numbers(n):
    """ Function to store first n prime_numbers in a list
    Return the list containing the prime numbers """
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % i != 0 for i in range(2, int(num ** 0.5 + 1))):
            primes.append(num)
        num += 1
    return primes
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    output = prime_numbers(n)
    for i in range(0,n):
        print(output[i])
    
main()

#========== User's Code Ends Here ==========
