'''
Write a program to perform the following operation (a+b) * c ( * is a multiplication sign)

Note (a, b and c is being provided by the user. Your task is to display result)


Example:-

Input
a=3 , b=4, c=9

Output
63


Input
a=10, b=6, c=4

Output:-
64
'''

#========== User's Code Starts Here ==========
def calculate(a,b, c):
    """write the code inside this block to calculate (a+b)*c"""
    return (a+b) * c    
    
    """Dont change anything below. If changed click on reset."""
    
def main():    
    a = int(input())
    b = int(input())
    c = int(input())
    result = calculate(a,b,c)
    print(result)
main()
#========== User's Code Ends Here ==========
