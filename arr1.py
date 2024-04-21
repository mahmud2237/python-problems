Write a program to declare an array of size n and store the numbers 1,2,3,4 ...n in the array and return the array.


#========== User's Code Starts Here ==========
def store_numbers(n):
    """write the code here """
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    return arr
    
    
"""Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    output = store_numbers(n)
    for i in range(0,n):
        print(output[i])
    
main()
#========== User's Code Ends Here ==========
