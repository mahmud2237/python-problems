'''
Write a program to print the maximum of two numbers using Ternary operator.


Example:-

Input:-

a=3, b=5

Output:-

5
'''

#========== User's Code Starts Here ==========
def find_max(a,b):
    """write the code inside this block to find the maximum between two numbers
    only print the maximum number  """
    return a if a > b else b
    
    """Dont change anything below. If changed click on reset."""
def main():
    a = int(input())
    b = int(input())
    print(find_max(a,b))
    
main()

#========== User's Code Ends Here ==========
