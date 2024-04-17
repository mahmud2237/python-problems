'''
Problem:
Write a program to print the digits of a number .

Input:-
N - 153 .

output:-
3
5
1
'''

#========== User's Code Starts Here ==========
def print_digits(n):
    """Function to print the digits of the number n 
    Note Print all the digits in a new line"""
    for digit in reversed(str(n)):
        print(digit)
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_digits(n)
    
main()
    
#========== User's Code Ends Here ==========
