'''

Given an array find the maximum sum subarray. Return the maximum sum of the subarray.

Input:-
[5,2,-4,-5, 3,-1,2,3,1]

Output:-
8

Reason :- 3,-1,2,3,1 is the maximum subarray possible.

'''
#========== User's Code Starts Here ==========

def find_max_subarray(arr, length):
    """write the code to find the maximum subarray sum
    only return the maximum sum of the subarray . 
    Both array and size of array is given """
    max_sum = float('-inf')  # Initialize maximum sum as negative infinity
    current_sum = 0  # Initialize current sum as 0

    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0  # Reset current sum if it becomes negative

    return max_sum
    
    
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(find_max_subarray(arr, n))
    
main()


#========== User's Code Ends Here ==========
