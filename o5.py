'''
Write a program to print the largest of the three numbers.

Input:-
a=3, b=5, c=1

Output:-
5
'''

#========== User's Code Starts Here ==========
def find_max(a,b,c):
    """write the code inside this block to find the maximum between three numbers
    only print the maximum number  """
    if (a>b and a>c):
        return a 
    elif (b>a and b>c):
        return b 
    else:
        return c
    
    """Dont change anything below. If changed click on reset."""
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(find_max(a,b,c))
    
main()
#========== User's Code Ends Here ==========
