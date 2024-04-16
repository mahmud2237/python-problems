'''
Write a program to perform the following operation a+b-c

Note (a, b and c is being provided by the user. Your task is to display a+b-c)

Example:-

Input

a=3 , b=4, c=9

Output
-2

Input

a=10, b=6, c=4

Output:-
12
'''
#========== User's Code Starts Here ==========
def calculate(a, b, c):
    """write the code inside this block to calculate a+b-c"""
    result = a + b - c
    return result
    
    
    """Dont change anything below. If changed click on reset."""
    
def main():    
    a = int(input())
    b = int(input())
    c = int(input())
    calculate(a,b,c)
    print(calculate(a, b, c))
main()
#========== User's Code Ends Here ==========
