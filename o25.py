'''
Problem:
Print the following pattern using while loops

*****
****
***
**
*

'''

#========== User's Code Starts Here ==========

def print_pattern(n):
    """ Function to print the pattern """
    i = n
    while i >= 1:
        j = 1
        while j<= i:
            print("*", end="")
            j += 1
        print()
        i -= 1

    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_pattern(n)
    
main()
#========== User's Code Ends Here ==========

"""

"""
