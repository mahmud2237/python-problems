'''
Problem:
Print the following pattern using for loops

*****
****
***
**
*

'''

#========== User's Code Starts Here ==========

def print_pattern():
    """ Function to print the pattern """
    for i in range(1, 6, 1):
        string = ""
        for j in range(10, 16-i, 1):
            string = string + "*"
        print(string)
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_pattern()
    
main()
#========== User's Code Ends Here ==========

"""

"""
