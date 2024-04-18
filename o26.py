'''
Problem:
Print the following pattern using for loops

*    *
**   **
***  ***
**** ****
**********

'''

#========== User's Code Starts Here ==========

def print_pattern(n):
    """ Function to print the pattern """
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end="")
        for k in range(i+1, n+1):
            print(" ", end="")
        for l in range(i, 0, -1):
            print("*", end="")
        print()

    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_pattern(n)
    
main()
#========== User's Code Ends Here ==========

"""

"""
