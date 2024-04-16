'''
Write a program to Swap two Variables a and b (Swapping basically means interchanging)

Example:-
Input
a=3 , b=4

Output
a=4, b=3
'''

#========== User's Code Starts Here ==========
def swap(a,b):
    """write the code inside this block to swap two numbers"""
    a, b = b, a
    return a, b
     
    """Dont change anything below. If changed click on reset."""

def main():    
    a = int(input())
    b = int(input())
    a, b = swap(a,b)
    print("a value is =",a)
    print("b value is =",b)
    
main()
#========== User's Code Ends Here ==========
