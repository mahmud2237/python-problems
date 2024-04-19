'''
Problem:
Print the following pattern using for loops

*****
****
***
**
*
*
**
***
****
*****

'''

#========== User's Code Starts Here ==========

def print_pattern(n):
    i = n
    while i>=1:
        j=1
        while j <= i:
            print("*", end="")
            j += 1
        print()
        i -= 1
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print("*", end="")
            j += 1
        print()
        i += 1  

"""
def print_first(n):
    i = n
    while i>=1:
        j=1
        while j <= i:
            print("*", end="")
            j += 1
        print()
        i -= 1


def print_last(n):
    i =1
    while i <= n:
        j = 1
        while j <= i:
            print("*", end="")
            j += 1
        print()
        i += 1   
"""  
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_pattern(n)
    # print_first(n)
    # print_last(n)
main()
#========== User's Code Ends Here ==========

"""

"""
