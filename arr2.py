Given an array find the maximum in it and return it.
Example:-

Input:-
Arr=[5, 4, 7, 2, 6]

Ouput:-
7

#========== User's Code Starts Here ==========

def find_maximum(arr, length):
    """Function to find the maximum in the array 
    return the maximum value"""
    max_element = max(arr)
    return max_element
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(find_maximum(arr, n))
    
main()

    
#========== User's Code Ends Here ==========
