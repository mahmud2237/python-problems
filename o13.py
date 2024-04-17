'''
Problem:
Write a program using only while loops to print all the even numbers from 1 to n

Input
if n = 10

Output
2
4
6
8
10
'''

#========== User's Code Starts Here ==========
def print_even(n):
    """Print all even numbers from 1 to n"""
    i = 2
    while(i<=n):
        print(i)
        i += 2
   

    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_even(n)
    
main()

    

#========== User's Code Ends Here ==========
