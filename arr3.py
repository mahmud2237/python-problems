'''
Given an array find the minimum in it and return it with the length of the array.

Example:-

Input:- User can give input Array and the length of the array
Arr=[5, 6, 2, 9, -2], 5

Ouput:-
-2

Now, write a program to return the minimum element of the array.
'''
#========== User's Code Starts Here ==========

def find_minimum(arr, length):
    """Function to find the minimum in the array 
    return the minimum value"""
    mini_element = min(arr)
    return mini_element
  
    
    """Dont change anything below. If changed click on reset."""
def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(find_minimum(arr, n))
main()

#========== User's Code Ends Here ==========
